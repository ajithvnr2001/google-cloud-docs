---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient
title: Class DeploymentClient (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:50.625090+00:00
---

# Class DeploymentClient (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DeploymentClient (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudsecuritycompliance/google-cloud-cloudsecuritycompliance/src/main/java/com/google/cloud/cloudsecuritycompliance/v1/DeploymentClient.java)| [Product Reference](https://cloud.google.com/security-command-center/docs/compliance-manager-overview)  
---|---  
  
Service Description: Deployment service allows users to manage deployments of Frameworks and Cloud Controls on a target resource.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       FrameworkDeploymentName name =
           FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]");
       FrameworkDeployment response = deploymentClient.getFrameworkDeployment(name);
     }
     

Note: close() needs to be called on the DeploymentClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateFrameworkDeployment |  Creates a framework deployment in a given parent resource. A framework deployment lets you assign a particular framework version to an organization, folder, or project so that you can control and monitor those resources using the framework's cloud controls. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFrameworkDeploymentAsync(CreateFrameworkDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createFrameworkDeploymentAsync(LocationName parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId) 
  * createFrameworkDeploymentAsync(OrganizationLocationName parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId) 
  * createFrameworkDeploymentAsync(String parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFrameworkDeploymentOperationCallable() 
  * createFrameworkDeploymentCallable() 

  
DeleteFrameworkDeployment |  Deletes a framework deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFrameworkDeploymentAsync(DeleteFrameworkDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteFrameworkDeploymentAsync(FrameworkDeploymentName name) 
  * deleteFrameworkDeploymentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFrameworkDeploymentOperationCallable() 
  * deleteFrameworkDeploymentCallable() 

  
GetFrameworkDeployment |  Gets details about a framework deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFrameworkDeployment(GetFrameworkDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFrameworkDeployment(FrameworkDeploymentName name) 
  * getFrameworkDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFrameworkDeploymentCallable() 

  
ListFrameworkDeployments |  Lists the framework deployments in a given parent resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFrameworkDeployments(ListFrameworkDeploymentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFrameworkDeployments(LocationName parent) 
  * listFrameworkDeployments(OrganizationLocationName parent) 
  * listFrameworkDeployments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFrameworkDeploymentsPagedCallable() 
  * listFrameworkDeploymentsCallable() 

  
GetCloudControlDeployment |  Gets details about a cloud control deployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCloudControlDeployment(GetCloudControlDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCloudControlDeployment(CloudControlDeploymentName name) 
  * getCloudControlDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCloudControlDeploymentCallable() 

  
ListCloudControlDeployments |  Lists the cloud conrol deployments in a given parent resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCloudControlDeployments(ListCloudControlDeploymentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCloudControlDeployments(LocationName parent) 
  * listCloudControlDeployments(OrganizationLocationName parent) 
  * listCloudControlDeployments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCloudControlDeploymentsPagedCallable() 
  * listCloudControlDeploymentsCallable() 

  
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

This class can be customized by passing in a custom instance of DeploymentSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeploymentSettings deploymentSettings =
         DeploymentSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DeploymentClient deploymentClient = DeploymentClient.create(deploymentSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeploymentSettings deploymentSettings =
         DeploymentSettings.newBuilder().setEndpoint(myEndpoint).build();
     DeploymentClient deploymentClient = DeploymentClient.create(deploymentSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeploymentSettings deploymentSettings = DeploymentSettings.newHttpJsonBuilder().build();
     DeploymentClient deploymentClient = DeploymentClient.create(deploymentSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DeploymentClient

## Static Methods 

### create()
    
    
    public static final DeploymentClient create()

Constructs an instance of DeploymentClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeploymentSettings settings)
    
    
    public static final DeploymentClient create(DeploymentSettings settings)

Constructs an instance of DeploymentClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeploymentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeploymentStub stub)
    
    
    public static final DeploymentClient create(DeploymentStub stub)

Constructs an instance of DeploymentClient, using the given stub for making calls. This is for advanced usage - prefer using create(DeploymentSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeploymentStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.DeploymentStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient)` |   
  
## Constructors 

### DeploymentClient(DeploymentSettings settings)
    
    
    protected DeploymentClient(DeploymentSettings settings)

Constructs an instance of DeploymentClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeploymentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentSettings)`  
  
  
### DeploymentClient(DeploymentStub stub)
    
    
    protected DeploymentClient(DeploymentStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeploymentStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.DeploymentStub)`  
  
  
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

### createFrameworkDeploymentAsync(@Nullable LocationName parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId)
    
    
    public final OperationFuture<FrameworkDeployment,OperationMetadata> createFrameworkDeploymentAsync(@Nullable LocationName parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId)

Creates a framework deployment in a given parent resource. A framework deployment lets you assign a particular framework version to an organization, folder, or project so that you can control and monitor those resources using the framework's cloud controls.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       FrameworkDeployment frameworkDeployment = FrameworkDeployment.newBuilder().build();
       String frameworkDeploymentId = "frameworkDeploymentId-1244700706";
       FrameworkDeployment response =
           deploymentClient
               .createFrameworkDeploymentAsync(parent, frameworkDeployment, frameworkDeploymentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource of the framework deployment in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. Only the global location is supported.  
`frameworkDeployment` | `[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment)`  
Required. The framework deployment that you're creating.  
`frameworkDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. An identifier for the framework deployment that's unique in scope of the parent. If you don't specify a value, then a random UUID is generated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### createFrameworkDeploymentAsync(@Nullable OrganizationLocationName parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId)
    
    
    public final OperationFuture<FrameworkDeployment,OperationMetadata> createFrameworkDeploymentAsync(@Nullable OrganizationLocationName parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId)

Creates a framework deployment in a given parent resource. A framework deployment lets you assign a particular framework version to an organization, folder, or project so that you can control and monitor those resources using the framework's cloud controls.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       FrameworkDeployment frameworkDeployment = FrameworkDeployment.newBuilder().build();
       String frameworkDeploymentId = "frameworkDeploymentId-1244700706";
       FrameworkDeployment response =
           deploymentClient
               .createFrameworkDeploymentAsync(parent, frameworkDeployment, frameworkDeploymentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource of the framework deployment in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. Only the global location is supported.  
`frameworkDeployment` | `[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment)`  
Required. The framework deployment that you're creating.  
`frameworkDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. An identifier for the framework deployment that's unique in scope of the parent. If you don't specify a value, then a random UUID is generated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### createFrameworkDeploymentAsync(CreateFrameworkDeploymentRequest request)
    
    
    public final OperationFuture<FrameworkDeployment,OperationMetadata> createFrameworkDeploymentAsync(CreateFrameworkDeploymentRequest request)

Creates a framework deployment in a given parent resource. A framework deployment lets you assign a particular framework version to an organization, folder, or project so that you can control and monitor those resources using the framework's cloud controls.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       CreateFrameworkDeploymentRequest request =
           CreateFrameworkDeploymentRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setFrameworkDeploymentId("frameworkDeploymentId-1244700706")
               .setFrameworkDeployment(FrameworkDeployment.newBuilder().build())
               .build();
       FrameworkDeployment response = deploymentClient.createFrameworkDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFrameworkDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### createFrameworkDeploymentAsync(String parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId)
    
    
    public final OperationFuture<FrameworkDeployment,OperationMetadata> createFrameworkDeploymentAsync(String parent, FrameworkDeployment frameworkDeployment, String frameworkDeploymentId)

Creates a framework deployment in a given parent resource. A framework deployment lets you assign a particular framework version to an organization, folder, or project so that you can control and monitor those resources using the framework's cloud controls.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       FrameworkDeployment frameworkDeployment = FrameworkDeployment.newBuilder().build();
       String frameworkDeploymentId = "frameworkDeploymentId-1244700706";
       FrameworkDeployment response =
           deploymentClient
               .createFrameworkDeploymentAsync(parent, frameworkDeployment, frameworkDeploymentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the framework deployment in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. Only the global location is supported.  
`frameworkDeployment` | `[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment)`  
Required. The framework deployment that you're creating.  
`frameworkDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. An identifier for the framework deployment that's unique in scope of the parent. If you don't specify a value, then a random UUID is generated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### createFrameworkDeploymentCallable()
    
    
    public final UnaryCallable<CreateFrameworkDeploymentRequest,Operation> createFrameworkDeploymentCallable()

Creates a framework deployment in a given parent resource. A framework deployment lets you assign a particular framework version to an organization, folder, or project so that you can control and monitor those resources using the framework's cloud controls.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       CreateFrameworkDeploymentRequest request =
           CreateFrameworkDeploymentRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setFrameworkDeploymentId("frameworkDeploymentId-1244700706")
               .setFrameworkDeployment(FrameworkDeployment.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           deploymentClient.createFrameworkDeploymentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFrameworkDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFrameworkDeploymentOperationCallable()
    
    
    public final OperationCallable<CreateFrameworkDeploymentRequest,FrameworkDeployment,OperationMetadata> createFrameworkDeploymentOperationCallable()

Creates a framework deployment in a given parent resource. A framework deployment lets you assign a particular framework version to an organization, folder, or project so that you can control and monitor those resources using the framework's cloud controls.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       CreateFrameworkDeploymentRequest request =
           CreateFrameworkDeploymentRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setFrameworkDeploymentId("frameworkDeploymentId-1244700706")
               .setFrameworkDeployment(FrameworkDeployment.newBuilder().build())
               .build();
       OperationFuture<FrameworkDeployment, OperationMetadata> future =
           deploymentClient.createFrameworkDeploymentOperationCallable().futureCall(request);
       // Do something.
       FrameworkDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateFrameworkDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkDeploymentRequest),[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### deleteFrameworkDeploymentAsync(@Nullable FrameworkDeploymentName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteFrameworkDeploymentAsync(@Nullable FrameworkDeploymentName name)

Deletes a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       FrameworkDeploymentName name =
           FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]");
       deploymentClient.deleteFrameworkDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeploymentName`  
Required. The name of the framework deployment that you want to delete, in the format `organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}` or `projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### deleteFrameworkDeploymentAsync(DeleteFrameworkDeploymentRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteFrameworkDeploymentAsync(DeleteFrameworkDeploymentRequest request)

Deletes a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       DeleteFrameworkDeploymentRequest request =
           DeleteFrameworkDeploymentRequest.newBuilder()
               .setName(
                   FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       deploymentClient.deleteFrameworkDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFrameworkDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteFrameworkDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### deleteFrameworkDeploymentAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteFrameworkDeploymentAsync(String name)

Deletes a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       String name =
           FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
                   "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]")
               .toString();
       deploymentClient.deleteFrameworkDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the framework deployment that you want to delete, in the format `organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}` or `projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### deleteFrameworkDeploymentCallable()
    
    
    public final UnaryCallable<DeleteFrameworkDeploymentRequest,Operation> deleteFrameworkDeploymentCallable()

Deletes a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       DeleteFrameworkDeploymentRequest request =
           DeleteFrameworkDeploymentRequest.newBuilder()
               .setName(
                   FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           deploymentClient.deleteFrameworkDeploymentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFrameworkDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteFrameworkDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFrameworkDeploymentOperationCallable()
    
    
    public final OperationCallable<DeleteFrameworkDeploymentRequest,Empty,OperationMetadata> deleteFrameworkDeploymentOperationCallable()

Deletes a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       DeleteFrameworkDeploymentRequest request =
           DeleteFrameworkDeploymentRequest.newBuilder()
               .setName(
                   FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           deploymentClient.deleteFrameworkDeploymentOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFrameworkDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteFrameworkDeploymentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.OperationMetadata)>` |   
  
### getCloudControlDeployment(@Nullable CloudControlDeploymentName name)
    
    
    public final CloudControlDeployment getCloudControlDeployment(@Nullable CloudControlDeploymentName name)

Gets details about a cloud control deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       CloudControlDeploymentName name =
           CloudControlDeploymentName.ofOrganizationLocationCloudControlDeploymentName(
               "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL_DEPLOYMENT]");
       CloudControlDeployment response = deploymentClient.getCloudControlDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.CloudControlDeploymentName`  
Required. The name for the cloud control deployment, in the format `organizations/{organization}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}` or `projects/{project}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControlDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControlDeployment)` |   
  
### getCloudControlDeployment(GetCloudControlDeploymentRequest request)
    
    
    public final CloudControlDeployment getCloudControlDeployment(GetCloudControlDeploymentRequest request)

Gets details about a cloud control deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       GetCloudControlDeploymentRequest request =
           GetCloudControlDeploymentRequest.newBuilder()
               .setName(
                   CloudControlDeploymentName.ofOrganizationLocationCloudControlDeploymentName(
                           "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL_DEPLOYMENT]")
                       .toString())
               .build();
       CloudControlDeployment response = deploymentClient.getCloudControlDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCloudControlDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetCloudControlDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControlDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControlDeployment)` |   
  
### getCloudControlDeployment(String name)
    
    
    public final CloudControlDeployment getCloudControlDeployment(String name)

Gets details about a cloud control deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       String name =
           CloudControlDeploymentName.ofOrganizationLocationCloudControlDeploymentName(
                   "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL_DEPLOYMENT]")
               .toString();
       CloudControlDeployment response = deploymentClient.getCloudControlDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name for the cloud control deployment, in the format `organizations/{organization}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}` or `projects/{project}/locations/{location}/cloudControlDeployments/{cloud_control_deployment}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControlDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControlDeployment)` |   
  
### getCloudControlDeploymentCallable()
    
    
    public final UnaryCallable<GetCloudControlDeploymentRequest,CloudControlDeployment> getCloudControlDeploymentCallable()

Gets details about a cloud control deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       GetCloudControlDeploymentRequest request =
           GetCloudControlDeploymentRequest.newBuilder()
               .setName(
                   CloudControlDeploymentName.ofOrganizationLocationCloudControlDeploymentName(
                           "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL_DEPLOYMENT]")
                       .toString())
               .build();
       ApiFuture<CloudControlDeployment> future =
           deploymentClient.getCloudControlDeploymentCallable().futureCall(request);
       // Do something.
       CloudControlDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCloudControlDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetCloudControlDeploymentRequest),[CloudControlDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControlDeployment)>` |   
  
### getFrameworkDeployment(@Nullable FrameworkDeploymentName name)
    
    
    public final FrameworkDeployment getFrameworkDeployment(@Nullable FrameworkDeploymentName name)

Gets details about a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       FrameworkDeploymentName name =
           FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]");
       FrameworkDeployment response = deploymentClient.getFrameworkDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeploymentName`  
Required. The name of the framework deployment, in the format `organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}` or `projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment)` |   
  
### getFrameworkDeployment(GetFrameworkDeploymentRequest request)
    
    
    public final FrameworkDeployment getFrameworkDeployment(GetFrameworkDeploymentRequest request)

Gets details about a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       GetFrameworkDeploymentRequest request =
           GetFrameworkDeploymentRequest.newBuilder()
               .setName(
                   FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]")
                       .toString())
               .build();
       FrameworkDeployment response = deploymentClient.getFrameworkDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFrameworkDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetFrameworkDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment)` |   
  
### getFrameworkDeployment(String name)
    
    
    public final FrameworkDeployment getFrameworkDeployment(String name)

Gets details about a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       String name =
           FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
                   "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]")
               .toString();
       FrameworkDeployment response = deploymentClient.getFrameworkDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the framework deployment, in the format `organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}` or `projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment)` |   
  
### getFrameworkDeploymentCallable()
    
    
    public final UnaryCallable<GetFrameworkDeploymentRequest,FrameworkDeployment> getFrameworkDeploymentCallable()

Gets details about a framework deployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       GetFrameworkDeploymentRequest request =
           GetFrameworkDeploymentRequest.newBuilder()
               .setName(
                   FrameworkDeploymentName.ofOrganizationLocationFrameworkDeploymentName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK_DEPLOYMENT]")
                       .toString())
               .build();
       ApiFuture<FrameworkDeployment> future =
           deploymentClient.getFrameworkDeploymentCallable().futureCall(request);
       // Do something.
       FrameworkDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFrameworkDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetFrameworkDeploymentRequest),[FrameworkDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkDeployment)>` |   
  
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
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = deploymentClient.getLocation(request);
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
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = deploymentClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable DeploymentSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.DeploymentSettings` |   
  
### getStub()
    
    
    public DeploymentStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DeploymentStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.DeploymentStub)` |   
  
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
  
