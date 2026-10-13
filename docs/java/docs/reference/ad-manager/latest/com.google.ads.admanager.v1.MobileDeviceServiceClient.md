---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient
title: Class MobileDeviceServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:51.906995+00:00
---

# Class MobileDeviceServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MobileDeviceServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/MobileDeviceServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `MobileDevice` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       MobileDeviceName name = MobileDeviceName.of("[NETWORK_CODE]", "[MOBILE_DEVICE]");
       MobileDevice response = mobileDeviceServiceClient.getMobileDevice(name);
     }
     

Note: close() needs to be called on the MobileDeviceServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetMobileDevice |  Retrieves a `MobileDevice` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMobileDevice(GetMobileDeviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMobileDevice(MobileDeviceName name) 
  * getMobileDevice(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMobileDeviceCallable() 

  
ListMobileDevices |  Lists `MobileDevice` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMobileDevices(ListMobileDevicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMobileDevices(NetworkName parent) 
  * listMobileDevices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMobileDevicesPagedCallable() 
  * listMobileDevicesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MobileDeviceServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MobileDeviceServiceSettings mobileDeviceServiceSettings =
         MobileDeviceServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MobileDeviceServiceClient mobileDeviceServiceClient =
         MobileDeviceServiceClient.create(mobileDeviceServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MobileDeviceServiceSettings mobileDeviceServiceSettings =
         MobileDeviceServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     MobileDeviceServiceClient mobileDeviceServiceClient =
         MobileDeviceServiceClient.create(mobileDeviceServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MobileDeviceServiceClient

## Static Methods 

### create()
    
    
    public static final MobileDeviceServiceClient create()

Constructs an instance of MobileDeviceServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MobileDeviceServiceSettings settings)
    
    
    public static final MobileDeviceServiceClient create(MobileDeviceServiceSettings settings)

Constructs an instance of MobileDeviceServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MobileDeviceServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MobileDeviceServiceStub stub)
    
    
    public static final MobileDeviceServiceClient create(MobileDeviceServiceStub stub)

Constructs an instance of MobileDeviceServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(MobileDeviceServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MobileDeviceServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileDeviceServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient)` |   
  
## Constructors 

### MobileDeviceServiceClient(MobileDeviceServiceSettings settings)
    
    
    protected MobileDeviceServiceClient(MobileDeviceServiceSettings settings)

Constructs an instance of MobileDeviceServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MobileDeviceServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceSettings)`  
  
  
### MobileDeviceServiceClient(MobileDeviceServiceStub stub)
    
    
    protected MobileDeviceServiceClient(MobileDeviceServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MobileDeviceServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileDeviceServiceStub)`  
  
  
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

### getMobileDevice(@Nullable MobileDeviceName name)
    
    
    public final MobileDevice getMobileDevice(@Nullable MobileDeviceName name)

Retrieves a `MobileDevice` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       MobileDeviceName name = MobileDeviceName.of("[NETWORK_CODE]", "[MOBILE_DEVICE]");
       MobileDevice response = mobileDeviceServiceClient.getMobileDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.MobileDeviceName`  
Required. The resource name of the MobileDevice. Format: `networks/{network_code}/mobileDevices/{mobile_device_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileDevice](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDevice)` |   
  
### getMobileDevice(GetMobileDeviceRequest request)
    
    
    public final MobileDevice getMobileDevice(GetMobileDeviceRequest request)

Retrieves a `MobileDevice` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       GetMobileDeviceRequest request =
           GetMobileDeviceRequest.newBuilder()
               .setName(MobileDeviceName.of("[NETWORK_CODE]", "[MOBILE_DEVICE]").toString())
               .build();
       MobileDevice response = mobileDeviceServiceClient.getMobileDevice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMobileDeviceRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetMobileDeviceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MobileDevice](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDevice)` |   
  
### getMobileDevice(String name)
    
    
    public final MobileDevice getMobileDevice(String name)

Retrieves a `MobileDevice` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       String name = MobileDeviceName.of("[NETWORK_CODE]", "[MOBILE_DEVICE]").toString();
       MobileDevice response = mobileDeviceServiceClient.getMobileDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MobileDevice. Format: `networks/{network_code}/mobileDevices/{mobile_device_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileDevice](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDevice)` |   
  
### getMobileDeviceCallable()
    
    
    public final UnaryCallable<GetMobileDeviceRequest,MobileDevice> getMobileDeviceCallable()

Retrieves a `MobileDevice` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       GetMobileDeviceRequest request =
           GetMobileDeviceRequest.newBuilder()
               .setName(MobileDeviceName.of("[NETWORK_CODE]", "[MOBILE_DEVICE]").toString())
               .build();
       ApiFuture<MobileDevice> future =
           mobileDeviceServiceClient.getMobileDeviceCallable().futureCall(request);
       // Do something.
       MobileDevice response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMobileDeviceRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetMobileDeviceRequest),[MobileDevice](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDevice)>` |   
  
### getSettings()
    
    
    public final @Nullable MobileDeviceServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.MobileDeviceServiceSettings` |   
  
### getStub()
    
    
    public MobileDeviceServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileDeviceServiceStub)` |   
  
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
  
### listMobileDevices(@Nullable NetworkName parent)
    
    
    public final MobileDeviceServiceClient.ListMobileDevicesPagedResponse listMobileDevices(@Nullable NetworkName parent)

Lists `MobileDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (MobileDevice element :
           mobileDeviceServiceClient.listMobileDevices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of MobileDevices. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceServiceClient.ListMobileDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient.ListMobileDevicesPagedResponse)` |   
  
### listMobileDevices(ListMobileDevicesRequest request)
    
    
    public final MobileDeviceServiceClient.ListMobileDevicesPagedResponse listMobileDevices(ListMobileDevicesRequest request)

Lists `MobileDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       ListMobileDevicesRequest request =
           ListMobileDevicesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (MobileDevice element :
           mobileDeviceServiceClient.listMobileDevices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMobileDevicesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileDevicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceServiceClient.ListMobileDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient.ListMobileDevicesPagedResponse)` |   
  
### listMobileDevices(String parent)
    
    
    public final MobileDeviceServiceClient.ListMobileDevicesPagedResponse listMobileDevices(String parent)

Lists `MobileDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (MobileDevice element :
           mobileDeviceServiceClient.listMobileDevices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of MobileDevices. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileDeviceServiceClient.ListMobileDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient.ListMobileDevicesPagedResponse)` |   
  
### listMobileDevicesCallable()
    
    
    public final UnaryCallable<ListMobileDevicesRequest,ListMobileDevicesResponse> listMobileDevicesCallable()

Lists `MobileDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       ListMobileDevicesRequest request =
           ListMobileDevicesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListMobileDevicesResponse response =
             mobileDeviceServiceClient.listMobileDevicesCallable().call(request);
         for (MobileDevice element : response.getMobileDevicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMobileDevicesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileDevicesRequest),[ListMobileDevicesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileDevicesResponse)>` |   
  
### listMobileDevicesPagedCallable()
    
    
    public final UnaryCallable<ListMobileDevicesRequest,MobileDeviceServiceClient.ListMobileDevicesPagedResponse> listMobileDevicesPagedCallable()

Lists `MobileDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileDeviceServiceClient mobileDeviceServiceClient = MobileDeviceServiceClient.create()) {
       ListMobileDevicesRequest request =
           ListMobileDevicesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<MobileDevice> future =
           mobileDeviceServiceClient.listMobileDevicesPagedCallable().futureCall(request);
       // Do something.
       for (MobileDevice element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMobileDevicesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileDevicesRequest),[ListMobileDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileDeviceServiceClient.ListMobileDevicesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
