---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient
title: Class BusinessGlossaryServiceClient (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:27.744691+00:00
---

# Class BusinessGlossaryServiceClient (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BusinessGlossaryServiceClient (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataplex/google-cloud-dataplex/src/main/java/com/google/cloud/dataplex/v1/BusinessGlossaryServiceClient.java)| [Product Reference](https://cloud.google.com/dataplex)| [REST Documentation](https://cloud.google.com/dataplex/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataplex/docs/reference/rpc)  
---|---|---|---  
  
Service Description: BusinessGlossaryService provides APIs for managing business glossary resources for enterprise customers. The resources currently supported in Business Glossary are:

  1. Glossary 2. GlossaryCategory 3. GlossaryTerm

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
         
         // This snippet has been automatically generated and should be regarded as a code template only.
         // It will require modifications to work:
         // - It may require correct/in-range values for request initialization.
         // - It may require specifying regional endpoints when creating the service client as shown in
         // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
         try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
          BusinessGlossaryServiceClient.create()) {
         GlossaryName name = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]");
         Glossary response = businessGlossaryServiceClient.getGlossary(name);
         }
         

Note: close() needs to be called on the BusinessGlossaryServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateGlossary |  Creates a new Glossary resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * createGlossaryAsync(CreateGlossaryRequest request) 
Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.
     * createGlossaryAsync(LocationName parent, Glossary glossary, String glossaryId) 
     * createGlossaryAsync(String parent, Glossary glossary, String glossaryId) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * createGlossaryOperationCallable() 
     * createGlossaryCallable()   
UpdateGlossary |  Updates a Glossary resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * updateGlossaryAsync(UpdateGlossaryRequest request) 
Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.
     * updateGlossaryAsync(Glossary glossary, FieldMask updateMask) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * updateGlossaryOperationCallable() 
     * updateGlossaryCallable()   
DeleteGlossary |  Deletes a Glossary resource. All the categories and terms within the Glossary must be deleted before the Glossary can be deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * deleteGlossaryAsync(DeleteGlossaryRequest request) 
Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.
     * deleteGlossaryAsync(GlossaryName name) 
     * deleteGlossaryAsync(String name) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * deleteGlossaryOperationCallable() 
     * deleteGlossaryCallable()   
