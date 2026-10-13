---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient
title: Class BackendBucketsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:01:57.108104+00:00
---

# Class BackendBucketsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BackendBucketsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/BackendBucketsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The BackendBuckets API.

This client uses BackendBuckets version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String backendBucket = "backendBucket713751966";
       BackendBucket response = backendBucketsClient.get(project, backendBucket);
     }
     

Note: close() needs to be called on the BackendBucketsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddSignedUrlKey |  Adds a key for validating requests with signed URLs for this backend bucket. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addSignedUrlKeyAsync(AddSignedUrlKeyBackendBucketRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addSignedUrlKeyAsync(String project, String backendBucket, SignedUrlKey signedUrlKeyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addSignedUrlKeyOperationCallable() 
  * addSignedUrlKeyCallable() 

  
AggregatedList |  Retrieves the list of all BackendBucket resources, regional and global, available to the specified project.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListBackendBucketsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified BackendBucket resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteBackendBucketRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String backendBucket) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DeleteSignedUrlKey |  Deletes a key for validating requests with signed URLs for this backend bucket. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSignedUrlKeyAsync(DeleteSignedUrlKeyBackendBucketRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSignedUrlKeyAsync(String project, String backendBucket, String keyName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSignedUrlKeyOperationCallable() 
  * deleteSignedUrlKeyCallable() 

  
Get |  Returns the specified BackendBucket resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetBackendBucketRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String backendBucket) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyBackendBucketRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a BackendBucket resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertBackendBucketRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, BackendBucket backendBucketResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of BackendBucket resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListBackendBucketsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListUsable |  Retrieves a list of all usable backend buckets in the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUsable(ListUsableBackendBucketsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUsable(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUsablePagedCallable() 
  * listUsableCallable() 

  
Patch |  Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchBackendBucketRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String backendBucket, BackendBucket backendBucketResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetEdgeSecurityPolicy |  Sets the edge security policy for the specified backend bucket. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setEdgeSecurityPolicyAsync(SetEdgeSecurityPolicyBackendBucketRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setEdgeSecurityPolicyAsync(String project, String backendBucket, SecurityPolicyReference securityPolicyReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setEdgeSecurityPolicyOperationCallable() 
  * setEdgeSecurityPolicyCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyBackendBucketRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsBackendBucketRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Updates the specified BackendBucket resource with the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateBackendBucketRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String backendBucket, BackendBucket backendBucketResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BackendBucketsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackendBucketsSettings backendBucketsSettings =
         BackendBucketsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BackendBucketsClient backendBucketsClient = BackendBucketsClient.create(backendBucketsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackendBucketsSettings backendBucketsSettings =
         BackendBucketsSettings.newBuilder().setEndpoint(myEndpoint).build();
     BackendBucketsClient backendBucketsClient = BackendBucketsClient.create(backendBucketsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BackendBucketsClient

## Static Methods 

### create()
    
    
    public static final BackendBucketsClient create()

Constructs an instance of BackendBucketsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BackendBucketsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BackendBucketsSettings settings)
    
    
    public static final BackendBucketsClient create(BackendBucketsSettings settings)

Constructs an instance of BackendBucketsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BackendBucketsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BackendBucketsStub stub)
    
    
    public static final BackendBucketsClient create(BackendBucketsStub stub)

Constructs an instance of BackendBucketsClient, using the given stub for making calls. This is for advanced usage - prefer using create(BackendBucketsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BackendBucketsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.BackendBucketsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient)` |   
  
## Constructors 

### BackendBucketsClient(BackendBucketsSettings settings)
    
    
    protected BackendBucketsClient(BackendBucketsSettings settings)

Constructs an instance of BackendBucketsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BackendBucketsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsSettings)`  
  
  
### BackendBucketsClient(BackendBucketsStub stub)
    
    
    protected BackendBucketsClient(BackendBucketsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BackendBucketsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.BackendBucketsStub)`  
  
  
## Methods 

### addSignedUrlKeyAsync(AddSignedUrlKeyBackendBucketRequest request)
    
    
    public final OperationFuture<Operation,Operation> addSignedUrlKeyAsync(AddSignedUrlKeyBackendBucketRequest request)

Adds a key for validating requests with signed URLs for this backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       AddSignedUrlKeyBackendBucketRequest request =
           AddSignedUrlKeyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSignedUrlKeyResource(SignedUrlKey.newBuilder().build())
               .build();
       Operation response = backendBucketsClient.addSignedUrlKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddSignedUrlKeyBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addSignedUrlKeyAsync(String project, String backendBucket, SignedUrlKey signedUrlKeyResource)
    
    
    public final OperationFuture<Operation,Operation> addSignedUrlKeyAsync(String project, String backendBucket, SignedUrlKey signedUrlKeyResource)

Adds a key for validating requests with signed URLs for this backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String backendBucket = "backendBucket713751966";
       SignedUrlKey signedUrlKeyResource = SignedUrlKey.newBuilder().build();
       Operation response =
           backendBucketsClient
               .addSignedUrlKeyAsync(project, backendBucket, signedUrlKeyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendBucket resource to which the Signed URL Key should be added. The name should conform to RFC1035.  
`signedUrlKeyResource` | `[SignedUrlKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SignedUrlKey)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addSignedUrlKeyCallable()
    
    
    public final UnaryCallable<AddSignedUrlKeyBackendBucketRequest,Operation> addSignedUrlKeyCallable()

Adds a key for validating requests with signed URLs for this backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       AddSignedUrlKeyBackendBucketRequest request =
           AddSignedUrlKeyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSignedUrlKeyResource(SignedUrlKey.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           backendBucketsClient.addSignedUrlKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddSignedUrlKeyBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addSignedUrlKeyOperationCallable()
    
    
    public final OperationCallable<AddSignedUrlKeyBackendBucketRequest,Operation,Operation> addSignedUrlKeyOperationCallable()

Adds a key for validating requests with signed URLs for this backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       AddSignedUrlKeyBackendBucketRequest request =
           AddSignedUrlKeyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSignedUrlKeyResource(SignedUrlKey.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           backendBucketsClient.addSignedUrlKeyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddSignedUrlKeyBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedList(AggregatedListBackendBucketsRequest request)
    
    
    public final BackendBucketsClient.AggregatedListPagedResponse aggregatedList(AggregatedListBackendBucketsRequest request)

Retrieves the list of all BackendBucket resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       AggregatedListBackendBucketsRequest request =
           AggregatedListBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, BackendBucketsScopedList> element :
           backendBucketsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListBackendBucketsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final BackendBucketsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all BackendBucket resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, BackendBucketsScopedList> element :
           backendBucketsClient.aggregatedList(project).iterateAll()) {
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
`[BackendBucketsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListBackendBucketsRequest,BackendBucketAggregatedList> aggregatedListCallable()

Retrieves the list of all BackendBucket resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       AggregatedListBackendBucketsRequest request =
           AggregatedListBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         BackendBucketAggregatedList response =
             backendBucketsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, BackendBucketsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListBackendBucketsRequest),[BackendBucketAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListBackendBucketsRequest,BackendBucketsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all BackendBucket resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       AggregatedListBackendBucketsRequest request =
           AggregatedListBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, BackendBucketsScopedList>> future =
           backendBucketsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, BackendBucketsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListBackendBucketsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteBackendBucketRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteBackendBucketRequest request)

Deletes the specified BackendBucket resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       DeleteBackendBucketRequest request =
           DeleteBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendBucketsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String backendBucket)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String backendBucket)

Deletes the specified BackendBucket resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String backendBucket = "backendBucket713751966";
       Operation response = backendBucketsClient.deleteAsync(project, backendBucket).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendBucket resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteBackendBucketRequest,Operation> deleteCallable()

Deletes the specified BackendBucket resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       DeleteBackendBucketRequest request =
           DeleteBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backendBucketsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteBackendBucketRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified BackendBucket resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       DeleteBackendBucketRequest request =
           DeleteBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendBucketsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSignedUrlKeyAsync(DeleteSignedUrlKeyBackendBucketRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteSignedUrlKeyAsync(DeleteSignedUrlKeyBackendBucketRequest request)

Deletes a key for validating requests with signed URLs for this backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       DeleteSignedUrlKeyBackendBucketRequest request =
           DeleteSignedUrlKeyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setKeyName("keyName-815643254")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendBucketsClient.deleteSignedUrlKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSignedUrlKeyBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSignedUrlKeyAsync(String project, String backendBucket, String keyName)
    
    
    public final OperationFuture<Operation,Operation> deleteSignedUrlKeyAsync(String project, String backendBucket, String keyName)

Deletes a key for validating requests with signed URLs for this backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String backendBucket = "backendBucket713751966";
       String keyName = "keyName-815643254";
       Operation response =
           backendBucketsClient.deleteSignedUrlKeyAsync(project, backendBucket, keyName).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendBucket resource to which the Signed URL Key should be added. The name should conform to RFC1035.  
`keyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the Signed URL Key to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSignedUrlKeyCallable()
    
    
    public final UnaryCallable<DeleteSignedUrlKeyBackendBucketRequest,Operation> deleteSignedUrlKeyCallable()

Deletes a key for validating requests with signed URLs for this backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       DeleteSignedUrlKeyBackendBucketRequest request =
           DeleteSignedUrlKeyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setKeyName("keyName-815643254")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           backendBucketsClient.deleteSignedUrlKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSignedUrlKeyBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSignedUrlKeyOperationCallable()
    
    
    public final OperationCallable<DeleteSignedUrlKeyBackendBucketRequest,Operation,Operation> deleteSignedUrlKeyOperationCallable()

Deletes a key for validating requests with signed URLs for this backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       DeleteSignedUrlKeyBackendBucketRequest request =
           DeleteSignedUrlKeyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setKeyName("keyName-815643254")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendBucketsClient.deleteSignedUrlKeyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSignedUrlKeyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSignedUrlKeyBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetBackendBucketRequest request)
    
    
    public final BackendBucket get(GetBackendBucketRequest request)

Returns the specified BackendBucket resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       GetBackendBucketRequest request =
           GetBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .build();
       BackendBucket response = backendBucketsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucket)` |   
  
### get(String project, String backendBucket)
    
    
    public final BackendBucket get(String project, String backendBucket)

Returns the specified BackendBucket resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String backendBucket = "backendBucket713751966";
       BackendBucket response = backendBucketsClient.get(project, backendBucket);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendBucket resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucket)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetBackendBucketRequest,BackendBucket> getCallable()

Returns the specified BackendBucket resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       GetBackendBucketRequest request =
           GetBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .build();
       ApiFuture<BackendBucket> future = backendBucketsClient.getCallable().futureCall(request);
       // Do something.
       BackendBucket response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetBackendBucketRequest),[BackendBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucket)>` |   
  
### getIamPolicy(GetIamPolicyBackendBucketRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyBackendBucketRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       GetIamPolicyBackendBucketRequest request =
           GetIamPolicyBackendBucketRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = backendBucketsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String resource)
    
    
    public final Policy getIamPolicy(String project, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       Policy response = backendBucketsClient.getIamPolicy(project, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyBackendBucketRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       GetIamPolicyBackendBucketRequest request =
           GetIamPolicyBackendBucketRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = backendBucketsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyBackendBucketRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable BackendBucketsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.BackendBucketsSettings` |   
  
### getStub()
    
    
    public BackendBucketsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BackendBucketsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.BackendBucketsStub)` |   
  
### insertAsync(InsertBackendBucketRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertBackendBucketRequest request)

Creates a BackendBucket resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       InsertBackendBucketRequest request =
           InsertBackendBucketRequest.newBuilder()
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendBucketsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, BackendBucket backendBucketResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, BackendBucket backendBucketResource)

Creates a BackendBucket resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       BackendBucket backendBucketResource = BackendBucket.newBuilder().build();
       Operation response = backendBucketsClient.insertAsync(project, backendBucketResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendBucketResource` | `[BackendBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucket)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertBackendBucketRequest,Operation> insertCallable()

Creates a BackendBucket resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       InsertBackendBucketRequest request =
           InsertBackendBucketRequest.newBuilder()
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backendBucketsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertBackendBucketRequest,Operation,Operation> insertOperationCallable()

Creates a BackendBucket resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       InsertBackendBucketRequest request =
           InsertBackendBucketRequest.newBuilder()
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendBucketsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListBackendBucketsRequest request)
    
    
    public final BackendBucketsClient.ListPagedResponse list(ListBackendBucketsRequest request)

Retrieves the list of BackendBucket resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       ListBackendBucketsRequest request =
           ListBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (BackendBucket element : backendBucketsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBackendBucketsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final BackendBucketsClient.ListPagedResponse list(String project)

Retrieves the list of BackendBucket resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       for (BackendBucket element : backendBucketsClient.list(project).iterateAll()) {
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
`[BackendBucketsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListBackendBucketsRequest,BackendBucketList> listCallable()

Retrieves the list of BackendBucket resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       ListBackendBucketsRequest request =
           ListBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         BackendBucketList response = backendBucketsClient.listCallable().call(request);
         for (BackendBucket element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBackendBucketsRequest),[BackendBucketList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListBackendBucketsRequest,BackendBucketsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of BackendBucket resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       ListBackendBucketsRequest request =
           ListBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<BackendBucket> future =
           backendBucketsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (BackendBucket element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBackendBucketsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.ListPagedResponse)>` |   
  
### listUsable(ListUsableBackendBucketsRequest request)
    
    
    public final BackendBucketsClient.ListUsablePagedResponse listUsable(ListUsableBackendBucketsRequest request)

Retrieves a list of all usable backend buckets in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       ListUsableBackendBucketsRequest request =
           ListUsableBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (BackendBucket element : backendBucketsClient.listUsable(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUsableBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableBackendBucketsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketsClient.ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.ListUsablePagedResponse)` |   
  
### listUsable(String project)
    
    
    public final BackendBucketsClient.ListUsablePagedResponse listUsable(String project)

Retrieves a list of all usable backend buckets in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       for (BackendBucket element : backendBucketsClient.listUsable(project).iterateAll()) {
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
`[BackendBucketsClient.ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.ListUsablePagedResponse)` |   
  
### listUsableCallable()
    
    
    public final UnaryCallable<ListUsableBackendBucketsRequest,BackendBucketListUsable> listUsableCallable()

Retrieves a list of all usable backend buckets in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       ListUsableBackendBucketsRequest request =
           ListUsableBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         BackendBucketListUsable response = backendBucketsClient.listUsableCallable().call(request);
         for (BackendBucket element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableBackendBucketsRequest),[BackendBucketListUsable](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketListUsable)>` |   
  
### listUsablePagedCallable()
    
    
    public final UnaryCallable<ListUsableBackendBucketsRequest,BackendBucketsClient.ListUsablePagedResponse> listUsablePagedCallable()

Retrieves a list of all usable backend buckets in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       ListUsableBackendBucketsRequest request =
           ListUsableBackendBucketsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<BackendBucket> future =
           backendBucketsClient.listUsablePagedCallable().futureCall(request);
       // Do something.
       for (BackendBucket element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableBackendBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableBackendBucketsRequest),[ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketsClient.ListUsablePagedResponse)>` |   
  
### patchAsync(PatchBackendBucketRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchBackendBucketRequest request)

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       PatchBackendBucketRequest request =
           PatchBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendBucketsClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String backendBucket, BackendBucket backendBucketResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String backendBucket, BackendBucket backendBucketResource)

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String backendBucket = "backendBucket713751966";
       BackendBucket backendBucketResource = BackendBucket.newBuilder().build();
       Operation response =
           backendBucketsClient.patchAsync(project, backendBucket, backendBucketResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendBucket resource to patch.  
`backendBucketResource` | `[BackendBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucket)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchBackendBucketRequest,Operation> patchCallable()

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       PatchBackendBucketRequest request =
           PatchBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backendBucketsClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchBackendBucketRequest,Operation,Operation> patchOperationCallable()

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       PatchBackendBucketRequest request =
           PatchBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendBucketsClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setEdgeSecurityPolicyAsync(SetEdgeSecurityPolicyBackendBucketRequest request)
    
    
    public final OperationFuture<Operation,Operation> setEdgeSecurityPolicyAsync(SetEdgeSecurityPolicyBackendBucketRequest request)

Sets the edge security policy for the specified backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       SetEdgeSecurityPolicyBackendBucketRequest request =
           SetEdgeSecurityPolicyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       Operation response = backendBucketsClient.setEdgeSecurityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetEdgeSecurityPolicyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetEdgeSecurityPolicyBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setEdgeSecurityPolicyAsync(String project, String backendBucket, SecurityPolicyReference securityPolicyReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setEdgeSecurityPolicyAsync(String project, String backendBucket, SecurityPolicyReference securityPolicyReferenceResource)

Sets the edge security policy for the specified backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String backendBucket = "backendBucket713751966";
       SecurityPolicyReference securityPolicyReferenceResource =
           SecurityPolicyReference.newBuilder().build();
       Operation response =
           backendBucketsClient
               .setEdgeSecurityPolicyAsync(project, backendBucket, securityPolicyReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendBucket resource to which the security policy should be set. The name should conform to RFC1035.  
`securityPolicyReferenceResource` | `[SecurityPolicyReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setEdgeSecurityPolicyCallable()
    
    
    public final UnaryCallable<SetEdgeSecurityPolicyBackendBucketRequest,Operation> setEdgeSecurityPolicyCallable()

Sets the edge security policy for the specified backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       SetEdgeSecurityPolicyBackendBucketRequest request =
           SetEdgeSecurityPolicyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           backendBucketsClient.setEdgeSecurityPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetEdgeSecurityPolicyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetEdgeSecurityPolicyBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setEdgeSecurityPolicyOperationCallable()
    
    
    public final OperationCallable<SetEdgeSecurityPolicyBackendBucketRequest,Operation,Operation> setEdgeSecurityPolicyOperationCallable()

Sets the edge security policy for the specified backend bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       SetEdgeSecurityPolicyBackendBucketRequest request =
           SetEdgeSecurityPolicyBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           backendBucketsClient.setEdgeSecurityPolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetEdgeSecurityPolicyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetEdgeSecurityPolicyBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyBackendBucketRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyBackendBucketRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       SetIamPolicyBackendBucketRequest request =
           SetIamPolicyBackendBucketRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = backendBucketsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetPolicyRequest globalSetPolicyRequestResource =
           GlobalSetPolicyRequest.newBuilder().build();
       Policy response =
           backendBucketsClient.setIamPolicy(project, resource, globalSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetPolicyRequestResource` | `[GlobalSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyBackendBucketRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       SetIamPolicyBackendBucketRequest request =
           SetIamPolicyBackendBucketRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = backendBucketsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyBackendBucketRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsBackendBucketRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsBackendBucketRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       TestIamPermissionsBackendBucketRequest request =
           TestIamPermissionsBackendBucketRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = backendBucketsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           backendBucketsClient.testIamPermissions(
               project, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsBackendBucketRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       TestIamPermissionsBackendBucketRequest request =
           TestIamPermissionsBackendBucketRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           backendBucketsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsBackendBucketRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateBackendBucketRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateBackendBucketRequest request)

Updates the specified BackendBucket resource with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       UpdateBackendBucketRequest request =
           UpdateBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendBucketsClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateBackendBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String backendBucket, BackendBucket backendBucketResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String backendBucket, BackendBucket backendBucketResource)

Updates the specified BackendBucket resource with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       String project = "project-309310695";
       String backendBucket = "backendBucket713751966";
       BackendBucket backendBucketResource = BackendBucket.newBuilder().build();
       Operation response =
           backendBucketsClient.updateAsync(project, backendBucket, backendBucketResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendBucket` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendBucket resource to update.  
`backendBucketResource` | `[BackendBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucket)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateBackendBucketRequest,Operation> updateCallable()

Updates the specified BackendBucket resource with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       UpdateBackendBucketRequest request =
           UpdateBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backendBucketsClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateBackendBucketRequest,Operation,Operation> updateOperationCallable()

Updates the specified BackendBucket resource with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendBucketsClient backendBucketsClient = BackendBucketsClient.create()) {
       UpdateBackendBucketRequest request =
           UpdateBackendBucketRequest.newBuilder()
               .setBackendBucket("backendBucket713751966")
               .setBackendBucketResource(BackendBucket.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendBucketsClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBackendBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateBackendBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