### listCloudControlDeployments(@Nullable LocationName parent)
    
    
    public final DeploymentClient.ListCloudControlDeploymentsPagedResponse listCloudControlDeployments(@Nullable LocationName parent)

Lists the cloud conrol deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (CloudControlDeployment element :
           deploymentClient.listCloudControlDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource for the cloud control deployment, in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient.ListCloudControlDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListCloudControlDeploymentsPagedResponse)` |   
  
### listCloudControlDeployments(@Nullable OrganizationLocationName parent)
    
    
    public final DeploymentClient.ListCloudControlDeploymentsPagedResponse listCloudControlDeployments(@Nullable OrganizationLocationName parent)

Lists the cloud conrol deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (CloudControlDeployment element :
           deploymentClient.listCloudControlDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource for the cloud control deployment, in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient.ListCloudControlDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListCloudControlDeploymentsPagedResponse)` |   
  
### listCloudControlDeployments(ListCloudControlDeploymentsRequest request)
    
    
    public final DeploymentClient.ListCloudControlDeploymentsPagedResponse listCloudControlDeployments(ListCloudControlDeploymentsRequest request)

Lists the cloud conrol deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListCloudControlDeploymentsRequest request =
           ListCloudControlDeploymentsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (CloudControlDeployment element :
           deploymentClient.listCloudControlDeployments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCloudControlDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient.ListCloudControlDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListCloudControlDeploymentsPagedResponse)` |   
  
### listCloudControlDeployments(String parent)
    
    
    public final DeploymentClient.ListCloudControlDeploymentsPagedResponse listCloudControlDeployments(String parent)

Lists the cloud conrol deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (CloudControlDeployment element :
           deploymentClient.listCloudControlDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource for the cloud control deployment, in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient.ListCloudControlDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListCloudControlDeploymentsPagedResponse)` |   
  
