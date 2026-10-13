---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient
title: Class AssuredWorkloadsServiceClient (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:07.351202+00:00
---

# Class AssuredWorkloadsServiceClient (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AssuredWorkloadsServiceClient (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.1.0  2.0.0  1.1.0  1.0.4  0.9.0  0.8.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-assured-workloads/google-cloud-assured-workloads/src/main/java/com/google/cloud/assuredworkloads/v1/AssuredWorkloadsServiceClient.java)| [Product Reference](https://cloud.google.com/assured-workloads/)| [REST Documentation](https://cloud.google.com/assured-workloads/docs/reference/rest)  
---|---|---  
  
Service Description: Service to manage AssuredWorkloads.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       Workload workload = Workload.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Workload response = assuredWorkloadsServiceClient.updateWorkload(workload, updateMask);
     }
     

Note: close() needs to be called on the AssuredWorkloadsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateWorkload |  Creates Assured Workload. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWorkloadAsync(CreateWorkloadRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createWorkloadAsync(LocationName parent, Workload workload) 
  * createWorkloadAsync(String parent, Workload workload) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWorkloadOperationCallable() 
  * createWorkloadCallable() 

  
UpdateWorkload |  Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateWorkload(UpdateWorkloadRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateWorkload(Workload workload, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateWorkloadCallable() 

  
RestrictAllowedResources |  Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restrictAllowedResources(RestrictAllowedResourcesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restrictAllowedResourcesCallable() 

  
DeleteWorkload |  Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteWorkload(DeleteWorkloadRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteWorkload(WorkloadName name) 
  * deleteWorkload(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteWorkloadCallable() 

  
GetWorkload |  Gets Assured Workload associated with a CRM Node |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWorkload(GetWorkloadRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWorkload(WorkloadName name) 
  * getWorkload(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWorkloadCallable() 

  
ListWorkloads |  Lists Assured Workloads under a CRM Node. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWorkloads(ListWorkloadsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWorkloads(LocationName parent) 
  * listWorkloads(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWorkloadsPagedCallable() 
  * listWorkloadsCallable() 

  
ListViolations |  Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listViolations(ListViolationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listViolations(WorkloadName parent) 
  * listViolations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listViolationsPagedCallable() 
  * listViolationsCallable() 

  
GetViolation |  Retrieves Assured Workload Violation based on ID. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getViolation(GetViolationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getViolation(ViolationName name) 
  * getViolation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getViolationCallable() 

  
AcknowledgeViolation |  Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * acknowledgeViolation(AcknowledgeViolationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * acknowledgeViolationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AssuredWorkloadsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AssuredWorkloadsServiceSettings assuredWorkloadsServiceSettings =
         AssuredWorkloadsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create(assuredWorkloadsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AssuredWorkloadsServiceSettings assuredWorkloadsServiceSettings =
         AssuredWorkloadsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create(assuredWorkloadsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AssuredWorkloadsServiceSettings assuredWorkloadsServiceSettings =
         AssuredWorkloadsServiceSettings.newHttpJsonBuilder().build();
     AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create(assuredWorkloadsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AssuredWorkloadsServiceClient

## Static Methods 

### create()
    
    
    public static final AssuredWorkloadsServiceClient create()

Constructs an instance of AssuredWorkloadsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AssuredWorkloadsServiceSettings settings)
    
    
    public static final AssuredWorkloadsServiceClient create(AssuredWorkloadsServiceSettings settings)

Constructs an instance of AssuredWorkloadsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AssuredWorkloadsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AssuredWorkloadsServiceStub stub)
    
    
    public static final AssuredWorkloadsServiceClient create(AssuredWorkloadsServiceStub stub)

Constructs an instance of AssuredWorkloadsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AssuredWorkloadsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AssuredWorkloadsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.stub.AssuredWorkloadsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient)` |   
  
## Constructors 

### AssuredWorkloadsServiceClient(AssuredWorkloadsServiceSettings settings)
    
    
    protected AssuredWorkloadsServiceClient(AssuredWorkloadsServiceSettings settings)

Constructs an instance of AssuredWorkloadsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AssuredWorkloadsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceSettings)`  
  
  
### AssuredWorkloadsServiceClient(AssuredWorkloadsServiceStub stub)
    
    
    protected AssuredWorkloadsServiceClient(AssuredWorkloadsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AssuredWorkloadsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.stub.AssuredWorkloadsServiceStub)`  
  
  
## Methods 

### acknowledgeViolation(AcknowledgeViolationRequest request)
    
    
    public final AcknowledgeViolationResponse acknowledgeViolation(AcknowledgeViolationRequest request)

Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       AcknowledgeViolationRequest request =
           AcknowledgeViolationRequest.newBuilder()
               .setName("name3373707")
               .setComment("comment950398559")
               .setNonCompliantOrgPolicy("nonCompliantOrgPolicy-1928466552")
               .build();
       AcknowledgeViolationResponse response =
           assuredWorkloadsServiceClient.acknowledgeViolation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AcknowledgeViolationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AcknowledgeViolationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AcknowledgeViolationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AcknowledgeViolationResponse)` |   
  
### acknowledgeViolationCallable()
    
    
    public final UnaryCallable<AcknowledgeViolationRequest,AcknowledgeViolationResponse> acknowledgeViolationCallable()

Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       AcknowledgeViolationRequest request =
           AcknowledgeViolationRequest.newBuilder()
               .setName("name3373707")
               .setComment("comment950398559")
               .setNonCompliantOrgPolicy("nonCompliantOrgPolicy-1928466552")
               .build();
       ApiFuture<AcknowledgeViolationResponse> future =
           assuredWorkloadsServiceClient.acknowledgeViolationCallable().futureCall(request);
       // Do something.
       AcknowledgeViolationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AcknowledgeViolationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AcknowledgeViolationRequest),[AcknowledgeViolationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AcknowledgeViolationResponse)>` |   
  
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

### createWorkloadAsync(@Nullable LocationName parent, Workload workload)
    
    
    public final OperationFuture<Workload,CreateWorkloadOperationMetadata> createWorkloadAsync(@Nullable LocationName parent, Workload workload)

Creates Assured Workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       LocationName parent = LocationName.of("[ORGANIZATION]", "[LOCATION]");
       Workload workload = Workload.newBuilder().build();
       Workload response = assuredWorkloadsServiceClient.createWorkloadAsync(parent, workload).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.assuredworkloads.v1.LocationName`  
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`.  
`workload` | `[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)`  
Required. Assured Workload to create  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload),[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.CreateWorkloadOperationMetadata)>` |   
  
### createWorkloadAsync(CreateWorkloadRequest request)
    
    
    public final OperationFuture<Workload,CreateWorkloadOperationMetadata> createWorkloadAsync(CreateWorkloadRequest request)

Creates Assured Workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       CreateWorkloadRequest request =
           CreateWorkloadRequest.newBuilder()
               .setParent(LocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setWorkload(Workload.newBuilder().build())
               .setExternalId("externalId-1699764666")
               .build();
       Workload response = assuredWorkloadsServiceClient.createWorkloadAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.CreateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload),[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.CreateWorkloadOperationMetadata)>` |   
  
### createWorkloadAsync(String parent, Workload workload)
    
    
    public final OperationFuture<Workload,CreateWorkloadOperationMetadata> createWorkloadAsync(String parent, Workload workload)

Creates Assured Workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       String parent = LocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       Workload workload = Workload.newBuilder().build();
       Workload response = assuredWorkloadsServiceClient.createWorkloadAsync(parent, workload).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the new Workload's parent. Must be of the form `organizations/{org_id}/locations/{location_id}`.  
`workload` | `[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)`  
Required. Assured Workload to create  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload),[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.CreateWorkloadOperationMetadata)>` |   
  
### createWorkloadCallable()
    
    
    public final UnaryCallable<CreateWorkloadRequest,Operation> createWorkloadCallable()

Creates Assured Workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       CreateWorkloadRequest request =
           CreateWorkloadRequest.newBuilder()
               .setParent(LocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setWorkload(Workload.newBuilder().build())
               .setExternalId("externalId-1699764666")
               .build();
       ApiFuture<Operation> future =
           assuredWorkloadsServiceClient.createWorkloadCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.CreateWorkloadRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWorkloadOperationCallable()
    
    
    public final OperationCallable<CreateWorkloadRequest,Workload,CreateWorkloadOperationMetadata> createWorkloadOperationCallable()

Creates Assured Workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       CreateWorkloadRequest request =
           CreateWorkloadRequest.newBuilder()
               .setParent(LocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setWorkload(Workload.newBuilder().build())
               .setExternalId("externalId-1699764666")
               .build();
       OperationFuture<Workload, CreateWorkloadOperationMetadata> future =
           assuredWorkloadsServiceClient.createWorkloadOperationCallable().futureCall(request);
       // Do something.
       Workload response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.CreateWorkloadRequest),[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload),[CreateWorkloadOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.CreateWorkloadOperationMetadata)>` |   
  
### deleteWorkload(@Nullable WorkloadName name)
    
    
    public final void deleteWorkload(@Nullable WorkloadName name)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       WorkloadName name = WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
       assuredWorkloadsServiceClient.deleteWorkload(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.assuredworkloads.v1.WorkloadName`  
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
  
### deleteWorkload(DeleteWorkloadRequest request)
    
    
    public final void deleteWorkload(DeleteWorkloadRequest request)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       DeleteWorkloadRequest request =
           DeleteWorkloadRequest.newBuilder()
               .setName(WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString())
               .setEtag("etag3123477")
               .build();
       assuredWorkloadsServiceClient.deleteWorkload(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.DeleteWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteWorkload(String name)
    
    
    public final void deleteWorkload(String name)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       String name = WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString();
       assuredWorkloadsServiceClient.deleteWorkload(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
  
### deleteWorkloadCallable()
    
    
    public final UnaryCallable<DeleteWorkloadRequest,Empty> deleteWorkloadCallable()

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       DeleteWorkloadRequest request =
           DeleteWorkloadRequest.newBuilder()
               .setName(WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future =
           assuredWorkloadsServiceClient.deleteWorkloadCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.DeleteWorkloadRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable AssuredWorkloadsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceSettings` |   
  
### getStub()
    
    
    public AssuredWorkloadsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.stub.AssuredWorkloadsServiceStub)` |   
  
### getViolation(@Nullable ViolationName name)
    
    
    public final Violation getViolation(@Nullable ViolationName name)

Retrieves Assured Workload Violation based on ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       ViolationName name =
           ViolationName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]");
       Violation response = assuredWorkloadsServiceClient.getViolation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.assuredworkloads.v1.ViolationName`  
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
**Returns**  
---  
**Type** | **Description**  
`[Violation](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Violation)` |   
  
### getViolation(GetViolationRequest request)
    
    
    public final Violation getViolation(GetViolationRequest request)

Retrieves Assured Workload Violation based on ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       GetViolationRequest request =
           GetViolationRequest.newBuilder()
               .setName(
                   ViolationName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]")
                       .toString())
               .build();
       Violation response = assuredWorkloadsServiceClient.getViolation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetViolationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.GetViolationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Violation](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Violation)` |   
  
### getViolation(String name)
    
    
    public final Violation getViolation(String name)

Retrieves Assured Workload Violation based on ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       String name =
           ViolationName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]").toString();
       Violation response = assuredWorkloadsServiceClient.getViolation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Violation to fetch (ie. Violation.name). Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
**Returns**  
---  
**Type** | **Description**  
`[Violation](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Violation)` |   
  
### getViolationCallable()
    
    
    public final UnaryCallable<GetViolationRequest,Violation> getViolationCallable()

Retrieves Assured Workload Violation based on ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       GetViolationRequest request =
           GetViolationRequest.newBuilder()
               .setName(
                   ViolationName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]", "[VIOLATION]")
                       .toString())
               .build();
       ApiFuture<Violation> future =
           assuredWorkloadsServiceClient.getViolationCallable().futureCall(request);
       // Do something.
       Violation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetViolationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.GetViolationRequest),[Violation](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Violation)>` |   
  
### getWorkload(@Nullable WorkloadName name)
    
    
    public final Workload getWorkload(@Nullable WorkloadName name)

Gets Assured Workload associated with a CRM Node

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       WorkloadName name = WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
       Workload response = assuredWorkloadsServiceClient.getWorkload(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.assuredworkloads.v1.WorkloadName`  
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)` |   
  
### getWorkload(GetWorkloadRequest request)
    
    
    public final Workload getWorkload(GetWorkloadRequest request)

Gets Assured Workload associated with a CRM Node

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       GetWorkloadRequest request =
           GetWorkloadRequest.newBuilder()
               .setName(WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString())
               .build();
       Workload response = assuredWorkloadsServiceClient.getWorkload(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.GetWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)` |   
  
### getWorkload(String name)
    
    
    public final Workload getWorkload(String name)

Gets Assured Workload associated with a CRM Node

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       String name = WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString();
       Workload response = assuredWorkloadsServiceClient.getWorkload(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Workload to fetch. This is the workload's relative path in the API, formatted as "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)` |   
  
### getWorkloadCallable()
    
    
    public final UnaryCallable<GetWorkloadRequest,Workload> getWorkloadCallable()

Gets Assured Workload associated with a CRM Node

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       GetWorkloadRequest request =
           GetWorkloadRequest.newBuilder()
               .setName(WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString())
               .build();
       ApiFuture<Workload> future =
           assuredWorkloadsServiceClient.getWorkloadCallable().futureCall(request);
       // Do something.
       Workload response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.GetWorkloadRequest),[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)>` |   
  
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
  
### listViolations(@Nullable WorkloadName parent)
    
    
    public final AssuredWorkloadsServiceClient.ListViolationsPagedResponse listViolations(@Nullable WorkloadName parent)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       WorkloadName parent = WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]");
       for (Violation element : assuredWorkloadsServiceClient.listViolations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.assuredworkloads.v1.WorkloadName`  
Required. The Workload name. Format `organizations/{org_id}/locations/{location}/workloads/{workload}`.  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient.ListViolationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient.ListViolationsPagedResponse)` |   
  
### listViolations(ListViolationsRequest request)
    
    
    public final AssuredWorkloadsServiceClient.ListViolationsPagedResponse listViolations(ListViolationsRequest request)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       ListViolationsRequest request =
           ListViolationsRequest.newBuilder()
               .setParent(WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString())
               .setInterval(TimeWindow.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Violation element : assuredWorkloadsServiceClient.listViolations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListViolationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListViolationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient.ListViolationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient.ListViolationsPagedResponse)` |   
  
### listViolations(String parent)
    
    
    public final AssuredWorkloadsServiceClient.ListViolationsPagedResponse listViolations(String parent)

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       String parent = WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString();
       for (Violation element : assuredWorkloadsServiceClient.listViolations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Workload name. Format `organizations/{org_id}/locations/{location}/workloads/{workload}`.  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient.ListViolationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient.ListViolationsPagedResponse)` |   
  
### listViolationsCallable()
    
    
    public final UnaryCallable<ListViolationsRequest,ListViolationsResponse> listViolationsCallable()

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       ListViolationsRequest request =
           ListViolationsRequest.newBuilder()
               .setParent(WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString())
               .setInterval(TimeWindow.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListViolationsResponse response =
             assuredWorkloadsServiceClient.listViolationsCallable().call(request);
         for (Violation element : response.getViolationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListViolationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListViolationsRequest),[ListViolationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListViolationsResponse)>` |   
  
### listViolationsPagedCallable()
    
    
    public final UnaryCallable<ListViolationsRequest,AssuredWorkloadsServiceClient.ListViolationsPagedResponse> listViolationsPagedCallable()

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       ListViolationsRequest request =
           ListViolationsRequest.newBuilder()
               .setParent(WorkloadName.of("[ORGANIZATION]", "[LOCATION]", "[WORKLOAD]").toString())
               .setInterval(TimeWindow.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Violation> future =
           assuredWorkloadsServiceClient.listViolationsPagedCallable().futureCall(request);
       // Do something.
       for (Violation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListViolationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListViolationsRequest),[ListViolationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient.ListViolationsPagedResponse)>` |   
  
### listWorkloads(@Nullable LocationName parent)
    
    
    public final AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse listWorkloads(@Nullable LocationName parent)

Lists Assured Workloads under a CRM Node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       LocationName parent = LocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (Workload element : assuredWorkloadsServiceClient.listWorkloads(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.assuredworkloads.v1.LocationName`  
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse)` |   
  
### listWorkloads(ListWorkloadsRequest request)
    
    
    public final AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse listWorkloads(ListWorkloadsRequest request)

Lists Assured Workloads under a CRM Node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       ListWorkloadsRequest request =
           ListWorkloadsRequest.newBuilder()
               .setParent(LocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Workload element : assuredWorkloadsServiceClient.listWorkloads(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse)` |   
  
### listWorkloads(String parent)
    
    
    public final AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse listWorkloads(String parent)

Lists Assured Workloads under a CRM Node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       String parent = LocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (Workload element : assuredWorkloadsServiceClient.listWorkloads(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse)` |   
  
### listWorkloadsCallable()
    
    
    public final UnaryCallable<ListWorkloadsRequest,ListWorkloadsResponse> listWorkloadsCallable()

Lists Assured Workloads under a CRM Node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       ListWorkloadsRequest request =
           ListWorkloadsRequest.newBuilder()
               .setParent(LocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListWorkloadsResponse response =
             assuredWorkloadsServiceClient.listWorkloadsCallable().call(request);
         for (Workload element : response.getWorkloadsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListWorkloadsRequest),[ListWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListWorkloadsResponse)>` |   
  
### listWorkloadsPagedCallable()
    
    
    public final UnaryCallable<ListWorkloadsRequest,AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse> listWorkloadsPagedCallable()

Lists Assured Workloads under a CRM Node.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       ListWorkloadsRequest request =
           ListWorkloadsRequest.newBuilder()
               .setParent(LocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Workload> future =
           assuredWorkloadsServiceClient.listWorkloadsPagedCallable().futureCall(request);
       // Do something.
       for (Workload element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ListWorkloadsRequest),[ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.AssuredWorkloadsServiceClient.ListWorkloadsPagedResponse)>` |   
  
### restrictAllowedResources(RestrictAllowedResourcesRequest request)
    
    
    public final RestrictAllowedResourcesResponse restrictAllowedResources(RestrictAllowedResourcesRequest request)

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       RestrictAllowedResourcesRequest request =
           RestrictAllowedResourcesRequest.newBuilder().setName("name3373707").build();
       RestrictAllowedResourcesResponse response =
           assuredWorkloadsServiceClient.restrictAllowedResources(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.RestrictAllowedResourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.RestrictAllowedResourcesResponse)` |   
  
### restrictAllowedResourcesCallable()
    
    
    public final UnaryCallable<RestrictAllowedResourcesRequest,RestrictAllowedResourcesResponse> restrictAllowedResourcesCallable()

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       RestrictAllowedResourcesRequest request =
           RestrictAllowedResourcesRequest.newBuilder().setName("name3373707").build();
       ApiFuture<RestrictAllowedResourcesResponse> future =
           assuredWorkloadsServiceClient.restrictAllowedResourcesCallable().futureCall(request);
       // Do something.
       RestrictAllowedResourcesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.RestrictAllowedResourcesRequest),[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.RestrictAllowedResourcesResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateWorkload(UpdateWorkloadRequest request)
    
    
    public final Workload updateWorkload(UpdateWorkloadRequest request)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       UpdateWorkloadRequest request =
           UpdateWorkloadRequest.newBuilder()
               .setWorkload(Workload.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Workload response = assuredWorkloadsServiceClient.updateWorkload(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.UpdateWorkloadRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)` |   
  
### updateWorkload(Workload workload, FieldMask updateMask)
    
    
    public final Workload updateWorkload(Workload workload, FieldMask updateMask)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       Workload workload = Workload.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Workload response = assuredWorkloadsServiceClient.updateWorkload(workload, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`workload` | `[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)`  
Required. The workload to update. The workload's `name` field is used to identify the workload to be updated. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)` |   
  
### updateWorkloadCallable()
    
    
    public final UnaryCallable<UpdateWorkloadRequest,Workload> updateWorkloadCallable()

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AssuredWorkloadsServiceClient assuredWorkloadsServiceClient =
         AssuredWorkloadsServiceClient.create()) {
       UpdateWorkloadRequest request =
           UpdateWorkloadRequest.newBuilder()
               .setWorkload(Workload.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Workload> future =
           assuredWorkloadsServiceClient.updateWorkloadCallable().futureCall(request);
       // Do something.
       Workload response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.UpdateWorkloadRequest),[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Workload)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
