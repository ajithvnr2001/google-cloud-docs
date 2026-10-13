---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient
title: Class ProgrammaticBuyerServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:00.347491+00:00
---

# Class ProgrammaticBuyerServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProgrammaticBuyerServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ProgrammaticBuyerServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `ProgrammaticBuyer` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       ProgrammaticBuyerName name =
           ProgrammaticBuyerName.of("[NETWORK_CODE]", "[PROGRAMMATIC_BUYER]");
       ProgrammaticBuyer response = programmaticBuyerServiceClient.getProgrammaticBuyer(name);
     }
     

Note: close() needs to be called on the ProgrammaticBuyerServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetProgrammaticBuyer |  Retrieves a `ProgrammaticBuyer` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProgrammaticBuyer(GetProgrammaticBuyerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProgrammaticBuyer(ProgrammaticBuyerName name) 
  * getProgrammaticBuyer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProgrammaticBuyerCallable() 

  
ListProgrammaticBuyers |  Lists `ProgrammaticBuyer` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProgrammaticBuyers(ListProgrammaticBuyersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProgrammaticBuyers(NetworkName parent) 
  * listProgrammaticBuyers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProgrammaticBuyersPagedCallable() 
  * listProgrammaticBuyersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ProgrammaticBuyerServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProgrammaticBuyerServiceSettings programmaticBuyerServiceSettings =
         ProgrammaticBuyerServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create(programmaticBuyerServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProgrammaticBuyerServiceSettings programmaticBuyerServiceSettings =
         ProgrammaticBuyerServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create(programmaticBuyerServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ProgrammaticBuyerServiceClient

## Static Methods 

### create()
    
    
    public static final ProgrammaticBuyerServiceClient create()

Constructs an instance of ProgrammaticBuyerServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProgrammaticBuyerServiceSettings settings)
    
    
    public static final ProgrammaticBuyerServiceClient create(ProgrammaticBuyerServiceSettings settings)

Constructs an instance of ProgrammaticBuyerServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProgrammaticBuyerServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProgrammaticBuyerServiceStub stub)
    
    
    public static final ProgrammaticBuyerServiceClient create(ProgrammaticBuyerServiceStub stub)

Constructs an instance of ProgrammaticBuyerServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ProgrammaticBuyerServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProgrammaticBuyerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ProgrammaticBuyerServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient)` |   
  
## Constructors 

### ProgrammaticBuyerServiceClient(ProgrammaticBuyerServiceSettings settings)
    
    
    protected ProgrammaticBuyerServiceClient(ProgrammaticBuyerServiceSettings settings)

Constructs an instance of ProgrammaticBuyerServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProgrammaticBuyerServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceSettings)`  
  
  
### ProgrammaticBuyerServiceClient(ProgrammaticBuyerServiceStub stub)
    
    
    protected ProgrammaticBuyerServiceClient(ProgrammaticBuyerServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProgrammaticBuyerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ProgrammaticBuyerServiceStub)`  
  
  
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

### getProgrammaticBuyer(@Nullable ProgrammaticBuyerName name)
    
    
    public final ProgrammaticBuyer getProgrammaticBuyer(@Nullable ProgrammaticBuyerName name)

Retrieves a `ProgrammaticBuyer` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       ProgrammaticBuyerName name =
           ProgrammaticBuyerName.of("[NETWORK_CODE]", "[PROGRAMMATIC_BUYER]");
       ProgrammaticBuyer response = programmaticBuyerServiceClient.getProgrammaticBuyer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ProgrammaticBuyerName`  
Required. The resource name of the ProgrammaticBuyer. Format: `networks/{network_code}/programmaticBuyers/{buyer_account_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyer](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyer)` |   
  
### getProgrammaticBuyer(GetProgrammaticBuyerRequest request)
    
    
    public final ProgrammaticBuyer getProgrammaticBuyer(GetProgrammaticBuyerRequest request)

Retrieves a `ProgrammaticBuyer` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       GetProgrammaticBuyerRequest request =
           GetProgrammaticBuyerRequest.newBuilder()
               .setName(
                   ProgrammaticBuyerName.of("[NETWORK_CODE]", "[PROGRAMMATIC_BUYER]").toString())
               .build();
       ProgrammaticBuyer response = programmaticBuyerServiceClient.getProgrammaticBuyer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProgrammaticBuyerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetProgrammaticBuyerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyer](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyer)` |   
  
### getProgrammaticBuyer(String name)
    
    
    public final ProgrammaticBuyer getProgrammaticBuyer(String name)

Retrieves a `ProgrammaticBuyer` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       String name = ProgrammaticBuyerName.of("[NETWORK_CODE]", "[PROGRAMMATIC_BUYER]").toString();
       ProgrammaticBuyer response = programmaticBuyerServiceClient.getProgrammaticBuyer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ProgrammaticBuyer. Format: `networks/{network_code}/programmaticBuyers/{buyer_account_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyer](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyer)` |   
  
### getProgrammaticBuyerCallable()
    
    
    public final UnaryCallable<GetProgrammaticBuyerRequest,ProgrammaticBuyer> getProgrammaticBuyerCallable()

Retrieves a `ProgrammaticBuyer` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       GetProgrammaticBuyerRequest request =
           GetProgrammaticBuyerRequest.newBuilder()
               .setName(
                   ProgrammaticBuyerName.of("[NETWORK_CODE]", "[PROGRAMMATIC_BUYER]").toString())
               .build();
       ApiFuture<ProgrammaticBuyer> future =
           programmaticBuyerServiceClient.getProgrammaticBuyerCallable().futureCall(request);
       // Do something.
       ProgrammaticBuyer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProgrammaticBuyerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetProgrammaticBuyerRequest),[ProgrammaticBuyer](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyer)>` |   
  
