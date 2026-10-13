---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient
title: Class SecurityPostureClient (0.64.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:06.740213+00:00
---

# Class SecurityPostureClient (0.64.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityPostureClient (0.64.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.64.0 (latest)  0.60.0  0.59.0  0.58.0  0.56.0  0.53.0  0.52.0  0.50.0  0.48.0  0.47.0  0.45.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.33.0  0.32.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-securityposture/google-cloud-securityposture/src/main/java/com/google/cloud/securityposture/v1/SecurityPostureClient.java)| [Product Reference](https://cloud.google.com/security-command-center/docs/security-posture-overview)  
---|---  
  
Service Description: Service describing handlers for resources.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       PostureName name = PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]");
       Posture response = securityPostureClient.getPosture(name);
     }
     

Note: close() needs to be called on the SecurityPostureClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListPostures |  (-- This option restricts the visibility of the API to only projects that will (-- be labeled as `PREVIEW` or `GOOGLE_INTERNAL` by the service. (-- option (google.api.api_visibility).restriction = "PREVIEW,GOOGLE_INTERNAL"; Postures Lists Postures in a given organization and location. In case a posture has multiple revisions, the latest revision as per UpdateTime will be returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPostures(ListPosturesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPostures(OrganizationName parent) 
  * listPostures(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPosturesPagedCallable() 
  * listPosturesCallable() 

  
ListPostureRevisions |  Lists revisions of a Posture in a given organization and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPostureRevisions(ListPostureRevisionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPostureRevisionsPagedCallable() 
  * listPostureRevisionsCallable() 

  
GetPosture |  Gets a posture in a given organization and location. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the Posture name does not exist. In case revision_id is not provided then the latest Posture revision by UpdateTime is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPosture(GetPostureRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPosture(PostureName name) 
  * getPosture(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPostureCallable() 

  
CreatePosture |  Creates a new Posture resource. If a Posture with the specified name already exists in the specified organization and location, the long running operation returns a ALREADY_EXISTS error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPostureAsync(CreatePostureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPostureAsync(OrganizationName parent, Posture posture, String postureId) 
  * createPostureAsync(String parent, Posture posture, String postureId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPostureOperationCallable() 
  * createPostureCallable() 

  
UpdatePosture |  Updates an existing Posture. A new revision of the posture will be created if the revision to be updated is currently deployed on a workload. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the Posture does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the Posture. Updatable fields are state, description and policy_sets. State update operation cannot be clubbed with update of description and policy_sets. An ACTIVE posture can be updated to both DRAFT or DEPRECATED states. Postures in DRAFT or DEPRECATED states can only be updated to ACTIVE state. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePostureAsync(UpdatePostureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePostureAsync(Posture posture, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePostureOperationCallable() 
  * updatePostureCallable() 

  
DeletePosture |  Deletes all the revisions of a resource. A posture can only be deleted when none of the revisions are deployed to any workload. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePostureAsync(DeletePostureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePostureAsync(PostureName name) 
  * deletePostureAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePostureOperationCallable() 
  * deletePostureCallable() 

  
ExtractPosture |  Extracts existing policies on a workload as a posture. If a Posture on the given workload already exists, the long running operation returns a ALREADY_EXISTS error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * extractPostureAsync(ExtractPostureRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * extractPostureAsync(OrganizationName parent, String postureId, String workload) 
  * extractPostureAsync(String parent, String postureId, String workload) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * extractPostureOperationCallable() 
  * extractPostureCallable() 

  
ListPostureDeployments |  PostureDeployments Lists PostureDeployments in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPostureDeployments(ListPostureDeploymentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPostureDeployments(OrganizationName parent) 
  * listPostureDeployments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPostureDeploymentsPagedCallable() 
  * listPostureDeploymentsCallable() 

  
GetPostureDeployment |  Gets details of a single PostureDeployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPostureDeployment(GetPostureDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPostureDeployment(PostureDeploymentName name) 
  * getPostureDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPostureDeploymentCallable() 

  
CreatePostureDeployment |  Creates a new PostureDeployment in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPostureDeploymentAsync(CreatePostureDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPostureDeploymentAsync(OrganizationName parent, PostureDeployment postureDeployment, String postureDeploymentId) 
  * createPostureDeploymentAsync(String parent, PostureDeployment postureDeployment, String postureDeploymentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPostureDeploymentOperationCallable() 
  * createPostureDeploymentCallable() 

  
UpdatePostureDeployment |  Updates the parameters of a single PostureDeployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePostureDeploymentAsync(UpdatePostureDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePostureDeploymentAsync(PostureDeployment postureDeployment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePostureDeploymentOperationCallable() 
  * updatePostureDeploymentCallable() 

  
DeletePostureDeployment |  Deletes a single PostureDeployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePostureDeploymentAsync(DeletePostureDeploymentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePostureDeploymentAsync(PostureDeploymentName name) 
  * deletePostureDeploymentAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePostureDeploymentOperationCallable() 
  * deletePostureDeploymentCallable() 

  
ListPostureTemplates |  PostureTemplates Lists all the PostureTemplates available to the user. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPostureTemplates(ListPostureTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPostureTemplates(OrganizationName parent) 
  * listPostureTemplates(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPostureTemplatesPagedCallable() 
  * listPostureTemplatesCallable() 

  
GetPostureTemplate |  Gets a PostureTemplate. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the PostureTemplate name does not exist. In case revision_id is not provided then the PostureTemplate with latest revision_id is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPostureTemplate(GetPostureTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPostureTemplate(PostureTemplateName name) 
  * getPostureTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPostureTemplateCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of SecurityPostureSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityPostureSettings securityPostureSettings =
         SecurityPostureSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SecurityPostureClient securityPostureClient =
         SecurityPostureClient.create(securityPostureSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityPostureSettings securityPostureSettings =
         SecurityPostureSettings.newBuilder().setEndpoint(myEndpoint).build();
     SecurityPostureClient securityPostureClient =
         SecurityPostureClient.create(securityPostureSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityPostureSettings securityPostureSettings =
         SecurityPostureSettings.newHttpJsonBuilder().build();
     SecurityPostureClient securityPostureClient =
         SecurityPostureClient.create(securityPostureSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SecurityPostureClient

## Static Methods 

### create()
    
    
    public static final SecurityPostureClient create()

Constructs an instance of SecurityPostureClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SecurityPostureSettings settings)
    
    
    public static final SecurityPostureClient create(SecurityPostureSettings settings)

Constructs an instance of SecurityPostureClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SecurityPostureSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SecurityPostureStub stub)
    
    
    public static final SecurityPostureClient create(SecurityPostureStub stub)

Constructs an instance of SecurityPostureClient, using the given stub for making calls. This is for advanced usage - prefer using create(SecurityPostureSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecurityPostureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.stub.SecurityPostureStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient)` |   
  
## Constructors 

### SecurityPostureClient(SecurityPostureSettings settings)
    
    
    protected SecurityPostureClient(SecurityPostureSettings settings)

Constructs an instance of SecurityPostureClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SecurityPostureSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings)`  
  
  
### SecurityPostureClient(SecurityPostureStub stub)
    
    
    protected SecurityPostureClient(SecurityPostureStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecurityPostureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.stub.SecurityPostureStub)`  
  
  
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

### createPostureAsync(@Nullable OrganizationName parent, Posture posture, String postureId)
    
    
    public final OperationFuture<Posture,OperationMetadata> createPostureAsync(@Nullable OrganizationName parent, Posture posture, String postureId)

Creates a new Posture resource. If a Posture with the specified name already exists in the specified organization and location, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]");
       Posture posture = Posture.newBuilder().build();
       String postureId = "postureId2023219203";
       Posture response = securityPostureClient.createPostureAsync(parent, posture, postureId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.OrganizationName`  
Required. Value for parent.  
`posture` | `[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture)`  
Required. The resource being created.  
`postureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User provided identifier. It should be unique in scope of an Organization and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureAsync(CreatePostureRequest request)
    
    
    public final OperationFuture<Posture,OperationMetadata> createPostureAsync(CreatePostureRequest request)

Creates a new Posture resource. If a Posture with the specified name already exists in the specified organization and location, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       CreatePostureRequest request =
           CreatePostureRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureId("postureId2023219203")
               .setPosture(Posture.newBuilder().build())
               .build();
       Posture response = securityPostureClient.createPostureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureAsync(String parent, Posture posture, String postureId)
    
    
    public final OperationFuture<Posture,OperationMetadata> createPostureAsync(String parent, Posture posture, String postureId)

Creates a new Posture resource. If a Posture with the specified name already exists in the specified organization and location, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       Posture posture = Posture.newBuilder().build();
       String postureId = "postureId2023219203";
       Posture response = securityPostureClient.createPostureAsync(parent, posture, postureId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`posture` | `[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture)`  
Required. The resource being created.  
`postureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User provided identifier. It should be unique in scope of an Organization and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureCallable()
    
    
    public final UnaryCallable<CreatePostureRequest,Operation> createPostureCallable()

Creates a new Posture resource. If a Posture with the specified name already exists in the specified organization and location, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       CreatePostureRequest request =
           CreatePostureRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureId("postureId2023219203")
               .setPosture(Posture.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           securityPostureClient.createPostureCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPostureDeploymentAsync(@Nullable OrganizationName parent, PostureDeployment postureDeployment, String postureDeploymentId)
    
    
    public final OperationFuture<PostureDeployment,OperationMetadata> createPostureDeploymentAsync(@Nullable OrganizationName parent, PostureDeployment postureDeployment, String postureDeploymentId)

Creates a new PostureDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]");
       PostureDeployment postureDeployment = PostureDeployment.newBuilder().build();
       String postureDeploymentId = "postureDeploymentId1771206568";
       PostureDeployment response =
           securityPostureClient
               .createPostureDeploymentAsync(parent, postureDeployment, postureDeploymentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.OrganizationName`  
Required. Value for parent. Format: organizations/{org_id}/locations/{location}  
`postureDeployment` | `[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment)`  
Required. The resource being created.  
`postureDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User provided identifier. It should be unique in scope of an Organization and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureDeploymentAsync(CreatePostureDeploymentRequest request)
    
    
    public final OperationFuture<PostureDeployment,OperationMetadata> createPostureDeploymentAsync(CreatePostureDeploymentRequest request)

Creates a new PostureDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       CreatePostureDeploymentRequest request =
           CreatePostureDeploymentRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureDeploymentId("postureDeploymentId1771206568")
               .setPostureDeployment(PostureDeployment.newBuilder().build())
               .build();
       PostureDeployment response =
           securityPostureClient.createPostureDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureDeploymentAsync(String parent, PostureDeployment postureDeployment, String postureDeploymentId)
    
    
    public final OperationFuture<PostureDeployment,OperationMetadata> createPostureDeploymentAsync(String parent, PostureDeployment postureDeployment, String postureDeploymentId)

Creates a new PostureDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       PostureDeployment postureDeployment = PostureDeployment.newBuilder().build();
       String postureDeploymentId = "postureDeploymentId1771206568";
       PostureDeployment response =
           securityPostureClient
               .createPostureDeploymentAsync(parent, postureDeployment, postureDeploymentId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent. Format: organizations/{org_id}/locations/{location}  
`postureDeployment` | `[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment)`  
Required. The resource being created.  
`postureDeploymentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User provided identifier. It should be unique in scope of an Organization and location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureDeploymentCallable()
    
    
    public final UnaryCallable<CreatePostureDeploymentRequest,Operation> createPostureDeploymentCallable()

Creates a new PostureDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       CreatePostureDeploymentRequest request =
           CreatePostureDeploymentRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureDeploymentId("postureDeploymentId1771206568")
               .setPostureDeployment(PostureDeployment.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           securityPostureClient.createPostureDeploymentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPostureDeploymentOperationCallable()
    
    
    public final OperationCallable<CreatePostureDeploymentRequest,PostureDeployment,OperationMetadata> createPostureDeploymentOperationCallable()

Creates a new PostureDeployment in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       CreatePostureDeploymentRequest request =
           CreatePostureDeploymentRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureDeploymentId("postureDeploymentId1771206568")
               .setPostureDeployment(PostureDeployment.newBuilder().build())
               .build();
       OperationFuture<PostureDeployment, OperationMetadata> future =
           securityPostureClient.createPostureDeploymentOperationCallable().futureCall(request);
       // Do something.
       PostureDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureDeploymentRequest),[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureOperationCallable()
    
    
    public final OperationCallable<CreatePostureRequest,Posture,OperationMetadata> createPostureOperationCallable()

Creates a new Posture resource. If a Posture with the specified name already exists in the specified organization and location, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       CreatePostureRequest request =
           CreatePostureRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureId("postureId2023219203")
               .setPosture(Posture.newBuilder().build())
               .build();
       OperationFuture<Posture, OperationMetadata> future =
           securityPostureClient.createPostureOperationCallable().futureCall(request);
       // Do something.
       Posture response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureRequest),[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureAsync(@Nullable PostureName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePostureAsync(@Nullable PostureName name)

Deletes all the revisions of a resource. A posture can only be deleted when none of the revisions are deployed to any workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       PostureName name = PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]");
       securityPostureClient.deletePostureAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.PostureName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureAsync(DeletePostureRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePostureAsync(DeletePostureRequest request)

Deletes all the revisions of a resource. A posture can only be deleted when none of the revisions are deployed to any workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       DeletePostureRequest request =
           DeletePostureRequest.newBuilder()
               .setName(PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString())
               .setEtag("etag3123477")
               .build();
       securityPostureClient.deletePostureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePostureAsync(String name)

Deletes all the revisions of a resource. A posture can only be deleted when none of the revisions are deployed to any workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String name = PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString();
       securityPostureClient.deletePostureAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureCallable()
    
    
    public final UnaryCallable<DeletePostureRequest,Operation> deletePostureCallable()

Deletes all the revisions of a resource. A posture can only be deleted when none of the revisions are deployed to any workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       DeletePostureRequest request =
           DeletePostureRequest.newBuilder()
               .setName(PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           securityPostureClient.deletePostureCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePostureDeploymentAsync(@Nullable PostureDeploymentName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePostureDeploymentAsync(@Nullable PostureDeploymentName name)

Deletes a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       PostureDeploymentName name =
           PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]");
       securityPostureClient.deletePostureDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.PostureDeploymentName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureDeploymentAsync(DeletePostureDeploymentRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePostureDeploymentAsync(DeletePostureDeploymentRequest request)

Deletes a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       DeletePostureDeploymentRequest request =
           DeletePostureDeploymentRequest.newBuilder()
               .setName(
                   PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       securityPostureClient.deletePostureDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureDeploymentAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePostureDeploymentAsync(String name)

Deletes a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String name =
           PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]")
               .toString();
       securityPostureClient.deletePostureDeploymentAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureDeploymentCallable()
    
    
    public final UnaryCallable<DeletePostureDeploymentRequest,Operation> deletePostureDeploymentCallable()

Deletes a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       DeletePostureDeploymentRequest request =
           DeletePostureDeploymentRequest.newBuilder()
               .setName(
                   PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           securityPostureClient.deletePostureDeploymentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePostureDeploymentOperationCallable()
    
    
    public final OperationCallable<DeletePostureDeploymentRequest,Empty,OperationMetadata> deletePostureDeploymentOperationCallable()

Deletes a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       DeletePostureDeploymentRequest request =
           DeletePostureDeploymentRequest.newBuilder()
               .setName(
                   PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           securityPostureClient.deletePostureDeploymentOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureDeploymentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureOperationCallable()
    
    
    public final OperationCallable<DeletePostureRequest,Empty,OperationMetadata> deletePostureOperationCallable()

Deletes all the revisions of a resource. A posture can only be deleted when none of the revisions are deployed to any workload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       DeletePostureRequest request =
           DeletePostureRequest.newBuilder()
               .setName(PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           securityPostureClient.deletePostureOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### extractPostureAsync(@Nullable OrganizationName parent, String postureId, String workload)
    
    
    public final OperationFuture<Posture,OperationMetadata> extractPostureAsync(@Nullable OrganizationName parent, String postureId, String workload)

Extracts existing policies on a workload as a posture. If a Posture on the given workload already exists, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]");
       String postureId = "postureId2023219203";
       String workload = "workload35560311";
       Posture response =
           securityPostureClient.extractPostureAsync(parent, postureId, workload).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.OrganizationName`  
Required. The parent resource name. The format of this value is as follows: `organizations/{organization}/locations/{location}`  
`postureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User provided identifier. It should be unique in scope of an Organization and location.  
`workload` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Workload from which the policies are to be extracted, it should belong to the same organization defined in parent. The format of this value varies depending on the scope of the request: - `folder/folderNumber` \- `project/projectNumber` \- `organization/organizationNumber`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### extractPostureAsync(ExtractPostureRequest request)
    
    
    public final OperationFuture<Posture,OperationMetadata> extractPostureAsync(ExtractPostureRequest request)

Extracts existing policies on a workload as a posture. If a Posture on the given workload already exists, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ExtractPostureRequest request =
           ExtractPostureRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureId("postureId2023219203")
               .setWorkload("workload35560311")
               .build();
       Posture response = securityPostureClient.extractPostureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExtractPostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ExtractPostureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### extractPostureAsync(String parent, String postureId, String workload)
    
    
    public final OperationFuture<Posture,OperationMetadata> extractPostureAsync(String parent, String postureId, String workload)

Extracts existing policies on a workload as a posture. If a Posture on the given workload already exists, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       String postureId = "postureId2023219203";
       String workload = "workload35560311";
       Posture response =
           securityPostureClient.extractPostureAsync(parent, postureId, workload).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name. The format of this value is as follows: `organizations/{organization}/locations/{location}`  
`postureId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User provided identifier. It should be unique in scope of an Organization and location.  
`workload` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Workload from which the policies are to be extracted, it should belong to the same organization defined in parent. The format of this value varies depending on the scope of the request: - `folder/folderNumber` \- `project/projectNumber` \- `organization/organizationNumber`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### extractPostureCallable()
    
    
    public final UnaryCallable<ExtractPostureRequest,Operation> extractPostureCallable()

Extracts existing policies on a workload as a posture. If a Posture on the given workload already exists, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ExtractPostureRequest request =
           ExtractPostureRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureId("postureId2023219203")
               .setWorkload("workload35560311")
               .build();
       ApiFuture<Operation> future =
           securityPostureClient.extractPostureCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExtractPostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ExtractPostureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### extractPostureOperationCallable()
    
    
    public final OperationCallable<ExtractPostureRequest,Posture,OperationMetadata> extractPostureOperationCallable()

Extracts existing policies on a workload as a posture. If a Posture on the given workload already exists, the long running operation returns a ALREADY_EXISTS error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ExtractPostureRequest request =
           ExtractPostureRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPostureId("postureId2023219203")
               .setWorkload("workload35560311")
               .build();
       OperationFuture<Posture, OperationMetadata> future =
           securityPostureClient.extractPostureOperationCallable().futureCall(request);
       // Do something.
       Posture response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExtractPostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ExtractPostureRequest),[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
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
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = securityPostureClient.getLocation(request);
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
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = securityPostureClient.getLocationCallable().futureCall(request);
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
  
### getPosture(@Nullable PostureName name)
    
    
    public final Posture getPosture(@Nullable PostureName name)

Gets a posture in a given organization and location. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the Posture name does not exist. In case revision_id is not provided then the latest Posture revision by UpdateTime is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       PostureName name = PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]");
       Posture response = securityPostureClient.getPosture(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.PostureName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture)` |   
  
### getPosture(GetPostureRequest request)
    
    
    public final Posture getPosture(GetPostureRequest request)

Gets a posture in a given organization and location. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the Posture name does not exist. In case revision_id is not provided then the latest Posture revision by UpdateTime is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       GetPostureRequest request =
           GetPostureRequest.newBuilder()
               .setName(PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString())
               .setRevisionId("revisionId-1507445162")
               .build();
       Posture response = securityPostureClient.getPosture(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture)` |   
  
### getPosture(String name)
    
    
    public final Posture getPosture(String name)

Gets a posture in a given organization and location. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the Posture name does not exist. In case revision_id is not provided then the latest Posture revision by UpdateTime is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String name = PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString();
       Posture response = securityPostureClient.getPosture(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture)` |   
  
### getPostureCallable()
    
    
    public final UnaryCallable<GetPostureRequest,Posture> getPostureCallable()

Gets a posture in a given organization and location. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the Posture name does not exist. In case revision_id is not provided then the latest Posture revision by UpdateTime is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       GetPostureRequest request =
           GetPostureRequest.newBuilder()
               .setName(PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString())
               .setRevisionId("revisionId-1507445162")
               .build();
       ApiFuture<Posture> future = securityPostureClient.getPostureCallable().futureCall(request);
       // Do something.
       Posture response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureRequest),[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture)>` |   
  
### getPostureDeployment(@Nullable PostureDeploymentName name)
    
    
    public final PostureDeployment getPostureDeployment(@Nullable PostureDeploymentName name)

Gets details of a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       PostureDeploymentName name =
           PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]");
       PostureDeployment response = securityPostureClient.getPostureDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.PostureDeploymentName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment)` |   
  
### getPostureDeployment(GetPostureDeploymentRequest request)
    
    
    public final PostureDeployment getPostureDeployment(GetPostureDeploymentRequest request)

Gets details of a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       GetPostureDeploymentRequest request =
           GetPostureDeploymentRequest.newBuilder()
               .setName(
                   PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]")
                       .toString())
               .build();
       PostureDeployment response = securityPostureClient.getPostureDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment)` |   
  
### getPostureDeployment(String name)
    
    
    public final PostureDeployment getPostureDeployment(String name)

Gets details of a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String name =
           PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]")
               .toString();
       PostureDeployment response = securityPostureClient.getPostureDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment)` |   
  
### getPostureDeploymentCallable()
    
    
    public final UnaryCallable<GetPostureDeploymentRequest,PostureDeployment> getPostureDeploymentCallable()

Gets details of a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       GetPostureDeploymentRequest request =
           GetPostureDeploymentRequest.newBuilder()
               .setName(
                   PostureDeploymentName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_DEPLOYMENT]")
                       .toString())
               .build();
       ApiFuture<PostureDeployment> future =
           securityPostureClient.getPostureDeploymentCallable().futureCall(request);
       // Do something.
       PostureDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureDeploymentRequest),[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment)>` |   
  
### getPostureTemplate(@Nullable PostureTemplateName name)
    
    
    public final PostureTemplate getPostureTemplate(@Nullable PostureTemplateName name)

Gets a PostureTemplate. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the PostureTemplate name does not exist. In case revision_id is not provided then the PostureTemplate with latest revision_id is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       PostureTemplateName name =
           PostureTemplateName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_TEMPLATE]");
       PostureTemplate response = securityPostureClient.getPostureTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.PostureTemplateName`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[PostureTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureTemplate)` |   
  
### getPostureTemplate(GetPostureTemplateRequest request)
    
    
    public final PostureTemplate getPostureTemplate(GetPostureTemplateRequest request)

Gets a PostureTemplate. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the PostureTemplate name does not exist. In case revision_id is not provided then the PostureTemplate with latest revision_id is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       GetPostureTemplateRequest request =
           GetPostureTemplateRequest.newBuilder()
               .setName(
                   PostureTemplateName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_TEMPLATE]")
                       .toString())
               .setRevisionId("revisionId-1507445162")
               .build();
       PostureTemplate response = securityPostureClient.getPostureTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPostureTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PostureTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureTemplate)` |   
  
### getPostureTemplate(String name)
    
    
    public final PostureTemplate getPostureTemplate(String name)

Gets a PostureTemplate. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the PostureTemplate name does not exist. In case revision_id is not provided then the PostureTemplate with latest revision_id is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String name =
           PostureTemplateName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_TEMPLATE]").toString();
       PostureTemplate response = securityPostureClient.getPostureTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource.  
**Returns**  
---  
**Type** | **Description**  
`[PostureTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureTemplate)` |   
  
### getPostureTemplateCallable()
    
    
    public final UnaryCallable<GetPostureTemplateRequest,PostureTemplate> getPostureTemplateCallable()

Gets a PostureTemplate. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the PostureTemplate name does not exist. In case revision_id is not provided then the PostureTemplate with latest revision_id is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       GetPostureTemplateRequest request =
           GetPostureTemplateRequest.newBuilder()
               .setName(
                   PostureTemplateName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE_TEMPLATE]")
                       .toString())
               .setRevisionId("revisionId-1507445162")
               .build();
       ApiFuture<PostureTemplate> future =
           securityPostureClient.getPostureTemplateCallable().futureCall(request);
       // Do something.
       PostureTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPostureTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureTemplateRequest),[PostureTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureTemplate)>` |   
  
### getSettings()
    
    
    public final @Nullable SecurityPostureSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.SecurityPostureSettings` |   
  
### getStub()
    
    
    public SecurityPostureStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.stub.SecurityPostureStub)` |   
  
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
    
    
    public final SecurityPostureClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : securityPostureClient.listLocations(request).iterateAll()) {
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
`[SecurityPostureClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             securityPostureClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SecurityPostureClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           securityPostureClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListLocationsPagedResponse)>` |   
  
### listPostureDeployments(@Nullable OrganizationName parent)
    
    
    public final SecurityPostureClient.ListPostureDeploymentsPagedResponse listPostureDeployments(@Nullable OrganizationName parent)

PostureDeployments Lists PostureDeployments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]");
       for (PostureDeployment element :
           securityPostureClient.listPostureDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.OrganizationName`  
Required. Parent value for ListPostureDeploymentsRequest.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPostureDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureDeploymentsPagedResponse)` |   
  
### listPostureDeployments(ListPostureDeploymentsRequest request)
    
    
    public final SecurityPostureClient.ListPostureDeploymentsPagedResponse listPostureDeployments(ListPostureDeploymentsRequest request)

PostureDeployments Lists PostureDeployments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureDeploymentsRequest request =
           ListPostureDeploymentsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (PostureDeployment element :
           securityPostureClient.listPostureDeployments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPostureDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPostureDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureDeploymentsPagedResponse)` |   
  
### listPostureDeployments(String parent)
    
    
    public final SecurityPostureClient.ListPostureDeploymentsPagedResponse listPostureDeployments(String parent)

PostureDeployments Lists PostureDeployments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (PostureDeployment element :
           securityPostureClient.listPostureDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListPostureDeploymentsRequest.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPostureDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureDeploymentsPagedResponse)` |   
  
### listPostureDeploymentsCallable()
    
    
    public final UnaryCallable<ListPostureDeploymentsRequest,ListPostureDeploymentsResponse> listPostureDeploymentsCallable()

PostureDeployments Lists PostureDeployments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureDeploymentsRequest request =
           ListPostureDeploymentsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListPostureDeploymentsResponse response =
             securityPostureClient.listPostureDeploymentsCallable().call(request);
         for (PostureDeployment element : response.getPostureDeploymentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPostureDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureDeploymentsRequest),[ListPostureDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureDeploymentsResponse)>` |   
  
### listPostureDeploymentsPagedCallable()
    
    
    public final UnaryCallable<ListPostureDeploymentsRequest,SecurityPostureClient.ListPostureDeploymentsPagedResponse> listPostureDeploymentsPagedCallable()

PostureDeployments Lists PostureDeployments in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureDeploymentsRequest request =
           ListPostureDeploymentsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<PostureDeployment> future =
           securityPostureClient.listPostureDeploymentsPagedCallable().futureCall(request);
       // Do something.
       for (PostureDeployment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPostureDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureDeploymentsRequest),[ListPostureDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureDeploymentsPagedResponse)>` |   
  
### listPostureRevisions(ListPostureRevisionsRequest request)
    
    
    public final SecurityPostureClient.ListPostureRevisionsPagedResponse listPostureRevisions(ListPostureRevisionsRequest request)

Lists revisions of a Posture in a given organization and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureRevisionsRequest request =
           ListPostureRevisionsRequest.newBuilder()
               .setName(PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Posture element : securityPostureClient.listPostureRevisions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPostureRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPostureRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureRevisionsPagedResponse)` |   
  
### listPostureRevisionsCallable()
    
    
    public final UnaryCallable<ListPostureRevisionsRequest,ListPostureRevisionsResponse> listPostureRevisionsCallable()

Lists revisions of a Posture in a given organization and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureRevisionsRequest request =
           ListPostureRevisionsRequest.newBuilder()
               .setName(PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPostureRevisionsResponse response =
             securityPostureClient.listPostureRevisionsCallable().call(request);
         for (Posture element : response.getRevisionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPostureRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureRevisionsRequest),[ListPostureRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureRevisionsResponse)>` |   
  
### listPostureRevisionsPagedCallable()
    
    
    public final UnaryCallable<ListPostureRevisionsRequest,SecurityPostureClient.ListPostureRevisionsPagedResponse> listPostureRevisionsPagedCallable()

Lists revisions of a Posture in a given organization and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureRevisionsRequest request =
           ListPostureRevisionsRequest.newBuilder()
               .setName(PostureName.of("[ORGANIZATION]", "[LOCATION]", "[POSTURE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Posture> future =
           securityPostureClient.listPostureRevisionsPagedCallable().futureCall(request);
       // Do something.
       for (Posture element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPostureRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureRevisionsRequest),[ListPostureRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureRevisionsPagedResponse)>` |   
  
### listPostureTemplates(@Nullable OrganizationName parent)
    
    
    public final SecurityPostureClient.ListPostureTemplatesPagedResponse listPostureTemplates(@Nullable OrganizationName parent)

PostureTemplates Lists all the PostureTemplates available to the user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]");
       for (PostureTemplate element :
           securityPostureClient.listPostureTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.OrganizationName`  
Required. Parent value for ListPostureTemplatesRequest.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPostureTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureTemplatesPagedResponse)` |   
  
### listPostureTemplates(ListPostureTemplatesRequest request)
    
    
    public final SecurityPostureClient.ListPostureTemplatesPagedResponse listPostureTemplates(ListPostureTemplatesRequest request)

PostureTemplates Lists all the PostureTemplates available to the user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureTemplatesRequest request =
           ListPostureTemplatesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (PostureTemplate element :
           securityPostureClient.listPostureTemplates(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPostureTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPostureTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureTemplatesPagedResponse)` |   
  
### listPostureTemplates(String parent)
    
    
    public final SecurityPostureClient.ListPostureTemplatesPagedResponse listPostureTemplates(String parent)

PostureTemplates Lists all the PostureTemplates available to the user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (PostureTemplate element :
           securityPostureClient.listPostureTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListPostureTemplatesRequest.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPostureTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureTemplatesPagedResponse)` |   
  
### listPostureTemplatesCallable()
    
    
    public final UnaryCallable<ListPostureTemplatesRequest,ListPostureTemplatesResponse> listPostureTemplatesCallable()

PostureTemplates Lists all the PostureTemplates available to the user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureTemplatesRequest request =
           ListPostureTemplatesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListPostureTemplatesResponse response =
             securityPostureClient.listPostureTemplatesCallable().call(request);
         for (PostureTemplate element : response.getPostureTemplatesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPostureTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureTemplatesRequest),[ListPostureTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureTemplatesResponse)>` |   
  
### listPostureTemplatesPagedCallable()
    
    
    public final UnaryCallable<ListPostureTemplatesRequest,SecurityPostureClient.ListPostureTemplatesPagedResponse> listPostureTemplatesPagedCallable()

PostureTemplates Lists all the PostureTemplates available to the user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPostureTemplatesRequest request =
           ListPostureTemplatesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<PostureTemplate> future =
           securityPostureClient.listPostureTemplatesPagedCallable().futureCall(request);
       // Do something.
       for (PostureTemplate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPostureTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureTemplatesRequest),[ListPostureTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureTemplatesPagedResponse)>` |   
  
### listPostures(@Nullable OrganizationName parent)
    
    
    public final SecurityPostureClient.ListPosturesPagedResponse listPostures(@Nullable OrganizationName parent)

(-- This option restricts the visibility of the API to only projects that will (-- be labeled as `PREVIEW` or `GOOGLE_INTERNAL` by the service. (-- option (google.api.api_visibility).restriction = "PREVIEW,GOOGLE_INTERNAL"; Postures Lists Postures in a given organization and location. In case a posture has multiple revisions, the latest revision as per UpdateTime will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]");
       for (Posture element : securityPostureClient.listPostures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securityposture.v1.OrganizationName`  
Required. Parent value for ListPosturesRequest.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPosturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPosturesPagedResponse)` |   
  
### listPostures(ListPosturesRequest request)
    
    
    public final SecurityPostureClient.ListPosturesPagedResponse listPostures(ListPosturesRequest request)

(-- This option restricts the visibility of the API to only projects that will (-- be labeled as `PREVIEW` or `GOOGLE_INTERNAL` by the service. (-- option (google.api.api_visibility).restriction = "PREVIEW,GOOGLE_INTERNAL"; Postures Lists Postures in a given organization and location. In case a posture has multiple revisions, the latest revision as per UpdateTime will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPosturesRequest request =
           ListPosturesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Posture element : securityPostureClient.listPostures(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPosturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPosturesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPosturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPosturesPagedResponse)` |   
  
### listPostures(String parent)
    
    
    public final SecurityPostureClient.ListPosturesPagedResponse listPostures(String parent)

(-- This option restricts the visibility of the API to only projects that will (-- be labeled as `PREVIEW` or `GOOGLE_INTERNAL` by the service. (-- option (google.api.api_visibility).restriction = "PREVIEW,GOOGLE_INTERNAL"; Postures Lists Postures in a given organization and location. In case a posture has multiple revisions, the latest revision as per UpdateTime will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (Posture element : securityPostureClient.listPostures(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListPosturesRequest.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureClient.ListPosturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPosturesPagedResponse)` |   
  
### listPosturesCallable()
    
    
    public final UnaryCallable<ListPosturesRequest,ListPosturesResponse> listPosturesCallable()

(-- This option restricts the visibility of the API to only projects that will (-- be labeled as `PREVIEW` or `GOOGLE_INTERNAL` by the service. (-- option (google.api.api_visibility).restriction = "PREVIEW,GOOGLE_INTERNAL"; Postures Lists Postures in a given organization and location. In case a posture has multiple revisions, the latest revision as per UpdateTime will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPosturesRequest request =
           ListPosturesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPosturesResponse response = securityPostureClient.listPosturesCallable().call(request);
         for (Posture element : response.getPosturesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPosturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPosturesRequest),[ListPosturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPosturesResponse)>` |   
  
### listPosturesPagedCallable()
    
    
    public final UnaryCallable<ListPosturesRequest,SecurityPostureClient.ListPosturesPagedResponse> listPosturesPagedCallable()

(-- This option restricts the visibility of the API to only projects that will (-- be labeled as `PREVIEW` or `GOOGLE_INTERNAL` by the service. (-- option (google.api.api_visibility).restriction = "PREVIEW,GOOGLE_INTERNAL"; Postures Lists Postures in a given organization and location. In case a posture has multiple revisions, the latest revision as per UpdateTime will be returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       ListPosturesRequest request =
           ListPosturesRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Posture> future =
           securityPostureClient.listPosturesPagedCallable().futureCall(request);
       // Do something.
       for (Posture element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPosturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPosturesRequest),[ListPosturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPosturesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePostureAsync(Posture posture, FieldMask updateMask)
    
    
    public final OperationFuture<Posture,OperationMetadata> updatePostureAsync(Posture posture, FieldMask updateMask)

Updates an existing Posture. A new revision of the posture will be created if the revision to be updated is currently deployed on a workload. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the Posture does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the Posture. Updatable fields are state, description and policy_sets. State update operation cannot be clubbed with update of description and policy_sets. An ACTIVE posture can be updated to both DRAFT or DEPRECATED states. Postures in DRAFT or DEPRECATED states can only be updated to ACTIVE state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       Posture posture = Posture.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Posture response = securityPostureClient.updatePostureAsync(posture, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`posture` | `[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Posture resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### updatePostureAsync(UpdatePostureRequest request)
    
    
    public final OperationFuture<Posture,OperationMetadata> updatePostureAsync(UpdatePostureRequest request)

Updates an existing Posture. A new revision of the posture will be created if the revision to be updated is currently deployed on a workload. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the Posture does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the Posture. Updatable fields are state, description and policy_sets. State update operation cannot be clubbed with update of description and policy_sets. An ACTIVE posture can be updated to both DRAFT or DEPRECATED states. Postures in DRAFT or DEPRECATED states can only be updated to ACTIVE state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       UpdatePostureRequest request =
           UpdatePostureRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setPosture(Posture.newBuilder().build())
               .setRevisionId("revisionId-1507445162")
               .build();
       Posture response = securityPostureClient.updatePostureAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### updatePostureCallable()
    
    
    public final UnaryCallable<UpdatePostureRequest,Operation> updatePostureCallable()

Updates an existing Posture. A new revision of the posture will be created if the revision to be updated is currently deployed on a workload. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the Posture does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the Posture. Updatable fields are state, description and policy_sets. State update operation cannot be clubbed with update of description and policy_sets. An ACTIVE posture can be updated to both DRAFT or DEPRECATED states. Postures in DRAFT or DEPRECATED states can only be updated to ACTIVE state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       UpdatePostureRequest request =
           UpdatePostureRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setPosture(Posture.newBuilder().build())
               .setRevisionId("revisionId-1507445162")
               .build();
       ApiFuture<Operation> future =
           securityPostureClient.updatePostureCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePostureDeploymentAsync(PostureDeployment postureDeployment, FieldMask updateMask)
    
    
    public final OperationFuture<PostureDeployment,OperationMetadata> updatePostureDeploymentAsync(PostureDeployment postureDeployment, FieldMask updateMask)

Updates the parameters of a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       PostureDeployment postureDeployment = PostureDeployment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PostureDeployment response =
           securityPostureClient.updatePostureDeploymentAsync(postureDeployment, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`postureDeployment` | `[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the PostureDeployment resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### updatePostureDeploymentAsync(UpdatePostureDeploymentRequest request)
    
    
    public final OperationFuture<PostureDeployment,OperationMetadata> updatePostureDeploymentAsync(UpdatePostureDeploymentRequest request)

Updates the parameters of a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       UpdatePostureDeploymentRequest request =
           UpdatePostureDeploymentRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setPostureDeployment(PostureDeployment.newBuilder().build())
               .build();
       PostureDeployment response =
           securityPostureClient.updatePostureDeploymentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### updatePostureDeploymentCallable()
    
    
    public final UnaryCallable<UpdatePostureDeploymentRequest,Operation> updatePostureDeploymentCallable()

Updates the parameters of a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       UpdatePostureDeploymentRequest request =
           UpdatePostureDeploymentRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setPostureDeployment(PostureDeployment.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           securityPostureClient.updatePostureDeploymentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePostureDeploymentOperationCallable()
    
    
    public final OperationCallable<UpdatePostureDeploymentRequest,PostureDeployment,OperationMetadata> updatePostureDeploymentOperationCallable()

Updates the parameters of a single PostureDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       UpdatePostureDeploymentRequest request =
           UpdatePostureDeploymentRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setPostureDeployment(PostureDeployment.newBuilder().build())
               .build();
       OperationFuture<PostureDeployment, OperationMetadata> future =
           securityPostureClient.updatePostureDeploymentOperationCallable().futureCall(request);
       // Do something.
       PostureDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureDeploymentRequest),[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### updatePostureOperationCallable()
    
    
    public final OperationCallable<UpdatePostureRequest,Posture,OperationMetadata> updatePostureOperationCallable()

Updates an existing Posture. A new revision of the posture will be created if the revision to be updated is currently deployed on a workload. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the Posture does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the Posture. Updatable fields are state, description and policy_sets. State update operation cannot be clubbed with update of description and policy_sets. An ACTIVE posture can be updated to both DRAFT or DEPRECATED states. Postures in DRAFT or DEPRECATED states can only be updated to ACTIVE state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityPostureClient securityPostureClient = SecurityPostureClient.create()) {
       UpdatePostureRequest request =
           UpdatePostureRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setPosture(Posture.newBuilder().build())
               .setRevisionId("revisionId-1507445162")
               .build();
       OperationFuture<Posture, OperationMetadata> future =
           securityPostureClient.updatePostureOperationCallable().futureCall(request);
       // Do something.
       Posture response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureRequest),[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
