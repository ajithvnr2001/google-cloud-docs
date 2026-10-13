---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient
title: Class DeviceManufacturerServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:45.198382+00:00
---

# Class DeviceManufacturerServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DeviceManufacturerServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/DeviceManufacturerServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `DeviceManufacturer` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       DeviceManufacturerName name =
           DeviceManufacturerName.of("[NETWORK_CODE]", "[DEVICE_MANUFACTURER]");
       DeviceManufacturer response = deviceManufacturerServiceClient.getDeviceManufacturer(name);
     }
     

Note: close() needs to be called on the DeviceManufacturerServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetDeviceManufacturer |  Retrieves a `DeviceManufacturer` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDeviceManufacturer(GetDeviceManufacturerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDeviceManufacturer(DeviceManufacturerName name) 
  * getDeviceManufacturer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDeviceManufacturerCallable() 

  
ListDeviceManufacturers |  Lists `DeviceManufacturer` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDeviceManufacturers(ListDeviceManufacturersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDeviceManufacturers(NetworkName parent) 
  * listDeviceManufacturers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDeviceManufacturersPagedCallable() 
  * listDeviceManufacturersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DeviceManufacturerServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeviceManufacturerServiceSettings deviceManufacturerServiceSettings =
         DeviceManufacturerServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create(deviceManufacturerServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeviceManufacturerServiceSettings deviceManufacturerServiceSettings =
         DeviceManufacturerServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create(deviceManufacturerServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DeviceManufacturerServiceClient

## Static Methods 

### create()
    
    
    public static final DeviceManufacturerServiceClient create()

Constructs an instance of DeviceManufacturerServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeviceManufacturerServiceSettings settings)
    
    
    public static final DeviceManufacturerServiceClient create(DeviceManufacturerServiceSettings settings)

Constructs an instance of DeviceManufacturerServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeviceManufacturerServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeviceManufacturerServiceStub stub)
    
    
    public static final DeviceManufacturerServiceClient create(DeviceManufacturerServiceStub stub)

Constructs an instance of DeviceManufacturerServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DeviceManufacturerServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeviceManufacturerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DeviceManufacturerServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient)` |   
  
## Constructors 

### DeviceManufacturerServiceClient(DeviceManufacturerServiceSettings settings)
    
    
    protected DeviceManufacturerServiceClient(DeviceManufacturerServiceSettings settings)

Constructs an instance of DeviceManufacturerServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeviceManufacturerServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceSettings)`  
  
  
### DeviceManufacturerServiceClient(DeviceManufacturerServiceStub stub)
    
    
    protected DeviceManufacturerServiceClient(DeviceManufacturerServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeviceManufacturerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DeviceManufacturerServiceStub)`  
  
  
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

### getDeviceManufacturer(@Nullable DeviceManufacturerName name)
    
    
    public final DeviceManufacturer getDeviceManufacturer(@Nullable DeviceManufacturerName name)

Retrieves a `DeviceManufacturer` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       DeviceManufacturerName name =
           DeviceManufacturerName.of("[NETWORK_CODE]", "[DEVICE_MANUFACTURER]");
       DeviceManufacturer response = deviceManufacturerServiceClient.getDeviceManufacturer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DeviceManufacturerName`  
Required. The resource name of the DeviceManufacturer. Format: `networks/{network_code}/deviceManufacturers/{device_manufacturer_id}`  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturer](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturer)` |   
  
### getDeviceManufacturer(GetDeviceManufacturerRequest request)
    
    
    public final DeviceManufacturer getDeviceManufacturer(GetDeviceManufacturerRequest request)

Retrieves a `DeviceManufacturer` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       GetDeviceManufacturerRequest request =
           GetDeviceManufacturerRequest.newBuilder()
               .setName(
                   DeviceManufacturerName.of("[NETWORK_CODE]", "[DEVICE_MANUFACTURER]").toString())
               .build();
       DeviceManufacturer response = deviceManufacturerServiceClient.getDeviceManufacturer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDeviceManufacturerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDeviceManufacturerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturer](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturer)` |   
  
