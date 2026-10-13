---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesClient
title: Class PublicAdvertisedPrefixesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:20.640936+00:00
---

# Class PublicAdvertisedPrefixesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PublicAdvertisedPrefixesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/PublicAdvertisedPrefixesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The PublicAdvertisedPrefixes API.

This client uses PublicAdvertisedPrefixes version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicAdvertisedPrefix = "publicAdvertisedPrefix1506440856";
       PublicAdvertisedPrefix response =
           publicAdvertisedPrefixesClient.get(project, publicAdvertisedPrefix);
     }
     

Note: close() needs to be called on the PublicAdvertisedPrefixesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Announce |  Announces the specified PublicAdvertisedPrefix |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * announceAsync(AnnouncePublicAdvertisedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * announceAsync(String project, String publicAdvertisedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * announceOperationCallable() 
  * announceCallable() 

  
Delete |  Deletes the specified PublicAdvertisedPrefix |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeletePublicAdvertisedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String publicAdvertisedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified PublicAdvertisedPrefix resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetPublicAdvertisedPrefixeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String publicAdvertisedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a PublicAdvertisedPrefix in the specified project using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertPublicAdvertisedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, PublicAdvertisedPrefix publicAdvertisedPrefixResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the PublicAdvertisedPrefixes for a project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListPublicAdvertisedPrefixesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchPublicAdvertisedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String publicAdvertisedPrefix, PublicAdvertisedPrefix publicAdvertisedPrefixResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
Withdraw |  Withdraws the specified PublicAdvertisedPrefix |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * withdrawAsync(WithdrawPublicAdvertisedPrefixeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * withdrawAsync(String project, String publicAdvertisedPrefix) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * withdrawOperationCallable() 
  * withdrawCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PublicAdvertisedPrefixesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PublicAdvertisedPrefixesSettings publicAdvertisedPrefixesSettings =
         PublicAdvertisedPrefixesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create(publicAdvertisedPrefixesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PublicAdvertisedPrefixesSettings publicAdvertisedPrefixesSettings =
         PublicAdvertisedPrefixesSettings.newBuilder().setEndpoint(myEndpoint).build();
     PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create(publicAdvertisedPrefixesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PublicAdvertisedPrefixesClient

## Static Methods 

### create()
    
    
    public static final PublicAdvertisedPrefixesClient create()

Constructs an instance of PublicAdvertisedPrefixesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PublicAdvertisedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PublicAdvertisedPrefixesSettings settings)
    
    
    public static final PublicAdvertisedPrefixesClient create(PublicAdvertisedPrefixesSettings settings)

Constructs an instance of PublicAdvertisedPrefixesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PublicAdvertisedPrefixesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublicAdvertisedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PublicAdvertisedPrefixesStub stub)
    
    
    public static final PublicAdvertisedPrefixesClient create(PublicAdvertisedPrefixesStub stub)

Constructs an instance of PublicAdvertisedPrefixesClient, using the given stub for making calls. This is for advanced usage - prefer using create(PublicAdvertisedPrefixesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PublicAdvertisedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PublicAdvertisedPrefixesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublicAdvertisedPrefixesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesClient)` |   
  
## Constructors 

### PublicAdvertisedPrefixesClient(PublicAdvertisedPrefixesSettings settings)
    
    
    protected PublicAdvertisedPrefixesClient(PublicAdvertisedPrefixesSettings settings)

Constructs an instance of PublicAdvertisedPrefixesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PublicAdvertisedPrefixesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesSettings)`  
  
  
### PublicAdvertisedPrefixesClient(PublicAdvertisedPrefixesStub stub)
    
    
    protected PublicAdvertisedPrefixesClient(PublicAdvertisedPrefixesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PublicAdvertisedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PublicAdvertisedPrefixesStub)`  
  
  
## Methods 

### announceAsync(AnnouncePublicAdvertisedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> announceAsync(AnnouncePublicAdvertisedPrefixeRequest request)

Announces the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       AnnouncePublicAdvertisedPrefixeRequest request =
           AnnouncePublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicAdvertisedPrefixesClient.announceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnnouncePublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AnnouncePublicAdvertisedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### announceAsync(String project, String publicAdvertisedPrefix)
    
    
    public final OperationFuture<Operation,Operation> announceAsync(String project, String publicAdvertisedPrefix)

Announces the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicAdvertisedPrefix = "publicAdvertisedPrefix1506440856";
       Operation response =
           publicAdvertisedPrefixesClient.announceAsync(project, publicAdvertisedPrefix).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicAdvertisedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the public advertised prefix. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### announceCallable()
    
    
    public final UnaryCallable<AnnouncePublicAdvertisedPrefixeRequest,Operation> announceCallable()

Announces the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       AnnouncePublicAdvertisedPrefixeRequest request =
           AnnouncePublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicAdvertisedPrefixesClient.announceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnnouncePublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AnnouncePublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### announceOperationCallable()
    
    
    public final OperationCallable<AnnouncePublicAdvertisedPrefixeRequest,Operation,Operation> announceOperationCallable()

Announces the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       AnnouncePublicAdvertisedPrefixeRequest request =
           AnnouncePublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicAdvertisedPrefixesClient.announceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AnnouncePublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AnnouncePublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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

### deleteAsync(DeletePublicAdvertisedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeletePublicAdvertisedPrefixeRequest request)

Deletes the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       DeletePublicAdvertisedPrefixeRequest request =
           DeletePublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicAdvertisedPrefixesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePublicAdvertisedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String publicAdvertisedPrefix)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String publicAdvertisedPrefix)

Deletes the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicAdvertisedPrefix = "publicAdvertisedPrefix1506440856";
       Operation response =
           publicAdvertisedPrefixesClient.deleteAsync(project, publicAdvertisedPrefix).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicAdvertisedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicAdvertisedPrefix resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeletePublicAdvertisedPrefixeRequest,Operation> deleteCallable()

Deletes the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       DeletePublicAdvertisedPrefixeRequest request =
           DeletePublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicAdvertisedPrefixesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeletePublicAdvertisedPrefixeRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       DeletePublicAdvertisedPrefixeRequest request =
           DeletePublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicAdvertisedPrefixesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeletePublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetPublicAdvertisedPrefixeRequest request)
    
    
    public final PublicAdvertisedPrefix get(GetPublicAdvertisedPrefixeRequest request)

Returns the specified PublicAdvertisedPrefix resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       GetPublicAdvertisedPrefixeRequest request =
           GetPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .build();
       PublicAdvertisedPrefix response = publicAdvertisedPrefixesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetPublicAdvertisedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PublicAdvertisedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefix)` |   
  
### get(String project, String publicAdvertisedPrefix)
    
    
    public final PublicAdvertisedPrefix get(String project, String publicAdvertisedPrefix)

Returns the specified PublicAdvertisedPrefix resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicAdvertisedPrefix = "publicAdvertisedPrefix1506440856";
       PublicAdvertisedPrefix response =
           publicAdvertisedPrefixesClient.get(project, publicAdvertisedPrefix);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicAdvertisedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicAdvertisedPrefix resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[PublicAdvertisedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefix)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetPublicAdvertisedPrefixeRequest,PublicAdvertisedPrefix> getCallable()

Returns the specified PublicAdvertisedPrefix resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       GetPublicAdvertisedPrefixeRequest request =
           GetPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .build();
       ApiFuture<PublicAdvertisedPrefix> future =
           publicAdvertisedPrefixesClient.getCallable().futureCall(request);
       // Do something.
       PublicAdvertisedPrefix response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetPublicAdvertisedPrefixeRequest),[PublicAdvertisedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefix)>` |   
  
### getSettings()
    
    
    public final @Nullable PublicAdvertisedPrefixesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.PublicAdvertisedPrefixesSettings` |   
  
### getStub()
    
    
    public PublicAdvertisedPrefixesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PublicAdvertisedPrefixesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.PublicAdvertisedPrefixesStub)` |   
  
### insertAsync(InsertPublicAdvertisedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertPublicAdvertisedPrefixeRequest request)

Creates a PublicAdvertisedPrefix in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       InsertPublicAdvertisedPrefixeRequest request =
           InsertPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefixResource(PublicAdvertisedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicAdvertisedPrefixesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertPublicAdvertisedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, PublicAdvertisedPrefix publicAdvertisedPrefixResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, PublicAdvertisedPrefix publicAdvertisedPrefixResource)

Creates a PublicAdvertisedPrefix in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       String project = "project-309310695";
       PublicAdvertisedPrefix publicAdvertisedPrefixResource =
           PublicAdvertisedPrefix.newBuilder().build();
       Operation response =
           publicAdvertisedPrefixesClient.insertAsync(project, publicAdvertisedPrefixResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicAdvertisedPrefixResource` | `[PublicAdvertisedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefix)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertPublicAdvertisedPrefixeRequest,Operation> insertCallable()

Creates a PublicAdvertisedPrefix in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       InsertPublicAdvertisedPrefixeRequest request =
           InsertPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefixResource(PublicAdvertisedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicAdvertisedPrefixesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertPublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertPublicAdvertisedPrefixeRequest,Operation,Operation> insertOperationCallable()

Creates a PublicAdvertisedPrefix in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       InsertPublicAdvertisedPrefixeRequest request =
           InsertPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefixResource(PublicAdvertisedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicAdvertisedPrefixesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertPublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListPublicAdvertisedPrefixesRequest request)
    
    
    public final PublicAdvertisedPrefixesClient.ListPagedResponse list(ListPublicAdvertisedPrefixesRequest request)

Lists the PublicAdvertisedPrefixes for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       ListPublicAdvertisedPrefixesRequest request =
           ListPublicAdvertisedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (PublicAdvertisedPrefix element :
           publicAdvertisedPrefixesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPublicAdvertisedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPublicAdvertisedPrefixesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PublicAdvertisedPrefixesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final PublicAdvertisedPrefixesClient.ListPagedResponse list(String project)

Lists the PublicAdvertisedPrefixes for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       String project = "project-309310695";
       for (PublicAdvertisedPrefix element :
           publicAdvertisedPrefixesClient.list(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[PublicAdvertisedPrefixesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListPublicAdvertisedPrefixesRequest,PublicAdvertisedPrefixList> listCallable()

Lists the PublicAdvertisedPrefixes for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       ListPublicAdvertisedPrefixesRequest request =
           ListPublicAdvertisedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         PublicAdvertisedPrefixList response =
             publicAdvertisedPrefixesClient.listCallable().call(request);
         for (PublicAdvertisedPrefix element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPublicAdvertisedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPublicAdvertisedPrefixesRequest),[PublicAdvertisedPrefixList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListPublicAdvertisedPrefixesRequest,PublicAdvertisedPrefixesClient.ListPagedResponse> listPagedCallable()

Lists the PublicAdvertisedPrefixes for a project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       ListPublicAdvertisedPrefixesRequest request =
           ListPublicAdvertisedPrefixesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<PublicAdvertisedPrefix> future =
           publicAdvertisedPrefixesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (PublicAdvertisedPrefix element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPublicAdvertisedPrefixesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPublicAdvertisedPrefixesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefixesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchPublicAdvertisedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchPublicAdvertisedPrefixeRequest request)

Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       PatchPublicAdvertisedPrefixeRequest request =
           PatchPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setPublicAdvertisedPrefixResource(PublicAdvertisedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicAdvertisedPrefixesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPublicAdvertisedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String publicAdvertisedPrefix, PublicAdvertisedPrefix publicAdvertisedPrefixResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String publicAdvertisedPrefix, PublicAdvertisedPrefix publicAdvertisedPrefixResource)

Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicAdvertisedPrefix = "publicAdvertisedPrefix1506440856";
       PublicAdvertisedPrefix publicAdvertisedPrefixResource =
           PublicAdvertisedPrefix.newBuilder().build();
       Operation response =
           publicAdvertisedPrefixesClient
               .patchAsync(project, publicAdvertisedPrefix, publicAdvertisedPrefixResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicAdvertisedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the PublicAdvertisedPrefix resource to patch.  
`publicAdvertisedPrefixResource` | `[PublicAdvertisedPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PublicAdvertisedPrefix)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchPublicAdvertisedPrefixeRequest,Operation> patchCallable()

Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       PatchPublicAdvertisedPrefixeRequest request =
           PatchPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setPublicAdvertisedPrefixResource(PublicAdvertisedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicAdvertisedPrefixesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchPublicAdvertisedPrefixeRequest,Operation,Operation> patchOperationCallable()

Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       PatchPublicAdvertisedPrefixeRequest request =
           PatchPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setPublicAdvertisedPrefixResource(PublicAdvertisedPrefix.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicAdvertisedPrefixesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### withdrawAsync(WithdrawPublicAdvertisedPrefixeRequest request)
    
    
    public final OperationFuture<Operation,Operation> withdrawAsync(WithdrawPublicAdvertisedPrefixeRequest request)

Withdraws the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       WithdrawPublicAdvertisedPrefixeRequest request =
           WithdrawPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       Operation response = publicAdvertisedPrefixesClient.withdrawAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WithdrawPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WithdrawPublicAdvertisedPrefixeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### withdrawAsync(String project, String publicAdvertisedPrefix)
    
    
    public final OperationFuture<Operation,Operation> withdrawAsync(String project, String publicAdvertisedPrefix)

Withdraws the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       String project = "project-309310695";
       String publicAdvertisedPrefix = "publicAdvertisedPrefix1506440856";
       Operation response =
           publicAdvertisedPrefixesClient.withdrawAsync(project, publicAdvertisedPrefix).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`publicAdvertisedPrefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the public advertised prefix. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### withdrawCallable()
    
    
    public final UnaryCallable<WithdrawPublicAdvertisedPrefixeRequest,Operation> withdrawCallable()

Withdraws the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       WithdrawPublicAdvertisedPrefixeRequest request =
           WithdrawPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           publicAdvertisedPrefixesClient.withdrawCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WithdrawPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WithdrawPublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### withdrawOperationCallable()
    
    
    public final OperationCallable<WithdrawPublicAdvertisedPrefixeRequest,Operation,Operation> withdrawOperationCallable()

Withdraws the specified PublicAdvertisedPrefix

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PublicAdvertisedPrefixesClient publicAdvertisedPrefixesClient =
         PublicAdvertisedPrefixesClient.create()) {
       WithdrawPublicAdvertisedPrefixeRequest request =
           WithdrawPublicAdvertisedPrefixeRequest.newBuilder()
               .setProject("project-309310695")
               .setPublicAdvertisedPrefix("publicAdvertisedPrefix1506440856")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           publicAdvertisedPrefixesClient.withdrawOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[WithdrawPublicAdvertisedPrefixeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WithdrawPublicAdvertisedPrefixeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
