---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient
title: Class WorkflowTemplateServiceClient (4.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:20.324465+00:00
---

# Class WorkflowTemplateServiceClient (4.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WorkflowTemplateServiceClient (4.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.96.0 (latest)  4.92.0  4.91.1  4.90.0  4.88.0  4.85.0  4.84.0  4.82.0  4.80.0  4.79.0  4.78.0  4.77.0  4.75.0  4.73.0  4.72.0  4.71.0  4.70.0  4.69.0  4.67.0  4.65.0  4.64.0  4.61.0  4.60.0  4.59.0  4.57.0  4.56.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.46.0  4.45.0  4.44.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.34.0  4.33.0  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.8  3.1.2  3.0.3  2.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataproc/google-cloud-dataproc/src/main/java/com/google/cloud/dataproc/v1/WorkflowTemplateServiceClient.java)| [Product Reference](https://cloud.google.com/dataproc)| [REST Documentation](https://cloud.google.com/dataproc/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataproc/docs/reference/rpc)  
---|---|---|---  
  
Service Description: The API interface for managing Workflow Templates in the Dataproc API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       WorkflowTemplate template = WorkflowTemplate.newBuilder().build();
       WorkflowTemplate response =
           workflowTemplateServiceClient.createWorkflowTemplate(parent, template);
     }
     

