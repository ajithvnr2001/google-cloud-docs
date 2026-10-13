---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient
title: Class OsConfigServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:57.901007+00:00
---

# Class OsConfigServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OsConfigServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-os-config/google-cloud-os-config/src/main/java/com/google/cloud/osconfig/v1/OsConfigServiceClient.java)| [Product Reference](https://cloud.google.com/compute/docs/os-patch-management)  
---|---  
  
Service Description: OS Config API

The OS Config service is a server-side component that you can use to manage package installations and patch jobs for virtual machine instances.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ExecutePatchJobRequest request =
           PatchJobs.ExecutePatchJobRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDescription("description-1724546052")
               .setInstanceFilter(PatchJobs.PatchInstanceFilter.newBuilder().build())
               .setPatchConfig(PatchJobs.PatchConfig.newBuilder().build())
               .setDuration(Duration.newBuilder().build())
               .setDryRun(true)
               .setDisplayName("displayName1714148973")
               .setRollout(PatchJobs.PatchRollout.newBuilder().build())
               .build();
       PatchJobs.PatchJob response = osConfigServiceClient.executePatchJob(request);
     }
     

Note: close() needs to be called on the OsConfigServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ExecutePatchJob |  Patch VM instances by creating and running a patch job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * executePatchJob(PatchJobs.ExecutePatchJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * executePatchJobCallable() 

  
GetPatchJob |  Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPatchJob(PatchJobs.GetPatchJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPatchJob(PatchJobName name) 
  * getPatchJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPatchJobCallable() 

  
CancelPatchJob |  Cancel a patch job. The patch job must be active. Canceled patch jobs cannot be restarted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelPatchJob(PatchJobs.CancelPatchJobRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelPatchJobCallable() 

  
ListPatchJobs |  Get a list of patch jobs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPatchJobs(PatchJobs.ListPatchJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPatchJobs(ProjectName parent) 
  * listPatchJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPatchJobsPagedCallable() 
  * listPatchJobsCallable() 

  
ListPatchJobInstanceDetails |  Get a list of instance details for a given patch job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPatchJobInstanceDetails(PatchJobs.ListPatchJobInstanceDetailsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPatchJobInstanceDetails(PatchJobName parent) 
  * listPatchJobInstanceDetails(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPatchJobInstanceDetailsPagedCallable() 
  * listPatchJobInstanceDetailsCallable() 

  
CreatePatchDeployment |  Create an OS Config patch deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPatchDeployment(PatchDeployments.CreatePatchDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createPatchDeployment(ProjectName parent, PatchDeployments.PatchDeployment patchDeployment, String patchDeploymentId) 
  * createPatchDeployment(String parent, PatchDeployments.PatchDeployment patchDeployment, String patchDeploymentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPatchDeploymentCallable() 

  
GetPatchDeployment |  Get an OS Config patch deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPatchDeployment(PatchDeployments.GetPatchDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPatchDeployment(PatchDeploymentName name) 
  * getPatchDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPatchDeploymentCallable() 

  
ListPatchDeployments |  Get a page of OS Config patch deployments. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPatchDeployments(PatchDeployments.ListPatchDeploymentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPatchDeployments(ProjectName parent) 
  * listPatchDeployments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPatchDeploymentsPagedCallable() 
  * listPatchDeploymentsCallable() 

  
DeletePatchDeployment |  Delete an OS Config patch deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePatchDeployment(PatchDeployments.DeletePatchDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deletePatchDeployment(PatchDeploymentName name) 
  * deletePatchDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePatchDeploymentCallable() 

  
UpdatePatchDeployment |  Update an OS Config patch deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePatchDeployment(PatchDeployments.UpdatePatchDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePatchDeployment(PatchDeployments.PatchDeployment patchDeployment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePatchDeploymentCallable() 

  
PausePatchDeployment |  Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * pausePatchDeployment(PatchDeployments.PausePatchDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * pausePatchDeployment(PatchDeploymentName name) 
  * pausePatchDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * pausePatchDeploymentCallable() 

  
ResumePatchDeployment |  Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resumePatchDeployment(PatchDeployments.ResumePatchDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * resumePatchDeployment(PatchDeploymentName name) 
  * resumePatchDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resumePatchDeploymentCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of OsConfigServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OsConfigServiceSettings osConfigServiceSettings =
         OsConfigServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     OsConfigServiceClient osConfigServiceClient =
         OsConfigServiceClient.create(osConfigServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OsConfigServiceSettings osConfigServiceSettings =
         OsConfigServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     OsConfigServiceClient osConfigServiceClient =
         OsConfigServiceClient.create(osConfigServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OsConfigServiceSettings osConfigServiceSettings =
         OsConfigServiceSettings.newHttpJsonBuilder().build();
     OsConfigServiceClient osConfigServiceClient =
         OsConfigServiceClient.create(osConfigServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OsConfigServiceClient

## Static Methods 

### create()
    
    
    public static final OsConfigServiceClient create()

Constructs an instance of OsConfigServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OsConfigServiceSettings settings)
    
    
    public static final OsConfigServiceClient create(OsConfigServiceSettings settings)

Constructs an instance of OsConfigServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OsConfigServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OsConfigServiceStub stub)
    
    
    public static final OsConfigServiceClient create(OsConfigServiceStub stub)

Constructs an instance of OsConfigServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(OsConfigServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OsConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.stub.OsConfigServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient)` |   
  
## Constructors 

### OsConfigServiceClient(OsConfigServiceSettings settings)
    
    
    protected OsConfigServiceClient(OsConfigServiceSettings settings)

Constructs an instance of OsConfigServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OsConfigServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceSettings)`  
  
  
### OsConfigServiceClient(OsConfigServiceStub stub)
    
    
    protected OsConfigServiceClient(OsConfigServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OsConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.stub.OsConfigServiceStub)`  
  
  
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
  
### cancelPatchJob(PatchJobs.CancelPatchJobRequest request)
    
    
    public final PatchJobs.PatchJob cancelPatchJob(PatchJobs.CancelPatchJobRequest request)

Cancel a patch job. The patch job must be active. Canceled patch jobs cannot be restarted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.CancelPatchJobRequest request =
           PatchJobs.CancelPatchJobRequest.newBuilder()
               .setName(PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString())
               .build();
       PatchJobs.PatchJob response = osConfigServiceClient.cancelPatchJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.CancelPatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.CancelPatchJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)` |   
  
### cancelPatchJobCallable()
    
    
    public final UnaryCallable<PatchJobs.CancelPatchJobRequest,PatchJobs.PatchJob> cancelPatchJobCallable()

Cancel a patch job. The patch job must be active. Canceled patch jobs cannot be restarted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.CancelPatchJobRequest request =
           PatchJobs.CancelPatchJobRequest.newBuilder()
               .setName(PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString())
               .build();
       ApiFuture<PatchJobs.PatchJob> future =
           osConfigServiceClient.cancelPatchJobCallable().futureCall(request);
       // Do something.
       PatchJobs.PatchJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelPatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.CancelPatchJobRequest),[PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)>` |   
  
### close()
    
    
    public final void close()

### createPatchDeployment(@Nullable ProjectName parent, PatchDeployments.PatchDeployment patchDeployment, String patchDeploymentId)
    
    
    public final PatchDeployments.PatchDeployment createPatchDeployment(@Nullable ProjectName parent, PatchDeployments.PatchDeployment patchDeployment, String patchDeploymentId)

Create an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       PatchDeployments.PatchDeployment patchDeployment =
           PatchDeployments.PatchDeployment.newBuilder().build();
       String patchDeploymentId = "patchDeploymentId-1180405976";
       PatchDeployments.PatchDeployment response =
           osConfigServiceClient.createPatchDeployment(parent, patchDeployment, patchDeploymentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.ProjectName`  
Required. The project to apply this patch deployment to in the form `projects/*`.  
`patchDeployment` | `[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)`  
Required. The patch deployment to create.  
`patchDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name for the patch deployment in the project. When creating a name the following rules apply: 

  * Must contain only lowercase letters, numbers, and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the project. 

  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### createPatchDeployment(PatchDeployments.CreatePatchDeploymentRequest request)
    
    
    public final PatchDeployments.PatchDeployment createPatchDeployment(PatchDeployments.CreatePatchDeploymentRequest request)

Create an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.CreatePatchDeploymentRequest request =
           PatchDeployments.CreatePatchDeploymentRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPatchDeploymentId("patchDeploymentId-1180405976")
               .setPatchDeployment(PatchDeployments.PatchDeployment.newBuilder().build())
               .build();
       PatchDeployments.PatchDeployment response =
           osConfigServiceClient.createPatchDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.CreatePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.CreatePatchDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### createPatchDeployment(String parent, PatchDeployments.PatchDeployment patchDeployment, String patchDeploymentId)
    
    
    public final PatchDeployments.PatchDeployment createPatchDeployment(String parent, PatchDeployments.PatchDeployment patchDeployment, String patchDeploymentId)

Create an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       PatchDeployments.PatchDeployment patchDeployment =
           PatchDeployments.PatchDeployment.newBuilder().build();
       String patchDeploymentId = "patchDeploymentId-1180405976";
       PatchDeployments.PatchDeployment response =
           osConfigServiceClient.createPatchDeployment(parent, patchDeployment, patchDeploymentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to apply this patch deployment to in the form `projects/*`.  
`patchDeployment` | `[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)`  
Required. The patch deployment to create.  
`patchDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name for the patch deployment in the project. When creating a name the following rules apply: 

  * Must contain only lowercase letters, numbers, and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the project. 

  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### createPatchDeploymentCallable()
    
    
    public final UnaryCallable<PatchDeployments.CreatePatchDeploymentRequest,PatchDeployments.PatchDeployment> createPatchDeploymentCallable()

Create an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.CreatePatchDeploymentRequest request =
           PatchDeployments.CreatePatchDeploymentRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPatchDeploymentId("patchDeploymentId-1180405976")
               .setPatchDeployment(PatchDeployments.PatchDeployment.newBuilder().build())
               .build();
       ApiFuture<PatchDeployments.PatchDeployment> future =
           osConfigServiceClient.createPatchDeploymentCallable().futureCall(request);
       // Do something.
       PatchDeployments.PatchDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.CreatePatchDeploymentRequest),[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)>` |   
  
### deletePatchDeployment(@Nullable PatchDeploymentName name)
    
    
    public final void deletePatchDeployment(@Nullable PatchDeploymentName name)

Delete an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeploymentName name = PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]");
       osConfigServiceClient.deletePatchDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.PatchDeploymentName`  
Required. The resource name of the patch deployment in the form `projects/*/patchDeployments/*`.  
  
### deletePatchDeployment(PatchDeployments.DeletePatchDeploymentRequest request)
    
    
    public final void deletePatchDeployment(PatchDeployments.DeletePatchDeploymentRequest request)

Delete an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.DeletePatchDeploymentRequest request =
           PatchDeployments.DeletePatchDeploymentRequest.newBuilder()
               .setName(PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString())
               .build();
       osConfigServiceClient.deletePatchDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.DeletePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.DeletePatchDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deletePatchDeployment(String name)
    
    
    public final void deletePatchDeployment(String name)

Delete an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String name = PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString();
       osConfigServiceClient.deletePatchDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the patch deployment in the form `projects/*/patchDeployments/*`.  
  
### deletePatchDeploymentCallable()
    
    
    public final UnaryCallable<PatchDeployments.DeletePatchDeploymentRequest,Empty> deletePatchDeploymentCallable()

Delete an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.DeletePatchDeploymentRequest request =
           PatchDeployments.DeletePatchDeploymentRequest.newBuilder()
               .setName(PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString())
               .build();
       ApiFuture<Empty> future =
           osConfigServiceClient.deletePatchDeploymentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.DeletePatchDeploymentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### executePatchJob(PatchJobs.ExecutePatchJobRequest request)
    
    
    public final PatchJobs.PatchJob executePatchJob(PatchJobs.ExecutePatchJobRequest request)

Patch VM instances by creating and running a patch job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ExecutePatchJobRequest request =
           PatchJobs.ExecutePatchJobRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDescription("description-1724546052")
               .setInstanceFilter(PatchJobs.PatchInstanceFilter.newBuilder().build())
               .setPatchConfig(PatchJobs.PatchConfig.newBuilder().build())
               .setDuration(Duration.newBuilder().build())
               .setDryRun(true)
               .setDisplayName("displayName1714148973")
               .setRollout(PatchJobs.PatchRollout.newBuilder().build())
               .build();
       PatchJobs.PatchJob response = osConfigServiceClient.executePatchJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.ExecutePatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ExecutePatchJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)` |   
  
### executePatchJobCallable()
    
    
    public final UnaryCallable<PatchJobs.ExecutePatchJobRequest,PatchJobs.PatchJob> executePatchJobCallable()

Patch VM instances by creating and running a patch job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ExecutePatchJobRequest request =
           PatchJobs.ExecutePatchJobRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDescription("description-1724546052")
               .setInstanceFilter(PatchJobs.PatchInstanceFilter.newBuilder().build())
               .setPatchConfig(PatchJobs.PatchConfig.newBuilder().build())
               .setDuration(Duration.newBuilder().build())
               .setDryRun(true)
               .setDisplayName("displayName1714148973")
               .setRollout(PatchJobs.PatchRollout.newBuilder().build())
               .build();
       ApiFuture<PatchJobs.PatchJob> future =
           osConfigServiceClient.executePatchJobCallable().futureCall(request);
       // Do something.
       PatchJobs.PatchJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExecutePatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ExecutePatchJobRequest),[PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)>` |   
  
### getPatchDeployment(@Nullable PatchDeploymentName name)
    
    
    public final PatchDeployments.PatchDeployment getPatchDeployment(@Nullable PatchDeploymentName name)

Get an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeploymentName name = PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]");
       PatchDeployments.PatchDeployment response = osConfigServiceClient.getPatchDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.PatchDeploymentName`  
Required. The resource name of the patch deployment in the form `projects/*/patchDeployments/*`.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### getPatchDeployment(PatchDeployments.GetPatchDeploymentRequest request)
    
    
    public final PatchDeployments.PatchDeployment getPatchDeployment(PatchDeployments.GetPatchDeploymentRequest request)

Get an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.GetPatchDeploymentRequest request =
           PatchDeployments.GetPatchDeploymentRequest.newBuilder()
               .setName(PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString())
               .build();
       PatchDeployments.PatchDeployment response = osConfigServiceClient.getPatchDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.GetPatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.GetPatchDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### getPatchDeployment(String name)
    
    
    public final PatchDeployments.PatchDeployment getPatchDeployment(String name)

Get an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String name = PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString();
       PatchDeployments.PatchDeployment response = osConfigServiceClient.getPatchDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the patch deployment in the form `projects/*/patchDeployments/*`.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### getPatchDeploymentCallable()
    
    
    public final UnaryCallable<PatchDeployments.GetPatchDeploymentRequest,PatchDeployments.PatchDeployment> getPatchDeploymentCallable()

Get an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.GetPatchDeploymentRequest request =
           PatchDeployments.GetPatchDeploymentRequest.newBuilder()
               .setName(PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString())
               .build();
       ApiFuture<PatchDeployments.PatchDeployment> future =
           osConfigServiceClient.getPatchDeploymentCallable().futureCall(request);
       // Do something.
       PatchDeployments.PatchDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.GetPatchDeploymentRequest),[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)>` |   
  
### getPatchJob(@Nullable PatchJobName name)
    
    
    public final PatchJobs.PatchJob getPatchJob(@Nullable PatchJobName name)

Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobName name = PatchJobName.of("[PROJECT]", "[PATCH_JOB]");
       PatchJobs.PatchJob response = osConfigServiceClient.getPatchJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.PatchJobName`  
Required. Name of the patch in the form `projects/*/patchJobs/*`  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)` |   
  
### getPatchJob(PatchJobs.GetPatchJobRequest request)
    
    
    public final PatchJobs.PatchJob getPatchJob(PatchJobs.GetPatchJobRequest request)

Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.GetPatchJobRequest request =
           PatchJobs.GetPatchJobRequest.newBuilder()
               .setName(PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString())
               .build();
       PatchJobs.PatchJob response = osConfigServiceClient.getPatchJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.GetPatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.GetPatchJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)` |   
  
### getPatchJob(String name)
    
    
    public final PatchJobs.PatchJob getPatchJob(String name)

Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String name = PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString();
       PatchJobs.PatchJob response = osConfigServiceClient.getPatchJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the patch in the form `projects/*/patchJobs/*`  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)` |   
  
### getPatchJobCallable()
    
    
    public final UnaryCallable<PatchJobs.GetPatchJobRequest,PatchJobs.PatchJob> getPatchJobCallable()

Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.GetPatchJobRequest request =
           PatchJobs.GetPatchJobRequest.newBuilder()
               .setName(PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString())
               .build();
       ApiFuture<PatchJobs.PatchJob> future =
           osConfigServiceClient.getPatchJobCallable().futureCall(request);
       // Do something.
       PatchJobs.PatchJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.GetPatchJobRequest),[PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)>` |   
  
### getSettings()
    
    
    public final @Nullable OsConfigServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.OsConfigServiceSettings` |   
  
### getStub()
    
    
    public OsConfigServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.stub.OsConfigServiceStub)` |   
  
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
  
### listPatchDeployments(@Nullable ProjectName parent)
    
    
    public final OsConfigServiceClient.ListPatchDeploymentsPagedResponse listPatchDeployments(@Nullable ProjectName parent)

Get a page of OS Config patch deployments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (PatchDeployments.PatchDeployment element :
           osConfigServiceClient.listPatchDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.ProjectName`  
Required. The resource name of the parent in the form `projects/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchDeploymentsPagedResponse)` |   
  
### listPatchDeployments(PatchDeployments.ListPatchDeploymentsRequest request)
    
    
    public final OsConfigServiceClient.ListPatchDeploymentsPagedResponse listPatchDeployments(PatchDeployments.ListPatchDeploymentsRequest request)

Get a page of OS Config patch deployments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.ListPatchDeploymentsRequest request =
           PatchDeployments.ListPatchDeploymentsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (PatchDeployments.PatchDeployment element :
           osConfigServiceClient.listPatchDeployments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.ListPatchDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.ListPatchDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchDeploymentsPagedResponse)` |   
  
### listPatchDeployments(String parent)
    
    
    public final OsConfigServiceClient.ListPatchDeploymentsPagedResponse listPatchDeployments(String parent)

Get a page of OS Config patch deployments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (PatchDeployments.PatchDeployment element :
           osConfigServiceClient.listPatchDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent in the form `projects/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchDeploymentsPagedResponse)` |   
  
### listPatchDeploymentsCallable()
    
    
    public final UnaryCallable<PatchDeployments.ListPatchDeploymentsRequest,PatchDeployments.ListPatchDeploymentsResponse> listPatchDeploymentsCallable()

Get a page of OS Config patch deployments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.ListPatchDeploymentsRequest request =
           PatchDeployments.ListPatchDeploymentsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         PatchDeployments.ListPatchDeploymentsResponse response =
             osConfigServiceClient.listPatchDeploymentsCallable().call(request);
         for (PatchDeployments.PatchDeployment element : response.getPatchDeploymentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPatchDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.ListPatchDeploymentsRequest),[ListPatchDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.ListPatchDeploymentsResponse)>` |   
  
### listPatchDeploymentsPagedCallable()
    
    
    public final UnaryCallable<PatchDeployments.ListPatchDeploymentsRequest,OsConfigServiceClient.ListPatchDeploymentsPagedResponse> listPatchDeploymentsPagedCallable()

Get a page of OS Config patch deployments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.ListPatchDeploymentsRequest request =
           PatchDeployments.ListPatchDeploymentsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<PatchDeployments.PatchDeployment> future =
           osConfigServiceClient.listPatchDeploymentsPagedCallable().futureCall(request);
       // Do something.
       for (PatchDeployments.PatchDeployment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPatchDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.ListPatchDeploymentsRequest),[ListPatchDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchDeploymentsPagedResponse)>` |   
  
### listPatchJobInstanceDetails(@Nullable PatchJobName parent)
    
    
    public final OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse listPatchJobInstanceDetails(@Nullable PatchJobName parent)

Get a list of instance details for a given patch job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobName parent = PatchJobName.of("[PROJECT]", "[PATCH_JOB]");
       for (PatchJobs.PatchJobInstanceDetails element :
           osConfigServiceClient.listPatchJobInstanceDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.PatchJobName`  
Required. The parent for the instances are in the form of `projects/*/patchJobs/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse)` |   
  
### listPatchJobInstanceDetails(PatchJobs.ListPatchJobInstanceDetailsRequest request)
    
    
    public final OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse listPatchJobInstanceDetails(PatchJobs.ListPatchJobInstanceDetailsRequest request)

Get a list of instance details for a given patch job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ListPatchJobInstanceDetailsRequest request =
           PatchJobs.ListPatchJobInstanceDetailsRequest.newBuilder()
               .setParent(PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (PatchJobs.PatchJobInstanceDetails element :
           osConfigServiceClient.listPatchJobInstanceDetails(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.ListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ListPatchJobInstanceDetailsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse)` |   
  
### listPatchJobInstanceDetails(String parent)
    
    
    public final OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse listPatchJobInstanceDetails(String parent)

Get a list of instance details for a given patch job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String parent = PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString();
       for (PatchJobs.PatchJobInstanceDetails element :
           osConfigServiceClient.listPatchJobInstanceDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent for the instances are in the form of `projects/*/patchJobs/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse)` |   
  
### listPatchJobInstanceDetailsCallable()
    
    
    public final UnaryCallable<PatchJobs.ListPatchJobInstanceDetailsRequest,PatchJobs.ListPatchJobInstanceDetailsResponse> listPatchJobInstanceDetailsCallable()

Get a list of instance details for a given patch job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ListPatchJobInstanceDetailsRequest request =
           PatchJobs.ListPatchJobInstanceDetailsRequest.newBuilder()
               .setParent(PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         PatchJobs.ListPatchJobInstanceDetailsResponse response =
             osConfigServiceClient.listPatchJobInstanceDetailsCallable().call(request);
         for (PatchJobs.PatchJobInstanceDetails element :
             response.getPatchJobInstanceDetailsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ListPatchJobInstanceDetailsRequest),[ListPatchJobInstanceDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ListPatchJobInstanceDetailsResponse)>` |   
  
### listPatchJobInstanceDetailsPagedCallable()
    
    
    public final UnaryCallable<PatchJobs.ListPatchJobInstanceDetailsRequest,OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse> listPatchJobInstanceDetailsPagedCallable()

Get a list of instance details for a given patch job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ListPatchJobInstanceDetailsRequest request =
           PatchJobs.ListPatchJobInstanceDetailsRequest.newBuilder()
               .setParent(PatchJobName.of("[PROJECT]", "[PATCH_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<PatchJobs.PatchJobInstanceDetails> future =
           osConfigServiceClient.listPatchJobInstanceDetailsPagedCallable().futureCall(request);
       // Do something.
       for (PatchJobs.PatchJobInstanceDetails element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ListPatchJobInstanceDetailsRequest),[ListPatchJobInstanceDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchJobInstanceDetailsPagedResponse)>` |   
  
### listPatchJobs(@Nullable ProjectName parent)
    
    
    public final OsConfigServiceClient.ListPatchJobsPagedResponse listPatchJobs(@Nullable ProjectName parent)

Get a list of patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (PatchJobs.PatchJob element : osConfigServiceClient.listPatchJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.ProjectName`  
Required. In the form of `projects/*`  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchJobsPagedResponse)` |   
  
### listPatchJobs(PatchJobs.ListPatchJobsRequest request)
    
    
    public final OsConfigServiceClient.ListPatchJobsPagedResponse listPatchJobs(PatchJobs.ListPatchJobsRequest request)

Get a list of patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ListPatchJobsRequest request =
           PatchJobs.ListPatchJobsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (PatchJobs.PatchJob element : osConfigServiceClient.listPatchJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.ListPatchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ListPatchJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchJobsPagedResponse)` |   
  
### listPatchJobs(String parent)
    
    
    public final OsConfigServiceClient.ListPatchJobsPagedResponse listPatchJobs(String parent)

Get a list of patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (PatchJobs.PatchJob element : osConfigServiceClient.listPatchJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. In the form of `projects/*`  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceClient.ListPatchJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchJobsPagedResponse)` |   
  
### listPatchJobsCallable()
    
    
    public final UnaryCallable<PatchJobs.ListPatchJobsRequest,PatchJobs.ListPatchJobsResponse> listPatchJobsCallable()

Get a list of patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ListPatchJobsRequest request =
           PatchJobs.ListPatchJobsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         PatchJobs.ListPatchJobsResponse response =
             osConfigServiceClient.listPatchJobsCallable().call(request);
         for (PatchJobs.PatchJob element : response.getPatchJobsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPatchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ListPatchJobsRequest),[ListPatchJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ListPatchJobsResponse)>` |   
  
### listPatchJobsPagedCallable()
    
    
    public final UnaryCallable<PatchJobs.ListPatchJobsRequest,OsConfigServiceClient.ListPatchJobsPagedResponse> listPatchJobsPagedCallable()

Get a list of patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchJobs.ListPatchJobsRequest request =
           PatchJobs.ListPatchJobsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<PatchJobs.PatchJob> future =
           osConfigServiceClient.listPatchJobsPagedCallable().futureCall(request);
       // Do something.
       for (PatchJobs.PatchJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPatchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.ListPatchJobsRequest),[ListPatchJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigServiceClient.ListPatchJobsPagedResponse)>` |   
  
### pausePatchDeployment(@Nullable PatchDeploymentName name)
    
    
    public final PatchDeployments.PatchDeployment pausePatchDeployment(@Nullable PatchDeploymentName name)

Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeploymentName name = PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]");
       PatchDeployments.PatchDeployment response = osConfigServiceClient.pausePatchDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.PatchDeploymentName`  
Required. The resource name of the patch deployment in the form `projects/*/patchDeployments/*`.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### pausePatchDeployment(PatchDeployments.PausePatchDeploymentRequest request)
    
    
    public final PatchDeployments.PatchDeployment pausePatchDeployment(PatchDeployments.PausePatchDeploymentRequest request)

Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.PausePatchDeploymentRequest request =
           PatchDeployments.PausePatchDeploymentRequest.newBuilder()
               .setName(PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString())
               .build();
       PatchDeployments.PatchDeployment response =
           osConfigServiceClient.pausePatchDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.PausePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PausePatchDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### pausePatchDeployment(String name)
    
    
    public final PatchDeployments.PatchDeployment pausePatchDeployment(String name)

Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String name = PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString();
       PatchDeployments.PatchDeployment response = osConfigServiceClient.pausePatchDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the patch deployment in the form `projects/*/patchDeployments/*`.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### pausePatchDeploymentCallable()
    
    
    public final UnaryCallable<PatchDeployments.PausePatchDeploymentRequest,PatchDeployments.PatchDeployment> pausePatchDeploymentCallable()

Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.PausePatchDeploymentRequest request =
           PatchDeployments.PausePatchDeploymentRequest.newBuilder()
               .setName(PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString())
               .build();
       ApiFuture<PatchDeployments.PatchDeployment> future =
           osConfigServiceClient.pausePatchDeploymentCallable().futureCall(request);
       // Do something.
       PatchDeployments.PatchDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PausePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PausePatchDeploymentRequest),[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)>` |   
  
### resumePatchDeployment(@Nullable PatchDeploymentName name)
    
    
    public final PatchDeployments.PatchDeployment resumePatchDeployment(@Nullable PatchDeploymentName name)

Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeploymentName name = PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]");
       PatchDeployments.PatchDeployment response = osConfigServiceClient.resumePatchDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.PatchDeploymentName`  
Required. The resource name of the patch deployment in the form `projects/*/patchDeployments/*`.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### resumePatchDeployment(PatchDeployments.ResumePatchDeploymentRequest request)
    
    
    public final PatchDeployments.PatchDeployment resumePatchDeployment(PatchDeployments.ResumePatchDeploymentRequest request)

Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.ResumePatchDeploymentRequest request =
           PatchDeployments.ResumePatchDeploymentRequest.newBuilder()
               .setName(PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString())
               .build();
       PatchDeployments.PatchDeployment response =
           osConfigServiceClient.resumePatchDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.ResumePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.ResumePatchDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### resumePatchDeployment(String name)
    
    
    public final PatchDeployments.PatchDeployment resumePatchDeployment(String name)

Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       String name = PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString();
       PatchDeployments.PatchDeployment response = osConfigServiceClient.resumePatchDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the patch deployment in the form `projects/*/patchDeployments/*`.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### resumePatchDeploymentCallable()
    
    
    public final UnaryCallable<PatchDeployments.ResumePatchDeploymentRequest,PatchDeployments.PatchDeployment> resumePatchDeploymentCallable()

Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.ResumePatchDeploymentRequest request =
           PatchDeployments.ResumePatchDeploymentRequest.newBuilder()
               .setName(PatchDeploymentName.of("[PROJECT]", "[PATCH_DEPLOYMENT]").toString())
               .build();
       ApiFuture<PatchDeployments.PatchDeployment> future =
           osConfigServiceClient.resumePatchDeploymentCallable().futureCall(request);
       // Do something.
       PatchDeployments.PatchDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResumePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.ResumePatchDeploymentRequest),[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePatchDeployment(PatchDeployments.PatchDeployment patchDeployment, FieldMask updateMask)
    
    
    public final PatchDeployments.PatchDeployment updatePatchDeployment(PatchDeployments.PatchDeployment patchDeployment, FieldMask updateMask)

Update an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.PatchDeployment patchDeployment =
           PatchDeployments.PatchDeployment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PatchDeployments.PatchDeployment response =
           osConfigServiceClient.updatePatchDeployment(patchDeployment, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`patchDeployment` | `[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)`  
Required. The patch deployment to Update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask that controls which fields of the patch deployment should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### updatePatchDeployment(PatchDeployments.UpdatePatchDeploymentRequest request)
    
    
    public final PatchDeployments.PatchDeployment updatePatchDeployment(PatchDeployments.UpdatePatchDeploymentRequest request)

Update an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.UpdatePatchDeploymentRequest request =
           PatchDeployments.UpdatePatchDeploymentRequest.newBuilder()
               .setPatchDeployment(PatchDeployments.PatchDeployment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       PatchDeployments.PatchDeployment response =
           osConfigServiceClient.updatePatchDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.UpdatePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.UpdatePatchDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PatchDeployments.PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)` |   
  
### updatePatchDeploymentCallable()
    
    
    public final UnaryCallable<PatchDeployments.UpdatePatchDeploymentRequest,PatchDeployments.PatchDeployment> updatePatchDeploymentCallable()

Update an OS Config patch deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigServiceClient osConfigServiceClient = OsConfigServiceClient.create()) {
       PatchDeployments.UpdatePatchDeploymentRequest request =
           PatchDeployments.UpdatePatchDeploymentRequest.newBuilder()
               .setPatchDeployment(PatchDeployments.PatchDeployment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<PatchDeployments.PatchDeployment> future =
           osConfigServiceClient.updatePatchDeploymentCallable().futureCall(request);
       // Do something.
       PatchDeployments.PatchDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.UpdatePatchDeploymentRequest),[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchDeployments.PatchDeployment)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