### listCloudControlDeploymentsCallable()
    
    
    public final UnaryCallable<ListCloudControlDeploymentsRequest,ListCloudControlDeploymentsResponse> listCloudControlDeploymentsCallable()

Lists the cloud conrol deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListCloudControlDeploymentsRequest request =
           ListCloudControlDeploymentsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListCloudControlDeploymentsResponse response =
             deploymentClient.listCloudControlDeploymentsCallable().call(request);
         for (CloudControlDeployment element : response.getCloudControlDeploymentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudControlDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlDeploymentsRequest),[ListCloudControlDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlDeploymentsResponse)>` |   
  
### listCloudControlDeploymentsPagedCallable()
    
    
    public final UnaryCallable<ListCloudControlDeploymentsRequest,DeploymentClient.ListCloudControlDeploymentsPagedResponse> listCloudControlDeploymentsPagedCallable()

Lists the cloud conrol deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListCloudControlDeploymentsRequest request =
           ListCloudControlDeploymentsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<CloudControlDeployment> future =
           deploymentClient.listCloudControlDeploymentsPagedCallable().futureCall(request);
       // Do something.
       for (CloudControlDeployment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudControlDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlDeploymentsRequest),[ListCloudControlDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListCloudControlDeploymentsPagedResponse)>` |   
  