Note: close() needs to be called on the WorkflowTemplateServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateWorkflowTemplate |  Creates new workflow template. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWorkflowTemplate(CreateWorkflowTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createWorkflowTemplate(LocationName parent, WorkflowTemplate template) 
  * createWorkflowTemplate(RegionName parent, WorkflowTemplate template) 
  * createWorkflowTemplate(String parent, WorkflowTemplate template) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWorkflowTemplateCallable() 

  
GetWorkflowTemplate |  Retrieves the latest workflow template.  Can retrieve previously instantiated template by specifying optional version parameter. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWorkflowTemplate(GetWorkflowTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWorkflowTemplate(WorkflowTemplateName name) 
  * getWorkflowTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWorkflowTemplateCallable() 

  
InstantiateWorkflowTemplate |  Instantiates a template and begins execution.  The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.  The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.  The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).  On successful completion, Operation.response will be Empty. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * instantiateWorkflowTemplateAsync(InstantiateWorkflowTemplateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * instantiateWorkflowTemplateAsync(WorkflowTemplateName name) 
  * instantiateWorkflowTemplateAsync(String name) 
  * instantiateWorkflowTemplateAsync(WorkflowTemplateName name, Map<String, String> parameters) 
  * instantiateWorkflowTemplateAsync(String name, Map<String, String> parameters) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * instantiateWorkflowTemplateOperationCallable() 
  * instantiateWorkflowTemplateCallable() 

  
InstantiateInlineWorkflowTemplate |  Instantiates a template and begins execution.  This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.  The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.  The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.  The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).  On successful completion, Operation.response will be Empty. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * instantiateInlineWorkflowTemplateAsync(InstantiateInlineWorkflowTemplateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * instantiateInlineWorkflowTemplateAsync(LocationName parent, WorkflowTemplate template) 
  * instantiateInlineWorkflowTemplateAsync(RegionName parent, WorkflowTemplate template) 
  * instantiateInlineWorkflowTemplateAsync(String parent, WorkflowTemplate template) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * instantiateInlineWorkflowTemplateOperationCallable() 
  * instantiateInlineWorkflowTemplateCallable() 

  
UpdateWorkflowTemplate |  Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateWorkflowTemplate(UpdateWorkflowTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateWorkflowTemplate(WorkflowTemplate template) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateWorkflowTemplateCallable() 

  
ListWorkflowTemplates |  Lists workflows that match the specified filter in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWorkflowTemplates(ListWorkflowTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWorkflowTemplates(LocationName parent) 
  * listWorkflowTemplates(RegionName parent) 
  * listWorkflowTemplates(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWorkflowTemplatesPagedCallable() 
  * listWorkflowTemplatesCallable() 

  
DeleteWorkflowTemplate |  Deletes a workflow template. It does not cancel in-progress workflows. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteWorkflowTemplate(DeleteWorkflowTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteWorkflowTemplate(WorkflowTemplateName name) 
  * deleteWorkflowTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteWorkflowTemplateCallable() 

  
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

This class can be customized by passing in a custom instance of WorkflowTemplateServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     WorkflowTemplateServiceSettings workflowTemplateServiceSettings =
         WorkflowTemplateServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create(workflowTemplateServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     WorkflowTemplateServiceSettings workflowTemplateServiceSettings =
         WorkflowTemplateServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create(workflowTemplateServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     WorkflowTemplateServiceSettings workflowTemplateServiceSettings =
         WorkflowTemplateServiceSettings.newHttpJsonBuilder().build();
     WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create(workflowTemplateServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > WorkflowTemplateServiceClient

## Static Methods 

### create()
    
    
    public static final WorkflowTemplateServiceClient create()

Constructs an instance of WorkflowTemplateServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(WorkflowTemplateServiceSettings settings)
    
    
    public static final WorkflowTemplateServiceClient create(WorkflowTemplateServiceSettings settings)

Constructs an instance of WorkflowTemplateServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[WorkflowTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(WorkflowTemplateServiceStub stub)
    
    
    public static final WorkflowTemplateServiceClient create(WorkflowTemplateServiceStub stub)

Constructs an instance of WorkflowTemplateServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(WorkflowTemplateServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[WorkflowTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.stub.WorkflowTemplateServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient)` |   
  
## Constructors 

### WorkflowTemplateServiceClient(WorkflowTemplateServiceSettings settings)
    
    
    protected WorkflowTemplateServiceClient(WorkflowTemplateServiceSettings settings)

Constructs an instance of WorkflowTemplateServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[WorkflowTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceSettings)`  
  
  
### WorkflowTemplateServiceClient(WorkflowTemplateServiceStub stub)
    
    
    protected WorkflowTemplateServiceClient(WorkflowTemplateServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[WorkflowTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.stub.WorkflowTemplateServiceStub)`  
  
  
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

### createWorkflowTemplate(@Nullable LocationName parent, WorkflowTemplate template)
    
    
    public final WorkflowTemplate createWorkflowTemplate(@Nullable LocationName parent, WorkflowTemplate template)

Creates new workflow template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       WorkflowTemplate template = WorkflowTemplate.newBuilder().build();
       WorkflowTemplate response =
           workflowTemplateServiceClient.createWorkflowTemplate(parent, template);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.LocationName`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.create`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.create`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
`template` | `[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)`  
Required. The Dataproc workflow template to create.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### createWorkflowTemplate(@Nullable RegionName parent, WorkflowTemplate template)
    
    
    public final WorkflowTemplate createWorkflowTemplate(@Nullable RegionName parent, WorkflowTemplate template)

Creates new workflow template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       RegionName parent = RegionName.of("[PROJECT]", "[REGION]");
       WorkflowTemplate template = WorkflowTemplate.newBuilder().build();
       WorkflowTemplate response =
           workflowTemplateServiceClient.createWorkflowTemplate(parent, template);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.RegionName`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.create`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.create`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
`template` | `[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)`  
Required. The Dataproc workflow template to create.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### createWorkflowTemplate(CreateWorkflowTemplateRequest request)
    
    
    public final WorkflowTemplate createWorkflowTemplate(CreateWorkflowTemplateRequest request)

Creates new workflow template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       CreateWorkflowTemplateRequest request =
           CreateWorkflowTemplateRequest.newBuilder()
               .setParent(RegionName.of("[PROJECT]", "[REGION]").toString())
               .setTemplate(WorkflowTemplate.newBuilder().build())
               .build();
       WorkflowTemplate response = workflowTemplateServiceClient.createWorkflowTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.CreateWorkflowTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### createWorkflowTemplate(String parent, WorkflowTemplate template)
    
    
    public final WorkflowTemplate createWorkflowTemplate(String parent, WorkflowTemplate template)

Creates new workflow template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       String parent = RegionName.of("[PROJECT]", "[REGION]").toString();
       WorkflowTemplate template = WorkflowTemplate.newBuilder().build();
       WorkflowTemplate response =
           workflowTemplateServiceClient.createWorkflowTemplate(parent, template);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.create`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.create`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
`template` | `[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)`  
Required. The Dataproc workflow template to create.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### createWorkflowTemplateCallable()
    
    
    public final UnaryCallable<CreateWorkflowTemplateRequest,WorkflowTemplate> createWorkflowTemplateCallable()

Creates new workflow template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       CreateWorkflowTemplateRequest request =
           CreateWorkflowTemplateRequest.newBuilder()
               .setParent(RegionName.of("[PROJECT]", "[REGION]").toString())
               .setTemplate(WorkflowTemplate.newBuilder().build())
               .build();
       ApiFuture<WorkflowTemplate> future =
           workflowTemplateServiceClient.createWorkflowTemplateCallable().futureCall(request);
       // Do something.
       WorkflowTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.CreateWorkflowTemplateRequest),[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)>` |   
  
### deleteWorkflowTemplate(@Nullable WorkflowTemplateName name)
    
    
    public final void deleteWorkflowTemplate(@Nullable WorkflowTemplateName name)

Deletes a workflow template. It does not cancel in-progress workflows.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       WorkflowTemplateName name =
           WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
               "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]");
       workflowTemplateServiceClient.deleteWorkflowTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.WorkflowTemplateName`  
Required. The resource name of the workflow template, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.delete`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`


  * For `projects.locations.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`

  
  
### deleteWorkflowTemplate(DeleteWorkflowTemplateRequest request)
    
    
    public final void deleteWorkflowTemplate(DeleteWorkflowTemplateRequest request)

Deletes a workflow template. It does not cancel in-progress workflows.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       DeleteWorkflowTemplateRequest request =
           DeleteWorkflowTemplateRequest.newBuilder()
               .setName(
                   WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
                           "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]")
                       .toString())
               .setVersion(351608024)
               .build();
       workflowTemplateServiceClient.deleteWorkflowTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.DeleteWorkflowTemplateRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteWorkflowTemplate(String name)
    
    
    public final void deleteWorkflowTemplate(String name)

Deletes a workflow template. It does not cancel in-progress workflows.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       String name =
           WorkflowTemplateName.ofProjectRegionWorkflowTemplateName(
                   "[PROJECT]", "[REGION]", "[WORKFLOW_TEMPLATE]")
               .toString();
       workflowTemplateServiceClient.deleteWorkflowTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the workflow template, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.delete`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`


  * For `projects.locations.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`

  
  
### deleteWorkflowTemplateCallable()
    
    
    public final UnaryCallable<DeleteWorkflowTemplateRequest,Empty> deleteWorkflowTemplateCallable()

Deletes a workflow template. It does not cancel in-progress workflows.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       DeleteWorkflowTemplateRequest request =
           DeleteWorkflowTemplateRequest.newBuilder()
               .setName(
                   WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
                           "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]")
                       .toString())
               .setVersion(351608024)
               .build();
       ApiFuture<Empty> future =
           workflowTemplateServiceClient.deleteWorkflowTemplateCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.DeleteWorkflowTemplateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   AutoscalingPolicyName.ofProjectRegionAutoscalingPolicyName(
                           "[PROJECT]", "[REGION]", "[AUTOSCALING_POLICY]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = workflowTemplateServiceClient.getIamPolicy(request);
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
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   AutoscalingPolicyName.ofProjectRegionAutoscalingPolicyName(
                           "[PROJECT]", "[REGION]", "[AUTOSCALING_POLICY]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           workflowTemplateServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable WorkflowTemplateServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.WorkflowTemplateServiceSettings` |   
  
### getStub()
    
    
    public WorkflowTemplateServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.stub.WorkflowTemplateServiceStub)` |   
  
### getWorkflowTemplate(@Nullable WorkflowTemplateName name)
    
    
    public final WorkflowTemplate getWorkflowTemplate(@Nullable WorkflowTemplateName name)

Retrieves the latest workflow template.

Can retrieve previously instantiated template by specifying optional version parameter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       WorkflowTemplateName name =
           WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
               "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]");
       WorkflowTemplate response = workflowTemplateServiceClient.getWorkflowTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.WorkflowTemplateName`  
Required. The resource name of the workflow template, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.get`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`


  * For `projects.locations.workflowTemplates.get`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`

  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### getWorkflowTemplate(GetWorkflowTemplateRequest request)
    
    
    public final WorkflowTemplate getWorkflowTemplate(GetWorkflowTemplateRequest request)

Retrieves the latest workflow template.

Can retrieve previously instantiated template by specifying optional version parameter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       GetWorkflowTemplateRequest request =
           GetWorkflowTemplateRequest.newBuilder()
               .setName(
                   WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
                           "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]")
                       .toString())
               .setVersion(351608024)
               .build();
       WorkflowTemplate response = workflowTemplateServiceClient.getWorkflowTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GetWorkflowTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### getWorkflowTemplate(String name)
    
    
    public final WorkflowTemplate getWorkflowTemplate(String name)

Retrieves the latest workflow template.

Can retrieve previously instantiated template by specifying optional version parameter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       String name =
           WorkflowTemplateName.ofProjectRegionWorkflowTemplateName(
                   "[PROJECT]", "[REGION]", "[WORKFLOW_TEMPLATE]")
               .toString();
       WorkflowTemplate response = workflowTemplateServiceClient.getWorkflowTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the workflow template, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.get`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`


  * For `projects.locations.workflowTemplates.get`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`

  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### getWorkflowTemplateCallable()
    
    
    public final UnaryCallable<GetWorkflowTemplateRequest,WorkflowTemplate> getWorkflowTemplateCallable()

Retrieves the latest workflow template.

Can retrieve previously instantiated template by specifying optional version parameter.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       GetWorkflowTemplateRequest request =
           GetWorkflowTemplateRequest.newBuilder()
               .setName(
                   WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
                           "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]")
                       .toString())
               .setVersion(351608024)
               .build();
       ApiFuture<WorkflowTemplate> future =
           workflowTemplateServiceClient.getWorkflowTemplateCallable().futureCall(request);
       // Do something.
       WorkflowTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.GetWorkflowTemplateRequest),[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)>` |   
  
### instantiateInlineWorkflowTemplateAsync(@Nullable LocationName parent, WorkflowTemplate template)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateInlineWorkflowTemplateAsync(@Nullable LocationName parent, WorkflowTemplate template)

Instantiates a template and begins execution.

This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       WorkflowTemplate template = WorkflowTemplate.newBuilder().build();
       workflowTemplateServiceClient.instantiateInlineWorkflowTemplateAsync(parent, template).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.LocationName`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates,instantiateinline`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.instantiateinline`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
`template` | `[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)`  
Required. The workflow template to instantiate.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateInlineWorkflowTemplateAsync(@Nullable RegionName parent, WorkflowTemplate template)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateInlineWorkflowTemplateAsync(@Nullable RegionName parent, WorkflowTemplate template)

Instantiates a template and begins execution.

This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       RegionName parent = RegionName.of("[PROJECT]", "[REGION]");
       WorkflowTemplate template = WorkflowTemplate.newBuilder().build();
       workflowTemplateServiceClient.instantiateInlineWorkflowTemplateAsync(parent, template).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.RegionName`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates,instantiateinline`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.instantiateinline`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
`template` | `[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)`  
Required. The workflow template to instantiate.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateInlineWorkflowTemplateAsync(InstantiateInlineWorkflowTemplateRequest request)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateInlineWorkflowTemplateAsync(InstantiateInlineWorkflowTemplateRequest request)

Instantiates a template and begins execution.

This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       InstantiateInlineWorkflowTemplateRequest request =
           InstantiateInlineWorkflowTemplateRequest.newBuilder()
               .setParent(RegionName.of("[PROJECT]", "[REGION]").toString())
               .setTemplate(WorkflowTemplate.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       workflowTemplateServiceClient.instantiateInlineWorkflowTemplateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InstantiateInlineWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstantiateInlineWorkflowTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateInlineWorkflowTemplateAsync(String parent, WorkflowTemplate template)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateInlineWorkflowTemplateAsync(String parent, WorkflowTemplate template)

Instantiates a template and begins execution.

This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       String parent = RegionName.of("[PROJECT]", "[REGION]").toString();
       WorkflowTemplate template = WorkflowTemplate.newBuilder().build();
       workflowTemplateServiceClient.instantiateInlineWorkflowTemplateAsync(parent, template).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates,instantiateinline`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.instantiateinline`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
`template` | `[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)`  
Required. The workflow template to instantiate.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateInlineWorkflowTemplateCallable()
    
    
    public final UnaryCallable<InstantiateInlineWorkflowTemplateRequest,Operation> instantiateInlineWorkflowTemplateCallable()

Instantiates a template and begins execution.

This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       InstantiateInlineWorkflowTemplateRequest request =
           InstantiateInlineWorkflowTemplateRequest.newBuilder()
               .setParent(RegionName.of("[PROJECT]", "[REGION]").toString())
               .setTemplate(WorkflowTemplate.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           workflowTemplateServiceClient
               .instantiateInlineWorkflowTemplateCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InstantiateInlineWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstantiateInlineWorkflowTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### instantiateInlineWorkflowTemplateOperationCallable()
    
    
    public final OperationCallable<InstantiateInlineWorkflowTemplateRequest,Empty,WorkflowMetadata> instantiateInlineWorkflowTemplateOperationCallable()

Instantiates a template and begins execution.

This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       InstantiateInlineWorkflowTemplateRequest request =
           InstantiateInlineWorkflowTemplateRequest.newBuilder()
               .setParent(RegionName.of("[PROJECT]", "[REGION]").toString())
               .setTemplate(WorkflowTemplate.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, WorkflowMetadata> future =
           workflowTemplateServiceClient
               .instantiateInlineWorkflowTemplateOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InstantiateInlineWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstantiateInlineWorkflowTemplateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateWorkflowTemplateAsync(@Nullable WorkflowTemplateName name)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateWorkflowTemplateAsync(@Nullable WorkflowTemplateName name)

Instantiates a template and begins execution.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       WorkflowTemplateName name =
           WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
               "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]");
       workflowTemplateServiceClient.instantiateWorkflowTemplateAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.WorkflowTemplateName`  
Required. The resource name of the workflow template, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`


  * For `projects.locations.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateWorkflowTemplateAsync(@Nullable WorkflowTemplateName name, Map<String,String> parameters)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateWorkflowTemplateAsync(@Nullable WorkflowTemplateName name, Map<String,String> parameters)

Instantiates a template and begins execution.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       WorkflowTemplateName name =
           WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
               "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]");
       Map<String, String> parameters = new HashMap<>();
       workflowTemplateServiceClient.instantiateWorkflowTemplateAsync(name, parameters).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.WorkflowTemplateName`  
Required. The resource name of the workflow template, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`


  * For `projects.locations.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`

  
`parameters` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Optional. Map from parameter names to values that should be used for those parameters. Values may not exceed 1000 characters.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateWorkflowTemplateAsync(InstantiateWorkflowTemplateRequest request)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateWorkflowTemplateAsync(InstantiateWorkflowTemplateRequest request)

Instantiates a template and begins execution.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       InstantiateWorkflowTemplateRequest request =
           InstantiateWorkflowTemplateRequest.newBuilder()
               .setName(
                   WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
                           "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]")
                       .toString())
               .setVersion(351608024)
               .setRequestId("requestId693933066")
               .putAllParameters(new HashMap<String, String>())
               .build();
       workflowTemplateServiceClient.instantiateWorkflowTemplateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InstantiateWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstantiateWorkflowTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateWorkflowTemplateAsync(String name)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateWorkflowTemplateAsync(String name)

Instantiates a template and begins execution.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       String name =
           WorkflowTemplateName.ofProjectRegionWorkflowTemplateName(
                   "[PROJECT]", "[REGION]", "[WORKFLOW_TEMPLATE]")
               .toString();
       workflowTemplateServiceClient.instantiateWorkflowTemplateAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the workflow template, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`


  * For `projects.locations.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateWorkflowTemplateAsync(String name, Map<String,String> parameters)
    
    
    public final OperationFuture<Empty,WorkflowMetadata> instantiateWorkflowTemplateAsync(String name, Map<String,String> parameters)

Instantiates a template and begins execution.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       String name =
           WorkflowTemplateName.ofProjectRegionWorkflowTemplateName(
                   "[PROJECT]", "[REGION]", "[WORKFLOW_TEMPLATE]")
               .toString();
       Map<String, String> parameters = new HashMap<>();
       workflowTemplateServiceClient.instantiateWorkflowTemplateAsync(name, parameters).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the workflow template, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/regions/{region}/workflowTemplates/{template_id}`


  * For `projects.locations.workflowTemplates.instantiate`, the resource name of the template has the following format: `projects/{project_id}/locations/{location}/workflowTemplates/{template_id}`

  
`parameters` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Optional. Map from parameter names to values that should be used for those parameters. Values may not exceed 1000 characters.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
### instantiateWorkflowTemplateCallable()
    
    
    public final UnaryCallable<InstantiateWorkflowTemplateRequest,Operation> instantiateWorkflowTemplateCallable()

Instantiates a template and begins execution.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       InstantiateWorkflowTemplateRequest request =
           InstantiateWorkflowTemplateRequest.newBuilder()
               .setName(
                   WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
                           "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]")
                       .toString())
               .setVersion(351608024)
               .setRequestId("requestId693933066")
               .putAllParameters(new HashMap<String, String>())
               .build();
       ApiFuture<Operation> future =
           workflowTemplateServiceClient.instantiateWorkflowTemplateCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InstantiateWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstantiateWorkflowTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### instantiateWorkflowTemplateOperationCallable()
    
    
    public final OperationCallable<InstantiateWorkflowTemplateRequest,Empty,WorkflowMetadata> instantiateWorkflowTemplateOperationCallable()

Instantiates a template and begins execution.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be [WorkflowMetadata](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see [Using WorkflowMetadata](https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).

On successful completion, Operation.response will be Empty.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       InstantiateWorkflowTemplateRequest request =
           InstantiateWorkflowTemplateRequest.newBuilder()
               .setName(
                   WorkflowTemplateName.ofProjectLocationWorkflowTemplateName(
                           "[PROJECT]", "[LOCATION]", "[WORKFLOW_TEMPLATE]")
                       .toString())
               .setVersion(351608024)
               .setRequestId("requestId693933066")
               .putAllParameters(new HashMap<String, String>())
               .build();
       OperationFuture<Empty, WorkflowMetadata> future =
           workflowTemplateServiceClient
               .instantiateWorkflowTemplateOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InstantiateWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstantiateWorkflowTemplateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[WorkflowMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowMetadata)>` |   
  
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
  
### listWorkflowTemplates(@Nullable LocationName parent)
    
    
    public final WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse listWorkflowTemplates(@Nullable LocationName parent)

Lists workflows that match the specified filter in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (WorkflowTemplate element :
           workflowTemplateServiceClient.listWorkflowTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.LocationName`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates,list`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.list`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse)` |   
  
### listWorkflowTemplates(@Nullable RegionName parent)
    
    
    public final WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse listWorkflowTemplates(@Nullable RegionName parent)

Lists workflows that match the specified filter in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       RegionName parent = RegionName.of("[PROJECT]", "[REGION]");
       for (WorkflowTemplate element :
           workflowTemplateServiceClient.listWorkflowTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataproc.v1.RegionName`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates,list`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.list`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse)` |   
  
### listWorkflowTemplates(ListWorkflowTemplatesRequest request)
    
    
    public final WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse listWorkflowTemplates(ListWorkflowTemplatesRequest request)

Lists workflows that match the specified filter in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       ListWorkflowTemplatesRequest request =
           ListWorkflowTemplatesRequest.newBuilder()
               .setParent(RegionName.of("[PROJECT]", "[REGION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (WorkflowTemplate element :
           workflowTemplateServiceClient.listWorkflowTemplates(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ListWorkflowTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse)` |   
  
### listWorkflowTemplates(String parent)
    
    
    public final WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse listWorkflowTemplates(String parent)

Lists workflows that match the specified filter in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       String parent = RegionName.of("[PROJECT]", "[REGION]").toString();
       for (WorkflowTemplate element :
           workflowTemplateServiceClient.listWorkflowTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>. 

  * For `projects.regions.workflowTemplates,list`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`


  * For `projects.locations.workflowTemplates.list`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse)` |   
  
### listWorkflowTemplatesCallable()
    
    
    public final UnaryCallable<ListWorkflowTemplatesRequest,ListWorkflowTemplatesResponse> listWorkflowTemplatesCallable()

Lists workflows that match the specified filter in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       ListWorkflowTemplatesRequest request =
           ListWorkflowTemplatesRequest.newBuilder()
               .setParent(RegionName.of("[PROJECT]", "[REGION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListWorkflowTemplatesResponse response =
             workflowTemplateServiceClient.listWorkflowTemplatesCallable().call(request);
         for (WorkflowTemplate element : response.getTemplatesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkflowTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ListWorkflowTemplatesRequest),[ListWorkflowTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ListWorkflowTemplatesResponse)>` |   
  
### listWorkflowTemplatesPagedCallable()
    
    
    public final UnaryCallable<ListWorkflowTemplatesRequest,WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse> listWorkflowTemplatesPagedCallable()

Lists workflows that match the specified filter in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       ListWorkflowTemplatesRequest request =
           ListWorkflowTemplatesRequest.newBuilder()
               .setParent(RegionName.of("[PROJECT]", "[REGION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<WorkflowTemplate> future =
           workflowTemplateServiceClient.listWorkflowTemplatesPagedCallable().futureCall(request);
       // Do something.
       for (WorkflowTemplate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkflowTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ListWorkflowTemplatesRequest),[ListWorkflowTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplateServiceClient.ListWorkflowTemplatesPagedResponse)>` |   
  
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
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   AutoscalingPolicyName.ofProjectRegionAutoscalingPolicyName(
                           "[PROJECT]", "[REGION]", "[AUTOSCALING_POLICY]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = workflowTemplateServiceClient.setIamPolicy(request);
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
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   AutoscalingPolicyName.ofProjectRegionAutoscalingPolicyName(
                           "[PROJECT]", "[REGION]", "[AUTOSCALING_POLICY]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           workflowTemplateServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   AutoscalingPolicyName.ofProjectRegionAutoscalingPolicyName(
                           "[PROJECT]", "[REGION]", "[AUTOSCALING_POLICY]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           workflowTemplateServiceClient.testIamPermissions(request);
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
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   AutoscalingPolicyName.ofProjectRegionAutoscalingPolicyName(
                           "[PROJECT]", "[REGION]", "[AUTOSCALING_POLICY]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           workflowTemplateServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateWorkflowTemplate(UpdateWorkflowTemplateRequest request)
    
    
    public final WorkflowTemplate updateWorkflowTemplate(UpdateWorkflowTemplateRequest request)

Updates (replaces) workflow template. The updated template must contain version that matches the current server version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       UpdateWorkflowTemplateRequest request =
           UpdateWorkflowTemplateRequest.newBuilder()
               .setTemplate(WorkflowTemplate.newBuilder().build())
               .build();
       WorkflowTemplate response = workflowTemplateServiceClient.updateWorkflowTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.UpdateWorkflowTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### updateWorkflowTemplate(WorkflowTemplate template)
    
    
    public final WorkflowTemplate updateWorkflowTemplate(WorkflowTemplate template)

Updates (replaces) workflow template. The updated template must contain version that matches the current server version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       WorkflowTemplate template = WorkflowTemplate.newBuilder().build();
       WorkflowTemplate response = workflowTemplateServiceClient.updateWorkflowTemplate(template);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`template` | `[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)`  
Required. The updated workflow template. The `template.version` field must match the current version.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)` |   
  
### updateWorkflowTemplateCallable()
    
    
    public final UnaryCallable<UpdateWorkflowTemplateRequest,WorkflowTemplate> updateWorkflowTemplateCallable()

Updates (replaces) workflow template. The updated template must contain version that matches the current server version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WorkflowTemplateServiceClient workflowTemplateServiceClient =
         WorkflowTemplateServiceClient.create()) {
       UpdateWorkflowTemplateRequest request =
           UpdateWorkflowTemplateRequest.newBuilder()
               .setTemplate(WorkflowTemplate.newBuilder().build())
               .build();
       ApiFuture<WorkflowTemplate> future =
           workflowTemplateServiceClient.updateWorkflowTemplateCallable().futureCall(request);
       // Do something.
       WorkflowTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateWorkflowTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.UpdateWorkflowTemplateRequest),[WorkflowTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.WorkflowTemplate)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
