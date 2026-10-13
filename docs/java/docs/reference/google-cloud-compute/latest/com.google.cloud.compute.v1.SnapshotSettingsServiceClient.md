---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettingsServiceClient
title: Class SnapshotSettingsServiceClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:23.584644+00:00
---

# Class SnapshotSettingsServiceClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettingsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SnapshotSettingsServiceClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/SnapshotSettingsServiceClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The SnapshotSettings API.

This client uses SnapshotSettingsService version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create()) {
       String project = "project-309310695";
       SnapshotSettings response = snapshotSettingsServiceClient.get(project);
     }
     

Note: close() needs to be called on the SnapshotSettingsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Get snapshot settings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetSnapshotSettingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Patch |  Patch snapshot settings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchSnapshotSettingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, SnapshotSettings snapshotSettingsResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SnapshotSettingsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SnapshotSettingsServiceSettings snapshotSettingsServiceSettings =
         SnapshotSettingsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create(snapshotSettingsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SnapshotSettingsServiceSettings snapshotSettingsServiceSettings =
         SnapshotSettingsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create(snapshotSettingsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SnapshotSettingsServiceClient

## Static Methods 

### create()
    
    
    public static final SnapshotSettingsServiceClient create()

Constructs an instance of SnapshotSettingsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SnapshotSettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettingsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SnapshotSettingsServiceSettings settings)
    
    
    public static final SnapshotSettingsServiceClient create(SnapshotSettingsServiceSettings settings)

Constructs an instance of SnapshotSettingsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SnapshotSettingsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettingsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotSettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettingsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SnapshotSettingsServiceStub stub)
    
    
    public static final SnapshotSettingsServiceClient create(SnapshotSettingsServiceStub stub)

Constructs an instance of SnapshotSettingsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SnapshotSettingsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SnapshotSettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SnapshotSettingsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotSettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettingsServiceClient)` |   
  
## Constructors 

### SnapshotSettingsServiceClient(SnapshotSettingsServiceSettings settings)
    
    
    protected SnapshotSettingsServiceClient(SnapshotSettingsServiceSettings settings)

Constructs an instance of SnapshotSettingsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SnapshotSettingsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettingsServiceSettings)`  
  
  
### SnapshotSettingsServiceClient(SnapshotSettingsServiceStub stub)
    
    
    protected SnapshotSettingsServiceClient(SnapshotSettingsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SnapshotSettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SnapshotSettingsServiceStub)`  
  
  
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

### get(GetSnapshotSettingRequest request)
    
    
    public final SnapshotSettings get(GetSnapshotSettingRequest request)

Get snapshot settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create()) {
       GetSnapshotSettingRequest request =
           GetSnapshotSettingRequest.newBuilder().setProject("project-309310695").build();
       SnapshotSettings response = snapshotSettingsServiceClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSnapshotSettingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettings)` |   
  
### get(String project)
    
    
    public final SnapshotSettings get(String project)

Get snapshot settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create()) {
       String project = "project-309310695";
       SnapshotSettings response = snapshotSettingsServiceClient.get(project);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettings)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetSnapshotSettingRequest,SnapshotSettings> getCallable()

Get snapshot settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create()) {
       GetSnapshotSettingRequest request =
           GetSnapshotSettingRequest.newBuilder().setProject("project-309310695").build();
       ApiFuture<SnapshotSettings> future =
           snapshotSettingsServiceClient.getCallable().futureCall(request);
       // Do something.
       SnapshotSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSnapshotSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSnapshotSettingRequest),[SnapshotSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettings)>` |   
  
### getSettings()
    
    
    public final @Nullable SnapshotSettingsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.SnapshotSettingsServiceSettings` |   
  
### getStub()
    
    
    public SnapshotSettingsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SnapshotSettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SnapshotSettingsServiceStub)` |   
  
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
  
### patchAsync(PatchSnapshotSettingRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchSnapshotSettingRequest request)

Patch snapshot settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create()) {
       PatchSnapshotSettingRequest request =
           PatchSnapshotSettingRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshotSettingsResource(SnapshotSettings.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .build();
       Operation response = snapshotSettingsServiceClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchSnapshotSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchSnapshotSettingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, SnapshotSettings snapshotSettingsResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, SnapshotSettings snapshotSettingsResource)

Patch snapshot settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create()) {
       String project = "project-309310695";
       SnapshotSettings snapshotSettingsResource = SnapshotSettings.newBuilder().build();
       Operation response =
           snapshotSettingsServiceClient.patchAsync(project, snapshotSettingsResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`snapshotSettingsResource` | `[SnapshotSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotSettings)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchSnapshotSettingRequest,Operation> patchCallable()

Patch snapshot settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create()) {
       PatchSnapshotSettingRequest request =
           PatchSnapshotSettingRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshotSettingsResource(SnapshotSettings.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .build();
       ApiFuture<Operation> future =
           snapshotSettingsServiceClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchSnapshotSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchSnapshotSettingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchSnapshotSettingRequest,Operation,Operation> patchOperationCallable()

Patch snapshot settings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotSettingsServiceClient snapshotSettingsServiceClient =
         SnapshotSettingsServiceClient.create()) {
       PatchSnapshotSettingRequest request =
           PatchSnapshotSettingRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshotSettingsResource(SnapshotSettings.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .build();
       OperationFuture<Operation, Operation> future =
           snapshotSettingsServiceClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchSnapshotSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchSnapshotSettingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