GetGlossary |  Gets a Glossary resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * getGlossary(GetGlossaryRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * getGlossary(GlossaryName name) 
     * getGlossary(String name) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * getGlossaryCallable()   
ListGlossaries |  Lists Glossary resources in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * listGlossaries(ListGlossariesRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * listGlossaries(LocationName parent) 
     * listGlossaries(String parent) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * listGlossariesPagedCallable() 
     * listGlossariesCallable()   
CreateGlossaryCategory |  Creates a new GlossaryCategory resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * createGlossaryCategory(CreateGlossaryCategoryRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * createGlossaryCategory(GlossaryName parent, GlossaryCategory category, String categoryId) 
     * createGlossaryCategory(String parent, GlossaryCategory category, String categoryId) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * createGlossaryCategoryCallable()   
UpdateGlossaryCategory |  Updates a GlossaryCategory resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * updateGlossaryCategory(UpdateGlossaryCategoryRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * updateGlossaryCategory(GlossaryCategory category, FieldMask updateMask) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * updateGlossaryCategoryCallable()   
DeleteGlossaryCategory |  Deletes a GlossaryCategory resource. All the GlossaryCategories and GlossaryTerms nested directly under the specified GlossaryCategory will be moved one level up to the parent in the hierarchy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * deleteGlossaryCategory(DeleteGlossaryCategoryRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * deleteGlossaryCategory(GlossaryCategoryName name) 
     * deleteGlossaryCategory(String name) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * deleteGlossaryCategoryCallable()   
GetGlossaryCategory |  Gets a GlossaryCategory resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * getGlossaryCategory(GetGlossaryCategoryRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * getGlossaryCategory(GlossaryCategoryName name) 
     * getGlossaryCategory(String name) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * getGlossaryCategoryCallable()   
ListGlossaryCategories |  Lists GlossaryCategory resources in a Glossary. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * listGlossaryCategories(ListGlossaryCategoriesRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * listGlossaryCategories(GlossaryName parent) 
     * listGlossaryCategories(String parent) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * listGlossaryCategoriesPagedCallable() 
     * listGlossaryCategoriesCallable()   
CreateGlossaryTerm |  Creates a new GlossaryTerm resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * createGlossaryTerm(CreateGlossaryTermRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * createGlossaryTerm(GlossaryName parent, GlossaryTerm term, String termId) 
     * createGlossaryTerm(String parent, GlossaryTerm term, String termId) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * createGlossaryTermCallable()   
UpdateGlossaryTerm |  Updates a GlossaryTerm resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * updateGlossaryTerm(UpdateGlossaryTermRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * updateGlossaryTerm(GlossaryTerm term, FieldMask updateMask) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * updateGlossaryTermCallable()   
DeleteGlossaryTerm |  Deletes a GlossaryTerm resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * deleteGlossaryTerm(DeleteGlossaryTermRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * deleteGlossaryTerm(GlossaryTermName name) 
     * deleteGlossaryTerm(String name) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * deleteGlossaryTermCallable()   
GetGlossaryTerm |  Gets a GlossaryTerm resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * getGlossaryTerm(GetGlossaryTermRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * getGlossaryTerm(GlossaryTermName name) 
     * getGlossaryTerm(String name) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * getGlossaryTermCallable()   
ListGlossaryTerms |  Lists GlossaryTerm resources in a Glossary. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
     * listGlossaryTerms(ListGlossaryTermsRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
     * listGlossaryTerms(GlossaryName parent) 
     * listGlossaryTerms(String parent) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
     * listGlossaryTermsPagedCallable() 
     * listGlossaryTermsCallable()   
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
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

This class can be customized by passing in a custom instance of BusinessGlossaryServiceSettings to create(). For example:

To customize credentials:
    
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    BusinessGlossaryServiceSettings businessGlossaryServiceSettings =
     BusinessGlossaryServiceSettings.newBuilder()
         .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
         .build();
    BusinessGlossaryServiceClient businessGlossaryServiceClient =
     BusinessGlossaryServiceClient.create(businessGlossaryServiceSettings);
    

To customize the endpoint:
    
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    BusinessGlossaryServiceSettings businessGlossaryServiceSettings =
     BusinessGlossaryServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
    BusinessGlossaryServiceClient businessGlossaryServiceClient =
     BusinessGlossaryServiceClient.create(businessGlossaryServiceSettings);
    

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    BusinessGlossaryServiceSettings businessGlossaryServiceSettings =
     BusinessGlossaryServiceSettings.newHttpJsonBuilder().build();
    BusinessGlossaryServiceClient businessGlossaryServiceClient =
     BusinessGlossaryServiceClient.create(businessGlossaryServiceSettings);
    

Please refer to the GitHub repository's samples for more quickstart code snippets.




## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BusinessGlossaryServiceClient

## Static Methods 

### create()
    
    
    public static final BusinessGlossaryServiceClient create()

Constructs an instance of BusinessGlossaryServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BusinessGlossaryServiceSettings settings)
    
    
    public static final BusinessGlossaryServiceClient create(BusinessGlossaryServiceSettings settings)

Constructs an instance of BusinessGlossaryServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BusinessGlossaryServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BusinessGlossaryServiceStub stub)
    
    
    public static final BusinessGlossaryServiceClient create(BusinessGlossaryServiceStub stub)

Constructs an instance of BusinessGlossaryServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(BusinessGlossaryServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BusinessGlossaryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.BusinessGlossaryServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient)` |   
  
## Constructors 

### BusinessGlossaryServiceClient(BusinessGlossaryServiceSettings settings)
    
    
    protected BusinessGlossaryServiceClient(BusinessGlossaryServiceSettings settings)

Constructs an instance of BusinessGlossaryServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BusinessGlossaryServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceSettings)`  
  
  
### BusinessGlossaryServiceClient(BusinessGlossaryServiceStub stub)
    
    
    protected BusinessGlossaryServiceClient(BusinessGlossaryServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BusinessGlossaryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.BusinessGlossaryServiceStub)`  
  
  
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

### createGlossaryAsync(@Nullable LocationName parent, Glossary glossary, String glossaryId)
    
    
    public final OperationFuture<Glossary,OperationMetadata> createGlossaryAsync(@Nullable LocationName parent, Glossary glossary, String glossaryId)

Creates a new Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Glossary glossary = Glossary.newBuilder().build();
       String glossaryId = "glossaryId1849967577";
       Glossary response =
           businessGlossaryServiceClient.createGlossaryAsync(parent, glossary, glossaryId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The parent resource where this Glossary will be created. Format: projects/{project_id_or_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`glossary` | `[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary)`  
Required. The Glossary to create.  
`glossaryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Glossary ID: Glossary identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createGlossaryAsync(CreateGlossaryRequest request)
    
    
    public final OperationFuture<Glossary,OperationMetadata> createGlossaryAsync(CreateGlossaryRequest request)

Creates a new Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       CreateGlossaryRequest request =
           CreateGlossaryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGlossaryId("glossaryId1849967577")
               .setGlossary(Glossary.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Glossary response = businessGlossaryServiceClient.createGlossaryAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createGlossaryAsync(String parent, Glossary glossary, String glossaryId)
    
    
    public final OperationFuture<Glossary,OperationMetadata> createGlossaryAsync(String parent, Glossary glossary, String glossaryId)

Creates a new Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Glossary glossary = Glossary.newBuilder().build();
       String glossaryId = "glossaryId1849967577";
       Glossary response =
           businessGlossaryServiceClient.createGlossaryAsync(parent, glossary, glossaryId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this Glossary will be created. Format: projects/{project_id_or_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`glossary` | `[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary)`  
Required. The Glossary to create.  
`glossaryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Glossary ID: Glossary identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createGlossaryCallable()
    
    
    public final UnaryCallable<CreateGlossaryRequest,Operation> createGlossaryCallable()

Creates a new Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       CreateGlossaryRequest request =
           CreateGlossaryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGlossaryId("glossaryId1849967577")
               .setGlossary(Glossary.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           businessGlossaryServiceClient.createGlossaryCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGlossaryCategory(@Nullable GlossaryName parent, GlossaryCategory category, String categoryId)
    
    
    public final GlossaryCategory createGlossaryCategory(@Nullable GlossaryName parent, GlossaryCategory category, String categoryId)

Creates a new GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryName parent = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]");
       GlossaryCategory category = GlossaryCategory.newBuilder().build();
       String categoryId = "categoryId1296531129";
       GlossaryCategory response =
           businessGlossaryServiceClient.createGlossaryCategory(parent, category, categoryId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryName`  
Required. The parent resource where this GlossaryCategory will be created. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `locationId` refers to a Google Cloud region.  
`category` | `[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)`  
Required. The GlossaryCategory to create.  
`categoryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. GlossaryCategory identifier.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)` |   
  
### createGlossaryCategory(CreateGlossaryCategoryRequest request)
    
    
    public final GlossaryCategory createGlossaryCategory(CreateGlossaryCategoryRequest request)

Creates a new GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       CreateGlossaryCategoryRequest request =
           CreateGlossaryCategoryRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setCategoryId("categoryId1296531129")
               .setCategory(GlossaryCategory.newBuilder().build())
               .build();
       GlossaryCategory response = businessGlossaryServiceClient.createGlossaryCategory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryCategoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)` |   
  
### createGlossaryCategory(String parent, GlossaryCategory category, String categoryId)
    
    
    public final GlossaryCategory createGlossaryCategory(String parent, GlossaryCategory category, String categoryId)

Creates a new GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String parent = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString();
       GlossaryCategory category = GlossaryCategory.newBuilder().build();
       String categoryId = "categoryId1296531129";
       GlossaryCategory response =
           businessGlossaryServiceClient.createGlossaryCategory(parent, category, categoryId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this GlossaryCategory will be created. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `locationId` refers to a Google Cloud region.  
`category` | `[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)`  
Required. The GlossaryCategory to create.  
`categoryId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. GlossaryCategory identifier.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)` |   
  
### createGlossaryCategoryCallable()
    
    
    public final UnaryCallable<CreateGlossaryCategoryRequest,GlossaryCategory> createGlossaryCategoryCallable()

Creates a new GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       CreateGlossaryCategoryRequest request =
           CreateGlossaryCategoryRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setCategoryId("categoryId1296531129")
               .setCategory(GlossaryCategory.newBuilder().build())
               .build();
       ApiFuture<GlossaryCategory> future =
           businessGlossaryServiceClient.createGlossaryCategoryCallable().futureCall(request);
       // Do something.
       GlossaryCategory response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryCategoryRequest),[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)>` |   
  
### createGlossaryOperationCallable()
    
    
    public final OperationCallable<CreateGlossaryRequest,Glossary,OperationMetadata> createGlossaryOperationCallable()

Creates a new Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       CreateGlossaryRequest request =
           CreateGlossaryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGlossaryId("glossaryId1849967577")
               .setGlossary(Glossary.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Glossary, OperationMetadata> future =
           businessGlossaryServiceClient.createGlossaryOperationCallable().futureCall(request);
       // Do something.
       Glossary response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryRequest),[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createGlossaryTerm(@Nullable GlossaryName parent, GlossaryTerm term, String termId)
    
    
    public final GlossaryTerm createGlossaryTerm(@Nullable GlossaryName parent, GlossaryTerm term, String termId)

Creates a new GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryName parent = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]");
       GlossaryTerm term = GlossaryTerm.newBuilder().build();
       String termId = "termId-877206873";
       GlossaryTerm response =
           businessGlossaryServiceClient.createGlossaryTerm(parent, term, termId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryName`  
Required. The parent resource where the GlossaryTerm will be created. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `location_id` refers to a Google Cloud region.  
`term` | `[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)`  
Required. The GlossaryTerm to create.  
`termId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. GlossaryTerm identifier.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)` |   
  
### createGlossaryTerm(CreateGlossaryTermRequest request)
    
    
    public final GlossaryTerm createGlossaryTerm(CreateGlossaryTermRequest request)

Creates a new GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       CreateGlossaryTermRequest request =
           CreateGlossaryTermRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setTermId("termId-877206873")
               .setTerm(GlossaryTerm.newBuilder().build())
               .build();
       GlossaryTerm response = businessGlossaryServiceClient.createGlossaryTerm(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryTermRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)` |   
  
### createGlossaryTerm(String parent, GlossaryTerm term, String termId)
    
    
    public final GlossaryTerm createGlossaryTerm(String parent, GlossaryTerm term, String termId)

Creates a new GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String parent = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString();
       GlossaryTerm term = GlossaryTerm.newBuilder().build();
       String termId = "termId-877206873";
       GlossaryTerm response =
           businessGlossaryServiceClient.createGlossaryTerm(parent, term, termId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where the GlossaryTerm will be created. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `location_id` refers to a Google Cloud region.  
`term` | `[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)`  
Required. The GlossaryTerm to create.  
`termId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. GlossaryTerm identifier.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)` |   
  
### createGlossaryTermCallable()
    
    
    public final UnaryCallable<CreateGlossaryTermRequest,GlossaryTerm> createGlossaryTermCallable()

Creates a new GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       CreateGlossaryTermRequest request =
           CreateGlossaryTermRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setTermId("termId-877206873")
               .setTerm(GlossaryTerm.newBuilder().build())
               .build();
       ApiFuture<GlossaryTerm> future =
           businessGlossaryServiceClient.createGlossaryTermCallable().futureCall(request);
       // Do something.
       GlossaryTerm response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryTermRequest),[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)>` |   
  
### deleteGlossaryAsync(@Nullable GlossaryName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGlossaryAsync(@Nullable GlossaryName name)

Deletes a Glossary resource. All the categories and terms within the Glossary must be deleted before the Glossary can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryName name = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]");
       businessGlossaryServiceClient.deleteGlossaryAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryName`  
Required. The name of the Glossary to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteGlossaryAsync(DeleteGlossaryRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGlossaryAsync(DeleteGlossaryRequest request)

Deletes a Glossary resource. All the categories and terms within the Glossary must be deleted before the Glossary can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       DeleteGlossaryRequest request =
           DeleteGlossaryRequest.newBuilder()
               .setName(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setEtag("etag3123477")
               .build();
       businessGlossaryServiceClient.deleteGlossaryAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteGlossaryAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGlossaryAsync(String name)

Deletes a Glossary resource. All the categories and terms within the Glossary must be deleted before the Glossary can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String name = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString();
       businessGlossaryServiceClient.deleteGlossaryAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Glossary to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteGlossaryCallable()
    
    
    public final UnaryCallable<DeleteGlossaryRequest,Operation> deleteGlossaryCallable()

Deletes a Glossary resource. All the categories and terms within the Glossary must be deleted before the Glossary can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       DeleteGlossaryRequest request =
           DeleteGlossaryRequest.newBuilder()
               .setName(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           businessGlossaryServiceClient.deleteGlossaryCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGlossaryCategory(@Nullable GlossaryCategoryName name)
    
    
    public final void deleteGlossaryCategory(@Nullable GlossaryCategoryName name)

Deletes a GlossaryCategory resource. All the GlossaryCategories and GlossaryTerms nested directly under the specified GlossaryCategory will be moved one level up to the parent in the hierarchy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryCategoryName name =
           GlossaryCategoryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_CATEGORY]");
       businessGlossaryServiceClient.deleteGlossaryCategory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryCategoryName`  
Required. The name of the GlossaryCategory to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}  
  
### deleteGlossaryCategory(DeleteGlossaryCategoryRequest request)
    
    
    public final void deleteGlossaryCategory(DeleteGlossaryCategoryRequest request)

Deletes a GlossaryCategory resource. All the GlossaryCategories and GlossaryTerms nested directly under the specified GlossaryCategory will be moved one level up to the parent in the hierarchy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       DeleteGlossaryCategoryRequest request =
           DeleteGlossaryCategoryRequest.newBuilder()
               .setName(
                   GlossaryCategoryName.of(
                           "[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_CATEGORY]")
                       .toString())
               .build();
       businessGlossaryServiceClient.deleteGlossaryCategory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryCategoryRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteGlossaryCategory(String name)
    
    
    public final void deleteGlossaryCategory(String name)

Deletes a GlossaryCategory resource. All the GlossaryCategories and GlossaryTerms nested directly under the specified GlossaryCategory will be moved one level up to the parent in the hierarchy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String name =
           GlossaryCategoryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_CATEGORY]")
               .toString();
       businessGlossaryServiceClient.deleteGlossaryCategory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GlossaryCategory to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}  
  
### deleteGlossaryCategoryCallable()
    
    
    public final UnaryCallable<DeleteGlossaryCategoryRequest,Empty> deleteGlossaryCategoryCallable()

Deletes a GlossaryCategory resource. All the GlossaryCategories and GlossaryTerms nested directly under the specified GlossaryCategory will be moved one level up to the parent in the hierarchy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       DeleteGlossaryCategoryRequest request =
           DeleteGlossaryCategoryRequest.newBuilder()
               .setName(
                   GlossaryCategoryName.of(
                           "[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_CATEGORY]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           businessGlossaryServiceClient.deleteGlossaryCategoryCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryCategoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteGlossaryOperationCallable()
    
    
    public final OperationCallable<DeleteGlossaryRequest,Empty,OperationMetadata> deleteGlossaryOperationCallable()

Deletes a Glossary resource. All the categories and terms within the Glossary must be deleted before the Glossary can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       DeleteGlossaryRequest request =
           DeleteGlossaryRequest.newBuilder()
               .setName(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           businessGlossaryServiceClient.deleteGlossaryOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteGlossaryTerm(@Nullable GlossaryTermName name)
    
    
    public final void deleteGlossaryTerm(@Nullable GlossaryTermName name)

Deletes a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryTermName name =
           GlossaryTermName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_TERM]");
       businessGlossaryServiceClient.deleteGlossaryTerm(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryTermName`  
Required. The name of the GlossaryTerm to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}  
  
### deleteGlossaryTerm(DeleteGlossaryTermRequest request)
    
    
    public final void deleteGlossaryTerm(DeleteGlossaryTermRequest request)

Deletes a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       DeleteGlossaryTermRequest request =
           DeleteGlossaryTermRequest.newBuilder()
               .setName(
                   GlossaryTermName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_TERM]")
                       .toString())
               .build();
       businessGlossaryServiceClient.deleteGlossaryTerm(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryTermRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteGlossaryTerm(String name)
    
    
    public final void deleteGlossaryTerm(String name)

Deletes a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String name =
           GlossaryTermName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_TERM]")
               .toString();
       businessGlossaryServiceClient.deleteGlossaryTerm(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GlossaryTerm to delete. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}  
  
### deleteGlossaryTermCallable()
    
    
    public final UnaryCallable<DeleteGlossaryTermRequest,Empty> deleteGlossaryTermCallable()

Deletes a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       DeleteGlossaryTermRequest request =
           DeleteGlossaryTermRequest.newBuilder()
               .setName(
                   GlossaryTermName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_TERM]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           businessGlossaryServiceClient.deleteGlossaryTermCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryTermRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGlossary(@Nullable GlossaryName name)
    
    
    public final Glossary getGlossary(@Nullable GlossaryName name)

Gets a Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryName name = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]");
       Glossary response = businessGlossaryServiceClient.getGlossary(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryName`  
Required. The name of the Glossary to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}  
**Returns**  
---  
**Type** | **Description**  
`[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary)` |   
  
### getGlossary(GetGlossaryRequest request)
    
    
    public final Glossary getGlossary(GetGlossaryRequest request)

Gets a Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetGlossaryRequest request =
           GetGlossaryRequest.newBuilder()
               .setName(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .build();
       Glossary response = businessGlossaryServiceClient.getGlossary(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary)` |   
  
### getGlossary(String name)
    
    
    public final Glossary getGlossary(String name)

Gets a Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String name = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString();
       Glossary response = businessGlossaryServiceClient.getGlossary(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Glossary to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}  
**Returns**  
---  
**Type** | **Description**  
`[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary)` |   
  
### getGlossaryCallable()
    
    
    public final UnaryCallable<GetGlossaryRequest,Glossary> getGlossaryCallable()

Gets a Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetGlossaryRequest request =
           GetGlossaryRequest.newBuilder()
               .setName(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .build();
       ApiFuture<Glossary> future =
           businessGlossaryServiceClient.getGlossaryCallable().futureCall(request);
       // Do something.
       Glossary response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryRequest),[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary)>` |   
  
### getGlossaryCategory(@Nullable GlossaryCategoryName name)
    
    
    public final GlossaryCategory getGlossaryCategory(@Nullable GlossaryCategoryName name)

Gets a GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryCategoryName name =
           GlossaryCategoryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_CATEGORY]");
       GlossaryCategory response = businessGlossaryServiceClient.getGlossaryCategory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryCategoryName`  
Required. The name of the GlossaryCategory to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)` |   
  
### getGlossaryCategory(GetGlossaryCategoryRequest request)
    
    
    public final GlossaryCategory getGlossaryCategory(GetGlossaryCategoryRequest request)

Gets a GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetGlossaryCategoryRequest request =
           GetGlossaryCategoryRequest.newBuilder()
               .setName(
                   GlossaryCategoryName.of(
                           "[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_CATEGORY]")
                       .toString())
               .build();
       GlossaryCategory response = businessGlossaryServiceClient.getGlossaryCategory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryCategoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)` |   
  
### getGlossaryCategory(String name)
    
    
    public final GlossaryCategory getGlossaryCategory(String name)

Gets a GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String name =
           GlossaryCategoryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_CATEGORY]")
               .toString();
       GlossaryCategory response = businessGlossaryServiceClient.getGlossaryCategory(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GlossaryCategory to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)` |   
  
### getGlossaryCategoryCallable()
    
    
    public final UnaryCallable<GetGlossaryCategoryRequest,GlossaryCategory> getGlossaryCategoryCallable()

Gets a GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetGlossaryCategoryRequest request =
           GetGlossaryCategoryRequest.newBuilder()
               .setName(
                   GlossaryCategoryName.of(
                           "[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_CATEGORY]")
                       .toString())
               .build();
       ApiFuture<GlossaryCategory> future =
           businessGlossaryServiceClient.getGlossaryCategoryCallable().futureCall(request);
       // Do something.
       GlossaryCategory response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryCategoryRequest),[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)>` |   
  
### getGlossaryTerm(@Nullable GlossaryTermName name)
    
    
    public final GlossaryTerm getGlossaryTerm(@Nullable GlossaryTermName name)

Gets a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryTermName name =
           GlossaryTermName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_TERM]");
       GlossaryTerm response = businessGlossaryServiceClient.getGlossaryTerm(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryTermName`  
Required. The name of the GlossaryTerm to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)` |   
  
### getGlossaryTerm(GetGlossaryTermRequest request)
    
    
    public final GlossaryTerm getGlossaryTerm(GetGlossaryTermRequest request)

Gets a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetGlossaryTermRequest request =
           GetGlossaryTermRequest.newBuilder()
               .setName(
                   GlossaryTermName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_TERM]")
                       .toString())
               .build();
       GlossaryTerm response = businessGlossaryServiceClient.getGlossaryTerm(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryTermRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)` |   
  
### getGlossaryTerm(String name)
    
    
    public final GlossaryTerm getGlossaryTerm(String name)

Gets a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String name =
           GlossaryTermName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_TERM]")
               .toString();
       GlossaryTerm response = businessGlossaryServiceClient.getGlossaryTerm(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GlossaryTerm to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)` |   
  
### getGlossaryTermCallable()
    
    
    public final UnaryCallable<GetGlossaryTermRequest,GlossaryTerm> getGlossaryTermCallable()

Gets a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetGlossaryTermRequest request =
           GetGlossaryTermRequest.newBuilder()
               .setName(
                   GlossaryTermName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]", "[GLOSSARY_TERM]")
                       .toString())
               .build();
       ApiFuture<GlossaryTerm> future =
           businessGlossaryServiceClient.getGlossaryTermCallable().futureCall(request);
       // Do something.
       GlossaryTerm response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryTermRequest),[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)>` |   
  
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = businessGlossaryServiceClient.getIamPolicy(request);
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           businessGlossaryServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = businessGlossaryServiceClient.getLocation(request);
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           businessGlossaryServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable BusinessGlossaryServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.BusinessGlossaryServiceSettings` |   
  
### getStub()
    
    
    public BusinessGlossaryServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.BusinessGlossaryServiceStub)` |   
  
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
  
### listGlossaries(@Nullable LocationName parent)
    
    
    public final BusinessGlossaryServiceClient.ListGlossariesPagedResponse listGlossaries(@Nullable LocationName parent)

Lists Glossary resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Glossary element : businessGlossaryServiceClient.listGlossaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The parent, which has this collection of Glossaries. Format: projects/{project_id_or_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossariesPagedResponse)` |   
  
### listGlossaries(ListGlossariesRequest request)
    
    
    public final BusinessGlossaryServiceClient.ListGlossariesPagedResponse listGlossaries(ListGlossariesRequest request)

Lists Glossary resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossariesRequest request =
           ListGlossariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Glossary element : businessGlossaryServiceClient.listGlossaries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossariesPagedResponse)` |   
  
### listGlossaries(String parent)
    
    
    public final BusinessGlossaryServiceClient.ListGlossariesPagedResponse listGlossaries(String parent)

Lists Glossary resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Glossary element : businessGlossaryServiceClient.listGlossaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which has this collection of Glossaries. Format: projects/{project_id_or_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossariesPagedResponse)` |   
  
### listGlossariesCallable()
    
    
    public final UnaryCallable<ListGlossariesRequest,ListGlossariesResponse> listGlossariesCallable()

Lists Glossary resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossariesRequest request =
           ListGlossariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGlossariesResponse response =
             businessGlossaryServiceClient.listGlossariesCallable().call(request);
         for (Glossary element : response.getGlossariesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesRequest),[ListGlossariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesResponse)>` |   
  
### listGlossariesPagedCallable()
    
    
    public final UnaryCallable<ListGlossariesRequest,BusinessGlossaryServiceClient.ListGlossariesPagedResponse> listGlossariesPagedCallable()

Lists Glossary resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossariesRequest request =
           ListGlossariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Glossary> future =
           businessGlossaryServiceClient.listGlossariesPagedCallable().futureCall(request);
       // Do something.
       for (Glossary element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesRequest),[ListGlossariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossariesPagedResponse)>` |   
  
### listGlossaryCategories(@Nullable GlossaryName parent)
    
    
    public final BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse listGlossaryCategories(@Nullable GlossaryName parent)

Lists GlossaryCategory resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryName parent = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]");
       for (GlossaryCategory element :
           businessGlossaryServiceClient.listGlossaryCategories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryName`  
Required. The parent, which has this collection of GlossaryCategories. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} Location is the Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse)` |   
  
### listGlossaryCategories(ListGlossaryCategoriesRequest request)
    
    
    public final BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse listGlossaryCategories(ListGlossaryCategoriesRequest request)

Lists GlossaryCategory resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossaryCategoriesRequest request =
           ListGlossaryCategoriesRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (GlossaryCategory element :
           businessGlossaryServiceClient.listGlossaryCategories(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlossaryCategoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryCategoriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse)` |   
  
### listGlossaryCategories(String parent)
    
    
    public final BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse listGlossaryCategories(String parent)

Lists GlossaryCategory resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String parent = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString();
       for (GlossaryCategory element :
           businessGlossaryServiceClient.listGlossaryCategories(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which has this collection of GlossaryCategories. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} Location is the Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse)` |   
  
### listGlossaryCategoriesCallable()
    
    
    public final UnaryCallable<ListGlossaryCategoriesRequest,ListGlossaryCategoriesResponse> listGlossaryCategoriesCallable()

Lists GlossaryCategory resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossaryCategoriesRequest request =
           ListGlossaryCategoriesRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGlossaryCategoriesResponse response =
             businessGlossaryServiceClient.listGlossaryCategoriesCallable().call(request);
         for (GlossaryCategory element : response.getCategoriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlossaryCategoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryCategoriesRequest),[ListGlossaryCategoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryCategoriesResponse)>` |   
  
### listGlossaryCategoriesPagedCallable()
    
    
    public final UnaryCallable<ListGlossaryCategoriesRequest,BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse> listGlossaryCategoriesPagedCallable()

Lists GlossaryCategory resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossaryCategoriesRequest request =
           ListGlossaryCategoriesRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<GlossaryCategory> future =
           businessGlossaryServiceClient.listGlossaryCategoriesPagedCallable().futureCall(request);
       // Do something.
       for (GlossaryCategory element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlossaryCategoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryCategoriesRequest),[ListGlossaryCategoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossaryCategoriesPagedResponse)>` |   
  
### listGlossaryTerms(@Nullable GlossaryName parent)
    
    
    public final BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse listGlossaryTerms(@Nullable GlossaryName parent)

Lists GlossaryTerm resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryName parent = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]");
       for (GlossaryTerm element :
           businessGlossaryServiceClient.listGlossaryTerms(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.GlossaryName`  
Required. The parent, which has this collection of GlossaryTerms. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse)` |   
  
### listGlossaryTerms(ListGlossaryTermsRequest request)
    
    
    public final BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse listGlossaryTerms(ListGlossaryTermsRequest request)

Lists GlossaryTerm resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossaryTermsRequest request =
           ListGlossaryTermsRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (GlossaryTerm element :
           businessGlossaryServiceClient.listGlossaryTerms(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlossaryTermsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryTermsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse)` |   
  
### listGlossaryTerms(String parent)
    
    
    public final BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse listGlossaryTerms(String parent)

Lists GlossaryTerm resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       String parent = GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString();
       for (GlossaryTerm element :
           businessGlossaryServiceClient.listGlossaryTerms(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which has this collection of GlossaryTerms. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id} where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse)` |   
  
### listGlossaryTermsCallable()
    
    
    public final UnaryCallable<ListGlossaryTermsRequest,ListGlossaryTermsResponse> listGlossaryTermsCallable()

Lists GlossaryTerm resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossaryTermsRequest request =
           ListGlossaryTermsRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListGlossaryTermsResponse response =
             businessGlossaryServiceClient.listGlossaryTermsCallable().call(request);
         for (GlossaryTerm element : response.getTermsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlossaryTermsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryTermsRequest),[ListGlossaryTermsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryTermsResponse)>` |   
  
### listGlossaryTermsPagedCallable()
    
    
    public final UnaryCallable<ListGlossaryTermsRequest,BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse> listGlossaryTermsPagedCallable()

Lists GlossaryTerm resources in a Glossary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListGlossaryTermsRequest request =
           ListGlossaryTermsRequest.newBuilder()
               .setParent(GlossaryName.of("[PROJECT]", "[LOCATION]", "[GLOSSARY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<GlossaryTerm> future =
           businessGlossaryServiceClient.listGlossaryTermsPagedCallable().futureCall(request);
       // Do something.
       for (GlossaryTerm element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlossaryTermsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryTermsRequest),[ListGlossaryTermsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListGlossaryTermsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final BusinessGlossaryServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : businessGlossaryServiceClient.listLocations(request).iterateAll()) {
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
`[BusinessGlossaryServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             businessGlossaryServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,BusinessGlossaryServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           businessGlossaryServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceClient.ListLocationsPagedResponse)>` |   
  
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = businessGlossaryServiceClient.setIamPolicy(request);
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           businessGlossaryServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           businessGlossaryServiceClient.testIamPermissions(request);
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
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           businessGlossaryServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateGlossaryAsync(Glossary glossary, FieldMask updateMask)
    
    
    public final OperationFuture<Glossary,OperationMetadata> updateGlossaryAsync(Glossary glossary, FieldMask updateMask)

Updates a Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       Glossary glossary = Glossary.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Glossary response =
           businessGlossaryServiceClient.updateGlossaryAsync(glossary, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`glossary` | `[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary)`  
Required. The Glossary to update. The Glossary's `name` field is used to identify the Glossary to update. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateGlossaryAsync(UpdateGlossaryRequest request)
    
    
    public final OperationFuture<Glossary,OperationMetadata> updateGlossaryAsync(UpdateGlossaryRequest request)

Updates a Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       UpdateGlossaryRequest request =
           UpdateGlossaryRequest.newBuilder()
               .setGlossary(Glossary.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Glossary response = businessGlossaryServiceClient.updateGlossaryAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateGlossaryCallable()
    
    
    public final UnaryCallable<UpdateGlossaryRequest,Operation> updateGlossaryCallable()

Updates a Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       UpdateGlossaryRequest request =
           UpdateGlossaryRequest.newBuilder()
               .setGlossary(Glossary.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           businessGlossaryServiceClient.updateGlossaryCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGlossaryCategory(GlossaryCategory category, FieldMask updateMask)
    
    
    public final GlossaryCategory updateGlossaryCategory(GlossaryCategory category, FieldMask updateMask)

Updates a GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryCategory category = GlossaryCategory.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GlossaryCategory response =
           businessGlossaryServiceClient.updateGlossaryCategory(category, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`category` | `[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)`  
Required. The GlossaryCategory to update. The GlossaryCategory's `name` field is used to identify the GlossaryCategory to update. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/categories/{category_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)` |   
  
### updateGlossaryCategory(UpdateGlossaryCategoryRequest request)
    
    
    public final GlossaryCategory updateGlossaryCategory(UpdateGlossaryCategoryRequest request)

Updates a GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       UpdateGlossaryCategoryRequest request =
           UpdateGlossaryCategoryRequest.newBuilder()
               .setCategory(GlossaryCategory.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       GlossaryCategory response = businessGlossaryServiceClient.updateGlossaryCategory(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryCategoryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)` |   
  
### updateGlossaryCategoryCallable()
    
    
    public final UnaryCallable<UpdateGlossaryCategoryRequest,GlossaryCategory> updateGlossaryCategoryCallable()

Updates a GlossaryCategory resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       UpdateGlossaryCategoryRequest request =
           UpdateGlossaryCategoryRequest.newBuilder()
               .setCategory(GlossaryCategory.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<GlossaryCategory> future =
           businessGlossaryServiceClient.updateGlossaryCategoryCallable().futureCall(request);
       // Do something.
       GlossaryCategory response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryCategoryRequest),[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)>` |   
  
### updateGlossaryOperationCallable()
    
    
    public final OperationCallable<UpdateGlossaryRequest,Glossary,OperationMetadata> updateGlossaryOperationCallable()

Updates a Glossary resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       UpdateGlossaryRequest request =
           UpdateGlossaryRequest.newBuilder()
               .setGlossary(Glossary.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Glossary, OperationMetadata> future =
           businessGlossaryServiceClient.updateGlossaryOperationCallable().futureCall(request);
       // Do something.
       Glossary response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryRequest),[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateGlossaryTerm(GlossaryTerm term, FieldMask updateMask)
    
    
    public final GlossaryTerm updateGlossaryTerm(GlossaryTerm term, FieldMask updateMask)

Updates a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       GlossaryTerm term = GlossaryTerm.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GlossaryTerm response = businessGlossaryServiceClient.updateGlossaryTerm(term, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`term` | `[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)`  
Required. The GlossaryTerm to update. The GlossaryTerm's `name` field is used to identify the GlossaryTerm to update. Format: projects/{project_id_or_number}/locations/{location_id}/glossaries/{glossary_id}/terms/{term_id}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)` |   
  
### updateGlossaryTerm(UpdateGlossaryTermRequest request)
    
    
    public final GlossaryTerm updateGlossaryTerm(UpdateGlossaryTermRequest request)

Updates a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       UpdateGlossaryTermRequest request =
           UpdateGlossaryTermRequest.newBuilder()
               .setTerm(GlossaryTerm.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       GlossaryTerm response = businessGlossaryServiceClient.updateGlossaryTerm(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryTermRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)` |   
  
### updateGlossaryTermCallable()
    
    
    public final UnaryCallable<UpdateGlossaryTermRequest,GlossaryTerm> updateGlossaryTermCallable()

Updates a GlossaryTerm resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BusinessGlossaryServiceClient businessGlossaryServiceClient =
         BusinessGlossaryServiceClient.create()) {
       UpdateGlossaryTermRequest request =
           UpdateGlossaryTermRequest.newBuilder()
               .setTerm(GlossaryTerm.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<GlossaryTerm> future =
           businessGlossaryServiceClient.updateGlossaryTermCallable().futureCall(request);
       // Do something.
       GlossaryTerm response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryTermRequest),[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