### getDeviceManufacturer(String name)
    
    
    public final DeviceManufacturer getDeviceManufacturer(String name)

Retrieves a `DeviceManufacturer` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       String name = DeviceManufacturerName.of("[NETWORK_CODE]", "[DEVICE_MANUFACTURER]").toString();
       DeviceManufacturer response = deviceManufacturerServiceClient.getDeviceManufacturer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DeviceManufacturer. Format: `networks/{network_code}/deviceManufacturers/{device_manufacturer_id}`  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturer](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturer)` |   
  
### getDeviceManufacturerCallable()
    
    
    public final UnaryCallable<GetDeviceManufacturerRequest,DeviceManufacturer> getDeviceManufacturerCallable()

Retrieves a `DeviceManufacturer` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       GetDeviceManufacturerRequest request =
           GetDeviceManufacturerRequest.newBuilder()
               .setName(
                   DeviceManufacturerName.of("[NETWORK_CODE]", "[DEVICE_MANUFACTURER]").toString())
               .build();
       ApiFuture<DeviceManufacturer> future =
           deviceManufacturerServiceClient.getDeviceManufacturerCallable().futureCall(request);
       // Do something.
       DeviceManufacturer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDeviceManufacturerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDeviceManufacturerRequest),[DeviceManufacturer](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturer)>` |   
  
### getSettings()
    
    
    public final @Nullable DeviceManufacturerServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DeviceManufacturerServiceSettings` |   
  
### getStub()
    
    
    public DeviceManufacturerServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DeviceManufacturerServiceStub)` |   
  
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
  
### listDeviceManufacturers(@Nullable NetworkName parent)
    
    
    public final DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse listDeviceManufacturers(@Nullable NetworkName parent)

Lists `DeviceManufacturer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (DeviceManufacturer element :
           deviceManufacturerServiceClient.listDeviceManufacturers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of DeviceManufacturers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse)` |   
  
### listDeviceManufacturers(ListDeviceManufacturersRequest request)
    
    
    public final DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse listDeviceManufacturers(ListDeviceManufacturersRequest request)

Lists `DeviceManufacturer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       ListDeviceManufacturersRequest request =
           ListDeviceManufacturersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (DeviceManufacturer element :
           deviceManufacturerServiceClient.listDeviceManufacturers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDeviceManufacturersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDeviceManufacturersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse)` |   
  
### listDeviceManufacturers(String parent)
    
    
    public final DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse listDeviceManufacturers(String parent)

Lists `DeviceManufacturer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (DeviceManufacturer element :
           deviceManufacturerServiceClient.listDeviceManufacturers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of DeviceManufacturers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse)` |   
  
### listDeviceManufacturersCallable()
    
    
    public final UnaryCallable<ListDeviceManufacturersRequest,ListDeviceManufacturersResponse> listDeviceManufacturersCallable()

Lists `DeviceManufacturer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       ListDeviceManufacturersRequest request =
           ListDeviceManufacturersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListDeviceManufacturersResponse response =
             deviceManufacturerServiceClient.listDeviceManufacturersCallable().call(request);
         for (DeviceManufacturer element : response.getDeviceManufacturersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeviceManufacturersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDeviceManufacturersRequest),[ListDeviceManufacturersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDeviceManufacturersResponse)>` |   
  
### listDeviceManufacturersPagedCallable()
    
    
    public final UnaryCallable<ListDeviceManufacturersRequest,DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse> listDeviceManufacturersPagedCallable()

Lists `DeviceManufacturer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManufacturerServiceClient deviceManufacturerServiceClient =
         DeviceManufacturerServiceClient.create()) {
       ListDeviceManufacturersRequest request =
           ListDeviceManufacturersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<DeviceManufacturer> future =
           deviceManufacturerServiceClient
               .listDeviceManufacturersPagedCallable()
               .futureCall(request);
       // Do something.
       for (DeviceManufacturer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeviceManufacturersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDeviceManufacturersRequest),[ListDeviceManufacturersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceManufacturerServiceClient.ListDeviceManufacturersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