### listFrameworkDeployments(@Nullable LocationName parent)
    
    
    public final DeploymentClient.ListFrameworkDeploymentsPagedResponse listFrameworkDeployments(@Nullable LocationName parent)

Lists the framework deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (FrameworkDeployment element :
           deploymentClient.listFrameworkDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource of the framework deployment, in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient.ListFrameworkDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListFrameworkDeploymentsPagedResponse)` |   
  
### listFrameworkDeployments(@Nullable OrganizationLocationName parent)
    
    
    public final DeploymentClient.ListFrameworkDeploymentsPagedResponse listFrameworkDeployments(@Nullable OrganizationLocationName parent)

Lists the framework deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (FrameworkDeployment element :
           deploymentClient.listFrameworkDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource of the framework deployment, in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient.ListFrameworkDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListFrameworkDeploymentsPagedResponse)` |   
  
### listFrameworkDeployments(ListFrameworkDeploymentsRequest request)
    
    
    public final DeploymentClient.ListFrameworkDeploymentsPagedResponse listFrameworkDeployments(ListFrameworkDeploymentsRequest request)

Lists the framework deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListFrameworkDeploymentsRequest request =
           ListFrameworkDeploymentsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (FrameworkDeployment element :
           deploymentClient.listFrameworkDeployments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFrameworkDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient.ListFrameworkDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListFrameworkDeploymentsPagedResponse)` |   
  
### listFrameworkDeployments(String parent)
    
    
    public final DeploymentClient.ListFrameworkDeploymentsPagedResponse listFrameworkDeployments(String parent)

Lists the framework deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (FrameworkDeployment element :
           deploymentClient.listFrameworkDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the framework deployment, in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentClient.ListFrameworkDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListFrameworkDeploymentsPagedResponse)` |   
  
