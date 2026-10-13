---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient
title: Class MobileDeviceSubmodelServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:52.445685+00:00
---

# Class MobileDeviceSubmodelServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MobileDeviceSubmodelServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/MobileDeviceSubmodelServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `MobileDeviceSubmodel` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       MobileDeviceSubmodelName name =
           MobileDeviceSubmodelName.of("[NETWORK_CODE]", "[MOBILE_DEVICE_SUBMODEL]");
       MobileDeviceSubmodel response =
           mobileDeviceSubmodelServiceClient.getMobileDeviceSubmodel(name);
     }
     

Note: close() needs to be called on the MobileDeviceSubmodelServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetMobileDeviceSubmodel |  Retrieves a `MobileDeviceSubmodel` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMobileDeviceSubmodel(GetMobileDeviceSubmodelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMobileDeviceSubmodel(MobileDeviceSubmodelName name) 
  * getMobileDeviceSubmodel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMobileDeviceSubmodelCallable() 

  
ListMobileDeviceSubmodels |  Lists `MobileDeviceSubmodel` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMobileDeviceSubmodels(ListMobileDeviceSubmodelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMobileDeviceSubmodels(NetworkName parent) 
  * listMobileDeviceSubmodels(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMobileDeviceSubmodelsPagedCallable() 
  * listMobileDeviceSubmodelsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MobileDeviceSubmodelServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MobileDeviceSubmodelServiceSettings mobileDeviceSubmodelServiceSettings =
         MobileDeviceSubmodelServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create(mobileDeviceSubmodelServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MobileDeviceSubmodelServiceSettings mobileDeviceSubmodelServiceSettings =
         MobileDeviceSubmodelServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create(mobileDeviceSubmodelServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MobileDeviceSubmodelServiceClient

## Static Methods 

### create()
    
    
    public static final MobileDeviceSubmodelServiceClient create()

Constructs an instance of MobileDeviceSubmodelServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MobileDeviceSubmodelServiceSettings settings)
    
    
    public static final MobileDeviceSubmodelServiceClient create(MobileDeviceSubmodelServiceSettings settings)

Constructs an instance of MobileDeviceSubmodelServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MobileDeviceSubmodelServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MobileDeviceSubmodelServiceStub stub)
    
    
    public static final MobileDeviceSubmodelServiceClient create(MobileDeviceSubmodelServiceStub stub)

Constructs an instance of MobileDeviceSubmodelServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(MobileDeviceSubmodelServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MobileDeviceSubmodelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileDeviceSubmodelServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient)` |   
  
## Constructors 

### MobileDeviceSubmodelServiceClient(MobileDeviceSubmodelServiceSettings settings)
    
    
    protected MobileDeviceSubmodelServiceClient(MobileDeviceSubmodelServiceSettings settings)

Constructs an instance of MobileDeviceSubmodelServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MobileDeviceSubmodelServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceSettings)`  
  
  
### MobileDeviceSubmodelServiceClient(MobileDeviceSubmodelServiceStub stub)
    
    
    protected MobileDeviceSubmodelServiceClient(MobileDeviceSubmodelServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MobileDeviceSubmodelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileDeviceSubmodelServiceStub)`  
  
  
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

### getMobileDeviceSubmodel(@Nullable MobileDeviceSubmodelName name)
    
    
    public final MobileDeviceSubmodel getMobileDeviceSubmodel(@Nullable MobileDeviceSubmodelName name)

Retrieves a `MobileDeviceSubmodel` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       MobileDeviceSubmodelName name =
           MobileDeviceSubmodelName.of("[NETWORK_CODE]", "[MOBILE_DEVICE_SUBMODEL]");
       MobileDeviceSubmodel response =
           mobileDeviceSubmodelServiceClient.getMobileDeviceSubmodel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.MobileDeviceSubmodelName`  
Required. The resource name of the MobileDeviceSubmodel. Format: `networks/{network_code}/mobileDeviceSubmodels/{mobile_device_submodel_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodel](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodel)` |   
  
### getMobileDeviceSubmodel(GetMobileDeviceSubmodelRequest request)
    
    
    public final MobileDeviceSubmodel getMobileDeviceSubmodel(GetMobileDeviceSubmodelRequest request)

Retrieves a `MobileDeviceSubmodel` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       GetMobileDeviceSubmodelRequest request =
           GetMobileDeviceSubmodelRequest.newBuilder()
               .setName(
                   MobileDeviceSubmodelName.of("[NETWORK_CODE]", "[MOBILE_DEVICE_SUBMODEL]")
                       .toString())
               .build();
       MobileDeviceSubmodel response =
           mobileDeviceSubmodelServiceClient.getMobileDeviceSubmodel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMobileDeviceSubmodelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetMobileDeviceSubmodelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodel](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodel)` |   
  
### getMobileDeviceSubmodel(String name)
    
    
    public final MobileDeviceSubmodel getMobileDeviceSubmodel(String name)

Retrieves a `MobileDeviceSubmodel` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       String name =
           MobileDeviceSubmodelName.of("[NETWORK_CODE]", "[MOBILE_DEVICE_SUBMODEL]").toString();
       MobileDeviceSubmodel response =
           mobileDeviceSubmodelServiceClient.getMobileDeviceSubmodel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MobileDeviceSubmodel. Format: `networks/{network_code}/mobileDeviceSubmodels/{mobile_device_submodel_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodel](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodel)` |   
  
### getMobileDeviceSubmodelCallable()
    
    
    public final UnaryCallable<GetMobileDeviceSubmodelRequest,MobileDeviceSubmodel> getMobileDeviceSubmodelCallable()

Retrieves a `MobileDeviceSubmodel` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       GetMobileDeviceSubmodelRequest request =
           GetMobileDeviceSubmodelRequest.newBuilder()
               .setName(
                   MobileDeviceSubmodelName.of("[NETWORK_CODE]", "[MOBILE_DEVICE_SUBMODEL]")
                       .toString())
               .build();
       ApiFuture<MobileDeviceSubmodel> future =
           mobileDeviceSubmodelServiceClient.getMobileDeviceSubmodelCallable().futureCall(request);
       // Do something.
       MobileDeviceSubmodel response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMobileDeviceSubmodelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetMobileDeviceSubmodelRequest),[MobileDeviceSubmodel](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodel)>` |   
  
### getSettings()
    
    
    public final @Nullable MobileDeviceSubmodelServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.MobileDeviceSubmodelServiceSettings` |   
  
### getStub()
    
    
    public MobileDeviceSubmodelServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileDeviceSubmodelServiceStub)` |   
  
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
  
### listMobileDeviceSubmodels(@Nullable NetworkName parent)
    
    
    public final MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse listMobileDeviceSubmodels(@Nullable NetworkName parent)

Lists `MobileDeviceSubmodel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (MobileDeviceSubmodel element :
           mobileDeviceSubmodelServiceClient.listMobileDeviceSubmodels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of MobileDeviceSubmodels. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse)` |   
  
### listMobileDeviceSubmodels(ListMobileDeviceSubmodelsRequest request)
    
    
    public final MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse listMobileDeviceSubmodels(ListMobileDeviceSubmodelsRequest request)

Lists `MobileDeviceSubmodel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       ListMobileDeviceSubmodelsRequest request =
           ListMobileDeviceSubmodelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (MobileDeviceSubmodel element :
           mobileDeviceSubmodelServiceClient.listMobileDeviceSubmodels(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMobileDeviceSubmodelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileDeviceSubmodelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse)` |   
  
### listMobileDeviceSubmodels(String parent)
    
    
    public final MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse listMobileDeviceSubmodels(String parent)

Lists `MobileDeviceSubmodel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (MobileDeviceSubmodel element :
           mobileDeviceSubmodelServiceClient.listMobileDeviceSubmodels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of MobileDeviceSubmodels. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse)` |   
  
### listMobileDeviceSubmodelsCallable()
    
    
    public final UnaryCallable<ListMobileDeviceSubmodelsRequest,ListMobileDeviceSubmodelsResponse> listMobileDeviceSubmodelsCallable()

Lists `MobileDeviceSubmodel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       ListMobileDeviceSubmodelsRequest request =
           ListMobileDeviceSubmodelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListMobileDeviceSubmodelsResponse response =
             mobileDeviceSubmodelServiceClient.listMobileDeviceSubmodelsCallable().call(request);
         for (MobileDeviceSubmodel element : response.getMobileDeviceSubmodelsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMobileDeviceSubmodelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileDeviceSubmodelsRequest),[ListMobileDeviceSubmodelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileDeviceSubmodelsResponse)>` |   
  
### listMobileDeviceSubmodelsPagedCallable()
    
    
    public final UnaryCallable<ListMobileDeviceSubmodelsRequest,MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse> listMobileDeviceSubmodelsPagedCallable()

Lists `MobileDeviceSubmodel` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceSubmodelServiceClient mobileDeviceSubmodelServiceClient =
         MobileDeviceSubmodelServiceClient.create()) {
       ListMobileDeviceSubmodelsRequest request =
           ListMobileDeviceSubmodelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<MobileDeviceSubmodel> future =
           mobileDeviceSubmodelServiceClient
               .listMobileDeviceSubmodelsPagedCallable()
               .futureCall(request);
       // Do something.
       for (MobileDeviceSubmodel element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMobileDeviceSubmodelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileDeviceSubmodelsRequest),[ListMobileDeviceSubmodelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceSubmodelServiceClient.ListMobileDeviceSubmodelsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
