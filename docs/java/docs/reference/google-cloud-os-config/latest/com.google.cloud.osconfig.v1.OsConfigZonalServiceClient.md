---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient
title: Class OsConfigZonalServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:58.732184+00:00
---

# Class OsConfigZonalServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OsConfigZonalServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-os-config/google-cloud-os-config/src/main/java/com/google/cloud/osconfig/v1/OsConfigZonalServiceClient.java)| [Product Reference](https://cloud.google.com/compute/docs/os-patch-management)  
---|---  
  
Service Description: Zonal OS Config API

The OS Config service is the server-side component that allows users to manage package installations and patch jobs for Compute Engine VM instances.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       OSPolicyAssignmentName name =
           OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
       OSPolicyAssignment response = osConfigZonalServiceClient.getOSPolicyAssignment(name);
     }
     

Note: close() needs to be called on the OsConfigZonalServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateOSPolicyAssignment |  Create an OS policy assignment.  This method also creates the first revision of the OS policy assignment.  This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.  For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createOSPolicyAssignmentAsync(CreateOSPolicyAssignmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createOSPolicyAssignmentAsync(LocationName parent, OSPolicyAssignment osPolicyAssignment, String osPolicyAssignmentId) 
  * createOSPolicyAssignmentAsync(String parent, OSPolicyAssignment osPolicyAssignment, String osPolicyAssignmentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createOSPolicyAssignmentOperationCallable() 
  * createOSPolicyAssignmentCallable() 

  
UpdateOSPolicyAssignment |  Update an existing OS policy assignment.  This method creates a new revision of the OS policy assignment.  This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.  For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateOSPolicyAssignmentAsync(UpdateOSPolicyAssignmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateOSPolicyAssignmentAsync(OSPolicyAssignment osPolicyAssignment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOSPolicyAssignmentOperationCallable() 
  * updateOSPolicyAssignmentCallable() 

  
GetOSPolicyAssignment |  Retrieve an existing OS policy assignment.  This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOSPolicyAssignment(GetOSPolicyAssignmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOSPolicyAssignment(OSPolicyAssignmentName name) 
  * getOSPolicyAssignment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOSPolicyAssignmentCallable() 

  
ListOSPolicyAssignments |  List the OS policy assignments under the parent resource.  For each OS policy assignment, the latest revision is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOSPolicyAssignments(ListOSPolicyAssignmentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOSPolicyAssignments(LocationName parent) 
  * listOSPolicyAssignments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOSPolicyAssignmentsPagedCallable() 
  * listOSPolicyAssignmentsCallable() 

  
ListOSPolicyAssignmentRevisions |  List the OS policy assignment revisions for a given OS policy assignment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOSPolicyAssignmentRevisions(ListOSPolicyAssignmentRevisionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOSPolicyAssignmentRevisions(OSPolicyAssignmentName name) 
  * listOSPolicyAssignmentRevisions(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOSPolicyAssignmentRevisionsPagedCallable() 
  * listOSPolicyAssignmentRevisionsCallable() 

  
DeleteOSPolicyAssignment |  Delete the OS policy assignment.  This method creates a new revision of the OS policy assignment.  This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.  If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.  For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteOSPolicyAssignmentAsync(DeleteOSPolicyAssignmentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteOSPolicyAssignmentAsync(OSPolicyAssignmentName name) 
  * deleteOSPolicyAssignmentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOSPolicyAssignmentOperationCallable() 
  * deleteOSPolicyAssignmentCallable() 

  
GetOSPolicyAssignmentReport |  Get the OS policy asssignment report for the specified Compute Engine VM instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOSPolicyAssignmentReport(GetOSPolicyAssignmentReportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOSPolicyAssignmentReport(OSPolicyAssignmentReportName name) 
  * getOSPolicyAssignmentReport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOSPolicyAssignmentReportCallable() 

  
ListOSPolicyAssignmentReports |  List OS policy asssignment reports for all Compute Engine VM instances in the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOSPolicyAssignmentReports(ListOSPolicyAssignmentReportsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOSPolicyAssignmentReports(InstanceOSPolicyAssignmentName parent) 
  * listOSPolicyAssignmentReports(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOSPolicyAssignmentReportsPagedCallable() 
  * listOSPolicyAssignmentReportsCallable() 

  
GetInventory |  Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInventory(GetInventoryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInventory(InventoryName name) 
  * getInventory(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInventoryCallable() 

  
ListInventories |  List inventory data for all VM instances in the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInventories(ListInventoriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInventories(InstanceName parent) 
  * listInventories(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInventoriesPagedCallable() 
  * listInventoriesCallable() 

  
GetVulnerabilityReport |  Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVulnerabilityReport(GetVulnerabilityReportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getVulnerabilityReport(VulnerabilityReportName name) 
  * getVulnerabilityReport(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVulnerabilityReportCallable() 

  
ListVulnerabilityReports |  List vulnerability reports for all VM instances in the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listVulnerabilityReports(ListVulnerabilityReportsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listVulnerabilityReports(InstanceName parent) 
  * listVulnerabilityReports(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listVulnerabilityReportsPagedCallable() 
  * listVulnerabilityReportsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of OsConfigZonalServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OsConfigZonalServiceSettings osConfigZonalServiceSettings =
         OsConfigZonalServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create(osConfigZonalServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OsConfigZonalServiceSettings osConfigZonalServiceSettings =
         OsConfigZonalServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create(osConfigZonalServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OsConfigZonalServiceSettings osConfigZonalServiceSettings =
         OsConfigZonalServiceSettings.newHttpJsonBuilder().build();
     OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create(osConfigZonalServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OsConfigZonalServiceClient

## Static Methods 

### create()
    
    
    public static final OsConfigZonalServiceClient create()

Constructs an instance of OsConfigZonalServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OsConfigZonalServiceSettings settings)
    
    
    public static final OsConfigZonalServiceClient create(OsConfigZonalServiceSettings settings)

Constructs an instance of OsConfigZonalServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OsConfigZonalServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OsConfigZonalServiceStub stub)
    
    
    public static final OsConfigZonalServiceClient create(OsConfigZonalServiceStub stub)

Constructs an instance of OsConfigZonalServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(OsConfigZonalServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OsConfigZonalServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.stub.OsConfigZonalServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient)` |   
  
## Constructors 

### OsConfigZonalServiceClient(OsConfigZonalServiceSettings settings)
    
    
    protected OsConfigZonalServiceClient(OsConfigZonalServiceSettings settings)

Constructs an instance of OsConfigZonalServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OsConfigZonalServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceSettings)`  
  
  
### OsConfigZonalServiceClient(OsConfigZonalServiceStub stub)
    
    
    protected OsConfigZonalServiceClient(OsConfigZonalServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OsConfigZonalServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.stub.OsConfigZonalServiceStub)`  
  
  
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

### createOSPolicyAssignmentAsync(@Nullable LocationName parent, OSPolicyAssignment osPolicyAssignment, String osPolicyAssignmentId)
    
    
    public final OperationFuture<OSPolicyAssignment,OSPolicyAssignmentOperationMetadata> createOSPolicyAssignmentAsync(@Nullable LocationName parent, OSPolicyAssignment osPolicyAssignment, String osPolicyAssignmentId)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       OSPolicyAssignment osPolicyAssignment = OSPolicyAssignment.newBuilder().build();
       String osPolicyAssignmentId = "osPolicyAssignmentId-44079074";
       OSPolicyAssignment response =
           osConfigZonalServiceClient
               .createOSPolicyAssignmentAsync(parent, osPolicyAssignment, osPolicyAssignmentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.LocationName`  
Required. The parent resource name in the form: projects/{project}/locations/{location}  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment)`  
Required. The OS policy assignment to be created.  
`osPolicyAssignmentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The logical name of the OS policy assignment in the project with the following restrictions: 

  * Must contain only lowercase letters, numbers, and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the project. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### createOSPolicyAssignmentAsync(CreateOSPolicyAssignmentRequest request)
    
    
    public final OperationFuture<OSPolicyAssignment,OSPolicyAssignmentOperationMetadata> createOSPolicyAssignmentAsync(CreateOSPolicyAssignmentRequest request)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       CreateOSPolicyAssignmentRequest request =
           CreateOSPolicyAssignmentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOsPolicyAssignment(OSPolicyAssignment.newBuilder().build())
               .setOsPolicyAssignmentId("osPolicyAssignmentId-44079074")
               .build();
       OSPolicyAssignment response =
           osConfigZonalServiceClient.createOSPolicyAssignmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.CreateOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### createOSPolicyAssignmentAsync(String parent, OSPolicyAssignment osPolicyAssignment, String osPolicyAssignmentId)
    
    
    public final OperationFuture<OSPolicyAssignment,OSPolicyAssignmentOperationMetadata> createOSPolicyAssignmentAsync(String parent, OSPolicyAssignment osPolicyAssignment, String osPolicyAssignmentId)

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       OSPolicyAssignment osPolicyAssignment = OSPolicyAssignment.newBuilder().build();
       String osPolicyAssignmentId = "osPolicyAssignmentId-44079074";
       OSPolicyAssignment response =
           osConfigZonalServiceClient
               .createOSPolicyAssignmentAsync(parent, osPolicyAssignment, osPolicyAssignmentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name in the form: projects/{project}/locations/{location}  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment)`  
Required. The OS policy assignment to be created.  
`osPolicyAssignmentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The logical name of the OS policy assignment in the project with the following restrictions: 

  * Must contain only lowercase letters, numbers, and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the project. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### createOSPolicyAssignmentCallable()
    
    
    public final UnaryCallable<CreateOSPolicyAssignmentRequest,Operation> createOSPolicyAssignmentCallable()

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       CreateOSPolicyAssignmentRequest request =
           CreateOSPolicyAssignmentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOsPolicyAssignment(OSPolicyAssignment.newBuilder().build())
               .setOsPolicyAssignmentId("osPolicyAssignmentId-44079074")
               .build();
       ApiFuture<Operation> future =
           osConfigZonalServiceClient.createOSPolicyAssignmentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.CreateOSPolicyAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createOSPolicyAssignmentOperationCallable()
    
    
    public final OperationCallable<CreateOSPolicyAssignmentRequest,OSPolicyAssignment,OSPolicyAssignmentOperationMetadata> createOSPolicyAssignmentOperationCallable()

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       CreateOSPolicyAssignmentRequest request =
           CreateOSPolicyAssignmentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOsPolicyAssignment(OSPolicyAssignment.newBuilder().build())
               .setOsPolicyAssignmentId("osPolicyAssignmentId-44079074")
               .build();
       OperationFuture<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> future =
           osConfigZonalServiceClient
               .createOSPolicyAssignmentOperationCallable()
               .futureCall(request);
       // Do something.
       OSPolicyAssignment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.CreateOSPolicyAssignmentRequest),[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### deleteOSPolicyAssignmentAsync(@Nullable OSPolicyAssignmentName name)
    
    
    public final OperationFuture<Empty,OSPolicyAssignmentOperationMetadata> deleteOSPolicyAssignmentAsync(@Nullable OSPolicyAssignmentName name)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       OSPolicyAssignmentName name =
           OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
       osConfigZonalServiceClient.deleteOSPolicyAssignmentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.OSPolicyAssignmentName`  
Required. The name of the OS policy assignment to be deleted  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### deleteOSPolicyAssignmentAsync(DeleteOSPolicyAssignmentRequest request)
    
    
    public final OperationFuture<Empty,OSPolicyAssignmentOperationMetadata> deleteOSPolicyAssignmentAsync(DeleteOSPolicyAssignmentRequest request)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       DeleteOSPolicyAssignmentRequest request =
           DeleteOSPolicyAssignmentRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]")
                       .toString())
               .build();
       osConfigZonalServiceClient.deleteOSPolicyAssignmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.DeleteOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### deleteOSPolicyAssignmentAsync(String name)
    
    
    public final OperationFuture<Empty,OSPolicyAssignmentOperationMetadata> deleteOSPolicyAssignmentAsync(String name)

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String name =
           OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]").toString();
       osConfigZonalServiceClient.deleteOSPolicyAssignmentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the OS policy assignment to be deleted  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### deleteOSPolicyAssignmentCallable()
    
    
    public final UnaryCallable<DeleteOSPolicyAssignmentRequest,Operation> deleteOSPolicyAssignmentCallable()

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       DeleteOSPolicyAssignmentRequest request =
           DeleteOSPolicyAssignmentRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           osConfigZonalServiceClient.deleteOSPolicyAssignmentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.DeleteOSPolicyAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteOSPolicyAssignmentOperationCallable()
    
    
    public final OperationCallable<DeleteOSPolicyAssignmentRequest,Empty,OSPolicyAssignmentOperationMetadata> deleteOSPolicyAssignmentOperationCallable()

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       DeleteOSPolicyAssignmentRequest request =
           DeleteOSPolicyAssignmentRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]")
                       .toString())
               .build();
       OperationFuture<Empty, OSPolicyAssignmentOperationMetadata> future =
           osConfigZonalServiceClient
               .deleteOSPolicyAssignmentOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.DeleteOSPolicyAssignmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getInventory(@Nullable InventoryName name)
    
    
    public final Inventory getInventory(@Nullable InventoryName name)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       InventoryName name = InventoryName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       Inventory response = osConfigZonalServiceClient.getInventory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.InventoryName`  
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory)` |   
  
### getInventory(GetInventoryRequest request)
    
    
    public final Inventory getInventory(GetInventoryRequest request)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       GetInventoryRequest request =
           GetInventoryRequest.newBuilder()
               .setName(InventoryName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setView(InventoryView.forNumber(0))
               .build();
       Inventory response = osConfigZonalServiceClient.getInventory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.GetInventoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory)` |   
  
### getInventory(String name)
    
    
    public final Inventory getInventory(String name)

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String name = InventoryName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       Inventory response = osConfigZonalServiceClient.getInventory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. API resource name for inventory resource. Format: `projects/{project}/locations/{location}/instances/{instance}/inventory` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory)` |   
  
### getInventoryCallable()
    
    
    public final UnaryCallable<GetInventoryRequest,Inventory> getInventoryCallable()

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       GetInventoryRequest request =
           GetInventoryRequest.newBuilder()
               .setName(InventoryName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setView(InventoryView.forNumber(0))
               .build();
       ApiFuture<Inventory> future =
           osConfigZonalServiceClient.getInventoryCallable().futureCall(request);
       // Do something.
       Inventory response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.GetInventoryRequest),[Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory)>` |   
  
### getOSPolicyAssignment(@Nullable OSPolicyAssignmentName name)
    
    
    public final OSPolicyAssignment getOSPolicyAssignment(@Nullable OSPolicyAssignmentName name)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       OSPolicyAssignmentName name =
           OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
       OSPolicyAssignment response = osConfigZonalServiceClient.getOSPolicyAssignment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.OSPolicyAssignmentName`  
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment)` |   
  
### getOSPolicyAssignment(GetOSPolicyAssignmentRequest request)
    
    
    public final OSPolicyAssignment getOSPolicyAssignment(GetOSPolicyAssignmentRequest request)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       GetOSPolicyAssignmentRequest request =
           GetOSPolicyAssignmentRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]")
                       .toString())
               .build();
       OSPolicyAssignment response = osConfigZonalServiceClient.getOSPolicyAssignment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.GetOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment)` |   
  
### getOSPolicyAssignment(String name)
    
    
    public final OSPolicyAssignment getOSPolicyAssignment(String name)

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String name =
           OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]").toString();
       OSPolicyAssignment response = osConfigZonalServiceClient.getOSPolicyAssignment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of OS policy assignment. Format: `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment)` |   
  
### getOSPolicyAssignmentCallable()
    
    
    public final UnaryCallable<GetOSPolicyAssignmentRequest,OSPolicyAssignment> getOSPolicyAssignmentCallable()

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       GetOSPolicyAssignmentRequest request =
           GetOSPolicyAssignmentRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]")
                       .toString())
               .build();
       ApiFuture<OSPolicyAssignment> future =
           osConfigZonalServiceClient.getOSPolicyAssignmentCallable().futureCall(request);
       // Do something.
       OSPolicyAssignment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.GetOSPolicyAssignmentRequest),[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment)>` |   
  
### getOSPolicyAssignmentReport(@Nullable OSPolicyAssignmentReportName name)
    
    
    public final OSPolicyAssignmentReport getOSPolicyAssignmentReport(@Nullable OSPolicyAssignmentReportName name)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       OSPolicyAssignmentReportName name =
           OSPolicyAssignmentReportName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]");
       OSPolicyAssignmentReport response =
           osConfigZonalServiceClient.getOSPolicyAssignmentReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.OSPolicyAssignmentReportName`  
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignmentReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentReport)` |   
  
### getOSPolicyAssignmentReport(GetOSPolicyAssignmentReportRequest request)
    
    
    public final OSPolicyAssignmentReport getOSPolicyAssignmentReport(GetOSPolicyAssignmentReportRequest request)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       GetOSPolicyAssignmentReportRequest request =
           GetOSPolicyAssignmentReportRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentReportName.of(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]")
                       .toString())
               .build();
       OSPolicyAssignmentReport response =
           osConfigZonalServiceClient.getOSPolicyAssignmentReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.GetOSPolicyAssignmentReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignmentReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentReport)` |   
  
### getOSPolicyAssignmentReport(String name)
    
    
    public final OSPolicyAssignmentReport getOSPolicyAssignmentReport(String name)

Get the OS policy asssignment report for the specified Compute Engine VM instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String name =
           OSPolicyAssignmentReportName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]")
               .toString();
       OSPolicyAssignmentReport response =
           osConfigZonalServiceClient.getOSPolicyAssignmentReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. API resource name for OS policy assignment report. Format: `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance_id}`, either Compute Engine `instance-id` or `instance-name` can be provided. For `{assignment_id}`, the OSPolicyAssignment id must be provided.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignmentReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentReport)` |   
  
### getOSPolicyAssignmentReportCallable()
    
    
    public final UnaryCallable<GetOSPolicyAssignmentReportRequest,OSPolicyAssignmentReport> getOSPolicyAssignmentReportCallable()

Get the OS policy asssignment report for the specified Compute Engine VM instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       GetOSPolicyAssignmentReportRequest request =
           GetOSPolicyAssignmentReportRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentReportName.of(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]")
                       .toString())
               .build();
       ApiFuture<OSPolicyAssignmentReport> future =
           osConfigZonalServiceClient.getOSPolicyAssignmentReportCallable().futureCall(request);
       // Do something.
       OSPolicyAssignmentReport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.GetOSPolicyAssignmentReportRequest),[OSPolicyAssignmentReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentReport)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable OsConfigZonalServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.OsConfigZonalServiceSettings` |   
  
### getStub()
    
    
    public OsConfigZonalServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.stub.OsConfigZonalServiceStub)` |   
  
### getVulnerabilityReport(@Nullable VulnerabilityReportName name)
    
    
    public final VulnerabilityReport getVulnerabilityReport(@Nullable VulnerabilityReportName name)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       VulnerabilityReportName name =
           VulnerabilityReportName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       VulnerabilityReport response = osConfigZonalServiceClient.getVulnerabilityReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.VulnerabilityReportName`  
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
**Returns**  
---  
**Type** | **Description**  
`[VulnerabilityReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.VulnerabilityReport)` |   
  
### getVulnerabilityReport(GetVulnerabilityReportRequest request)
    
    
    public final VulnerabilityReport getVulnerabilityReport(GetVulnerabilityReportRequest request)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       GetVulnerabilityReportRequest request =
           GetVulnerabilityReportRequest.newBuilder()
               .setName(
                   VulnerabilityReportName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       VulnerabilityReport response = osConfigZonalServiceClient.getVulnerabilityReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVulnerabilityReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.GetVulnerabilityReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VulnerabilityReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.VulnerabilityReport)` |   
  
### getVulnerabilityReport(String name)
    
    
    public final VulnerabilityReport getVulnerabilityReport(String name)

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String name = VulnerabilityReportName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       VulnerabilityReport response = osConfigZonalServiceClient.getVulnerabilityReport(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. API resource name for vulnerability resource. Format: `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either Compute Engine `instance-id` or `instance-name` can be provided.  
**Returns**  
---  
**Type** | **Description**  
`[VulnerabilityReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.VulnerabilityReport)` |   
  
### getVulnerabilityReportCallable()
    
    
    public final UnaryCallable<GetVulnerabilityReportRequest,VulnerabilityReport> getVulnerabilityReportCallable()

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       GetVulnerabilityReportRequest request =
           GetVulnerabilityReportRequest.newBuilder()
               .setName(
                   VulnerabilityReportName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<VulnerabilityReport> future =
           osConfigZonalServiceClient.getVulnerabilityReportCallable().futureCall(request);
       // Do something.
       VulnerabilityReport response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVulnerabilityReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.GetVulnerabilityReportRequest),[VulnerabilityReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.VulnerabilityReport)>` |   
  
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
  
### listInventories(@Nullable InstanceName parent)
    
    
    public final OsConfigZonalServiceClient.ListInventoriesPagedResponse listInventories(@Nullable InstanceName parent)

List inventory data for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       InstanceName parent =
           InstanceName.ofProjectLocationInstanceName("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       for (Inventory element : osConfigZonalServiceClient.listInventories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.InstanceName`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListInventoriesPagedResponse)` |   
  
### listInventories(ListInventoriesRequest request)
    
    
    public final OsConfigZonalServiceClient.ListInventoriesPagedResponse listInventories(ListInventoriesRequest request)

List inventory data for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListInventoriesRequest request =
           ListInventoriesRequest.newBuilder()
               .setParent(
                   InstanceName.ofProjectLocationInstanceName(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]")
                       .toString())
               .setView(InventoryView.forNumber(0))
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Inventory element : osConfigZonalServiceClient.listInventories(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListInventoriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListInventoriesPagedResponse)` |   
  
### listInventories(String parent)
    
    
    public final OsConfigZonalServiceClient.ListInventoriesPagedResponse listInventories(String parent)

List inventory data for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String parent =
           InstanceName.ofProjectZoneInstanceName("[PROJECT]", "[ZONE]", "[INSTANCE]").toString();
       for (Inventory element : osConfigZonalServiceClient.listInventories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListInventoriesPagedResponse)` |   
  
### listInventoriesCallable()
    
    
    public final UnaryCallable<ListInventoriesRequest,ListInventoriesResponse> listInventoriesCallable()

List inventory data for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListInventoriesRequest request =
           ListInventoriesRequest.newBuilder()
               .setParent(
                   InstanceName.ofProjectLocationInstanceName(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]")
                       .toString())
               .setView(InventoryView.forNumber(0))
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListInventoriesResponse response =
             osConfigZonalServiceClient.listInventoriesCallable().call(request);
         for (Inventory element : response.getInventoriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListInventoriesRequest),[ListInventoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListInventoriesResponse)>` |   
  
### listInventoriesPagedCallable()
    
    
    public final UnaryCallable<ListInventoriesRequest,OsConfigZonalServiceClient.ListInventoriesPagedResponse> listInventoriesPagedCallable()

List inventory data for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListInventoriesRequest request =
           ListInventoriesRequest.newBuilder()
               .setParent(
                   InstanceName.ofProjectLocationInstanceName(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]")
                       .toString())
               .setView(InventoryView.forNumber(0))
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Inventory> future =
           osConfigZonalServiceClient.listInventoriesPagedCallable().futureCall(request);
       // Do something.
       for (Inventory element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInventoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListInventoriesRequest),[ListInventoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListInventoriesPagedResponse)>` |   
  
### listOSPolicyAssignmentReports(@Nullable InstanceOSPolicyAssignmentName parent)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse listOSPolicyAssignmentReports(@Nullable InstanceOSPolicyAssignmentName parent)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       InstanceOSPolicyAssignmentName parent =
           InstanceOSPolicyAssignmentName.of(
               "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]");
       for (OSPolicyAssignmentReport element :
           osConfigZonalServiceClient.listOSPolicyAssignmentReports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.InstanceOSPolicyAssignmentName`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either `instance-name`, `instance-id`, or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all instances in the project/location. For `{assignment}`, either `assignment-id` or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all OSPolicyAssignments in the project/location. Either {instance} or {assignment} must be `-`. For example: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports` returns all reports for the instance `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports` returns all the reports for the given assignment across all instances. `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports` returns all the reports for all assignments across all instances.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse)` |   
  
### listOSPolicyAssignmentReports(ListOSPolicyAssignmentReportsRequest request)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse listOSPolicyAssignmentReports(ListOSPolicyAssignmentReportsRequest request)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentReportsRequest request =
           ListOSPolicyAssignmentReportsRequest.newBuilder()
               .setParent(
                   InstanceOSPolicyAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]")
                       .toString())
               .setPageSize(883849137)
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .build();
       for (OSPolicyAssignmentReport element :
           osConfigZonalServiceClient.listOSPolicyAssignmentReports(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentReportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse)` |   
  
### listOSPolicyAssignmentReports(String parent)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse listOSPolicyAssignmentReports(String parent)

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String parent =
           InstanceOSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]")
               .toString();
       for (OSPolicyAssignmentReport element :
           osConfigZonalServiceClient.listOSPolicyAssignmentReports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports` For `{project}`, either `project-number` or `project-id` can be provided. For `{instance}`, either `instance-name`, `instance-id`, or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all instances in the project/location. For `{assignment}`, either `assignment-id` or `-` can be provided. If '-' is provided, the response will include OSPolicyAssignmentReports for all OSPolicyAssignments in the project/location. Either {instance} or {assignment} must be `-`. For example: `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports` returns all reports for the instance `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports` returns all the reports for the given assignment across all instances. `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports` returns all the reports for all assignments across all instances.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse)` |   
  
### listOSPolicyAssignmentReportsCallable()
    
    
    public final UnaryCallable<ListOSPolicyAssignmentReportsRequest,ListOSPolicyAssignmentReportsResponse> listOSPolicyAssignmentReportsCallable()

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentReportsRequest request =
           ListOSPolicyAssignmentReportsRequest.newBuilder()
               .setParent(
                   InstanceOSPolicyAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]")
                       .toString())
               .setPageSize(883849137)
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListOSPolicyAssignmentReportsResponse response =
             osConfigZonalServiceClient.listOSPolicyAssignmentReportsCallable().call(request);
         for (OSPolicyAssignmentReport element : response.getOsPolicyAssignmentReportsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentReportsRequest),[ListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentReportsResponse)>` |   
  
### listOSPolicyAssignmentReportsPagedCallable()
    
    
    public final UnaryCallable<ListOSPolicyAssignmentReportsRequest,OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse> listOSPolicyAssignmentReportsPagedCallable()

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentReportsRequest request =
           ListOSPolicyAssignmentReportsRequest.newBuilder()
               .setParent(
                   InstanceOSPolicyAssignmentName.of(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[ASSIGNMENT]")
                       .toString())
               .setPageSize(883849137)
               .setFilter("filter-1274492040")
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<OSPolicyAssignmentReport> future =
           osConfigZonalServiceClient
               .listOSPolicyAssignmentReportsPagedCallable()
               .futureCall(request);
       // Do something.
       for (OSPolicyAssignmentReport element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentReportsRequest),[ListOSPolicyAssignmentReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentReportsPagedResponse)>` |   
  
### listOSPolicyAssignmentRevisions(@Nullable OSPolicyAssignmentName name)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse listOSPolicyAssignmentRevisions(@Nullable OSPolicyAssignmentName name)

List the OS policy assignment revisions for a given OS policy assignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       OSPolicyAssignmentName name =
           OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]");
       for (OSPolicyAssignment element :
           osConfigZonalServiceClient.listOSPolicyAssignmentRevisions(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.OSPolicyAssignmentName`  
Required. The name of the OS policy assignment to list revisions for.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse)` |   
  
### listOSPolicyAssignmentRevisions(ListOSPolicyAssignmentRevisionsRequest request)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse listOSPolicyAssignmentRevisions(ListOSPolicyAssignmentRevisionsRequest request)

List the OS policy assignment revisions for a given OS policy assignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentRevisionsRequest request =
           ListOSPolicyAssignmentRevisionsRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (OSPolicyAssignment element :
           osConfigZonalServiceClient.listOSPolicyAssignmentRevisions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse)` |   
  
### listOSPolicyAssignmentRevisions(String name)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse listOSPolicyAssignmentRevisions(String name)

List the OS policy assignment revisions for a given OS policy assignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String name =
           OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]").toString();
       for (OSPolicyAssignment element :
           osConfigZonalServiceClient.listOSPolicyAssignmentRevisions(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the OS policy assignment to list revisions for.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse)` |   
  
### listOSPolicyAssignmentRevisionsCallable()
    
    
    public final UnaryCallable<ListOSPolicyAssignmentRevisionsRequest,ListOSPolicyAssignmentRevisionsResponse> listOSPolicyAssignmentRevisionsCallable()

List the OS policy assignment revisions for a given OS policy assignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentRevisionsRequest request =
           ListOSPolicyAssignmentRevisionsRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListOSPolicyAssignmentRevisionsResponse response =
             osConfigZonalServiceClient.listOSPolicyAssignmentRevisionsCallable().call(request);
         for (OSPolicyAssignment element : response.getOsPolicyAssignmentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentRevisionsRequest),[ListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentRevisionsResponse)>` |   
  
### listOSPolicyAssignmentRevisionsPagedCallable()
    
    
    public final UnaryCallable<ListOSPolicyAssignmentRevisionsRequest,OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse> listOSPolicyAssignmentRevisionsPagedCallable()

List the OS policy assignment revisions for a given OS policy assignment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentRevisionsRequest request =
           ListOSPolicyAssignmentRevisionsRequest.newBuilder()
               .setName(
                   OSPolicyAssignmentName.of("[PROJECT]", "[LOCATION]", "[OS_POLICY_ASSIGNMENT]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<OSPolicyAssignment> future =
           osConfigZonalServiceClient
               .listOSPolicyAssignmentRevisionsPagedCallable()
               .futureCall(request);
       // Do something.
       for (OSPolicyAssignment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentRevisionsRequest),[ListOSPolicyAssignmentRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentRevisionsPagedResponse)>` |   
  
### listOSPolicyAssignments(@Nullable LocationName parent)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse listOSPolicyAssignments(@Nullable LocationName parent)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (OSPolicyAssignment element :
           osConfigZonalServiceClient.listOSPolicyAssignments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.LocationName`  
Required. The parent resource name.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse)` |   
  
### listOSPolicyAssignments(ListOSPolicyAssignmentsRequest request)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse listOSPolicyAssignments(ListOSPolicyAssignmentsRequest request)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentsRequest request =
           ListOSPolicyAssignmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (OSPolicyAssignment element :
           osConfigZonalServiceClient.listOSPolicyAssignments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse)` |   
  
### listOSPolicyAssignments(String parent)
    
    
    public final OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse listOSPolicyAssignments(String parent)

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (OSPolicyAssignment element :
           osConfigZonalServiceClient.listOSPolicyAssignments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse)` |   
  
### listOSPolicyAssignmentsCallable()
    
    
    public final UnaryCallable<ListOSPolicyAssignmentsRequest,ListOSPolicyAssignmentsResponse> listOSPolicyAssignmentsCallable()

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentsRequest request =
           ListOSPolicyAssignmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListOSPolicyAssignmentsResponse response =
             osConfigZonalServiceClient.listOSPolicyAssignmentsCallable().call(request);
         for (OSPolicyAssignment element : response.getOsPolicyAssignmentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentsRequest),[ListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentsResponse)>` |   
  
### listOSPolicyAssignmentsPagedCallable()
    
    
    public final UnaryCallable<ListOSPolicyAssignmentsRequest,OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse> listOSPolicyAssignmentsPagedCallable()

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListOSPolicyAssignmentsRequest request =
           ListOSPolicyAssignmentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<OSPolicyAssignment> future =
           osConfigZonalServiceClient.listOSPolicyAssignmentsPagedCallable().futureCall(request);
       // Do something.
       for (OSPolicyAssignment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListOSPolicyAssignmentsRequest),[ListOSPolicyAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListOSPolicyAssignmentsPagedResponse)>` |   
  
### listVulnerabilityReports(@Nullable InstanceName parent)
    
    
    public final OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse listVulnerabilityReports(@Nullable InstanceName parent)

List vulnerability reports for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       InstanceName parent =
           InstanceName.ofProjectLocationInstanceName("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       for (VulnerabilityReport element :
           osConfigZonalServiceClient.listVulnerabilityReports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.osconfig.v1.InstanceName`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse)` |   
  
### listVulnerabilityReports(ListVulnerabilityReportsRequest request)
    
    
    public final OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse listVulnerabilityReports(ListVulnerabilityReportsRequest request)

List vulnerability reports for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListVulnerabilityReportsRequest request =
           ListVulnerabilityReportsRequest.newBuilder()
               .setParent(
                   InstanceName.ofProjectLocationInstanceName(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (VulnerabilityReport element :
           osConfigZonalServiceClient.listVulnerabilityReports(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVulnerabilityReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListVulnerabilityReportsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse)` |   
  
### listVulnerabilityReports(String parent)
    
    
    public final OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse listVulnerabilityReports(String parent)

List vulnerability reports for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       String parent =
           InstanceName.ofProjectZoneInstanceName("[PROJECT]", "[ZONE]", "[INSTANCE]").toString();
       for (VulnerabilityReport element :
           osConfigZonalServiceClient.listVulnerabilityReports(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name. Format: `projects/{project}/locations/{location}/instances/-` For `{project}`, either `project-number` or `project-id` can be provided.  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse)` |   
  
### listVulnerabilityReportsCallable()
    
    
    public final UnaryCallable<ListVulnerabilityReportsRequest,ListVulnerabilityReportsResponse> listVulnerabilityReportsCallable()

List vulnerability reports for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListVulnerabilityReportsRequest request =
           ListVulnerabilityReportsRequest.newBuilder()
               .setParent(
                   InstanceName.ofProjectLocationInstanceName(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListVulnerabilityReportsResponse response =
             osConfigZonalServiceClient.listVulnerabilityReportsCallable().call(request);
         for (VulnerabilityReport element : response.getVulnerabilityReportsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVulnerabilityReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListVulnerabilityReportsRequest),[ListVulnerabilityReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListVulnerabilityReportsResponse)>` |   
  
### listVulnerabilityReportsPagedCallable()
    
    
    public final UnaryCallable<ListVulnerabilityReportsRequest,OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse> listVulnerabilityReportsPagedCallable()

List vulnerability reports for all VM instances in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       ListVulnerabilityReportsRequest request =
           ListVulnerabilityReportsRequest.newBuilder()
               .setParent(
                   InstanceName.ofProjectLocationInstanceName(
                           "[PROJECT]", "[LOCATION]", "[INSTANCE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<VulnerabilityReport> future =
           osConfigZonalServiceClient.listVulnerabilityReportsPagedCallable().futureCall(request);
       // Do something.
       for (VulnerabilityReport element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVulnerabilityReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.ListVulnerabilityReportsRequest),[ListVulnerabilityReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OsConfigZonalServiceClient.ListVulnerabilityReportsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateOSPolicyAssignmentAsync(OSPolicyAssignment osPolicyAssignment, FieldMask updateMask)
    
    
    public final OperationFuture<OSPolicyAssignment,OSPolicyAssignmentOperationMetadata> updateOSPolicyAssignmentAsync(OSPolicyAssignment osPolicyAssignment, FieldMask updateMask)

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       OSPolicyAssignment osPolicyAssignment = OSPolicyAssignment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       OSPolicyAssignment response =
           osConfigZonalServiceClient
               .updateOSPolicyAssignmentAsync(osPolicyAssignment, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`osPolicyAssignment` | `[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment)`  
Required. The updated OS policy assignment.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask that controls which fields of the assignment should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### updateOSPolicyAssignmentAsync(UpdateOSPolicyAssignmentRequest request)
    
    
    public final OperationFuture<OSPolicyAssignment,OSPolicyAssignmentOperationMetadata> updateOSPolicyAssignmentAsync(UpdateOSPolicyAssignmentRequest request)

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       UpdateOSPolicyAssignmentRequest request =
           UpdateOSPolicyAssignmentRequest.newBuilder()
               .setOsPolicyAssignment(OSPolicyAssignment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OSPolicyAssignment response =
           osConfigZonalServiceClient.updateOSPolicyAssignmentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.UpdateOSPolicyAssignmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
### updateOSPolicyAssignmentCallable()
    
    
    public final UnaryCallable<UpdateOSPolicyAssignmentRequest,Operation> updateOSPolicyAssignmentCallable()

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       UpdateOSPolicyAssignmentRequest request =
           UpdateOSPolicyAssignmentRequest.newBuilder()
               .setOsPolicyAssignment(OSPolicyAssignment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           osConfigZonalServiceClient.updateOSPolicyAssignmentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.UpdateOSPolicyAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateOSPolicyAssignmentOperationCallable()
    
    
    public final OperationCallable<UpdateOSPolicyAssignmentRequest,OSPolicyAssignment,OSPolicyAssignmentOperationMetadata> updateOSPolicyAssignmentOperationCallable()

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OsConfigZonalServiceClient osConfigZonalServiceClient =
         OsConfigZonalServiceClient.create()) {
       UpdateOSPolicyAssignmentRequest request =
           UpdateOSPolicyAssignmentRequest.newBuilder()
               .setOsPolicyAssignment(OSPolicyAssignment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<OSPolicyAssignment, OSPolicyAssignmentOperationMetadata> future =
           osConfigZonalServiceClient
               .updateOSPolicyAssignmentOperationCallable()
               .futureCall(request);
       // Do something.
       OSPolicyAssignment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.UpdateOSPolicyAssignmentRequest),[OSPolicyAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment),[OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignmentOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
