---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient
title: Class PublicDelegatedPrefixesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:22.351821+00:00
---

# Class PublicDelegatedPrefixesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PublicDelegatedPrefixesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/PublicDelegatedPrefixesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The PublicDelegatedPrefixes API.

This client uses PublicDelegatedPrefixes version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       PublicDelegatedPrefix response =
           publicDelegatedPrefixesClient.get(project, region, publicDelegatedPrefix);
     }
     

Note: close() needs to be called on the PublicDelegatedPrefixesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Lists all PublicDelegatedPrefix resources owned by the specific project across all scopes.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListPublicDelegatedPrefixesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Announce |  Announces the specified PublicDelegatedPrefix in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * announceAsync(AnnouncePublicDelegatedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * announceAsync(String project, String region, String publicDelegatedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * announceOperationCallable() 
  * announceCallable() 

  
Delete |  Deletes the specified PublicDelegatedPrefix in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeletePublicDelegatedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String publicDelegatedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified PublicDelegatedPrefix resource in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetPublicDelegatedPrefixeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String publicDelegatedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a PublicDelegatedPrefix in the specified project in the given region using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertPublicDelegatedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, PublicDelegatedPrefix publicDelegatedPrefixResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the PublicDelegatedPrefixes for a project in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListPublicDelegatedPrefixesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchPublicDelegatedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String publicDelegatedPrefix, PublicDelegatedPrefix publicDelegatedPrefixResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
Withdraw |  Withdraws the specified PublicDelegatedPrefix in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * withdrawAsync(WithdrawPublicDelegatedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * withdrawAsync(String project, String region, String publicDelegatedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * withdrawOperationCallable() 
  * withdrawCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PublicDelegatedPrefixesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PublicDelegatedPrefixesSettings publicDelegatedPrefixesSettings =
         PublicDelegatedPrefixesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create(publicDelegatedPrefixesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PublicDelegatedPrefixesSettings publicDelegatedPrefixesSettings =
         PublicDelegatedPrefixesSettings.newBuilder().setEndpoint(myEndpoint).build();
     PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create(publicDelegatedPrefixesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PublicDelegatedPrefixesClient

## Static Methods 

### create()
    
    
    public static final PublicDelegatedPrefixesClient create()

Constructs an instance of PublicDelegatedPrefixesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PublicDelegatedPrefixesSettings settings)
    
    
    public static final PublicDelegatedPrefixesClient create(PublicDelegatedPrefixesSettings settings)

Constructs an instance of PublicDelegatedPrefixesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PublicDelegatedPrefixesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PublicDelegatedPrefixesStub stub)
    
    
    public static final PublicDelegatedPrefixesClient create(PublicDelegatedPrefixesStub stub)

Constructs an instance of PublicDelegatedPrefixesClient, using the given stub for making calls. This is for advanced usage - prefer using create(PublicDelegatedPrefixesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PublicDelegatedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PublicDelegatedPrefixesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient)` |   
  
## Constructors 

### PublicDelegatedPrefixesClient(PublicDelegatedPrefixesSettings settings)
    
    
    protected PublicDelegatedPrefixesClient(PublicDelegatedPrefixesSettings settings)

Constructs an instance of PublicDelegatedPrefixesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PublicDelegatedPrefixesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesSettings)`  
  
  
### PublicDelegatedPrefixesClient(PublicDelegatedPrefixesStub stub)
    
    
    protected PublicDelegatedPrefixesClient(PublicDelegatedPrefixesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PublicDelegatedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PublicDelegatedPrefixesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListPublicDelegatedPrefixesRequest request)
    
    
    public final PublicDelegatedPrefixesClient.AggregatedListPagedResponse aggregatedList(AggregatedListPublicDelegatedPrefixesRequest request)

Lists all PublicDelegatedPrefix resources owned by the specific project across all scopes.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       AggregatedListPublicDelegatedPrefixesRequest request =
           AggregatedListPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, PublicDelegatedPrefixesScopedList> element :
           publicDelegatedPrefixesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListPublicDelegatedPrefixesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefixesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final PublicDelegatedPrefixesClient.AggregatedListPagedResponse aggregatedList(String project)

Lists all PublicDelegatedPrefix resources owned by the specific project across all scopes.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, PublicDelegatedPrefixesScopedList> element :
           publicDelegatedPrefixesClient.aggregatedList(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the project scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefixesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListPublicDelegatedPrefixesRequest,PublicDelegatedPrefixAggregatedList> aggregatedListCallable()

Lists all PublicDelegatedPrefix resources owned by the specific project across all scopes.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       AggregatedListPublicDelegatedPrefixesRequest request =
           AggregatedListPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         PublicDelegatedPrefixAggregatedList response =
             publicDelegatedPrefixesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, PublicDelegatedPrefixesScopedList> element :
             response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListPublicDelegatedPrefixesRequest),[PublicDelegatedPrefixAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListPublicDelegatedPrefixesRequest,PublicDelegatedPrefixesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Lists all PublicDelegatedPrefix resources owned by the specific project across all scopes.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       AggregatedListPublicDelegatedPrefixesRequest request =
           AggregatedListPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, PublicDelegatedPrefixesScopedList>> future =
           publicDelegatedPrefixesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, PublicDelegatedPrefixesScopedList> element :
           future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListPublicDelegatedPrefixesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient.AggregatedListPagedResponse)>` |   
  
### announceAsync(AnnouncePublicDelegatedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> announceAsync(AnnouncePublicDelegatedPrefixeRequest request)

Announces the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       AnnouncePublicDelegatedPrefixeRequest request =
           AnnouncePublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicDelegatedPrefixesClient.announceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnnouncePublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AnnouncePublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### announceAsync(String project, String region, String publicDelegatedPrefix)
    
    
    public final OperationFuture<Operation,Operation> announceAsync(String project, String region, String publicDelegatedPrefix)

Announces the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       Operation response =
           publicDelegatedPrefixesClient.announceAsync(project, region, publicDelegatedPrefix).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of theregion where the public delegated prefix is located. It should comply with RFC1035.  
`publicDelegatedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the public delegated prefix. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### announceCallable()
    
    
    public final UnaryCallable<AnnouncePublicDelegatedPrefixeRequest,Operation> announceCallable()

Announces the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       AnnouncePublicDelegatedPrefixeRequest request =
           AnnouncePublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicDelegatedPrefixesClient.announceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnnouncePublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AnnouncePublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### announceOperationCallable()
    
    
    public final OperationCallable<AnnouncePublicDelegatedPrefixeRequest,Operation,Operation> announceOperationCallable()

Announces the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       AnnouncePublicDelegatedPrefixeRequest request =
           AnnouncePublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicDelegatedPrefixesClient.announceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AnnouncePublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AnnouncePublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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

### deleteAsync(DeletePublicDelegatedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeletePublicDelegatedPrefixeRequest request)

Deletes the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       DeletePublicDelegatedPrefixeRequest request =
           DeletePublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicDelegatedPrefixesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String publicDelegatedPrefix)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String publicDelegatedPrefix)

Deletes the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       Operation response =
           publicDelegatedPrefixesClient.deleteAsync(project, region, publicDelegatedPrefix).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region of this request.  
`publicDelegatedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicDelegatedPrefix resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeletePublicDelegatedPrefixeRequest,Operation> deleteCallable()

Deletes the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       DeletePublicDelegatedPrefixeRequest request =
           DeletePublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicDelegatedPrefixesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeletePublicDelegatedPrefixeRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       DeletePublicDelegatedPrefixeRequest request =
           DeletePublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicDelegatedPrefixesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetPublicDelegatedPrefixeRequest request)
    
    
    public final PublicDelegatedPrefix get(GetPublicDelegatedPrefixeRequest request)

Returns the specified PublicDelegatedPrefix resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       GetPublicDelegatedPrefixeRequest request =
           GetPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .build();
       PublicDelegatedPrefix response = publicDelegatedPrefixesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetPublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)` |   
  
### get(String project, String region, String publicDelegatedPrefix)
    
    
    public final PublicDelegatedPrefix get(String project, String region, String publicDelegatedPrefix)

Returns the specified PublicDelegatedPrefix resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       PublicDelegatedPrefix response =
           publicDelegatedPrefixesClient.get(project, region, publicDelegatedPrefix);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region of this request.  
`publicDelegatedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicDelegatedPrefix resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetPublicDelegatedPrefixeRequest,PublicDelegatedPrefix> getCallable()

Returns the specified PublicDelegatedPrefix resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       GetPublicDelegatedPrefixeRequest request =
           GetPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .build();
       ApiFuture<PublicDelegatedPrefix> future =
           publicDelegatedPrefixesClient.getCallable().futureCall(request);
       // Do something.
       PublicDelegatedPrefix response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetPublicDelegatedPrefixeRequest),[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)>` |   
  
### getSettings()
    
    
    public final @Nullable PublicDelegatedPrefixesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.PublicDelegatedPrefixesSettings` |   
  
### getStub()
    
    
    public PublicDelegatedPrefixesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PublicDelegatedPrefixesStub)` |   
  
### insertAsync(InsertPublicDelegatedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertPublicDelegatedPrefixeRequest request)

Creates a PublicDelegatedPrefix in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       InsertPublicDelegatedPrefixeRequest request =
           InsertPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicDelegatedPrefixesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertPublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, PublicDelegatedPrefix publicDelegatedPrefixResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, PublicDelegatedPrefix publicDelegatedPrefixResource)

Creates a PublicDelegatedPrefix in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       PublicDelegatedPrefix publicDelegatedPrefixResource =
           PublicDelegatedPrefix.newBuilder().build();
       Operation response =
           publicDelegatedPrefixesClient
               .insertAsync(project, region, publicDelegatedPrefixResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region of this request.  
`publicDelegatedPrefixResource` | `[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertPublicDelegatedPrefixeRequest,Operation> insertCallable()

Creates a PublicDelegatedPrefix in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       InsertPublicDelegatedPrefixeRequest request =
           InsertPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicDelegatedPrefixesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertPublicDelegatedPrefixeRequest,Operation,Operation> insertOperationCallable()

Creates a PublicDelegatedPrefix in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       InsertPublicDelegatedPrefixeRequest request =
           InsertPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicDelegatedPrefixesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListPublicDelegatedPrefixesRequest request)
    
    
    public final PublicDelegatedPrefixesClient.ListPagedResponse list(ListPublicDelegatedPrefixesRequest request)

Lists the PublicDelegatedPrefixes for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       ListPublicDelegatedPrefixesRequest request =
           ListPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (PublicDelegatedPrefix element :
           publicDelegatedPrefixesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPublicDelegatedPrefixesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefixesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final PublicDelegatedPrefixesClient.ListPagedResponse list(String project, String region)

Lists the PublicDelegatedPrefixes for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (PublicDelegatedPrefix element :
           publicDelegatedPrefixesClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region of this request.  
**Returns**  
---  
**Type** | **Description**  
`[PublicDelegatedPrefixesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListPublicDelegatedPrefixesRequest,PublicDelegatedPrefixList> listCallable()

Lists the PublicDelegatedPrefixes for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       ListPublicDelegatedPrefixesRequest request =
           ListPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         PublicDelegatedPrefixList response =
             publicDelegatedPrefixesClient.listCallable().call(request);
         for (PublicDelegatedPrefix element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPublicDelegatedPrefixesRequest),[PublicDelegatedPrefixList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListPublicDelegatedPrefixesRequest,PublicDelegatedPrefixesClient.ListPagedResponse> listPagedCallable()

Lists the PublicDelegatedPrefixes for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       ListPublicDelegatedPrefixesRequest request =
           ListPublicDelegatedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<PublicDelegatedPrefix> future =
           publicDelegatedPrefixesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (PublicDelegatedPrefix element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPublicDelegatedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPublicDelegatedPrefixesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefixesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchPublicDelegatedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchPublicDelegatedPrefixeRequest request)

Patches the specified PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       PatchPublicDelegatedPrefixeRequest request =
           PatchPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicDelegatedPrefixesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String publicDelegatedPrefix, PublicDelegatedPrefix publicDelegatedPrefixResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String publicDelegatedPrefix, PublicDelegatedPrefix publicDelegatedPrefixResource)

Patches the specified PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       PublicDelegatedPrefix publicDelegatedPrefixResource =
           PublicDelegatedPrefix.newBuilder().build();
       Operation response =
           publicDelegatedPrefixesClient
               .patchAsync(project, region, publicDelegatedPrefix, publicDelegatedPrefixResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`publicDelegatedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicDelegatedPrefix resource to patch.  
`publicDelegatedPrefixResource` | `[PublicDelegatedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicDelegatedPrefix)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchPublicDelegatedPrefixeRequest,Operation> patchCallable()

Patches the specified PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       PatchPublicDelegatedPrefixeRequest request =
           PatchPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicDelegatedPrefixesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchPublicDelegatedPrefixeRequest,Operation,Operation> patchOperationCallable()

Patches the specified PublicDelegatedPrefix resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       PatchPublicDelegatedPrefixeRequest request =
           PatchPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setPublicDelegatedPrefixResource(PublicDelegatedPrefix.newBuilder().build())
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicDelegatedPrefixesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### withdrawAsync(WithdrawPublicDelegatedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> withdrawAsync(WithdrawPublicDelegatedPrefixeRequest request)

Withdraws the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       WithdrawPublicDelegatedPrefixeRequest request =
           WithdrawPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicDelegatedPrefixesClient.withdrawAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WithdrawPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WithdrawPublicDelegatedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### withdrawAsync(String project, String region, String publicDelegatedPrefix)
    
    
    public final OperationFuture<Operation,Operation> withdrawAsync(String project, String region, String publicDelegatedPrefix)

Withdraws the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String publicDelegatedPrefix = "publicDelegatedPrefix-663003832";
       Operation response =
           publicDelegatedPrefixesClient.withdrawAsync(project, region, publicDelegatedPrefix).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of theregion where the public delegated prefix is located. It should comply with RFC1035.  
`publicDelegatedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the public delegated prefix. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### withdrawCallable()
    
    
    public final UnaryCallable<WithdrawPublicDelegatedPrefixeRequest,Operation> withdrawCallable()

Withdraws the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       WithdrawPublicDelegatedPrefixeRequest request =
           WithdrawPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicDelegatedPrefixesClient.withdrawCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WithdrawPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WithdrawPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### withdrawOperationCallable()
    
    
    public final OperationCallable<WithdrawPublicDelegatedPrefixeRequest,Operation,Operation> withdrawOperationCallable()

Withdraws the specified PublicDelegatedPrefix in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicDelegatedPrefixesClient publicDelegatedPrefixesClient =
         PublicDelegatedPrefixesClient.create()) {
       WithdrawPublicDelegatedPrefixeRequest request =
           WithdrawPublicDelegatedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicDelegatedPrefix("publicDelegatedPrefix-663003832")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicDelegatedPrefixesClient.withdrawOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[WithdrawPublicDelegatedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WithdrawPublicDelegatedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
