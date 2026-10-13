---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient
title: Class AuditClient (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:49.985758+00:00
---

# Class AuditClient (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AuditClient (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudsecuritycompliance/google-cloud-cloudsecuritycompliance/src/main/java/com/google/cloud/cloudsecuritycompliance/v1/AuditClient.java)| [Product Reference](https://cloud.google.com/security-command-center/docs/compliance-manager-overview)  
---|---  
  
Service Description: Service describing handlers for resources

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       String scope = "scope109264468";
       GenerateFrameworkAuditScopeReportRequest.Format reportFormat =
           GenerateFrameworkAuditScopeReportRequest.Format.forNumber(0);
       String complianceFramework = "complianceFramework-1808314333";
       GenerateFrameworkAuditScopeReportResponse response =
           auditClient.generateFrameworkAuditScopeReport(scope, reportFormat, complianceFramework);
     }
     

Note: close() needs to be called on the AuditClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GenerateFrameworkAuditScopeReport |  Generates an audit scope report for a framework. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateFrameworkAuditScopeReport(GenerateFrameworkAuditScopeReportRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * generateFrameworkAuditScopeReport(String scope, GenerateFrameworkAuditScopeReportRequest.Format reportFormat, String complianceFramework) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateFrameworkAuditScopeReportCallable() 

  
CreateFrameworkAudit |  Creates an audit scope report for a framework. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFrameworkAuditAsync(CreateFrameworkAuditRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFrameworkAuditAsync(LocationName parent, FrameworkAudit frameworkAudit, String frameworkAuditId) 
  * createFrameworkAuditAsync(OrganizationLocationName parent, FrameworkAudit frameworkAudit, String frameworkAuditId) 
  * createFrameworkAuditAsync(String parent, FrameworkAudit frameworkAudit, String frameworkAuditId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFrameworkAuditOperationCallable() 
  * createFrameworkAuditCallable() 

  
ListFrameworkAudits |  Lists the framework audits for a given organization, folder, or project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFrameworkAudits(ListFrameworkAuditsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFrameworkAudits(LocationName parent) 
  * listFrameworkAudits(OrganizationLocationName parent) 
  * listFrameworkAudits(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFrameworkAuditsPagedCallable() 
  * listFrameworkAuditsCallable() 

  
GetFrameworkAudit |  Gets the details for a framework audit. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFrameworkAudit(GetFrameworkAuditRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFrameworkAudit(FrameworkAuditName name) 
  * getFrameworkAudit(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFrameworkAuditCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AuditSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AuditSettings auditSettings =
         AuditSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AuditClient auditClient = AuditClient.create(auditSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AuditSettings auditSettings = AuditSettings.newBuilder().setEndpoint(myEndpoint).build();
     AuditClient auditClient = AuditClient.create(auditSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AuditSettings auditSettings = AuditSettings.newHttpJsonBuilder().build();
     AuditClient auditClient = AuditClient.create(auditSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AuditClient

## Static Methods 

### create()
    
    
    public static final AuditClient create()

Constructs an instance of AuditClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AuditClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AuditSettings settings)
    
    
    public static final AuditClient create(AuditSettings settings)

Constructs an instance of AuditClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AuditSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuditClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AuditStub stub)
    
    
    public static final AuditClient create(AuditStub stub)

Constructs an instance of AuditClient, using the given stub for making calls. This is for advanced usage - prefer using create(AuditSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AuditStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.AuditStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuditClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient)` |   
  
## Constructors 

### AuditClient(AuditSettings settings)
    
    
    protected AuditClient(AuditSettings settings)

Constructs an instance of AuditClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AuditSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditSettings)`  
  
  
### AuditClient(AuditStub stub)
    
    
    protected AuditClient(AuditStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AuditStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.AuditStub)`  
  
  
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

### createFrameworkAuditAsync(@Nullable LocationName parent, FrameworkAudit frameworkAudit, String frameworkAuditId)
    
    
    public final OperationFuture<FrameworkAudit,OperationMetadata> createFrameworkAuditAsync(@Nullable LocationName parent, FrameworkAudit frameworkAudit, String frameworkAuditId)

Creates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       FrameworkAudit frameworkAudit = FrameworkAudit.newBuilder().build();
       String frameworkAuditId = "frameworkAuditId-548788616";
       FrameworkAudit response =
           auditClient.createFrameworkAuditAsync(parent, frameworkAudit, frameworkAuditId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource where this framework audit is created. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `projects/{project_id}/locations/{location}`

  
`frameworkAudit` | `[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit)`  
Required. The framework audit to create.  
`frameworkAuditId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the framework audit. The ID becomes the final component of the framework audit's full resource name. The ID must be between 4-63 characters, and valid characters are `<xref uid="" data-throw-if-not-resolved="false">a-z-</code>.`` `  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### createFrameworkAuditAsync(@Nullable OrganizationLocationName parent, FrameworkAudit frameworkAudit, String frameworkAuditId)
    
    
    public final OperationFuture<FrameworkAudit,OperationMetadata> createFrameworkAuditAsync(@Nullable OrganizationLocationName parent, FrameworkAudit frameworkAudit, String frameworkAuditId)

Creates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       FrameworkAudit frameworkAudit = FrameworkAudit.newBuilder().build();
       String frameworkAuditId = "frameworkAuditId-548788616";
       FrameworkAudit response =
           auditClient.createFrameworkAuditAsync(parent, frameworkAudit, frameworkAuditId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource where this framework audit is created. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `projects/{project_id}/locations/{location}`

  
`frameworkAudit` | `[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit)`  
Required. The framework audit to create.  
`frameworkAuditId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the framework audit. The ID becomes the final component of the framework audit's full resource name. The ID must be between 4-63 characters, and valid characters are `<xref uid="" data-throw-if-not-resolved="false">a-z-</code>.`` `  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### createFrameworkAuditAsync(CreateFrameworkAuditRequest request)
    
    
    public final OperationFuture<FrameworkAudit,OperationMetadata> createFrameworkAuditAsync(CreateFrameworkAuditRequest request)

Creates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       CreateFrameworkAuditRequest request =
           CreateFrameworkAuditRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFrameworkAuditId("frameworkAuditId-548788616")
               .setFrameworkAudit(FrameworkAudit.newBuilder().build())
               .build();
       FrameworkAudit response = auditClient.createFrameworkAuditAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFrameworkAuditRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkAuditRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### createFrameworkAuditAsync(String parent, FrameworkAudit frameworkAudit, String frameworkAuditId)
    
    
    public final OperationFuture<FrameworkAudit,OperationMetadata> createFrameworkAuditAsync(String parent, FrameworkAudit frameworkAudit, String frameworkAuditId)

Creates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       FrameworkAudit frameworkAudit = FrameworkAudit.newBuilder().build();
       String frameworkAuditId = "frameworkAuditId-548788616";
       FrameworkAudit response =
           auditClient.createFrameworkAuditAsync(parent, frameworkAudit, frameworkAuditId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this framework audit is created. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `projects/{project_id}/locations/{location}`

  
`frameworkAudit` | `[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit)`  
Required. The framework audit to create.  
`frameworkAuditId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the framework audit. The ID becomes the final component of the framework audit's full resource name. The ID must be between 4-63 characters, and valid characters are `<xref uid="" data-throw-if-not-resolved="false">a-z-</code>.`` `  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### createFrameworkAuditCallable()
    
    
    public final UnaryCallable<CreateFrameworkAuditRequest,Operation> createFrameworkAuditCallable()

Creates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       CreateFrameworkAuditRequest request =
           CreateFrameworkAuditRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFrameworkAuditId("frameworkAuditId-548788616")
               .setFrameworkAudit(FrameworkAudit.newBuilder().build())
               .build();
       ApiFuture<Operation> future = auditClient.createFrameworkAuditCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFrameworkAuditRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkAuditRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFrameworkAuditOperationCallable()
    
    
    public final OperationCallable<CreateFrameworkAuditRequest,FrameworkAudit,OperationMetadata> createFrameworkAuditOperationCallable()

Creates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       CreateFrameworkAuditRequest request =
           CreateFrameworkAuditRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFrameworkAuditId("frameworkAuditId-548788616")
               .setFrameworkAudit(FrameworkAudit.newBuilder().build())
               .build();
       OperationFuture<FrameworkAudit, OperationMetadata> future =
           auditClient.createFrameworkAuditOperationCallable().futureCall(request);
       // Do something.
       FrameworkAudit response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFrameworkAuditRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkAuditRequest),[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### generateFrameworkAuditScopeReport(GenerateFrameworkAuditScopeReportRequest request)
    
    
    public final GenerateFrameworkAuditScopeReportResponse generateFrameworkAuditScopeReport(GenerateFrameworkAuditScopeReportRequest request)

Generates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       GenerateFrameworkAuditScopeReportRequest request =
           GenerateFrameworkAuditScopeReportRequest.newBuilder()
               .setScope("scope109264468")
               .setComplianceFramework("complianceFramework-1808314333")
               .build();
       GenerateFrameworkAuditScopeReportResponse response =
           auditClient.generateFrameworkAuditScopeReport(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateFrameworkAuditScopeReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GenerateFrameworkAuditScopeReportRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateFrameworkAuditScopeReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GenerateFrameworkAuditScopeReportResponse)` |   
  
### generateFrameworkAuditScopeReport(String scope, GenerateFrameworkAuditScopeReportRequest.Format reportFormat, String complianceFramework)
    
    
    public final GenerateFrameworkAuditScopeReportResponse generateFrameworkAuditScopeReport(String scope, GenerateFrameworkAuditScopeReportRequest.Format reportFormat, String complianceFramework)

Generates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       String scope = "scope109264468";
       GenerateFrameworkAuditScopeReportRequest.Format reportFormat =
           GenerateFrameworkAuditScopeReportRequest.Format.forNumber(0);
       String complianceFramework = "complianceFramework-1808314333";
       GenerateFrameworkAuditScopeReportResponse response =
           auditClient.generateFrameworkAuditScopeReport(scope, reportFormat, complianceFramework);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`scope` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The organization, folder or project for the audit report. Supported formats are the following: 

  * `projects/{project_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `organizations/{organization_id}/locations/{location}`

  
`reportFormat` | `[GenerateFrameworkAuditScopeReportRequest.Format](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GenerateFrameworkAuditScopeReportRequest.Format)`  
Required. The format that the scope report bytes is returned in.  
`complianceFramework` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The compliance framework that the scope report is generated for.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateFrameworkAuditScopeReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GenerateFrameworkAuditScopeReportResponse)` |   
  
### generateFrameworkAuditScopeReportCallable()
    
    
    public final UnaryCallable<GenerateFrameworkAuditScopeReportRequest,GenerateFrameworkAuditScopeReportResponse> generateFrameworkAuditScopeReportCallable()

Generates an audit scope report for a framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       GenerateFrameworkAuditScopeReportRequest request =
           GenerateFrameworkAuditScopeReportRequest.newBuilder()
               .setScope("scope109264468")
               .setComplianceFramework("complianceFramework-1808314333")
               .build();
       ApiFuture<GenerateFrameworkAuditScopeReportResponse> future =
           auditClient.generateFrameworkAuditScopeReportCallable().futureCall(request);
       // Do something.
       GenerateFrameworkAuditScopeReportResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateFrameworkAuditScopeReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GenerateFrameworkAuditScopeReportRequest),[GenerateFrameworkAuditScopeReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GenerateFrameworkAuditScopeReportResponse)>` |   
  
### getFrameworkAudit(@Nullable FrameworkAuditName name)
    
    
    public final FrameworkAudit getFrameworkAudit(@Nullable FrameworkAuditName name)

Gets the details for a framework audit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       FrameworkAuditName name =
           FrameworkAuditName.ofOrganizationLocationFrameworkAuditName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_AUDIT]");
       FrameworkAudit response = auditClient.getFrameworkAudit(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FrameworkAuditName`  
Required. The name of the framework audit to retrieve. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}/frameworkAudits/{frameworkAuditName}`
  * `folders/{folder_id}/locations/{location}/frameworkAudits/{frameworkAuditName}`
  * `projects/{project_id}/locations/{location}/frameworkAudits/{frameworkAuditName}`

  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit)` |   
  
### getFrameworkAudit(GetFrameworkAuditRequest request)
    
    
    public final FrameworkAudit getFrameworkAudit(GetFrameworkAuditRequest request)

Gets the details for a framework audit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       GetFrameworkAuditRequest request =
           GetFrameworkAuditRequest.newBuilder()
               .setName(
                   FrameworkAuditName.ofOrganizationLocationFrameworkAuditName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_AUDIT]")
                       .toString())
               .build();
       FrameworkAudit response = auditClient.getFrameworkAudit(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFrameworkAuditRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetFrameworkAuditRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit)` |   
  
### getFrameworkAudit(String name)
    
    
    public final FrameworkAudit getFrameworkAudit(String name)

Gets the details for a framework audit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       String name =
           FrameworkAuditName.ofProjectLocationFrameworkAuditName(
                   "[PROJECT]", "[LOCATION]", "[FRAMEWORK_AUDIT]")
               .toString();
       FrameworkAudit response = auditClient.getFrameworkAudit(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the framework audit to retrieve. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}/frameworkAudits/{frameworkAuditName}`
  * `folders/{folder_id}/locations/{location}/frameworkAudits/{frameworkAuditName}`
  * `projects/{project_id}/locations/{location}/frameworkAudits/{frameworkAuditName}`

  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit)` |   
  
### getFrameworkAuditCallable()
    
    
    public final UnaryCallable<GetFrameworkAuditRequest,FrameworkAudit> getFrameworkAuditCallable()

Gets the details for a framework audit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       GetFrameworkAuditRequest request =
           GetFrameworkAuditRequest.newBuilder()
               .setName(
                   FrameworkAuditName.ofOrganizationLocationFrameworkAuditName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_AUDIT]")
                       .toString())
               .build();
       ApiFuture<FrameworkAudit> future =
           auditClient.getFrameworkAuditCallable().futureCall(request);
       // Do something.
       FrameworkAudit response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFrameworkAuditRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetFrameworkAuditRequest),[FrameworkAudit](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkAudit)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = auditClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = auditClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable AuditSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.AuditSettings` |   
  
### getStub()
    
    
    public AuditStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AuditStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.AuditStub)` |   
  
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
  
### listFrameworkAudits(@Nullable LocationName parent)
    
    
    public final AuditClient.ListFrameworkAuditsPagedResponse listFrameworkAudits(@Nullable LocationName parent)

Lists the framework audits for a given organization, folder, or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (FrameworkAudit element : auditClient.listFrameworkAudits(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource where the framework audits are listed. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `projects/{project_id}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[AuditClient.ListFrameworkAuditsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient.ListFrameworkAuditsPagedResponse)` |   
  
### listFrameworkAudits(@Nullable OrganizationLocationName parent)
    
    
    public final AuditClient.ListFrameworkAuditsPagedResponse listFrameworkAudits(@Nullable OrganizationLocationName parent)

Lists the framework audits for a given organization, folder, or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (FrameworkAudit element : auditClient.listFrameworkAudits(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource where the framework audits are listed. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `projects/{project_id}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[AuditClient.ListFrameworkAuditsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient.ListFrameworkAuditsPagedResponse)` |   
  
### listFrameworkAudits(ListFrameworkAuditsRequest request)
    
    
    public final AuditClient.ListFrameworkAuditsPagedResponse listFrameworkAudits(ListFrameworkAuditsRequest request)

Lists the framework audits for a given organization, folder, or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       ListFrameworkAuditsRequest request =
           ListFrameworkAuditsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (FrameworkAudit element : auditClient.listFrameworkAudits(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFrameworkAuditsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkAuditsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuditClient.ListFrameworkAuditsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient.ListFrameworkAuditsPagedResponse)` |   
  
### listFrameworkAudits(String parent)
    
    
    public final AuditClient.ListFrameworkAuditsPagedResponse listFrameworkAudits(String parent)

Lists the framework audits for a given organization, folder, or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (FrameworkAudit element : auditClient.listFrameworkAudits(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where the framework audits are listed. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `projects/{project_id}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[AuditClient.ListFrameworkAuditsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient.ListFrameworkAuditsPagedResponse)` |   
  
### listFrameworkAuditsCallable()
    
    
    public final UnaryCallable<ListFrameworkAuditsRequest,ListFrameworkAuditsResponse> listFrameworkAuditsCallable()

Lists the framework audits for a given organization, folder, or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       ListFrameworkAuditsRequest request =
           ListFrameworkAuditsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListFrameworkAuditsResponse response =
             auditClient.listFrameworkAuditsCallable().call(request);
         for (FrameworkAudit element : response.getFrameworkAuditsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFrameworkAuditsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkAuditsRequest),[ListFrameworkAuditsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkAuditsResponse)>` |   
  
### listFrameworkAuditsPagedCallable()
    
    
    public final UnaryCallable<ListFrameworkAuditsRequest,AuditClient.ListFrameworkAuditsPagedResponse> listFrameworkAuditsPagedCallable()

Lists the framework audits for a given organization, folder, or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       ListFrameworkAuditsRequest request =
           ListFrameworkAuditsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<FrameworkAudit> future =
           auditClient.listFrameworkAuditsPagedCallable().futureCall(request);
       // Do something.
       for (FrameworkAudit element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFrameworkAuditsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkAuditsRequest),[ListFrameworkAuditsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient.ListFrameworkAuditsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final AuditClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : auditClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuditClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = auditClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,AuditClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuditClient auditClient = AuditClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = auditClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
