---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient
title: Class DeviceCapabilityServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:46.558881+00:00
---

# Class DeviceCapabilityServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DeviceCapabilityServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/DeviceCapabilityServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `DeviceCapability` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       DeviceCapabilityName name = DeviceCapabilityName.of("[NETWORK_CODE]", "[DEVICE_CAPABILITY]");
       DeviceCapability response = deviceCapabilityServiceClient.getDeviceCapability(name);
     }
     

Note: close() needs to be called on the DeviceCapabilityServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetDeviceCapability |  Retrieves a `DeviceCapability` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDeviceCapability(GetDeviceCapabilityRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDeviceCapability(DeviceCapabilityName name) 
  * getDeviceCapability(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDeviceCapabilityCallable() 

  
ListDeviceCapabilities |  Lists `DeviceCapability` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDeviceCapabilities(ListDeviceCapabilitiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDeviceCapabilities(NetworkName parent) 
  * listDeviceCapabilities(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDeviceCapabilitiesPagedCallable() 
  * listDeviceCapabilitiesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DeviceCapabilityServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeviceCapabilityServiceSettings deviceCapabilityServiceSettings =
         DeviceCapabilityServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create(deviceCapabilityServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeviceCapabilityServiceSettings deviceCapabilityServiceSettings =
         DeviceCapabilityServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create(deviceCapabilityServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DeviceCapabilityServiceClient

## Static Methods 

### create()
    
    
    public static final DeviceCapabilityServiceClient create()

Constructs an instance of DeviceCapabilityServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DeviceCapabilityServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeviceCapabilityServiceSettings settings)
    
    
    public static final DeviceCapabilityServiceClient create(DeviceCapabilityServiceSettings settings)

Constructs an instance of DeviceCapabilityServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeviceCapabilityServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeviceCapabilityServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeviceCapabilityServiceStub stub)
    
    
    public static final DeviceCapabilityServiceClient create(DeviceCapabilityServiceStub stub)

Constructs an instance of DeviceCapabilityServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DeviceCapabilityServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeviceCapabilityServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DeviceCapabilityServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeviceCapabilityServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient)` |   
  
## Constructors 

### DeviceCapabilityServiceClient(DeviceCapabilityServiceSettings settings)
    
    
    protected DeviceCapabilityServiceClient(DeviceCapabilityServiceSettings settings)

Constructs an instance of DeviceCapabilityServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeviceCapabilityServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceSettings)`  
  
  
### DeviceCapabilityServiceClient(DeviceCapabilityServiceStub stub)
    
    
    protected DeviceCapabilityServiceClient(DeviceCapabilityServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeviceCapabilityServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DeviceCapabilityServiceStub)`  
  
  
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

### getDeviceCapability(@Nullable DeviceCapabilityName name)
    
    
    public final DeviceCapability getDeviceCapability(@Nullable DeviceCapabilityName name)

Retrieves a `DeviceCapability` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       DeviceCapabilityName name = DeviceCapabilityName.of("[NETWORK_CODE]", "[DEVICE_CAPABILITY]");
       DeviceCapability response = deviceCapabilityServiceClient.getDeviceCapability(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DeviceCapabilityName`  
Required. The resource name of the DeviceCapability. Format: `networks/{network_code}/deviceCapabilities/{device_capability_id}`  
**Returns**  
---  
**Type** | **Description**  
`[DeviceCapability](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapability)` |   
  
### getDeviceCapability(GetDeviceCapabilityRequest request)
    
    
    public final DeviceCapability getDeviceCapability(GetDeviceCapabilityRequest request)

Retrieves a `DeviceCapability` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       GetDeviceCapabilityRequest request =
           GetDeviceCapabilityRequest.newBuilder()
               .setName(DeviceCapabilityName.of("[NETWORK_CODE]", "[DEVICE_CAPABILITY]").toString())
               .build();
       DeviceCapability response = deviceCapabilityServiceClient.getDeviceCapability(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDeviceCapabilityRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDeviceCapabilityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceCapability](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapability)` |   
  
### getDeviceCapability(String name)
    
    
    public final DeviceCapability getDeviceCapability(String name)

Retrieves a `DeviceCapability` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       String name = DeviceCapabilityName.of("[NETWORK_CODE]", "[DEVICE_CAPABILITY]").toString();
       DeviceCapability response = deviceCapabilityServiceClient.getDeviceCapability(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DeviceCapability. Format: `networks/{network_code}/deviceCapabilities/{device_capability_id}`  
**Returns**  
---  
**Type** | **Description**  
`[DeviceCapability](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapability)` |   
  
### getDeviceCapabilityCallable()
    
    
    public final UnaryCallable<GetDeviceCapabilityRequest,DeviceCapability> getDeviceCapabilityCallable()

Retrieves a `DeviceCapability` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       GetDeviceCapabilityRequest request =
           GetDeviceCapabilityRequest.newBuilder()
               .setName(DeviceCapabilityName.of("[NETWORK_CODE]", "[DEVICE_CAPABILITY]").toString())
               .build();
       ApiFuture<DeviceCapability> future =
           deviceCapabilityServiceClient.getDeviceCapabilityCallable().futureCall(request);
       // Do something.
       DeviceCapability response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDeviceCapabilityRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDeviceCapabilityRequest),[DeviceCapability](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapability)>` |   
  
### getSettings()
    
    
    public final @Nullable DeviceCapabilityServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DeviceCapabilityServiceSettings` |   
  
### getStub()
    
    
    public DeviceCapabilityServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DeviceCapabilityServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DeviceCapabilityServiceStub)` |   
  
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
  
### listDeviceCapabilities(@Nullable NetworkName parent)
    
    
    public final DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse listDeviceCapabilities(@Nullable NetworkName parent)

Lists `DeviceCapability` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (DeviceCapability element :
           deviceCapabilityServiceClient.listDeviceCapabilities(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of DeviceCapabilities. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse)` |   
  
### listDeviceCapabilities(ListDeviceCapabilitiesRequest request)
    
    
    public final DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse listDeviceCapabilities(ListDeviceCapabilitiesRequest request)

Lists `DeviceCapability` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       ListDeviceCapabilitiesRequest request =
           ListDeviceCapabilitiesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (DeviceCapability element :
           deviceCapabilityServiceClient.listDeviceCapabilities(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDeviceCapabilitiesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDeviceCapabilitiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse)` |   
  
### listDeviceCapabilities(String parent)
    
    
    public final DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse listDeviceCapabilities(String parent)

Lists `DeviceCapability` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (DeviceCapability element :
           deviceCapabilityServiceClient.listDeviceCapabilities(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of DeviceCapabilities. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse)` |   
  
### listDeviceCapabilitiesCallable()
    
    
    public final UnaryCallable<ListDeviceCapabilitiesRequest,ListDeviceCapabilitiesResponse> listDeviceCapabilitiesCallable()

Lists `DeviceCapability` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       ListDeviceCapabilitiesRequest request =
           ListDeviceCapabilitiesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListDeviceCapabilitiesResponse response =
             deviceCapabilityServiceClient.listDeviceCapabilitiesCallable().call(request);
         for (DeviceCapability element : response.getDeviceCapabilitiesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeviceCapabilitiesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDeviceCapabilitiesRequest),[ListDeviceCapabilitiesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDeviceCapabilitiesResponse)>` |   
  
### listDeviceCapabilitiesPagedCallable()
    
    
    public final UnaryCallable<ListDeviceCapabilitiesRequest,DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse> listDeviceCapabilitiesPagedCallable()

Lists `DeviceCapability` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceCapabilityServiceClient deviceCapabilityServiceClient =
         DeviceCapabilityServiceClient.create()) {
       ListDeviceCapabilitiesRequest request =
           ListDeviceCapabilitiesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<DeviceCapability> future =
           deviceCapabilityServiceClient.listDeviceCapabilitiesPagedCallable().futureCall(request);
       // Do something.
       for (DeviceCapability element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeviceCapabilitiesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDeviceCapabilitiesRequest),[ListDeviceCapabilitiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeviceCapabilityServiceClient.ListDeviceCapabilitiesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
