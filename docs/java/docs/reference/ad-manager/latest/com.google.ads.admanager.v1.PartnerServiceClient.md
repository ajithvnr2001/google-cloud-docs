---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient
title: Class PartnerServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:58.375764+00:00
---

# Class PartnerServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PartnerServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/PartnerServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling Partner objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       PartnerName name = PartnerName.of("[NETWORK_CODE]", "[PARTNER]");
       Partner response = partnerServiceClient.getPartner(name);
     }
     

Note: close() needs to be called on the PartnerServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetPartner |  Retrieves a Partner object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPartner(GetPartnerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPartner(PartnerName name) 
  * getPartner(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPartnerCallable() 

  
ListPartners |  Lists Partner objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPartners(ListPartnersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPartners(NetworkName parent) 
  * listPartners(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPartnersPagedCallable() 
  * listPartnersCallable() 

  
UpdatePartner |  Updates a Partner object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePartner(UpdatePartnerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePartner(Partner partner, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePartnerCallable() 

  
BatchUpdatePartners |  Batch updates Partner objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdatePartners(NetworkName parent, List<UpdatePartnerRequest> requests) 
  * batchUpdatePartners(String parent, List<UpdatePartnerRequest> requests) 
  * batchUpdatePartners(BatchUpdatePartnersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdatePartnersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PartnerServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PartnerServiceSettings partnerServiceSettings =
         PartnerServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PartnerServiceClient partnerServiceClient = PartnerServiceClient.create(partnerServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PartnerServiceSettings partnerServiceSettings =
         PartnerServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PartnerServiceClient partnerServiceClient = PartnerServiceClient.create(partnerServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PartnerServiceClient

## Static Methods 

### create()
    
    
    public static final PartnerServiceClient create()

Constructs an instance of PartnerServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PartnerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PartnerServiceSettings settings)
    
    
    public static final PartnerServiceClient create(PartnerServiceSettings settings)

Constructs an instance of PartnerServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PartnerServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PartnerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PartnerServiceStub stub)
    
    
    public static final PartnerServiceClient create(PartnerServiceStub stub)

Constructs an instance of PartnerServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PartnerServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PartnerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PartnerServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PartnerServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient)` |   
  
## Constructors 

### PartnerServiceClient(PartnerServiceSettings settings)
    
    
    protected PartnerServiceClient(PartnerServiceSettings settings)

Constructs an instance of PartnerServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PartnerServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceSettings)`  
  
  
### PartnerServiceClient(PartnerServiceStub stub)
    
    
    protected PartnerServiceClient(PartnerServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PartnerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PartnerServiceStub)`  
  
  
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
  
### batchUpdatePartners(@Nullable NetworkName parent, List<UpdatePartnerRequest> requests)
    
    
    public final BatchUpdatePartnersResponse batchUpdatePartners(@Nullable NetworkName parent, List<UpdatePartnerRequest> requests)

Batch updates Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdatePartnerRequest> requests = new ArrayList<>();
       BatchUpdatePartnersResponse response =
           partnerServiceClient.batchUpdatePartners(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where Partners will be updated. Format: `networks/{network_code}` The parent field in the UpdatePartnerRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdatePartnerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePartnerRequest)>`  
Required. The Partner objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePartnersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePartnersResponse)` |   
  
### batchUpdatePartners(BatchUpdatePartnersRequest request)
    
    
    public final BatchUpdatePartnersResponse batchUpdatePartners(BatchUpdatePartnersRequest request)

Batch updates Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       BatchUpdatePartnersRequest request =
           BatchUpdatePartnersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdatePartnerRequest>())
               .build();
       BatchUpdatePartnersResponse response = partnerServiceClient.batchUpdatePartners(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdatePartnersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePartnersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePartnersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePartnersResponse)` |   
  
### batchUpdatePartners(String parent, List<UpdatePartnerRequest> requests)
    
    
    public final BatchUpdatePartnersResponse batchUpdatePartners(String parent, List<UpdatePartnerRequest> requests)

Batch updates Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdatePartnerRequest> requests = new ArrayList<>();
       BatchUpdatePartnersResponse response =
           partnerServiceClient.batchUpdatePartners(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where Partners will be updated. Format: `networks/{network_code}` The parent field in the UpdatePartnerRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdatePartnerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePartnerRequest)>`  
Required. The Partner objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdatePartnersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePartnersResponse)` |   
  
### batchUpdatePartnersCallable()
    
    
    public final UnaryCallable<BatchUpdatePartnersRequest,BatchUpdatePartnersResponse> batchUpdatePartnersCallable()

Batch updates Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       BatchUpdatePartnersRequest request =
           BatchUpdatePartnersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdatePartnerRequest>())
               .build();
       ApiFuture<BatchUpdatePartnersResponse> future =
           partnerServiceClient.batchUpdatePartnersCallable().futureCall(request);
       // Do something.
       BatchUpdatePartnersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdatePartnersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePartnersRequest),[BatchUpdatePartnersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdatePartnersResponse)>` |   
  
### close()
    
    
    public final void close()

### getPartner(@Nullable PartnerName name)
    
    
    public final Partner getPartner(@Nullable PartnerName name)

Retrieves a Partner object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       PartnerName name = PartnerName.of("[NETWORK_CODE]", "[PARTNER]");
       Partner response = partnerServiceClient.getPartner(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.PartnerName`  
Required. The resource name of the Partner. Format: `networks/{network_code}/partners/{partner_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Partner](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Partner)` |   
  
### getPartner(GetPartnerRequest request)
    
    
    public final Partner getPartner(GetPartnerRequest request)

Retrieves a Partner object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       GetPartnerRequest request =
           GetPartnerRequest.newBuilder()
               .setName(PartnerName.of("[NETWORK_CODE]", "[PARTNER]").toString())
               .build();
       Partner response = partnerServiceClient.getPartner(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPartnerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetPartnerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Partner](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Partner)` |   
  
### getPartner(String name)
    
    
    public final Partner getPartner(String name)

Retrieves a Partner object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       String name = PartnerName.of("[NETWORK_CODE]", "[PARTNER]").toString();
       Partner response = partnerServiceClient.getPartner(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Partner. Format: `networks/{network_code}/partners/{partner_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Partner](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Partner)` |   
  
### getPartnerCallable()
    
    
    public final UnaryCallable<GetPartnerRequest,Partner> getPartnerCallable()

Retrieves a Partner object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       GetPartnerRequest request =
           GetPartnerRequest.newBuilder()
               .setName(PartnerName.of("[NETWORK_CODE]", "[PARTNER]").toString())
               .build();
       ApiFuture<Partner> future = partnerServiceClient.getPartnerCallable().futureCall(request);
       // Do something.
       Partner response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPartnerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetPartnerRequest),[Partner](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Partner)>` |   
  
### getSettings()
    
    
    public final @Nullable PartnerServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.PartnerServiceSettings` |   
  
### getStub()
    
    
    public PartnerServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PartnerServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.PartnerServiceStub)` |   
  
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
  
### listPartners(@Nullable NetworkName parent)
    
    
    public final PartnerServiceClient.ListPartnersPagedResponse listPartners(@Nullable NetworkName parent)

Lists Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Partner element : partnerServiceClient.listPartners(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Partners. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[PartnerServiceClient.ListPartnersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient.ListPartnersPagedResponse)` |   
  
### listPartners(ListPartnersRequest request)
    
    
    public final PartnerServiceClient.ListPartnersPagedResponse listPartners(ListPartnersRequest request)

Lists Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       ListPartnersRequest request =
           ListPartnersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Partner element : partnerServiceClient.listPartners(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPartnersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPartnersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PartnerServiceClient.ListPartnersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient.ListPartnersPagedResponse)` |   
  
### listPartners(String parent)
    
    
    public final PartnerServiceClient.ListPartnersPagedResponse listPartners(String parent)

Lists Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Partner element : partnerServiceClient.listPartners(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Partners. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[PartnerServiceClient.ListPartnersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient.ListPartnersPagedResponse)` |   
  
### listPartnersCallable()
    
    
    public final UnaryCallable<ListPartnersRequest,ListPartnersResponse> listPartnersCallable()

Lists Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       ListPartnersRequest request =
           ListPartnersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListPartnersResponse response = partnerServiceClient.listPartnersCallable().call(request);
         for (Partner element : response.getPartnersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPartnersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPartnersRequest),[ListPartnersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPartnersResponse)>` |   
  
### listPartnersPagedCallable()
    
    
    public final UnaryCallable<ListPartnersRequest,PartnerServiceClient.ListPartnersPagedResponse> listPartnersPagedCallable()

Lists Partner objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       ListPartnersRequest request =
           ListPartnersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Partner> future =
           partnerServiceClient.listPartnersPagedCallable().futureCall(request);
       // Do something.
       for (Partner element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPartnersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListPartnersRequest),[ListPartnersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.PartnerServiceClient.ListPartnersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePartner(Partner partner, FieldMask updateMask)
    
    
    public final Partner updatePartner(Partner partner, FieldMask updateMask)

Updates a Partner object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       Partner partner = Partner.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Partner response = partnerServiceClient.updatePartner(partner, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`partner` | `[Partner](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Partner)`  
Required. The Partner to update. The Partner's `name` is used to identify the Partner to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Partner](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Partner)` |   
  
### updatePartner(UpdatePartnerRequest request)
    
    
    public final Partner updatePartner(UpdatePartnerRequest request)

Updates a Partner object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       UpdatePartnerRequest request =
           UpdatePartnerRequest.newBuilder()
               .setPartner(Partner.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Partner response = partnerServiceClient.updatePartner(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePartnerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePartnerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Partner](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Partner)` |   
  
### updatePartnerCallable()
    
    
    public final UnaryCallable<UpdatePartnerRequest,Partner> updatePartnerCallable()

Updates a Partner object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PartnerServiceClient partnerServiceClient = PartnerServiceClient.create()) {
       UpdatePartnerRequest request =
           UpdatePartnerRequest.newBuilder()
               .setPartner(Partner.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Partner> future = partnerServiceClient.updatePartnerCallable().futureCall(request);
       // Do something.
       Partner response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePartnerRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdatePartnerRequest),[Partner](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Partner)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
