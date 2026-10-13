---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchServiceClient
title: Class BranchServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:01.549177+00:00
---

# Class BranchServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BranchServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2alpha/BranchServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for Branch Management

Branches are automatically created when a Catalog is created. There are fixed three branches in each catalog, and may use ListBranches method to get the details of all branches.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       ListBranchesResponse response = branchServiceClient.listBranches(parent);
     }
     

Note: close() needs to be called on the BranchServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListBranches |  Lists all instances of Branch under the specified parent Catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBranches(ListBranchesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBranches(CatalogName parent) 
  * listBranches(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBranchesCallable() 

  
GetBranch |  Retrieves a Branch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBranch(GetBranchRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBranch(BranchName name) 
  * getBranch(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBranchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BranchServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BranchServiceSettings branchServiceSettings =
         BranchServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BranchServiceClient branchServiceClient = BranchServiceClient.create(branchServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BranchServiceSettings branchServiceSettings =
         BranchServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     BranchServiceClient branchServiceClient = BranchServiceClient.create(branchServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BranchServiceSettings branchServiceSettings =
         BranchServiceSettings.newHttpJsonBuilder().build();
     BranchServiceClient branchServiceClient = BranchServiceClient.create(branchServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BranchServiceClient

## Static Methods 

### create()
    
    
    public static final BranchServiceClient create()

Constructs an instance of BranchServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BranchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BranchServiceSettings settings)
    
    
    public static final BranchServiceClient create(BranchServiceSettings settings)

Constructs an instance of BranchServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BranchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BranchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BranchServiceStub stub)
    
    
    public static final BranchServiceClient create(BranchServiceStub stub)

Constructs an instance of BranchServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(BranchServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BranchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.BranchServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BranchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchServiceClient)` |   
  
## Constructors 

### BranchServiceClient(BranchServiceSettings settings)
    
    
    protected BranchServiceClient(BranchServiceSettings settings)

Constructs an instance of BranchServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BranchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.BranchServiceSettings)`  
  
  
### BranchServiceClient(BranchServiceStub stub)
    
    
    protected BranchServiceClient(BranchServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BranchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.BranchServiceStub)`  
  
  
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

### getBranch(@Nullable BranchName name)
    
    
    public final Branch getBranch(@Nullable BranchName name)

Retrieves a Branch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       BranchName name = BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]");
       Branch response = branchServiceClient.getBranch(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2alpha.BranchName`  
Required. The name of the branch to retrieve. Format: `projects/*/locations/global/catalogs/default_catalog/branches/some_branch_id`. "default_branch" can be used as a special branch_id, it returns the default branch that has been set for the catalog.  
**Returns**  
---  
**Type** | **Description**  
`[Branch](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch)` |   
  
### getBranch(GetBranchRequest request)
    
    
    public final Branch getBranch(GetBranchRequest request)

Retrieves a Branch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       GetBranchRequest request =
           GetBranchRequest.newBuilder()
               .setName(BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setView(BranchView.forNumber(0))
               .build();
       Branch response = branchServiceClient.getBranch(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.GetBranchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Branch](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch)` |   
  
### getBranch(String name)
    
    
    public final Branch getBranch(String name)

Retrieves a Branch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       String name = BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString();
       Branch response = branchServiceClient.getBranch(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the branch to retrieve. Format: `projects/*/locations/global/catalogs/default_catalog/branches/some_branch_id`. "default_branch" can be used as a special branch_id, it returns the default branch that has been set for the catalog.  
**Returns**  
---  
**Type** | **Description**  
`[Branch](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch)` |   
  
### getBranchCallable()
    
    
    public final UnaryCallable<GetBranchRequest,Branch> getBranchCallable()

Retrieves a Branch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       GetBranchRequest request =
           GetBranchRequest.newBuilder()
               .setName(BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setView(BranchView.forNumber(0))
               .build();
       ApiFuture<Branch> future = branchServiceClient.getBranchCallable().futureCall(request);
       // Do something.
       Branch response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.GetBranchRequest),[Branch](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.Branch)>` |   
  
### getSettings()
    
    
    public final @Nullable BranchServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2alpha.BranchServiceSettings` |   
  
### getStub()
    
    
    public BranchServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BranchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.stub.BranchServiceStub)` |   
  
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
  
### listBranches(@Nullable CatalogName parent)
    
    
    public final ListBranchesResponse listBranches(@Nullable CatalogName parent)

Lists all instances of Branch under the specified parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       ListBranchesResponse response = branchServiceClient.listBranches(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2alpha.CatalogName`  
Required. The parent catalog resource name.  
**Returns**  
---  
**Type** | **Description**  
`[ListBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ListBranchesResponse)` |   
  
### listBranches(ListBranchesRequest request)
    
    
    public final ListBranchesResponse listBranches(ListBranchesRequest request)

Lists all instances of Branch under the specified parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       ListBranchesRequest request =
           ListBranchesRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setView(BranchView.forNumber(0))
               .build();
       ListBranchesResponse response = branchServiceClient.listBranches(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ListBranchesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ListBranchesResponse)` |   
  
### listBranches(String parent)
    
    
    public final ListBranchesResponse listBranches(String parent)

Lists all instances of Branch under the specified parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       ListBranchesResponse response = branchServiceClient.listBranches(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent catalog resource name.  
**Returns**  
---  
**Type** | **Description**  
`[ListBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ListBranchesResponse)` |   
  
### listBranchesCallable()
    
    
    public final UnaryCallable<ListBranchesRequest,ListBranchesResponse> listBranchesCallable()

Lists all instances of Branch under the specified parent Catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BranchServiceClient branchServiceClient = BranchServiceClient.create()) {
       ListBranchesRequest request =
           ListBranchesRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setView(BranchView.forNumber(0))
               .build();
       ApiFuture<ListBranchesResponse> future =
           branchServiceClient.listBranchesCallable().futureCall(request);
       // Do something.
       ListBranchesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ListBranchesRequest),[ListBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ListBranchesResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