### listFrameworkDeploymentsCallable()
    
    
    public final UnaryCallable<ListFrameworkDeploymentsRequest,ListFrameworkDeploymentsResponse> listFrameworkDeploymentsCallable()

Lists the framework deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListFrameworkDeploymentsRequest request =
           ListFrameworkDeploymentsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListFrameworkDeploymentsResponse response =
             deploymentClient.listFrameworkDeploymentsCallable().call(request);
         for (FrameworkDeployment element : response.getFrameworkDeploymentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFrameworkDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkDeploymentsRequest),[ListFrameworkDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkDeploymentsResponse)>` |   
  
### listFrameworkDeploymentsPagedCallable()
    
    
    public final UnaryCallable<ListFrameworkDeploymentsRequest,DeploymentClient.ListFrameworkDeploymentsPagedResponse> listFrameworkDeploymentsPagedCallable()

Lists the framework deployments in a given parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListFrameworkDeploymentsRequest request =
           ListFrameworkDeploymentsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<FrameworkDeployment> future =
           deploymentClient.listFrameworkDeploymentsPagedCallable().futureCall(request);
       // Do something.
       for (FrameworkDeployment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFrameworkDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkDeploymentsRequest),[ListFrameworkDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListFrameworkDeploymentsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DeploymentClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : deploymentClient.listLocations(request).iterateAll()) {
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
`[DeploymentClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListLocationsPagedResponse)` |   
  
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
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = deploymentClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DeploymentClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentClient deploymentClient = DeploymentClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           deploymentClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeploymentClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
