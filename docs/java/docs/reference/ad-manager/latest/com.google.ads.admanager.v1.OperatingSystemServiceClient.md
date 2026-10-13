---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient
title: Class OperatingSystemServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:55.339161+00:00
---

# Class OperatingSystemServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OperatingSystemServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/OperatingSystemServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `OperatingSystem` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       OperatingSystemName name = OperatingSystemName.of("[NETWORK_CODE]", "[OPERATING_SYSTEM]");
       OperatingSystem response = operatingSystemServiceClient.getOperatingSystem(name);
     }
     

Note: close() needs to be called on the OperatingSystemServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetOperatingSystem |  Retrieves a `OperatingSystem` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOperatingSystem(GetOperatingSystemRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOperatingSystem(OperatingSystemName name) 
  * getOperatingSystem(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOperatingSystemCallable() 

  
ListOperatingSystems |  Lists `OperatingSystem` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOperatingSystems(ListOperatingSystemsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOperatingSystems(NetworkName parent) 
  * listOperatingSystems(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOperatingSystemsPagedCallable() 
  * listOperatingSystemsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of OperatingSystemServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OperatingSystemServiceSettings operatingSystemServiceSettings =
         OperatingSystemServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create(operatingSystemServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OperatingSystemServiceSettings operatingSystemServiceSettings =
         OperatingSystemServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create(operatingSystemServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OperatingSystemServiceClient

## Static Methods 

### create()
    
    
    public static final OperatingSystemServiceClient create()

Constructs an instance of OperatingSystemServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[OperatingSystemServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OperatingSystemServiceSettings settings)
    
    
    public static final OperatingSystemServiceClient create(OperatingSystemServiceSettings settings)

Constructs an instance of OperatingSystemServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OperatingSystemServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperatingSystemServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OperatingSystemServiceStub stub)
    
    
    public static final OperatingSystemServiceClient create(OperatingSystemServiceStub stub)

Constructs an instance of OperatingSystemServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(OperatingSystemServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OperatingSystemServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.OperatingSystemServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperatingSystemServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient)` |   
  
## Constructors 

### OperatingSystemServiceClient(OperatingSystemServiceSettings settings)
    
    
    protected OperatingSystemServiceClient(OperatingSystemServiceSettings settings)

Constructs an instance of OperatingSystemServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OperatingSystemServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceSettings)`  
  
  
### OperatingSystemServiceClient(OperatingSystemServiceStub stub)
    
    
    protected OperatingSystemServiceClient(OperatingSystemServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OperatingSystemServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.OperatingSystemServiceStub)`  
  
  
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

### getOperatingSystem(@Nullable OperatingSystemName name)
    
    
    public final OperatingSystem getOperatingSystem(@Nullable OperatingSystemName name)

Retrieves a `OperatingSystem` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       OperatingSystemName name = OperatingSystemName.of("[NETWORK_CODE]", "[OPERATING_SYSTEM]");
       OperatingSystem response = operatingSystemServiceClient.getOperatingSystem(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.OperatingSystemName`  
Required. The resource name of the OperatingSystem. Format: `networks/{network_code}/operatingSystems/{operating_system_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperatingSystem](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystem)` |   
  
### getOperatingSystem(GetOperatingSystemRequest request)
    
    
    public final OperatingSystem getOperatingSystem(GetOperatingSystemRequest request)

Retrieves a `OperatingSystem` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       GetOperatingSystemRequest request =
           GetOperatingSystemRequest.newBuilder()
               .setName(OperatingSystemName.of("[NETWORK_CODE]", "[OPERATING_SYSTEM]").toString())
               .build();
       OperatingSystem response = operatingSystemServiceClient.getOperatingSystem(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOperatingSystemRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetOperatingSystemRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperatingSystem](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystem)` |   
  
### getOperatingSystem(String name)
    
    
    public final OperatingSystem getOperatingSystem(String name)

Retrieves a `OperatingSystem` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       String name = OperatingSystemName.of("[NETWORK_CODE]", "[OPERATING_SYSTEM]").toString();
       OperatingSystem response = operatingSystemServiceClient.getOperatingSystem(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the OperatingSystem. Format: `networks/{network_code}/operatingSystems/{operating_system_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperatingSystem](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystem)` |   
  
### getOperatingSystemCallable()
    
    
    public final UnaryCallable<GetOperatingSystemRequest,OperatingSystem> getOperatingSystemCallable()

Retrieves a `OperatingSystem` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       GetOperatingSystemRequest request =
           GetOperatingSystemRequest.newBuilder()
               .setName(OperatingSystemName.of("[NETWORK_CODE]", "[OPERATING_SYSTEM]").toString())
               .build();
       ApiFuture<OperatingSystem> future =
           operatingSystemServiceClient.getOperatingSystemCallable().futureCall(request);
       // Do something.
       OperatingSystem response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOperatingSystemRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetOperatingSystemRequest),[OperatingSystem](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystem)>` |   
  
### getSettings()
    
    
    public final @Nullable OperatingSystemServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.OperatingSystemServiceSettings` |   
  
### getStub()
    
    
    public OperatingSystemServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[OperatingSystemServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.OperatingSystemServiceStub)` |   
  
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
  
### listOperatingSystems(@Nullable NetworkName parent)
    
    
    public final OperatingSystemServiceClient.ListOperatingSystemsPagedResponse listOperatingSystems(@Nullable NetworkName parent)

Lists `OperatingSystem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (OperatingSystem element :
           operatingSystemServiceClient.listOperatingSystems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of OperatingSystems. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[OperatingSystemServiceClient.ListOperatingSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient.ListOperatingSystemsPagedResponse)` |   
  
### listOperatingSystems(ListOperatingSystemsRequest request)
    
    
    public final OperatingSystemServiceClient.ListOperatingSystemsPagedResponse listOperatingSystems(ListOperatingSystemsRequest request)

Lists `OperatingSystem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       ListOperatingSystemsRequest request =
           ListOperatingSystemsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (OperatingSystem element :
           operatingSystemServiceClient.listOperatingSystems(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOperatingSystemsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOperatingSystemsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperatingSystemServiceClient.ListOperatingSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient.ListOperatingSystemsPagedResponse)` |   
  
### listOperatingSystems(String parent)
    
    
    public final OperatingSystemServiceClient.ListOperatingSystemsPagedResponse listOperatingSystems(String parent)

Lists `OperatingSystem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (OperatingSystem element :
           operatingSystemServiceClient.listOperatingSystems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of OperatingSystems. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[OperatingSystemServiceClient.ListOperatingSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient.ListOperatingSystemsPagedResponse)` |   
  
### listOperatingSystemsCallable()
    
    
    public final UnaryCallable<ListOperatingSystemsRequest,ListOperatingSystemsResponse> listOperatingSystemsCallable()

Lists `OperatingSystem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       ListOperatingSystemsRequest request =
           ListOperatingSystemsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListOperatingSystemsResponse response =
             operatingSystemServiceClient.listOperatingSystemsCallable().call(request);
         for (OperatingSystem element : response.getOperatingSystemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOperatingSystemsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOperatingSystemsRequest),[ListOperatingSystemsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOperatingSystemsResponse)>` |   
  
### listOperatingSystemsPagedCallable()
    
    
    public final UnaryCallable<ListOperatingSystemsRequest,OperatingSystemServiceClient.ListOperatingSystemsPagedResponse> listOperatingSystemsPagedCallable()

Lists `OperatingSystem` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OperatingSystemServiceClient operatingSystemServiceClient =
         OperatingSystemServiceClient.create()) {
       ListOperatingSystemsRequest request =
           ListOperatingSystemsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<OperatingSystem> future =
           operatingSystemServiceClient.listOperatingSystemsPagedCallable().futureCall(request);
       // Do something.
       for (OperatingSystem element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOperatingSystemsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListOperatingSystemsRequest),[ListOperatingSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemServiceClient.ListOperatingSystemsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