### getSettings()
    
    
    public final @Nullable ProgrammaticBuyerServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ProgrammaticBuyerServiceSettings` |   
  
### getStub()
    
    
    public ProgrammaticBuyerServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ProgrammaticBuyerServiceStub)` |   
  
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
  
### listProgrammaticBuyers(@Nullable NetworkName parent)
    
    
    public final ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse listProgrammaticBuyers(@Nullable NetworkName parent)

Lists `ProgrammaticBuyer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (ProgrammaticBuyer element :
           programmaticBuyerServiceClient.listProgrammaticBuyers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of ProgrammaticBuyers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse)` |   
  
### listProgrammaticBuyers(ListProgrammaticBuyersRequest request)
    
    
    public final ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse listProgrammaticBuyers(ListProgrammaticBuyersRequest request)

Lists `ProgrammaticBuyer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       ListProgrammaticBuyersRequest request =
           ListProgrammaticBuyersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (ProgrammaticBuyer element :
           programmaticBuyerServiceClient.listProgrammaticBuyers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProgrammaticBuyersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListProgrammaticBuyersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse)` |   
  
### listProgrammaticBuyers(String parent)
    
    
    public final ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse listProgrammaticBuyers(String parent)

Lists `ProgrammaticBuyer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (ProgrammaticBuyer element :
           programmaticBuyerServiceClient.listProgrammaticBuyers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of ProgrammaticBuyers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse)` |   
  
### listProgrammaticBuyersCallable()
    
    
    public final UnaryCallable<ListProgrammaticBuyersRequest,ListProgrammaticBuyersResponse> listProgrammaticBuyersCallable()

Lists `ProgrammaticBuyer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       ListProgrammaticBuyersRequest request =
           ListProgrammaticBuyersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListProgrammaticBuyersResponse response =
             programmaticBuyerServiceClient.listProgrammaticBuyersCallable().call(request);
         for (ProgrammaticBuyer element : response.getProgrammaticBuyersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProgrammaticBuyersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListProgrammaticBuyersRequest),[ListProgrammaticBuyersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListProgrammaticBuyersResponse)>` |   
  
### listProgrammaticBuyersPagedCallable()
    
    
    public final UnaryCallable<ListProgrammaticBuyersRequest,ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse> listProgrammaticBuyersPagedCallable()

Lists `ProgrammaticBuyer` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProgrammaticBuyerServiceClient programmaticBuyerServiceClient =
         ProgrammaticBuyerServiceClient.create()) {
       ListProgrammaticBuyersRequest request =
           ListProgrammaticBuyersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<ProgrammaticBuyer> future =
           programmaticBuyerServiceClient.listProgrammaticBuyersPagedCallable().futureCall(request);
       // Do something.
       for (ProgrammaticBuyer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProgrammaticBuyersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListProgrammaticBuyersRequest),[ListProgrammaticBuyersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ProgrammaticBuyerServiceClient.ListProgrammaticBuyersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
