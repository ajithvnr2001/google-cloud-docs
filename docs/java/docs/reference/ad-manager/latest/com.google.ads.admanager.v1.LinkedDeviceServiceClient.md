---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient
title: Class LinkedDeviceServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:48.995983+00:00
---

# Class LinkedDeviceServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LinkedDeviceServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/LinkedDeviceServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `LinkedDevice` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       LinkedDeviceName name = LinkedDeviceName.of("[NETWORK_CODE]", "[LINKED_DEVICE]");
       LinkedDevice response = linkedDeviceServiceClient.getLinkedDevice(name);
     }
     

Note: close() needs to be called on the LinkedDeviceServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetLinkedDevice |  Gets a `LinkedDevice`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLinkedDevice(GetLinkedDeviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLinkedDevice(LinkedDeviceName name) 
  * getLinkedDevice(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLinkedDeviceCallable() 

  
ListLinkedDevices |  Lists `LinkedDevice` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLinkedDevices(ListLinkedDevicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLinkedDevices(NetworkName parent) 
  * listLinkedDevices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLinkedDevicesPagedCallable() 
  * listLinkedDevicesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LinkedDeviceServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LinkedDeviceServiceSettings linkedDeviceServiceSettings =
         LinkedDeviceServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LinkedDeviceServiceClient linkedDeviceServiceClient =
         LinkedDeviceServiceClient.create(linkedDeviceServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LinkedDeviceServiceSettings linkedDeviceServiceSettings =
         LinkedDeviceServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     LinkedDeviceServiceClient linkedDeviceServiceClient =
         LinkedDeviceServiceClient.create(linkedDeviceServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LinkedDeviceServiceClient

## Static Methods 

### create()
    
    
    public static final LinkedDeviceServiceClient create()

Constructs an instance of LinkedDeviceServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LinkedDeviceServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LinkedDeviceServiceSettings settings)
    
    
    public static final LinkedDeviceServiceClient create(LinkedDeviceServiceSettings settings)

Constructs an instance of LinkedDeviceServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LinkedDeviceServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LinkedDeviceServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LinkedDeviceServiceStub stub)
    
    
    public static final LinkedDeviceServiceClient create(LinkedDeviceServiceStub stub)

Constructs an instance of LinkedDeviceServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(LinkedDeviceServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LinkedDeviceServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LinkedDeviceServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LinkedDeviceServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient)` |   
  
## Constructors 

### LinkedDeviceServiceClient(LinkedDeviceServiceSettings settings)
    
    
    protected LinkedDeviceServiceClient(LinkedDeviceServiceSettings settings)

Constructs an instance of LinkedDeviceServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LinkedDeviceServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceSettings)`  
  
  
### LinkedDeviceServiceClient(LinkedDeviceServiceStub stub)
    
    
    protected LinkedDeviceServiceClient(LinkedDeviceServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LinkedDeviceServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LinkedDeviceServiceStub)`  
  
  
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

### getLinkedDevice(@Nullable LinkedDeviceName name)
    
    
    public final LinkedDevice getLinkedDevice(@Nullable LinkedDeviceName name)

Gets a `LinkedDevice`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       LinkedDeviceName name = LinkedDeviceName.of("[NETWORK_CODE]", "[LINKED_DEVICE]");
       LinkedDevice response = linkedDeviceServiceClient.getLinkedDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LinkedDeviceName`  
Required. The resource name of the LinkedDevice. Format: `networks/{network_code}/linkedDevices/{linked_device_id}`  
**Returns**  
---  
**Type** | **Description**  
`[LinkedDevice](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDevice)` |   
  
### getLinkedDevice(GetLinkedDeviceRequest request)
    
    
    public final LinkedDevice getLinkedDevice(GetLinkedDeviceRequest request)

Gets a `LinkedDevice`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       GetLinkedDeviceRequest request =
           GetLinkedDeviceRequest.newBuilder()
               .setName(LinkedDeviceName.of("[NETWORK_CODE]", "[LINKED_DEVICE]").toString())
               .build();
       LinkedDevice response = linkedDeviceServiceClient.getLinkedDevice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLinkedDeviceRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetLinkedDeviceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LinkedDevice](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDevice)` |   
  
### getLinkedDevice(String name)
    
    
    public final LinkedDevice getLinkedDevice(String name)

Gets a `LinkedDevice`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       String name = LinkedDeviceName.of("[NETWORK_CODE]", "[LINKED_DEVICE]").toString();
       LinkedDevice response = linkedDeviceServiceClient.getLinkedDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the LinkedDevice. Format: `networks/{network_code}/linkedDevices/{linked_device_id}`  
**Returns**  
---  
**Type** | **Description**  
`[LinkedDevice](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDevice)` |   
  
### getLinkedDeviceCallable()
    
    
    public final UnaryCallable<GetLinkedDeviceRequest,LinkedDevice> getLinkedDeviceCallable()

Gets a `LinkedDevice`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       GetLinkedDeviceRequest request =
           GetLinkedDeviceRequest.newBuilder()
               .setName(LinkedDeviceName.of("[NETWORK_CODE]", "[LINKED_DEVICE]").toString())
               .build();
       ApiFuture<LinkedDevice> future =
           linkedDeviceServiceClient.getLinkedDeviceCallable().futureCall(request);
       // Do something.
       LinkedDevice response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLinkedDeviceRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetLinkedDeviceRequest),[LinkedDevice](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDevice)>` |   
  
### getSettings()
    
    
    public final @Nullable LinkedDeviceServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LinkedDeviceServiceSettings` |   
  
### getStub()
    
    
    public LinkedDeviceServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LinkedDeviceServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LinkedDeviceServiceStub)` |   
  
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
  
### listLinkedDevices(@Nullable NetworkName parent)
    
    
    public final LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse listLinkedDevices(@Nullable NetworkName parent)

Lists `LinkedDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (LinkedDevice element :
           linkedDeviceServiceClient.listLinkedDevices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of LinkedDevices. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse)` |   
  
### listLinkedDevices(ListLinkedDevicesRequest request)
    
    
    public final LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse listLinkedDevices(ListLinkedDevicesRequest request)

Lists `LinkedDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       ListLinkedDevicesRequest request =
           ListLinkedDevicesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (LinkedDevice element :
           linkedDeviceServiceClient.listLinkedDevices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLinkedDevicesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLinkedDevicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse)` |   
  
### listLinkedDevices(String parent)
    
    
    public final LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse listLinkedDevices(String parent)

Lists `LinkedDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (LinkedDevice element :
           linkedDeviceServiceClient.listLinkedDevices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of LinkedDevices. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse)` |   
  
### listLinkedDevicesCallable()
    
    
    public final UnaryCallable<ListLinkedDevicesRequest,ListLinkedDevicesResponse> listLinkedDevicesCallable()

Lists `LinkedDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       ListLinkedDevicesRequest request =
           ListLinkedDevicesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListLinkedDevicesResponse response =
             linkedDeviceServiceClient.listLinkedDevicesCallable().call(request);
         for (LinkedDevice element : response.getLinkedDevicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLinkedDevicesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLinkedDevicesRequest),[ListLinkedDevicesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLinkedDevicesResponse)>` |   
  
### listLinkedDevicesPagedCallable()
    
    
    public final UnaryCallable<ListLinkedDevicesRequest,LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse> listLinkedDevicesPagedCallable()

Lists `LinkedDevice` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LinkedDeviceServiceClient linkedDeviceServiceClient = LinkedDeviceServiceClient.create()) {
       ListLinkedDevicesRequest request =
           ListLinkedDevicesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<LinkedDevice> future =
           linkedDeviceServiceClient.listLinkedDevicesPagedCallable().futureCall(request);
       // Do something.
       for (LinkedDevice element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLinkedDevicesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLinkedDevicesRequest),[ListLinkedDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LinkedDeviceServiceClient.ListLinkedDevicesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
