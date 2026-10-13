---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient
title: Class AggregateProductStatusesServiceClient (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:49.623995+00:00
---

# Class AggregateProductStatusesServiceClient (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AggregateProductStatusesServiceClient (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-shopping-merchant-issue-resolution/google-shopping-merchant-issue-resolution/src/main/java/com/google/shopping/merchant/issueresolution/v1/AggregateProductStatusesServiceClient.java)| [Product Reference](https://developers.google.com/merchant/api)  
---|---  
  
Service Description: Service to manage aggregate product statuses.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create()) {
       AccountName parent = AccountName.of("[ACCOUNT]");
       for (AggregateProductStatus element :
           aggregateProductStatusesServiceClient.listAggregateProductStatuses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

Note: close() needs to be called on the AggregateProductStatusesServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListAggregateProductStatuses |  Lists the `AggregateProductStatuses` resources for your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAggregateProductStatuses(ListAggregateProductStatusesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAggregateProductStatuses(AccountName parent) 
  * listAggregateProductStatuses(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAggregateProductStatusesPagedCallable() 
  * listAggregateProductStatusesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AggregateProductStatusesServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AggregateProductStatusesServiceSettings aggregateProductStatusesServiceSettings =
         AggregateProductStatusesServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create(aggregateProductStatusesServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AggregateProductStatusesServiceSettings aggregateProductStatusesServiceSettings =
         AggregateProductStatusesServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create(aggregateProductStatusesServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AggregateProductStatusesServiceSettings aggregateProductStatusesServiceSettings =
         AggregateProductStatusesServiceSettings.newHttpJsonBuilder().build();
     AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create(aggregateProductStatusesServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AggregateProductStatusesServiceClient

## Static Methods 

### create()
    
    
    public static final AggregateProductStatusesServiceClient create()

Constructs an instance of AggregateProductStatusesServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatusesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AggregateProductStatusesServiceSettings settings)
    
    
    public static final AggregateProductStatusesServiceClient create(AggregateProductStatusesServiceSettings settings)

Constructs an instance of AggregateProductStatusesServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AggregateProductStatusesServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatusesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AggregateProductStatusesServiceStub stub)
    
    
    public static final AggregateProductStatusesServiceClient create(AggregateProductStatusesServiceStub stub)

Constructs an instance of AggregateProductStatusesServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AggregateProductStatusesServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AggregateProductStatusesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.stub.AggregateProductStatusesServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatusesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient)` |   
  
## Constructors 

### AggregateProductStatusesServiceClient(AggregateProductStatusesServiceSettings settings)
    
    
    protected AggregateProductStatusesServiceClient(AggregateProductStatusesServiceSettings settings)

Constructs an instance of AggregateProductStatusesServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AggregateProductStatusesServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceSettings)`  
  
  
### AggregateProductStatusesServiceClient(AggregateProductStatusesServiceStub stub)
    
    
    protected AggregateProductStatusesServiceClient(AggregateProductStatusesServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AggregateProductStatusesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.stub.AggregateProductStatusesServiceStub)`  
  
  
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
    
    
    public final @Nullable AggregateProductStatusesServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceSettings` |   
  
### getStub()
    
    
    public AggregateProductStatusesServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatusesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.stub.AggregateProductStatusesServiceStub)` |   
  
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
  
### listAggregateProductStatuses(@Nullable AccountName parent)
    
    
    public final AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse listAggregateProductStatuses(@Nullable AccountName parent)

Lists the `AggregateProductStatuses` resources for your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create()) {
       AccountName parent = AccountName.of("[ACCOUNT]");
       for (AggregateProductStatus element :
           aggregateProductStatusesServiceClient.listAggregateProductStatuses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.issueresolution.v1.AccountName`  
Required. The account to list aggregate product statuses for. Format: `accounts/{account}`  
**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse)` |   
  
### listAggregateProductStatuses(ListAggregateProductStatusesRequest request)
    
    
    public final AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse listAggregateProductStatuses(ListAggregateProductStatusesRequest request)

Lists the `AggregateProductStatuses` resources for your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create()) {
       ListAggregateProductStatusesRequest request =
           ListAggregateProductStatusesRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (AggregateProductStatus element :
           aggregateProductStatusesServiceClient
               .listAggregateProductStatuses(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAggregateProductStatusesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.ListAggregateProductStatusesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse)` |   
  
### listAggregateProductStatuses(String parent)
    
    
    public final AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse listAggregateProductStatuses(String parent)

Lists the `AggregateProductStatuses` resources for your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create()) {
       String parent = AccountName.of("[ACCOUNT]").toString();
       for (AggregateProductStatus element :
           aggregateProductStatusesServiceClient.listAggregateProductStatuses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The account to list aggregate product statuses for. Format: `accounts/{account}`  
**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse)` |   
  
### listAggregateProductStatusesCallable()
    
    
    public final UnaryCallable<ListAggregateProductStatusesRequest,ListAggregateProductStatusesResponse> listAggregateProductStatusesCallable()

Lists the `AggregateProductStatuses` resources for your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create()) {
       ListAggregateProductStatusesRequest request =
           ListAggregateProductStatusesRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListAggregateProductStatusesResponse response =
             aggregateProductStatusesServiceClient
                 .listAggregateProductStatusesCallable()
                 .call(request);
         for (AggregateProductStatus element : response.getAggregateProductStatusesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAggregateProductStatusesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.ListAggregateProductStatusesRequest),[ListAggregateProductStatusesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.ListAggregateProductStatusesResponse)>` |   
  
### listAggregateProductStatusesPagedCallable()
    
    
    public final UnaryCallable<ListAggregateProductStatusesRequest,AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse> listAggregateProductStatusesPagedCallable()

Lists the `AggregateProductStatuses` resources for your merchant account. The response might contain fewer items than specified by `pageSize`. If `pageToken` was returned in previous request, it can be used to obtain additional results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AggregateProductStatusesServiceClient aggregateProductStatusesServiceClient =
         AggregateProductStatusesServiceClient.create()) {
       ListAggregateProductStatusesRequest request =
           ListAggregateProductStatusesRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<AggregateProductStatus> future =
           aggregateProductStatusesServiceClient
               .listAggregateProductStatusesPagedCallable()
               .futureCall(request);
       // Do something.
       for (AggregateProductStatus element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAggregateProductStatusesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.ListAggregateProductStatusesRequest),[ListAggregateProductStatusesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatusesServiceClient.ListAggregateProductStatusesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
