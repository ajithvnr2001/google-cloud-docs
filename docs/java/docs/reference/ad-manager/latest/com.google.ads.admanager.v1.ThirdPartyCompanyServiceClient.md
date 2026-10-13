---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient
title: Class ThirdPartyCompanyServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:06.911168+00:00
---

# Class ThirdPartyCompanyServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ThirdPartyCompanyServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ThirdPartyCompanyServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Service to retrieve and list recognized third-party companies in Google Ad Manager.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       ThirdPartyCompanyName name =
           ThirdPartyCompanyName.of("[NETWORK_CODE]", "[THIRD_PARTY_COMPANY]");
       ThirdPartyCompany response = thirdPartyCompanyServiceClient.getThirdPartyCompany(name);
     }
     

Note: close() needs to be called on the ThirdPartyCompanyServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetThirdPartyCompany |  Retrieves a `ThirdPartyCompany` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getThirdPartyCompany(GetThirdPartyCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getThirdPartyCompany(ThirdPartyCompanyName name) 
  * getThirdPartyCompany(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getThirdPartyCompanyCallable() 

  
ListThirdPartyCompanies |  Lists `ThirdPartyCompany` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listThirdPartyCompanies(ListThirdPartyCompaniesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listThirdPartyCompanies(NetworkName parent) 
  * listThirdPartyCompanies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listThirdPartyCompaniesPagedCallable() 
  * listThirdPartyCompaniesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ThirdPartyCompanyServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ThirdPartyCompanyServiceSettings thirdPartyCompanyServiceSettings =
         ThirdPartyCompanyServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create(thirdPartyCompanyServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ThirdPartyCompanyServiceSettings thirdPartyCompanyServiceSettings =
         ThirdPartyCompanyServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create(thirdPartyCompanyServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ThirdPartyCompanyServiceClient

## Static Methods 

### create()
    
    
    public static final ThirdPartyCompanyServiceClient create()

Constructs an instance of ThirdPartyCompanyServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ThirdPartyCompanyServiceSettings settings)
    
    
    public static final ThirdPartyCompanyServiceClient create(ThirdPartyCompanyServiceSettings settings)

Constructs an instance of ThirdPartyCompanyServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ThirdPartyCompanyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ThirdPartyCompanyServiceStub stub)
    
    
    public static final ThirdPartyCompanyServiceClient create(ThirdPartyCompanyServiceStub stub)

Constructs an instance of ThirdPartyCompanyServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ThirdPartyCompanyServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ThirdPartyCompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ThirdPartyCompanyServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient)` |   
  
## Constructors 

### ThirdPartyCompanyServiceClient(ThirdPartyCompanyServiceSettings settings)
    
    
    protected ThirdPartyCompanyServiceClient(ThirdPartyCompanyServiceSettings settings)

Constructs an instance of ThirdPartyCompanyServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ThirdPartyCompanyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceSettings)`  
  
  
### ThirdPartyCompanyServiceClient(ThirdPartyCompanyServiceStub stub)
    
    
    protected ThirdPartyCompanyServiceClient(ThirdPartyCompanyServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ThirdPartyCompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ThirdPartyCompanyServiceStub)`  
  
  
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

### getSettings()
    
    
    public final @Nullable ThirdPartyCompanyServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ThirdPartyCompanyServiceSettings` |   
  
### getStub()
    
    
    public ThirdPartyCompanyServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ThirdPartyCompanyServiceStub)` |   
  
### getThirdPartyCompany(@Nullable ThirdPartyCompanyName name)
    
    
    public final ThirdPartyCompany getThirdPartyCompany(@Nullable ThirdPartyCompanyName name)

Retrieves a `ThirdPartyCompany` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       ThirdPartyCompanyName name =
           ThirdPartyCompanyName.of("[NETWORK_CODE]", "[THIRD_PARTY_COMPANY]");
       ThirdPartyCompany response = thirdPartyCompanyServiceClient.getThirdPartyCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ThirdPartyCompanyName`  
Required. The resource name of the ThirdPartyCompany. Format: `networks/{network_code}/thirdPartyCompanies/{third_party_company_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompany](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompany)` |   
  
### getThirdPartyCompany(GetThirdPartyCompanyRequest request)
    
    
    public final ThirdPartyCompany getThirdPartyCompany(GetThirdPartyCompanyRequest request)

Retrieves a `ThirdPartyCompany` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       GetThirdPartyCompanyRequest request =
           GetThirdPartyCompanyRequest.newBuilder()
               .setName(
                   ThirdPartyCompanyName.of("[NETWORK_CODE]", "[THIRD_PARTY_COMPANY]").toString())
               .build();
       ThirdPartyCompany response = thirdPartyCompanyServiceClient.getThirdPartyCompany(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetThirdPartyCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetThirdPartyCompanyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompany](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompany)` |   
  
### getThirdPartyCompany(String name)
    
    
    public final ThirdPartyCompany getThirdPartyCompany(String name)

Retrieves a `ThirdPartyCompany` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       String name = ThirdPartyCompanyName.of("[NETWORK_CODE]", "[THIRD_PARTY_COMPANY]").toString();
       ThirdPartyCompany response = thirdPartyCompanyServiceClient.getThirdPartyCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ThirdPartyCompany. Format: `networks/{network_code}/thirdPartyCompanies/{third_party_company_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompany](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompany)` |   
  
### getThirdPartyCompanyCallable()
    
    
    public final UnaryCallable<GetThirdPartyCompanyRequest,ThirdPartyCompany> getThirdPartyCompanyCallable()

Retrieves a `ThirdPartyCompany` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       GetThirdPartyCompanyRequest request =
           GetThirdPartyCompanyRequest.newBuilder()
               .setName(
                   ThirdPartyCompanyName.of("[NETWORK_CODE]", "[THIRD_PARTY_COMPANY]").toString())
               .build();
       ApiFuture<ThirdPartyCompany> future =
           thirdPartyCompanyServiceClient.getThirdPartyCompanyCallable().futureCall(request);
       // Do something.
       ThirdPartyCompany response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetThirdPartyCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetThirdPartyCompanyRequest),[ThirdPartyCompany](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompany)>` |   
  
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
  
### listThirdPartyCompanies(@Nullable NetworkName parent)
    
    
    public final ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse listThirdPartyCompanies(@Nullable NetworkName parent)

Lists `ThirdPartyCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (ThirdPartyCompany element :
           thirdPartyCompanyServiceClient.listThirdPartyCompanies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of ThirdPartyCompanies. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse)` |   
  
### listThirdPartyCompanies(ListThirdPartyCompaniesRequest request)
    
    
    public final ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse listThirdPartyCompanies(ListThirdPartyCompaniesRequest request)

Lists `ThirdPartyCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       ListThirdPartyCompaniesRequest request =
           ListThirdPartyCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (ThirdPartyCompany element :
           thirdPartyCompanyServiceClient.listThirdPartyCompanies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListThirdPartyCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListThirdPartyCompaniesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse)` |   
  
### listThirdPartyCompanies(String parent)
    
    
    public final ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse listThirdPartyCompanies(String parent)

Lists `ThirdPartyCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (ThirdPartyCompany element :
           thirdPartyCompanyServiceClient.listThirdPartyCompanies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of ThirdPartyCompanies. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse)` |   
  
### listThirdPartyCompaniesCallable()
    
    
    public final UnaryCallable<ListThirdPartyCompaniesRequest,ListThirdPartyCompaniesResponse> listThirdPartyCompaniesCallable()

Lists `ThirdPartyCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       ListThirdPartyCompaniesRequest request =
           ListThirdPartyCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListThirdPartyCompaniesResponse response =
             thirdPartyCompanyServiceClient.listThirdPartyCompaniesCallable().call(request);
         for (ThirdPartyCompany element : response.getThirdPartyCompaniesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListThirdPartyCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListThirdPartyCompaniesRequest),[ListThirdPartyCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListThirdPartyCompaniesResponse)>` |   
  
### listThirdPartyCompaniesPagedCallable()
    
    
    public final UnaryCallable<ListThirdPartyCompaniesRequest,ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse> listThirdPartyCompaniesPagedCallable()

Lists `ThirdPartyCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ThirdPartyCompanyServiceClient thirdPartyCompanyServiceClient =
         ThirdPartyCompanyServiceClient.create()) {
       ListThirdPartyCompaniesRequest request =
           ListThirdPartyCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<ThirdPartyCompany> future =
           thirdPartyCompanyServiceClient.listThirdPartyCompaniesPagedCallable().futureCall(request);
       // Do something.
       for (ThirdPartyCompany element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListThirdPartyCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListThirdPartyCompaniesRequest),[ListThirdPartyCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ThirdPartyCompanyServiceClient.ListThirdPartyCompaniesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
