---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient
title: Class NotebookServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:17.137892+00:00
---

# Class NotebookServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NotebookServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/NotebookServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: The interface for Vertex Notebook service (a.k.a. Colab on Workbench).

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeTemplateName name =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]");
       NotebookRuntimeTemplate response = notebookServiceClient.getNotebookRuntimeTemplate(name);
     }
     

Note: close() needs to be called on the NotebookServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateNotebookRuntimeTemplate |  Creates a NotebookRuntimeTemplate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNotebookRuntimeTemplateAsync(CreateNotebookRuntimeTemplateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createNotebookRuntimeTemplateAsync(LocationName parent, NotebookRuntimeTemplate notebookRuntimeTemplate, String notebookRuntimeTemplateId) 
  * createNotebookRuntimeTemplateAsync(String parent, NotebookRuntimeTemplate notebookRuntimeTemplate, String notebookRuntimeTemplateId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNotebookRuntimeTemplateOperationCallable() 
  * createNotebookRuntimeTemplateCallable() 

  
GetNotebookRuntimeTemplate |  Gets a NotebookRuntimeTemplate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNotebookRuntimeTemplate(GetNotebookRuntimeTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNotebookRuntimeTemplate(NotebookRuntimeTemplateName name) 
  * getNotebookRuntimeTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNotebookRuntimeTemplateCallable() 

  
ListNotebookRuntimeTemplates |  Lists NotebookRuntimeTemplates in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNotebookRuntimeTemplates(ListNotebookRuntimeTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNotebookRuntimeTemplates(LocationName parent) 
  * listNotebookRuntimeTemplates(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNotebookRuntimeTemplatesPagedCallable() 
  * listNotebookRuntimeTemplatesCallable() 

  
DeleteNotebookRuntimeTemplate |  Deletes a NotebookRuntimeTemplate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNotebookRuntimeTemplateAsync(DeleteNotebookRuntimeTemplateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNotebookRuntimeTemplateAsync(NotebookRuntimeTemplateName name) 
  * deleteNotebookRuntimeTemplateAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNotebookRuntimeTemplateOperationCallable() 
  * deleteNotebookRuntimeTemplateCallable() 

  
UpdateNotebookRuntimeTemplate |  Updates a NotebookRuntimeTemplate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNotebookRuntimeTemplate(UpdateNotebookRuntimeTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateNotebookRuntimeTemplate(NotebookRuntimeTemplate notebookRuntimeTemplate, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNotebookRuntimeTemplateCallable() 

  
AssignNotebookRuntime |  Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * assignNotebookRuntimeAsync(AssignNotebookRuntimeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * assignNotebookRuntimeAsync(LocationName parent, NotebookRuntimeTemplateName notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId) 
  * assignNotebookRuntimeAsync(LocationName parent, String notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId) 
  * assignNotebookRuntimeAsync(String parent, NotebookRuntimeTemplateName notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId) 
  * assignNotebookRuntimeAsync(String parent, String notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * assignNotebookRuntimeOperationCallable() 
  * assignNotebookRuntimeCallable() 

  
GetNotebookRuntime |  Gets a NotebookRuntime. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNotebookRuntime(GetNotebookRuntimeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNotebookRuntime(NotebookRuntimeName name) 
  * getNotebookRuntime(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNotebookRuntimeCallable() 

  
ListNotebookRuntimes |  Lists NotebookRuntimes in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNotebookRuntimes(ListNotebookRuntimesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNotebookRuntimes(LocationName parent) 
  * listNotebookRuntimes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNotebookRuntimesPagedCallable() 
  * listNotebookRuntimesCallable() 

  
DeleteNotebookRuntime |  Deletes a NotebookRuntime. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNotebookRuntimeAsync(DeleteNotebookRuntimeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNotebookRuntimeAsync(NotebookRuntimeName name) 
  * deleteNotebookRuntimeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNotebookRuntimeOperationCallable() 
  * deleteNotebookRuntimeCallable() 

  
UpgradeNotebookRuntime |  Upgrades a NotebookRuntime. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * upgradeNotebookRuntimeAsync(UpgradeNotebookRuntimeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * upgradeNotebookRuntimeAsync(NotebookRuntimeName name) 
  * upgradeNotebookRuntimeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * upgradeNotebookRuntimeOperationCallable() 
  * upgradeNotebookRuntimeCallable() 

  
StartNotebookRuntime |  Starts a NotebookRuntime. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startNotebookRuntimeAsync(StartNotebookRuntimeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * startNotebookRuntimeAsync(NotebookRuntimeName name) 
  * startNotebookRuntimeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startNotebookRuntimeOperationCallable() 
  * startNotebookRuntimeCallable() 

  
StopNotebookRuntime |  Stops a NotebookRuntime. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopNotebookRuntimeAsync(StopNotebookRuntimeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * stopNotebookRuntimeAsync(NotebookRuntimeName name) 
  * stopNotebookRuntimeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopNotebookRuntimeOperationCallable() 
  * stopNotebookRuntimeCallable() 

  
CreateNotebookExecutionJob |  Creates a NotebookExecutionJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNotebookExecutionJobAsync(CreateNotebookExecutionJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createNotebookExecutionJobAsync(LocationName parent, NotebookExecutionJob notebookExecutionJob, String notebookExecutionJobId) 
  * createNotebookExecutionJobAsync(String parent, NotebookExecutionJob notebookExecutionJob, String notebookExecutionJobId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNotebookExecutionJobOperationCallable() 
  * createNotebookExecutionJobCallable() 

  
GetNotebookExecutionJob |  Gets a NotebookExecutionJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNotebookExecutionJob(GetNotebookExecutionJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNotebookExecutionJob(NotebookExecutionJobName name) 
  * getNotebookExecutionJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNotebookExecutionJobCallable() 

  
ListNotebookExecutionJobs |  Lists NotebookExecutionJobs in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNotebookExecutionJobs(ListNotebookExecutionJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNotebookExecutionJobs(LocationName parent) 
  * listNotebookExecutionJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNotebookExecutionJobsPagedCallable() 
  * listNotebookExecutionJobsCallable() 

  
DeleteNotebookExecutionJob |  Deletes a NotebookExecutionJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNotebookExecutionJobAsync(DeleteNotebookExecutionJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNotebookExecutionJobAsync(NotebookExecutionJobName name) 
  * deleteNotebookExecutionJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNotebookExecutionJobOperationCallable() 
  * deleteNotebookExecutionJobCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NotebookServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NotebookServiceSettings notebookServiceSettings =
         NotebookServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NotebookServiceClient notebookServiceClient =
         NotebookServiceClient.create(notebookServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NotebookServiceSettings notebookServiceSettings =
         NotebookServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     NotebookServiceClient notebookServiceClient =
         NotebookServiceClient.create(notebookServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NotebookServiceClient

## Static Methods 

### create()
    
    
    public static final NotebookServiceClient create()

Constructs an instance of NotebookServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NotebookServiceSettings settings)
    
    
    public static final NotebookServiceClient create(NotebookServiceSettings settings)

Constructs an instance of NotebookServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NotebookServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NotebookServiceStub stub)
    
    
    public static final NotebookServiceClient create(NotebookServiceStub stub)

Constructs an instance of NotebookServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(NotebookServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NotebookServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.NotebookServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient)` |   
  
## Constructors 

### NotebookServiceClient(NotebookServiceSettings settings)
    
    
    protected NotebookServiceClient(NotebookServiceSettings settings)

Constructs an instance of NotebookServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NotebookServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceSettings)`  
  
  
### NotebookServiceClient(NotebookServiceStub stub)
    
    
    protected NotebookServiceClient(NotebookServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NotebookServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.NotebookServiceStub)`  
  
  
## Methods 

### assignNotebookRuntimeAsync(@Nullable LocationName parent, @Nullable NotebookRuntimeTemplateName notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId)
    
    
    public final OperationFuture<NotebookRuntime,AssignNotebookRuntimeOperationMetadata> assignNotebookRuntimeAsync(@Nullable LocationName parent, @Nullable NotebookRuntimeTemplateName notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId)

Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       NotebookRuntimeTemplateName notebookRuntimeTemplate =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]");
       NotebookRuntime notebookRuntime = NotebookRuntime.newBuilder().build();
       String notebookRuntimeId = "notebookRuntimeId400795512";
       NotebookRuntime response =
           notebookServiceClient
               .assignNotebookRuntimeAsync(
                   parent, notebookRuntimeTemplate, notebookRuntime, notebookRuntimeId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to get the NotebookRuntime assignment. Format: `projects/{project}/locations/{location}`  
`notebookRuntimeTemplate` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeTemplateName`  
Required. The resource name of the NotebookRuntimeTemplate based on which a NotebookRuntime will be assigned (reuse or create a new one).  
`notebookRuntime` | `[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)`  
Required. Provide runtime specific information (e.g. runtime owner, notebook id) used for NotebookRuntime assignment.  
`notebookRuntimeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User specified ID for the notebook runtime.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime),[AssignNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeOperationMetadata)>` |   
  
### assignNotebookRuntimeAsync(@Nullable LocationName parent, String notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId)
    
    
    public final OperationFuture<NotebookRuntime,AssignNotebookRuntimeOperationMetadata> assignNotebookRuntimeAsync(@Nullable LocationName parent, String notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId)

Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String notebookRuntimeTemplate =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
               .toString();
       NotebookRuntime notebookRuntime = NotebookRuntime.newBuilder().build();
       String notebookRuntimeId = "notebookRuntimeId400795512";
       NotebookRuntime response =
           notebookServiceClient
               .assignNotebookRuntimeAsync(
                   parent, notebookRuntimeTemplate, notebookRuntime, notebookRuntimeId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to get the NotebookRuntime assignment. Format: `projects/{project}/locations/{location}`  
`notebookRuntimeTemplate` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the NotebookRuntimeTemplate based on which a NotebookRuntime will be assigned (reuse or create a new one).  
`notebookRuntime` | `[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)`  
Required. Provide runtime specific information (e.g. runtime owner, notebook id) used for NotebookRuntime assignment.  
`notebookRuntimeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User specified ID for the notebook runtime.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime),[AssignNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeOperationMetadata)>` |   
  
### assignNotebookRuntimeAsync(AssignNotebookRuntimeRequest request)
    
    
    public final OperationFuture<NotebookRuntime,AssignNotebookRuntimeOperationMetadata> assignNotebookRuntimeAsync(AssignNotebookRuntimeRequest request)

Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       AssignNotebookRuntimeRequest request =
           AssignNotebookRuntimeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookRuntimeTemplate(
                   NotebookRuntimeTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
                       .toString())
               .setNotebookRuntime(NotebookRuntime.newBuilder().build())
               .setNotebookRuntimeId("notebookRuntimeId400795512")
               .build();
       NotebookRuntime response = notebookServiceClient.assignNotebookRuntimeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AssignNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime),[AssignNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeOperationMetadata)>` |   
  
### assignNotebookRuntimeAsync(String parent, @Nullable NotebookRuntimeTemplateName notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId)
    
    
    public final OperationFuture<NotebookRuntime,AssignNotebookRuntimeOperationMetadata> assignNotebookRuntimeAsync(String parent, @Nullable NotebookRuntimeTemplateName notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId)

Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       NotebookRuntimeTemplateName notebookRuntimeTemplate =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]");
       NotebookRuntime notebookRuntime = NotebookRuntime.newBuilder().build();
       String notebookRuntimeId = "notebookRuntimeId400795512";
       NotebookRuntime response =
           notebookServiceClient
               .assignNotebookRuntimeAsync(
                   parent, notebookRuntimeTemplate, notebookRuntime, notebookRuntimeId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to get the NotebookRuntime assignment. Format: `projects/{project}/locations/{location}`  
`notebookRuntimeTemplate` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeTemplateName`  
Required. The resource name of the NotebookRuntimeTemplate based on which a NotebookRuntime will be assigned (reuse or create a new one).  
`notebookRuntime` | `[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)`  
Required. Provide runtime specific information (e.g. runtime owner, notebook id) used for NotebookRuntime assignment.  
`notebookRuntimeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User specified ID for the notebook runtime.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime),[AssignNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeOperationMetadata)>` |   
  
### assignNotebookRuntimeAsync(String parent, String notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId)
    
    
    public final OperationFuture<NotebookRuntime,AssignNotebookRuntimeOperationMetadata> assignNotebookRuntimeAsync(String parent, String notebookRuntimeTemplate, NotebookRuntime notebookRuntime, String notebookRuntimeId)

Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String notebookRuntimeTemplate =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
               .toString();
       NotebookRuntime notebookRuntime = NotebookRuntime.newBuilder().build();
       String notebookRuntimeId = "notebookRuntimeId400795512";
       NotebookRuntime response =
           notebookServiceClient
               .assignNotebookRuntimeAsync(
                   parent, notebookRuntimeTemplate, notebookRuntime, notebookRuntimeId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to get the NotebookRuntime assignment. Format: `projects/{project}/locations/{location}`  
`notebookRuntimeTemplate` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the NotebookRuntimeTemplate based on which a NotebookRuntime will be assigned (reuse or create a new one).  
`notebookRuntime` | `[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)`  
Required. Provide runtime specific information (e.g. runtime owner, notebook id) used for NotebookRuntime assignment.  
`notebookRuntimeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User specified ID for the notebook runtime.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime),[AssignNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeOperationMetadata)>` |   
  
### assignNotebookRuntimeCallable()
    
    
    public final UnaryCallable<AssignNotebookRuntimeRequest,Operation> assignNotebookRuntimeCallable()

Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       AssignNotebookRuntimeRequest request =
           AssignNotebookRuntimeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookRuntimeTemplate(
                   NotebookRuntimeTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
                       .toString())
               .setNotebookRuntime(NotebookRuntime.newBuilder().build())
               .setNotebookRuntimeId("notebookRuntimeId400795512")
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.assignNotebookRuntimeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AssignNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### assignNotebookRuntimeOperationCallable()
    
    
    public final OperationCallable<AssignNotebookRuntimeRequest,NotebookRuntime,AssignNotebookRuntimeOperationMetadata> assignNotebookRuntimeOperationCallable()

Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       AssignNotebookRuntimeRequest request =
           AssignNotebookRuntimeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookRuntimeTemplate(
                   NotebookRuntimeTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
                       .toString())
               .setNotebookRuntime(NotebookRuntime.newBuilder().build())
               .setNotebookRuntimeId("notebookRuntimeId400795512")
               .build();
       OperationFuture<NotebookRuntime, AssignNotebookRuntimeOperationMetadata> future =
           notebookServiceClient.assignNotebookRuntimeOperationCallable().futureCall(request);
       // Do something.
       NotebookRuntime response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AssignNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeRequest),[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime),[AssignNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeOperationMetadata)>` |   
  
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

### createNotebookExecutionJobAsync(@Nullable LocationName parent, NotebookExecutionJob notebookExecutionJob, String notebookExecutionJobId)
    
    
    public final OperationFuture<NotebookExecutionJob,CreateNotebookExecutionJobOperationMetadata> createNotebookExecutionJobAsync(@Nullable LocationName parent, NotebookExecutionJob notebookExecutionJob, String notebookExecutionJobId)

Creates a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       NotebookExecutionJob notebookExecutionJob = NotebookExecutionJob.newBuilder().build();
       String notebookExecutionJobId = "notebookExecutionJobId1598189627";
       NotebookExecutionJob response =
           notebookServiceClient
               .createNotebookExecutionJobAsync(parent, notebookExecutionJob, notebookExecutionJobId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the NotebookExecutionJob. Format: `projects/{project}/locations/{location}`  
`notebookExecutionJob` | `[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob)`  
Required. The NotebookExecutionJob to create.  
`notebookExecutionJobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User specified ID for the NotebookExecutionJob.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob),[CreateNotebookExecutionJobOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookExecutionJobOperationMetadata)>` |   
  
### createNotebookExecutionJobAsync(CreateNotebookExecutionJobRequest request)
    
    
    public final OperationFuture<NotebookExecutionJob,CreateNotebookExecutionJobOperationMetadata> createNotebookExecutionJobAsync(CreateNotebookExecutionJobRequest request)

Creates a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       CreateNotebookExecutionJobRequest request =
           CreateNotebookExecutionJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookExecutionJob(NotebookExecutionJob.newBuilder().build())
               .setNotebookExecutionJobId("notebookExecutionJobId1598189627")
               .build();
       NotebookExecutionJob response =
           notebookServiceClient.createNotebookExecutionJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookExecutionJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob),[CreateNotebookExecutionJobOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookExecutionJobOperationMetadata)>` |   
  
### createNotebookExecutionJobAsync(String parent, NotebookExecutionJob notebookExecutionJob, String notebookExecutionJobId)
    
    
    public final OperationFuture<NotebookExecutionJob,CreateNotebookExecutionJobOperationMetadata> createNotebookExecutionJobAsync(String parent, NotebookExecutionJob notebookExecutionJob, String notebookExecutionJobId)

Creates a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       NotebookExecutionJob notebookExecutionJob = NotebookExecutionJob.newBuilder().build();
       String notebookExecutionJobId = "notebookExecutionJobId1598189627";
       NotebookExecutionJob response =
           notebookServiceClient
               .createNotebookExecutionJobAsync(parent, notebookExecutionJob, notebookExecutionJobId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the NotebookExecutionJob. Format: `projects/{project}/locations/{location}`  
`notebookExecutionJob` | `[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob)`  
Required. The NotebookExecutionJob to create.  
`notebookExecutionJobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User specified ID for the NotebookExecutionJob.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob),[CreateNotebookExecutionJobOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookExecutionJobOperationMetadata)>` |   
  
### createNotebookExecutionJobCallable()
    
    
    public final UnaryCallable<CreateNotebookExecutionJobRequest,Operation> createNotebookExecutionJobCallable()

Creates a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       CreateNotebookExecutionJobRequest request =
           CreateNotebookExecutionJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookExecutionJob(NotebookExecutionJob.newBuilder().build())
               .setNotebookExecutionJobId("notebookExecutionJobId1598189627")
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.createNotebookExecutionJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookExecutionJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNotebookExecutionJobOperationCallable()
    
    
    public final OperationCallable<CreateNotebookExecutionJobRequest,NotebookExecutionJob,CreateNotebookExecutionJobOperationMetadata> createNotebookExecutionJobOperationCallable()

Creates a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       CreateNotebookExecutionJobRequest request =
           CreateNotebookExecutionJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookExecutionJob(NotebookExecutionJob.newBuilder().build())
               .setNotebookExecutionJobId("notebookExecutionJobId1598189627")
               .build();
       OperationFuture<NotebookExecutionJob, CreateNotebookExecutionJobOperationMetadata> future =
           notebookServiceClient.createNotebookExecutionJobOperationCallable().futureCall(request);
       // Do something.
       NotebookExecutionJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookExecutionJobRequest),[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob),[CreateNotebookExecutionJobOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookExecutionJobOperationMetadata)>` |   
  
### createNotebookRuntimeTemplateAsync(@Nullable LocationName parent, NotebookRuntimeTemplate notebookRuntimeTemplate, String notebookRuntimeTemplateId)
    
    
    public final OperationFuture<NotebookRuntimeTemplate,CreateNotebookRuntimeTemplateOperationMetadata> createNotebookRuntimeTemplateAsync(@Nullable LocationName parent, NotebookRuntimeTemplate notebookRuntimeTemplate, String notebookRuntimeTemplateId)

Creates a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       NotebookRuntimeTemplate notebookRuntimeTemplate =
           NotebookRuntimeTemplate.newBuilder().build();
       String notebookRuntimeTemplateId = "notebookRuntimeTemplateId-633369454";
       NotebookRuntimeTemplate response =
           notebookServiceClient
               .createNotebookRuntimeTemplateAsync(
                   parent, notebookRuntimeTemplate, notebookRuntimeTemplateId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the NotebookRuntimeTemplate. Format: `projects/{project}/locations/{location}`  
`notebookRuntimeTemplate` | `[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)`  
Required. The NotebookRuntimeTemplate to create.  
`notebookRuntimeTemplateId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User specified ID for the notebook runtime template.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate),[CreateNotebookRuntimeTemplateOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookRuntimeTemplateOperationMetadata)>` |   
  
### createNotebookRuntimeTemplateAsync(CreateNotebookRuntimeTemplateRequest request)
    
    
    public final OperationFuture<NotebookRuntimeTemplate,CreateNotebookRuntimeTemplateOperationMetadata> createNotebookRuntimeTemplateAsync(CreateNotebookRuntimeTemplateRequest request)

Creates a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       CreateNotebookRuntimeTemplateRequest request =
           CreateNotebookRuntimeTemplateRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookRuntimeTemplate(NotebookRuntimeTemplate.newBuilder().build())
               .setNotebookRuntimeTemplateId("notebookRuntimeTemplateId-633369454")
               .build();
       NotebookRuntimeTemplate response =
           notebookServiceClient.createNotebookRuntimeTemplateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookRuntimeTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate),[CreateNotebookRuntimeTemplateOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookRuntimeTemplateOperationMetadata)>` |   
  
### createNotebookRuntimeTemplateAsync(String parent, NotebookRuntimeTemplate notebookRuntimeTemplate, String notebookRuntimeTemplateId)
    
    
    public final OperationFuture<NotebookRuntimeTemplate,CreateNotebookRuntimeTemplateOperationMetadata> createNotebookRuntimeTemplateAsync(String parent, NotebookRuntimeTemplate notebookRuntimeTemplate, String notebookRuntimeTemplateId)

Creates a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       NotebookRuntimeTemplate notebookRuntimeTemplate =
           NotebookRuntimeTemplate.newBuilder().build();
       String notebookRuntimeTemplateId = "notebookRuntimeTemplateId-633369454";
       NotebookRuntimeTemplate response =
           notebookServiceClient
               .createNotebookRuntimeTemplateAsync(
                   parent, notebookRuntimeTemplate, notebookRuntimeTemplateId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the NotebookRuntimeTemplate. Format: `projects/{project}/locations/{location}`  
`notebookRuntimeTemplate` | `[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)`  
Required. The NotebookRuntimeTemplate to create.  
`notebookRuntimeTemplateId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. User specified ID for the notebook runtime template.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate),[CreateNotebookRuntimeTemplateOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookRuntimeTemplateOperationMetadata)>` |   
  
### createNotebookRuntimeTemplateCallable()
    
    
    public final UnaryCallable<CreateNotebookRuntimeTemplateRequest,Operation> createNotebookRuntimeTemplateCallable()

Creates a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       CreateNotebookRuntimeTemplateRequest request =
           CreateNotebookRuntimeTemplateRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookRuntimeTemplate(NotebookRuntimeTemplate.newBuilder().build())
               .setNotebookRuntimeTemplateId("notebookRuntimeTemplateId-633369454")
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.createNotebookRuntimeTemplateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookRuntimeTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNotebookRuntimeTemplateOperationCallable()
    
    
    public final OperationCallable<CreateNotebookRuntimeTemplateRequest,NotebookRuntimeTemplate,CreateNotebookRuntimeTemplateOperationMetadata> createNotebookRuntimeTemplateOperationCallable()

Creates a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       CreateNotebookRuntimeTemplateRequest request =
           CreateNotebookRuntimeTemplateRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNotebookRuntimeTemplate(NotebookRuntimeTemplate.newBuilder().build())
               .setNotebookRuntimeTemplateId("notebookRuntimeTemplateId-633369454")
               .build();
       OperationFuture<NotebookRuntimeTemplate, CreateNotebookRuntimeTemplateOperationMetadata>
           future =
               notebookServiceClient
                   .createNotebookRuntimeTemplateOperationCallable()
                   .futureCall(request);
       // Do something.
       NotebookRuntimeTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookRuntimeTemplateRequest),[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate),[CreateNotebookRuntimeTemplateOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookRuntimeTemplateOperationMetadata)>` |   
  
### deleteNotebookExecutionJobAsync(@Nullable NotebookExecutionJobName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookExecutionJobAsync(@Nullable NotebookExecutionJobName name)

Deletes a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookExecutionJobName name =
           NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]");
       notebookServiceClient.deleteNotebookExecutionJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookExecutionJobName`  
Required. The name of the NotebookExecutionJob resource to be deleted.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookExecutionJobAsync(DeleteNotebookExecutionJobRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookExecutionJobAsync(DeleteNotebookExecutionJobRequest request)

Deletes a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookExecutionJobRequest request =
           DeleteNotebookExecutionJobRequest.newBuilder()
               .setName(
                   NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]")
                       .toString())
               .build();
       notebookServiceClient.deleteNotebookExecutionJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookExecutionJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookExecutionJobAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookExecutionJobAsync(String name)

Deletes a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]")
               .toString();
       notebookServiceClient.deleteNotebookExecutionJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookExecutionJob resource to be deleted.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookExecutionJobCallable()
    
    
    public final UnaryCallable<DeleteNotebookExecutionJobRequest,Operation> deleteNotebookExecutionJobCallable()

Deletes a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookExecutionJobRequest request =
           DeleteNotebookExecutionJobRequest.newBuilder()
               .setName(
                   NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.deleteNotebookExecutionJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookExecutionJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNotebookExecutionJobOperationCallable()
    
    
    public final OperationCallable<DeleteNotebookExecutionJobRequest,Empty,DeleteOperationMetadata> deleteNotebookExecutionJobOperationCallable()

Deletes a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookExecutionJobRequest request =
           DeleteNotebookExecutionJobRequest.newBuilder()
               .setName(
                   NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           notebookServiceClient.deleteNotebookExecutionJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookExecutionJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookRuntimeAsync(@Nullable NotebookRuntimeName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookRuntimeAsync(@Nullable NotebookRuntimeName name)

Deletes a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeName name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]");
       notebookServiceClient.deleteNotebookRuntimeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeName`  
Required. The name of the NotebookRuntime resource to be deleted. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookRuntimeAsync(DeleteNotebookRuntimeRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookRuntimeAsync(DeleteNotebookRuntimeRequest request)

Deletes a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookRuntimeRequest request =
           DeleteNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       notebookServiceClient.deleteNotebookRuntimeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookRuntimeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookRuntimeAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookRuntimeAsync(String name)

Deletes a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]").toString();
       notebookServiceClient.deleteNotebookRuntimeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookRuntime resource to be deleted. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookRuntimeCallable()
    
    
    public final UnaryCallable<DeleteNotebookRuntimeRequest,Operation> deleteNotebookRuntimeCallable()

Deletes a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookRuntimeRequest request =
           DeleteNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.deleteNotebookRuntimeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNotebookRuntimeOperationCallable()
    
    
    public final OperationCallable<DeleteNotebookRuntimeRequest,Empty,DeleteOperationMetadata> deleteNotebookRuntimeOperationCallable()

Deletes a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookRuntimeRequest request =
           DeleteNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           notebookServiceClient.deleteNotebookRuntimeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookRuntimeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookRuntimeTemplateAsync(@Nullable NotebookRuntimeTemplateName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookRuntimeTemplateAsync(@Nullable NotebookRuntimeTemplateName name)

Deletes a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeTemplateName name =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]");
       notebookServiceClient.deleteNotebookRuntimeTemplateAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeTemplateName`  
Required. The name of the NotebookRuntimeTemplate resource to be deleted. Format: `projects/{project}/locations/{location}/notebookRuntimeTemplates/{notebook_runtime_template}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookRuntimeTemplateAsync(DeleteNotebookRuntimeTemplateRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookRuntimeTemplateAsync(DeleteNotebookRuntimeTemplateRequest request)

Deletes a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookRuntimeTemplateRequest request =
           DeleteNotebookRuntimeTemplateRequest.newBuilder()
               .setName(
                   NotebookRuntimeTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
                       .toString())
               .build();
       notebookServiceClient.deleteNotebookRuntimeTemplateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookRuntimeTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookRuntimeTemplateAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNotebookRuntimeTemplateAsync(String name)

Deletes a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
               .toString();
       notebookServiceClient.deleteNotebookRuntimeTemplateAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookRuntimeTemplate resource to be deleted. Format: `projects/{project}/locations/{location}/notebookRuntimeTemplates/{notebook_runtime_template}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNotebookRuntimeTemplateCallable()
    
    
    public final UnaryCallable<DeleteNotebookRuntimeTemplateRequest,Operation> deleteNotebookRuntimeTemplateCallable()

Deletes a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookRuntimeTemplateRequest request =
           DeleteNotebookRuntimeTemplateRequest.newBuilder()
               .setName(
                   NotebookRuntimeTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.deleteNotebookRuntimeTemplateCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookRuntimeTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNotebookRuntimeTemplateOperationCallable()
    
    
    public final OperationCallable<DeleteNotebookRuntimeTemplateRequest,Empty,DeleteOperationMetadata> deleteNotebookRuntimeTemplateOperationCallable()

Deletes a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       DeleteNotebookRuntimeTemplateRequest request =
           DeleteNotebookRuntimeTemplateRequest.newBuilder()
               .setName(
                   NotebookRuntimeTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           notebookServiceClient
               .deleteNotebookRuntimeTemplateOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookRuntimeTemplateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = notebookServiceClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = notebookServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = notebookServiceClient.getLocation(request);
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
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = notebookServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getNotebookExecutionJob(@Nullable NotebookExecutionJobName name)
    
    
    public final NotebookExecutionJob getNotebookExecutionJob(@Nullable NotebookExecutionJobName name)

Gets a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookExecutionJobName name =
           NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]");
       NotebookExecutionJob response = notebookServiceClient.getNotebookExecutionJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookExecutionJobName`  
Required. The name of the NotebookExecutionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob)` |   
  
### getNotebookExecutionJob(GetNotebookExecutionJobRequest request)
    
    
    public final NotebookExecutionJob getNotebookExecutionJob(GetNotebookExecutionJobRequest request)

Gets a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetNotebookExecutionJobRequest request =
           GetNotebookExecutionJobRequest.newBuilder()
               .setName(
                   NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]")
                       .toString())
               .setView(NotebookExecutionJobView.forNumber(0))
               .build();
       NotebookExecutionJob response = notebookServiceClient.getNotebookExecutionJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookExecutionJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob)` |   
  
### getNotebookExecutionJob(String name)
    
    
    public final NotebookExecutionJob getNotebookExecutionJob(String name)

Gets a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]")
               .toString();
       NotebookExecutionJob response = notebookServiceClient.getNotebookExecutionJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookExecutionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob)` |   
  
### getNotebookExecutionJobCallable()
    
    
    public final UnaryCallable<GetNotebookExecutionJobRequest,NotebookExecutionJob> getNotebookExecutionJobCallable()

Gets a NotebookExecutionJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetNotebookExecutionJobRequest request =
           GetNotebookExecutionJobRequest.newBuilder()
               .setName(
                   NotebookExecutionJobName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_EXECUTION_JOB]")
                       .toString())
               .setView(NotebookExecutionJobView.forNumber(0))
               .build();
       ApiFuture<NotebookExecutionJob> future =
           notebookServiceClient.getNotebookExecutionJobCallable().futureCall(request);
       // Do something.
       NotebookExecutionJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookExecutionJobRequest),[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob)>` |   
  
### getNotebookRuntime(@Nullable NotebookRuntimeName name)
    
    
    public final NotebookRuntime getNotebookRuntime(@Nullable NotebookRuntimeName name)

Gets a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeName name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]");
       NotebookRuntime response = notebookServiceClient.getNotebookRuntime(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeName`  
Required. The name of the NotebookRuntime resource. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)` |   
  
### getNotebookRuntime(GetNotebookRuntimeRequest request)
    
    
    public final NotebookRuntime getNotebookRuntime(GetNotebookRuntimeRequest request)

Gets a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetNotebookRuntimeRequest request =
           GetNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       NotebookRuntime response = notebookServiceClient.getNotebookRuntime(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookRuntimeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)` |   
  
### getNotebookRuntime(String name)
    
    
    public final NotebookRuntime getNotebookRuntime(String name)

Gets a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]").toString();
       NotebookRuntime response = notebookServiceClient.getNotebookRuntime(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookRuntime resource. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)` |   
  
### getNotebookRuntimeCallable()
    
    
    public final UnaryCallable<GetNotebookRuntimeRequest,NotebookRuntime> getNotebookRuntimeCallable()

Gets a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetNotebookRuntimeRequest request =
           GetNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       ApiFuture<NotebookRuntime> future =
           notebookServiceClient.getNotebookRuntimeCallable().futureCall(request);
       // Do something.
       NotebookRuntime response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookRuntimeRequest),[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)>` |   
  
### getNotebookRuntimeTemplate(@Nullable NotebookRuntimeTemplateName name)
    
    
    public final NotebookRuntimeTemplate getNotebookRuntimeTemplate(@Nullable NotebookRuntimeTemplateName name)

Gets a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeTemplateName name =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]");
       NotebookRuntimeTemplate response = notebookServiceClient.getNotebookRuntimeTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeTemplateName`  
Required. The name of the NotebookRuntimeTemplate resource. Format: `projects/{project}/locations/{location}/notebookRuntimeTemplates/{notebook_runtime_template}`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)` |   
  
### getNotebookRuntimeTemplate(GetNotebookRuntimeTemplateRequest request)
    
    
    public final NotebookRuntimeTemplate getNotebookRuntimeTemplate(GetNotebookRuntimeTemplateRequest request)

Gets a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetNotebookRuntimeTemplateRequest request =
           GetNotebookRuntimeTemplateRequest.newBuilder()
               .setName(
                   NotebookRuntimeTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
                       .toString())
               .build();
       NotebookRuntimeTemplate response = notebookServiceClient.getNotebookRuntimeTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookRuntimeTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)` |   
  
### getNotebookRuntimeTemplate(String name)
    
    
    public final NotebookRuntimeTemplate getNotebookRuntimeTemplate(String name)

Gets a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookRuntimeTemplateName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
               .toString();
       NotebookRuntimeTemplate response = notebookServiceClient.getNotebookRuntimeTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookRuntimeTemplate resource. Format: `projects/{project}/locations/{location}/notebookRuntimeTemplates/{notebook_runtime_template}`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)` |   
  
### getNotebookRuntimeTemplateCallable()
    
    
    public final UnaryCallable<GetNotebookRuntimeTemplateRequest,NotebookRuntimeTemplate> getNotebookRuntimeTemplateCallable()

Gets a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       GetNotebookRuntimeTemplateRequest request =
           GetNotebookRuntimeTemplateRequest.newBuilder()
               .setName(
                   NotebookRuntimeTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME_TEMPLATE]")
                       .toString())
               .build();
       ApiFuture<NotebookRuntimeTemplate> future =
           notebookServiceClient.getNotebookRuntimeTemplateCallable().futureCall(request);
       // Do something.
       NotebookRuntimeTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookRuntimeTemplateRequest),[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable NotebookServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookServiceSettings` |   
  
### getStub()
    
    
    public NotebookServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.NotebookServiceStub)` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final NotebookServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : notebookServiceClient.listLocations(request).iterateAll()) {
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
`[NotebookServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             notebookServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,NotebookServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           notebookServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListLocationsPagedResponse)>` |   
  
### listNotebookExecutionJobs(@Nullable LocationName parent)
    
    
    public final NotebookServiceClient.ListNotebookExecutionJobsPagedResponse listNotebookExecutionJobs(@Nullable LocationName parent)

Lists NotebookExecutionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (NotebookExecutionJob element :
           notebookServiceClient.listNotebookExecutionJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to list the NotebookExecutionJobs. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookExecutionJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookExecutionJobsPagedResponse)` |   
  
### listNotebookExecutionJobs(ListNotebookExecutionJobsRequest request)
    
    
    public final NotebookServiceClient.ListNotebookExecutionJobsPagedResponse listNotebookExecutionJobs(ListNotebookExecutionJobsRequest request)

Lists NotebookExecutionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookExecutionJobsRequest request =
           ListNotebookExecutionJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setView(NotebookExecutionJobView.forNumber(0))
               .build();
       for (NotebookExecutionJob element :
           notebookServiceClient.listNotebookExecutionJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotebookExecutionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookExecutionJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookExecutionJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookExecutionJobsPagedResponse)` |   
  
### listNotebookExecutionJobs(String parent)
    
    
    public final NotebookServiceClient.ListNotebookExecutionJobsPagedResponse listNotebookExecutionJobs(String parent)

Lists NotebookExecutionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (NotebookExecutionJob element :
           notebookServiceClient.listNotebookExecutionJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to list the NotebookExecutionJobs. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookExecutionJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookExecutionJobsPagedResponse)` |   
  
### listNotebookExecutionJobsCallable()
    
    
    public final UnaryCallable<ListNotebookExecutionJobsRequest,ListNotebookExecutionJobsResponse> listNotebookExecutionJobsCallable()

Lists NotebookExecutionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookExecutionJobsRequest request =
           ListNotebookExecutionJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setView(NotebookExecutionJobView.forNumber(0))
               .build();
       while (true) {
         ListNotebookExecutionJobsResponse response =
             notebookServiceClient.listNotebookExecutionJobsCallable().call(request);
         for (NotebookExecutionJob element : response.getNotebookExecutionJobsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNotebookExecutionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookExecutionJobsRequest),[ListNotebookExecutionJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookExecutionJobsResponse)>` |   
  
### listNotebookExecutionJobsPagedCallable()
    
    
    public final UnaryCallable<ListNotebookExecutionJobsRequest,NotebookServiceClient.ListNotebookExecutionJobsPagedResponse> listNotebookExecutionJobsPagedCallable()

Lists NotebookExecutionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookExecutionJobsRequest request =
           ListNotebookExecutionJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setView(NotebookExecutionJobView.forNumber(0))
               .build();
       ApiFuture<NotebookExecutionJob> future =
           notebookServiceClient.listNotebookExecutionJobsPagedCallable().futureCall(request);
       // Do something.
       for (NotebookExecutionJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNotebookExecutionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookExecutionJobsRequest),[ListNotebookExecutionJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookExecutionJobsPagedResponse)>` |   
  
### listNotebookRuntimeTemplates(@Nullable LocationName parent)
    
    
    public final NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse listNotebookRuntimeTemplates(@Nullable LocationName parent)

Lists NotebookRuntimeTemplates in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (NotebookRuntimeTemplate element :
           notebookServiceClient.listNotebookRuntimeTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to list the NotebookRuntimeTemplates. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse)` |   
  
### listNotebookRuntimeTemplates(ListNotebookRuntimeTemplatesRequest request)
    
    
    public final NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse listNotebookRuntimeTemplates(ListNotebookRuntimeTemplatesRequest request)

Lists NotebookRuntimeTemplates in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookRuntimeTemplatesRequest request =
           ListNotebookRuntimeTemplatesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (NotebookRuntimeTemplate element :
           notebookServiceClient.listNotebookRuntimeTemplates(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotebookRuntimeTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimeTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse)` |   
  
### listNotebookRuntimeTemplates(String parent)
    
    
    public final NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse listNotebookRuntimeTemplates(String parent)

Lists NotebookRuntimeTemplates in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (NotebookRuntimeTemplate element :
           notebookServiceClient.listNotebookRuntimeTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to list the NotebookRuntimeTemplates. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse)` |   
  
### listNotebookRuntimeTemplatesCallable()
    
    
    public final UnaryCallable<ListNotebookRuntimeTemplatesRequest,ListNotebookRuntimeTemplatesResponse> listNotebookRuntimeTemplatesCallable()

Lists NotebookRuntimeTemplates in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookRuntimeTemplatesRequest request =
           ListNotebookRuntimeTemplatesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListNotebookRuntimeTemplatesResponse response =
             notebookServiceClient.listNotebookRuntimeTemplatesCallable().call(request);
         for (NotebookRuntimeTemplate element : response.getNotebookRuntimeTemplatesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNotebookRuntimeTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimeTemplatesRequest),[ListNotebookRuntimeTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimeTemplatesResponse)>` |   
  
### listNotebookRuntimeTemplatesPagedCallable()
    
    
    public final UnaryCallable<ListNotebookRuntimeTemplatesRequest,NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse> listNotebookRuntimeTemplatesPagedCallable()

Lists NotebookRuntimeTemplates in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookRuntimeTemplatesRequest request =
           ListNotebookRuntimeTemplatesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<NotebookRuntimeTemplate> future =
           notebookServiceClient.listNotebookRuntimeTemplatesPagedCallable().futureCall(request);
       // Do something.
       for (NotebookRuntimeTemplate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNotebookRuntimeTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimeTemplatesRequest),[ListNotebookRuntimeTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookRuntimeTemplatesPagedResponse)>` |   
  
### listNotebookRuntimes(@Nullable LocationName parent)
    
    
    public final NotebookServiceClient.ListNotebookRuntimesPagedResponse listNotebookRuntimes(@Nullable LocationName parent)

Lists NotebookRuntimes in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (NotebookRuntime element :
           notebookServiceClient.listNotebookRuntimes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to list the NotebookRuntimes. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookRuntimesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookRuntimesPagedResponse)` |   
  
### listNotebookRuntimes(ListNotebookRuntimesRequest request)
    
    
    public final NotebookServiceClient.ListNotebookRuntimesPagedResponse listNotebookRuntimes(ListNotebookRuntimesRequest request)

Lists NotebookRuntimes in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookRuntimesRequest request =
           ListNotebookRuntimesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (NotebookRuntime element :
           notebookServiceClient.listNotebookRuntimes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotebookRuntimesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookRuntimesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookRuntimesPagedResponse)` |   
  
### listNotebookRuntimes(String parent)
    
    
    public final NotebookServiceClient.ListNotebookRuntimesPagedResponse listNotebookRuntimes(String parent)

Lists NotebookRuntimes in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (NotebookRuntime element :
           notebookServiceClient.listNotebookRuntimes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to list the NotebookRuntimes. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceClient.ListNotebookRuntimesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookRuntimesPagedResponse)` |   
  
### listNotebookRuntimesCallable()
    
    
    public final UnaryCallable<ListNotebookRuntimesRequest,ListNotebookRuntimesResponse> listNotebookRuntimesCallable()

Lists NotebookRuntimes in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookRuntimesRequest request =
           ListNotebookRuntimesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListNotebookRuntimesResponse response =
             notebookServiceClient.listNotebookRuntimesCallable().call(request);
         for (NotebookRuntime element : response.getNotebookRuntimesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNotebookRuntimesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimesRequest),[ListNotebookRuntimesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimesResponse)>` |   
  
### listNotebookRuntimesPagedCallable()
    
    
    public final UnaryCallable<ListNotebookRuntimesRequest,NotebookServiceClient.ListNotebookRuntimesPagedResponse> listNotebookRuntimesPagedCallable()

Lists NotebookRuntimes in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       ListNotebookRuntimesRequest request =
           ListNotebookRuntimesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<NotebookRuntime> future =
           notebookServiceClient.listNotebookRuntimesPagedCallable().futureCall(request);
       // Do something.
       for (NotebookRuntime element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNotebookRuntimesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimesRequest),[ListNotebookRuntimesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceClient.ListNotebookRuntimesPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = notebookServiceClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = notebookServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startNotebookRuntimeAsync(@Nullable NotebookRuntimeName name)
    
    
    public final OperationFuture<StartNotebookRuntimeResponse,StartNotebookRuntimeOperationMetadata> startNotebookRuntimeAsync(@Nullable NotebookRuntimeName name)

Starts a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeName name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]");
       StartNotebookRuntimeResponse response =
           notebookServiceClient.startNotebookRuntimeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeName`  
Required. The name of the NotebookRuntime resource to be started. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[StartNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeResponse),[StartNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeOperationMetadata)>` |   
  
### startNotebookRuntimeAsync(StartNotebookRuntimeRequest request)
    
    
    public final OperationFuture<StartNotebookRuntimeResponse,StartNotebookRuntimeOperationMetadata> startNotebookRuntimeAsync(StartNotebookRuntimeRequest request)

Starts a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       StartNotebookRuntimeRequest request =
           StartNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       StartNotebookRuntimeResponse response =
           notebookServiceClient.startNotebookRuntimeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[StartNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeResponse),[StartNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeOperationMetadata)>` |   
  
### startNotebookRuntimeAsync(String name)
    
    
    public final OperationFuture<StartNotebookRuntimeResponse,StartNotebookRuntimeOperationMetadata> startNotebookRuntimeAsync(String name)

Starts a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]").toString();
       StartNotebookRuntimeResponse response =
           notebookServiceClient.startNotebookRuntimeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookRuntime resource to be started. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[StartNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeResponse),[StartNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeOperationMetadata)>` |   
  
### startNotebookRuntimeCallable()
    
    
    public final UnaryCallable<StartNotebookRuntimeRequest,Operation> startNotebookRuntimeCallable()

Starts a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       StartNotebookRuntimeRequest request =
           StartNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.startNotebookRuntimeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startNotebookRuntimeOperationCallable()
    
    
    public final OperationCallable<StartNotebookRuntimeRequest,StartNotebookRuntimeResponse,StartNotebookRuntimeOperationMetadata> startNotebookRuntimeOperationCallable()

Starts a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       StartNotebookRuntimeRequest request =
           StartNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       OperationFuture<StartNotebookRuntimeResponse, StartNotebookRuntimeOperationMetadata> future =
           notebookServiceClient.startNotebookRuntimeOperationCallable().futureCall(request);
       // Do something.
       StartNotebookRuntimeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeRequest),[StartNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeResponse),[StartNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeOperationMetadata)>` |   
  
### stopNotebookRuntimeAsync(@Nullable NotebookRuntimeName name)
    
    
    public final OperationFuture<StopNotebookRuntimeResponse,StopNotebookRuntimeOperationMetadata> stopNotebookRuntimeAsync(@Nullable NotebookRuntimeName name)

Stops a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeName name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]");
       StopNotebookRuntimeResponse response =
           notebookServiceClient.stopNotebookRuntimeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeName`  
Required. The name of the NotebookRuntime resource to be stopped. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[StopNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeResponse),[StopNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeOperationMetadata)>` |   
  
### stopNotebookRuntimeAsync(StopNotebookRuntimeRequest request)
    
    
    public final OperationFuture<StopNotebookRuntimeResponse,StopNotebookRuntimeOperationMetadata> stopNotebookRuntimeAsync(StopNotebookRuntimeRequest request)

Stops a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       StopNotebookRuntimeRequest request =
           StopNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       StopNotebookRuntimeResponse response =
           notebookServiceClient.stopNotebookRuntimeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[StopNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeResponse),[StopNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeOperationMetadata)>` |   
  
### stopNotebookRuntimeAsync(String name)
    
    
    public final OperationFuture<StopNotebookRuntimeResponse,StopNotebookRuntimeOperationMetadata> stopNotebookRuntimeAsync(String name)

Stops a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]").toString();
       StopNotebookRuntimeResponse response =
           notebookServiceClient.stopNotebookRuntimeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookRuntime resource to be stopped. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[StopNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeResponse),[StopNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeOperationMetadata)>` |   
  
### stopNotebookRuntimeCallable()
    
    
    public final UnaryCallable<StopNotebookRuntimeRequest,Operation> stopNotebookRuntimeCallable()

Stops a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       StopNotebookRuntimeRequest request =
           StopNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.stopNotebookRuntimeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopNotebookRuntimeOperationCallable()
    
    
    public final OperationCallable<StopNotebookRuntimeRequest,StopNotebookRuntimeResponse,StopNotebookRuntimeOperationMetadata> stopNotebookRuntimeOperationCallable()

Stops a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       StopNotebookRuntimeRequest request =
           StopNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       OperationFuture<StopNotebookRuntimeResponse, StopNotebookRuntimeOperationMetadata> future =
           notebookServiceClient.stopNotebookRuntimeOperationCallable().futureCall(request);
       // Do something.
       StopNotebookRuntimeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeRequest),[StopNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeResponse),[StopNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeOperationMetadata)>` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = notebookServiceClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           notebookServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateNotebookRuntimeTemplate(NotebookRuntimeTemplate notebookRuntimeTemplate, FieldMask updateMask)
    
    
    public final NotebookRuntimeTemplate updateNotebookRuntimeTemplate(NotebookRuntimeTemplate notebookRuntimeTemplate, FieldMask updateMask)

Updates a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeTemplate notebookRuntimeTemplate =
           NotebookRuntimeTemplate.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       NotebookRuntimeTemplate response =
           notebookServiceClient.updateNotebookRuntimeTemplate(notebookRuntimeTemplate, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`notebookRuntimeTemplate` | `[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)`  
Required. The NotebookRuntimeTemplate to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. For the `FieldMask` definition, see google.protobuf.FieldMask. Input format: `{paths: "${updated_filed}"}` Updatable fields: * `encryption_spec.kms_key_name`  
**Returns**  
---  
**Type** | **Description**  
`[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)` |   
  
### updateNotebookRuntimeTemplate(UpdateNotebookRuntimeTemplateRequest request)
    
    
    public final NotebookRuntimeTemplate updateNotebookRuntimeTemplate(UpdateNotebookRuntimeTemplateRequest request)

Updates a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       UpdateNotebookRuntimeTemplateRequest request =
           UpdateNotebookRuntimeTemplateRequest.newBuilder()
               .setNotebookRuntimeTemplate(NotebookRuntimeTemplate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       NotebookRuntimeTemplate response =
           notebookServiceClient.updateNotebookRuntimeTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateNotebookRuntimeTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)` |   
  
### updateNotebookRuntimeTemplateCallable()
    
    
    public final UnaryCallable<UpdateNotebookRuntimeTemplateRequest,NotebookRuntimeTemplate> updateNotebookRuntimeTemplateCallable()

Updates a NotebookRuntimeTemplate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       UpdateNotebookRuntimeTemplateRequest request =
           UpdateNotebookRuntimeTemplateRequest.newBuilder()
               .setNotebookRuntimeTemplate(NotebookRuntimeTemplate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<NotebookRuntimeTemplate> future =
           notebookServiceClient.updateNotebookRuntimeTemplateCallable().futureCall(request);
       // Do something.
       NotebookRuntimeTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateNotebookRuntimeTemplateRequest),[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)>` |   
  
### upgradeNotebookRuntimeAsync(@Nullable NotebookRuntimeName name)
    
    
    public final OperationFuture<UpgradeNotebookRuntimeResponse,UpgradeNotebookRuntimeOperationMetadata> upgradeNotebookRuntimeAsync(@Nullable NotebookRuntimeName name)

Upgrades a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       NotebookRuntimeName name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]");
       UpgradeNotebookRuntimeResponse response =
           notebookServiceClient.upgradeNotebookRuntimeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NotebookRuntimeName`  
Required. The name of the NotebookRuntime resource to be upgrade. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpgradeNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeResponse),[UpgradeNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeOperationMetadata)>` |   
  
### upgradeNotebookRuntimeAsync(UpgradeNotebookRuntimeRequest request)
    
    
    public final OperationFuture<UpgradeNotebookRuntimeResponse,UpgradeNotebookRuntimeOperationMetadata> upgradeNotebookRuntimeAsync(UpgradeNotebookRuntimeRequest request)

Upgrades a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       UpgradeNotebookRuntimeRequest request =
           UpgradeNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       UpgradeNotebookRuntimeResponse response =
           notebookServiceClient.upgradeNotebookRuntimeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpgradeNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpgradeNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeResponse),[UpgradeNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeOperationMetadata)>` |   
  
### upgradeNotebookRuntimeAsync(String name)
    
    
    public final OperationFuture<UpgradeNotebookRuntimeResponse,UpgradeNotebookRuntimeOperationMetadata> upgradeNotebookRuntimeAsync(String name)

Upgrades a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       String name =
           NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]").toString();
       UpgradeNotebookRuntimeResponse response =
           notebookServiceClient.upgradeNotebookRuntimeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NotebookRuntime resource to be upgrade. Instead of checking whether the name is in valid NotebookRuntime resource name format, directly throw NotFound exception if there is no such NotebookRuntime in spanner.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UpgradeNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeResponse),[UpgradeNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeOperationMetadata)>` |   
  
### upgradeNotebookRuntimeCallable()
    
    
    public final UnaryCallable<UpgradeNotebookRuntimeRequest,Operation> upgradeNotebookRuntimeCallable()

Upgrades a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       UpgradeNotebookRuntimeRequest request =
           UpgradeNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           notebookServiceClient.upgradeNotebookRuntimeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpgradeNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### upgradeNotebookRuntimeOperationCallable()
    
    
    public final OperationCallable<UpgradeNotebookRuntimeRequest,UpgradeNotebookRuntimeResponse,UpgradeNotebookRuntimeOperationMetadata> upgradeNotebookRuntimeOperationCallable()

Upgrades a NotebookRuntime.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NotebookServiceClient notebookServiceClient = NotebookServiceClient.create()) {
       UpgradeNotebookRuntimeRequest request =
           UpgradeNotebookRuntimeRequest.newBuilder()
               .setName(
                   NotebookRuntimeName.of("[PROJECT]", "[LOCATION]", "[NOTEBOOK_RUNTIME]")
                       .toString())
               .build();
       OperationFuture<UpgradeNotebookRuntimeResponse, UpgradeNotebookRuntimeOperationMetadata>
           future =
               notebookServiceClient.upgradeNotebookRuntimeOperationCallable().futureCall(request);
       // Do something.
       UpgradeNotebookRuntimeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpgradeNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeRequest),[UpgradeNotebookRuntimeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeResponse),[UpgradeNotebookRuntimeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
