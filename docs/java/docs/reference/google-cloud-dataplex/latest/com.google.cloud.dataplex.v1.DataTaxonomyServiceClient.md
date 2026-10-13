---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient
title: Class DataTaxonomyServiceClient (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:32:13.395880+00:00
---

# Class DataTaxonomyServiceClient (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataTaxonomyServiceClient (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataplex/google-cloud-dataplex/src/main/java/com/google/cloud/dataplex/v1/DataTaxonomyServiceClient.java)| [Product Reference](https://cloud.google.com/dataplex)| [REST Documentation](https://cloud.google.com/dataplex/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataplex/docs/reference/rpc)  
---|---|---|---  
  
**Deprecated.** _This class is deprecated and will be removed in the next major version update._

Service Description: DataTaxonomyService enables attribute-based governance. The resources currently offered include DataTaxonomy and DataAttribute.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataTaxonomyName name = DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]");
       DataTaxonomy response = dataTaxonomyServiceClient.getDataTaxonomy(name);
     }
     

Note: close() needs to be called on the DataTaxonomyServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDataTaxonomy |  Create a DataTaxonomy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataTaxonomyAsync(CreateDataTaxonomyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDataTaxonomyAsync(LocationName parent, DataTaxonomy dataTaxonomy, String dataTaxonomyId) 
  * createDataTaxonomyAsync(String parent, DataTaxonomy dataTaxonomy, String dataTaxonomyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataTaxonomyOperationCallable() 
  * createDataTaxonomyCallable() 

  
UpdateDataTaxonomy |  Updates a DataTaxonomy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataTaxonomyAsync(UpdateDataTaxonomyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDataTaxonomyAsync(DataTaxonomy dataTaxonomy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataTaxonomyOperationCallable() 
  * updateDataTaxonomyCallable() 

  
DeleteDataTaxonomy |  Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataTaxonomyAsync(DeleteDataTaxonomyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDataTaxonomyAsync(DataTaxonomyName name) 
  * deleteDataTaxonomyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataTaxonomyOperationCallable() 
  * deleteDataTaxonomyCallable() 

  
ListDataTaxonomies |  Lists DataTaxonomy resources in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataTaxonomies(ListDataTaxonomiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataTaxonomies(LocationName parent) 
  * listDataTaxonomies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataTaxonomiesPagedCallable() 
  * listDataTaxonomiesCallable() 

  
GetDataTaxonomy |  Retrieves a DataTaxonomy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataTaxonomy(GetDataTaxonomyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataTaxonomy(DataTaxonomyName name) 
  * getDataTaxonomy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataTaxonomyCallable() 

  
CreateDataAttributeBinding |  Create a DataAttributeBinding resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataAttributeBindingAsync(CreateDataAttributeBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDataAttributeBindingAsync(LocationName parent, DataAttributeBinding dataAttributeBinding, String dataAttributeBindingId) 
  * createDataAttributeBindingAsync(String parent, DataAttributeBinding dataAttributeBinding, String dataAttributeBindingId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataAttributeBindingOperationCallable() 
  * createDataAttributeBindingCallable() 

  
UpdateDataAttributeBinding |  Updates a DataAttributeBinding resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataAttributeBindingAsync(UpdateDataAttributeBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDataAttributeBindingAsync(DataAttributeBinding dataAttributeBinding, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataAttributeBindingOperationCallable() 
  * updateDataAttributeBindingCallable() 

  
DeleteDataAttributeBinding |  Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataAttributeBindingAsync(DeleteDataAttributeBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDataAttributeBindingAsync(DataAttributeBindingName name) 
  * deleteDataAttributeBindingAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataAttributeBindingOperationCallable() 
  * deleteDataAttributeBindingCallable() 

  
ListDataAttributeBindings |  Lists DataAttributeBinding resources in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataAttributeBindings(ListDataAttributeBindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataAttributeBindings(LocationName parent) 
  * listDataAttributeBindings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataAttributeBindingsPagedCallable() 
  * listDataAttributeBindingsCallable() 

  
GetDataAttributeBinding |  Retrieves a DataAttributeBinding resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataAttributeBinding(GetDataAttributeBindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataAttributeBinding(DataAttributeBindingName name) 
  * getDataAttributeBinding(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataAttributeBindingCallable() 

  
CreateDataAttribute |  Create a DataAttribute resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataAttributeAsync(CreateDataAttributeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDataAttributeAsync(DataTaxonomyName parent, DataAttribute dataAttribute, String dataAttributeId) 
  * createDataAttributeAsync(String parent, DataAttribute dataAttribute, String dataAttributeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataAttributeOperationCallable() 
  * createDataAttributeCallable() 

  
UpdateDataAttribute |  Updates a DataAttribute resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataAttributeAsync(UpdateDataAttributeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDataAttributeAsync(DataAttribute dataAttribute, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataAttributeOperationCallable() 
  * updateDataAttributeCallable() 

  
DeleteDataAttribute |  Deletes a Data Attribute resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataAttributeAsync(DeleteDataAttributeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDataAttributeAsync(DataAttributeName name) 
  * deleteDataAttributeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataAttributeOperationCallable() 
  * deleteDataAttributeCallable() 

  
ListDataAttributes |  Lists Data Attribute resources in a DataTaxonomy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataAttributes(ListDataAttributesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataAttributes(DataTaxonomyName parent) 
  * listDataAttributes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataAttributesPagedCallable() 
  * listDataAttributesCallable() 

  
GetDataAttribute |  Retrieves a Data Attribute resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataAttribute(GetDataAttributeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataAttribute(DataAttributeName name) 
  * getDataAttribute(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataAttributeCallable() 

  
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

This class can be customized by passing in a custom instance of DataTaxonomyServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataTaxonomyServiceSettings dataTaxonomyServiceSettings =
         DataTaxonomyServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataTaxonomyServiceClient dataTaxonomyServiceClient =
         DataTaxonomyServiceClient.create(dataTaxonomyServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataTaxonomyServiceSettings dataTaxonomyServiceSettings =
         DataTaxonomyServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataTaxonomyServiceClient dataTaxonomyServiceClient =
         DataTaxonomyServiceClient.create(dataTaxonomyServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataTaxonomyServiceSettings dataTaxonomyServiceSettings =
         DataTaxonomyServiceSettings.newHttpJsonBuilder().build();
     DataTaxonomyServiceClient dataTaxonomyServiceClient =
         DataTaxonomyServiceClient.create(dataTaxonomyServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataTaxonomyServiceClient

## Static Methods 

### create() (deprecated)
    
    
    public static final DataTaxonomyServiceClient create()

Constructs an instance of DataTaxonomyServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataTaxonomyServiceSettings settings) (deprecated)
    
    
    public static final DataTaxonomyServiceClient create(DataTaxonomyServiceSettings settings)

Constructs an instance of DataTaxonomyServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataTaxonomyServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataTaxonomyServiceStub stub) (deprecated)
    
    
    public static final DataTaxonomyServiceClient create(DataTaxonomyServiceStub stub)

Constructs an instance of DataTaxonomyServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataTaxonomyServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataTaxonomyServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataTaxonomyServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient)` |   
  
## Constructors 

### DataTaxonomyServiceClient(DataTaxonomyServiceSettings settings) (deprecated)
    
    
    protected DataTaxonomyServiceClient(DataTaxonomyServiceSettings settings)

Constructs an instance of DataTaxonomyServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataTaxonomyServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceSettings)`  
  
  
### DataTaxonomyServiceClient(DataTaxonomyServiceStub stub) (deprecated)
    
    
    protected DataTaxonomyServiceClient(DataTaxonomyServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataTaxonomyServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataTaxonomyServiceStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit) (deprecated)
    
    
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
  
### close() (deprecated)
    
    
    public final void close()

### createDataAttributeAsync(@Nullable DataTaxonomyName parent, DataAttribute dataAttribute, String dataAttributeId) (deprecated)
    
    
    public final OperationFuture<DataAttribute,OperationMetadata> createDataAttributeAsync(@Nullable DataTaxonomyName parent, DataAttribute dataAttribute, String dataAttributeId)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataTaxonomyName parent =
           DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]");
       DataAttribute dataAttribute = DataAttribute.newBuilder().build();
       String dataAttributeId = "dataAttributeId-44128563";
       DataAttribute response =
           dataTaxonomyServiceClient
               .createDataAttributeAsync(parent, dataAttribute, dataAttributeId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataTaxonomyName`  
Required. The resource name of the parent data taxonomy projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}  
`dataAttribute` | `[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute)`  
Required. DataAttribute resource.  
`dataAttributeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. DataAttribute identifier. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the DataTaxonomy. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAttributeAsync(CreateDataAttributeRequest request) (deprecated)
    
    
    public final OperationFuture<DataAttribute,OperationMetadata> createDataAttributeAsync(CreateDataAttributeRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataAttributeRequest request =
           CreateDataAttributeRequest.newBuilder()
               .setParent(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setDataAttributeId("dataAttributeId-44128563")
               .setDataAttribute(DataAttribute.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataAttribute response = dataTaxonomyServiceClient.createDataAttributeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAttributeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAttributeAsync(String parent, DataAttribute dataAttribute, String dataAttributeId) (deprecated)
    
    
    public final OperationFuture<DataAttribute,OperationMetadata> createDataAttributeAsync(String parent, DataAttribute dataAttribute, String dataAttributeId)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String parent =
           DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString();
       DataAttribute dataAttribute = DataAttribute.newBuilder().build();
       String dataAttributeId = "dataAttributeId-44128563";
       DataAttribute response =
           dataTaxonomyServiceClient
               .createDataAttributeAsync(parent, dataAttribute, dataAttributeId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent data taxonomy projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}  
`dataAttribute` | `[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute)`  
Required. DataAttribute resource.  
`dataAttributeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. DataAttribute identifier. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the DataTaxonomy. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAttributeBindingAsync(@Nullable LocationName parent, DataAttributeBinding dataAttributeBinding, String dataAttributeBindingId) (deprecated)
    
    
    public final OperationFuture<DataAttributeBinding,OperationMetadata> createDataAttributeBindingAsync(@Nullable LocationName parent, DataAttributeBinding dataAttributeBinding, String dataAttributeBindingId)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DataAttributeBinding dataAttributeBinding = DataAttributeBinding.newBuilder().build();
       String dataAttributeBindingId = "dataAttributeBindingId1952425102";
       DataAttributeBinding response =
           dataTaxonomyServiceClient
               .createDataAttributeBindingAsync(parent, dataAttributeBinding, dataAttributeBindingId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the parent data taxonomy projects/{project_number}/locations/{location_id}  
`dataAttributeBinding` | `[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding)`  
Required. DataAttributeBinding resource.  
`dataAttributeBindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. DataAttributeBinding identifier. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the Location. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAttributeBindingAsync(CreateDataAttributeBindingRequest request) (deprecated)
    
    
    public final OperationFuture<DataAttributeBinding,OperationMetadata> createDataAttributeBindingAsync(CreateDataAttributeBindingRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataAttributeBindingRequest request =
           CreateDataAttributeBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataAttributeBindingId("dataAttributeBindingId1952425102")
               .setDataAttributeBinding(DataAttributeBinding.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataAttributeBinding response =
           dataTaxonomyServiceClient.createDataAttributeBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAttributeBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAttributeBindingAsync(String parent, DataAttributeBinding dataAttributeBinding, String dataAttributeBindingId) (deprecated)
    
    
    public final OperationFuture<DataAttributeBinding,OperationMetadata> createDataAttributeBindingAsync(String parent, DataAttributeBinding dataAttributeBinding, String dataAttributeBindingId)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DataAttributeBinding dataAttributeBinding = DataAttributeBinding.newBuilder().build();
       String dataAttributeBindingId = "dataAttributeBindingId1952425102";
       DataAttributeBinding response =
           dataTaxonomyServiceClient
               .createDataAttributeBindingAsync(parent, dataAttributeBinding, dataAttributeBindingId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent data taxonomy projects/{project_number}/locations/{location_id}  
`dataAttributeBinding` | `[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding)`  
Required. DataAttributeBinding resource.  
`dataAttributeBindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. DataAttributeBinding identifier. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the Location. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAttributeBindingCallable() (deprecated)
    
    
    public final UnaryCallable<CreateDataAttributeBindingRequest,Operation> createDataAttributeBindingCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataAttributeBindingRequest request =
           CreateDataAttributeBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataAttributeBindingId("dataAttributeBindingId1952425102")
               .setDataAttributeBinding(DataAttributeBinding.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.createDataAttributeBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAttributeBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataAttributeBindingOperationCallable() (deprecated)
    
    
    public final OperationCallable<CreateDataAttributeBindingRequest,DataAttributeBinding,OperationMetadata> createDataAttributeBindingOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataAttributeBindingRequest request =
           CreateDataAttributeBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataAttributeBindingId("dataAttributeBindingId1952425102")
               .setDataAttributeBinding(DataAttributeBinding.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataAttributeBinding, OperationMetadata> future =
           dataTaxonomyServiceClient
               .createDataAttributeBindingOperationCallable()
               .futureCall(request);
       // Do something.
       DataAttributeBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAttributeBindingRequest),[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAttributeCallable() (deprecated)
    
    
    public final UnaryCallable<CreateDataAttributeRequest,Operation> createDataAttributeCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataAttributeRequest request =
           CreateDataAttributeRequest.newBuilder()
               .setParent(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setDataAttributeId("dataAttributeId-44128563")
               .setDataAttribute(DataAttribute.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.createDataAttributeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAttributeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataAttributeOperationCallable() (deprecated)
    
    
    public final OperationCallable<CreateDataAttributeRequest,DataAttribute,OperationMetadata> createDataAttributeOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataAttributeRequest request =
           CreateDataAttributeRequest.newBuilder()
               .setParent(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setDataAttributeId("dataAttributeId-44128563")
               .setDataAttribute(DataAttribute.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataAttribute, OperationMetadata> future =
           dataTaxonomyServiceClient.createDataAttributeOperationCallable().futureCall(request);
       // Do something.
       DataAttribute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAttributeRequest),[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataTaxonomyAsync(@Nullable LocationName parent, DataTaxonomy dataTaxonomy, String dataTaxonomyId) (deprecated)
    
    
    public final OperationFuture<DataTaxonomy,OperationMetadata> createDataTaxonomyAsync(@Nullable LocationName parent, DataTaxonomy dataTaxonomy, String dataTaxonomyId)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DataTaxonomy dataTaxonomy = DataTaxonomy.newBuilder().build();
       String dataTaxonomyId = "dataTaxonomyId987458454";
       DataTaxonomy response =
           dataTaxonomyServiceClient
               .createDataTaxonomyAsync(parent, dataTaxonomy, dataTaxonomyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
  
`dataTaxonomy` | `[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy)`  
Required. DataTaxonomy resource.  
`dataTaxonomyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. DataTaxonomy identifier. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the Project. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataTaxonomyAsync(CreateDataTaxonomyRequest request) (deprecated)
    
    
    public final OperationFuture<DataTaxonomy,OperationMetadata> createDataTaxonomyAsync(CreateDataTaxonomyRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataTaxonomyRequest request =
           CreateDataTaxonomyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataTaxonomyId("dataTaxonomyId987458454")
               .setDataTaxonomy(DataTaxonomy.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataTaxonomy response = dataTaxonomyServiceClient.createDataTaxonomyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataTaxonomyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataTaxonomyAsync(String parent, DataTaxonomy dataTaxonomy, String dataTaxonomyId) (deprecated)
    
    
    public final OperationFuture<DataTaxonomy,OperationMetadata> createDataTaxonomyAsync(String parent, DataTaxonomy dataTaxonomy, String dataTaxonomyId)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DataTaxonomy dataTaxonomy = DataTaxonomy.newBuilder().build();
       String dataTaxonomyId = "dataTaxonomyId987458454";
       DataTaxonomy response =
           dataTaxonomyServiceClient
               .createDataTaxonomyAsync(parent, dataTaxonomy, dataTaxonomyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`dataTaxonomy` | `[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy)`  
Required. DataTaxonomy resource.  
`dataTaxonomyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. DataTaxonomy identifier. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must be between 1-63 characters. 
  * Must end with a number or a letter. 
  * Must be unique within the Project. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataTaxonomyCallable() (deprecated)
    
    
    public final UnaryCallable<CreateDataTaxonomyRequest,Operation> createDataTaxonomyCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataTaxonomyRequest request =
           CreateDataTaxonomyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataTaxonomyId("dataTaxonomyId987458454")
               .setDataTaxonomy(DataTaxonomy.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.createDataTaxonomyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataTaxonomyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataTaxonomyOperationCallable() (deprecated)
    
    
    public final OperationCallable<CreateDataTaxonomyRequest,DataTaxonomy,OperationMetadata> createDataTaxonomyOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Create a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       CreateDataTaxonomyRequest request =
           CreateDataTaxonomyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataTaxonomyId("dataTaxonomyId987458454")
               .setDataTaxonomy(DataTaxonomy.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataTaxonomy, OperationMetadata> future =
           dataTaxonomyServiceClient.createDataTaxonomyOperationCallable().futureCall(request);
       // Do something.
       DataTaxonomy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataTaxonomyRequest),[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAttributeAsync(@Nullable DataAttributeName name) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAttributeAsync(@Nullable DataAttributeName name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataAttributeName name =
           DataAttributeName.of("[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]");
       dataTaxonomyServiceClient.deleteDataAttributeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataAttributeName`  
Required. The resource name of the DataAttribute: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAttributeAsync(DeleteDataAttributeRequest request) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAttributeAsync(DeleteDataAttributeRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataAttributeRequest request =
           DeleteDataAttributeRequest.newBuilder()
               .setName(
                   DataAttributeName.of(
                           "[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       dataTaxonomyServiceClient.deleteDataAttributeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAttributeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAttributeAsync(String name) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAttributeAsync(String name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String name =
           DataAttributeName.of("[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]")
               .toString();
       dataTaxonomyServiceClient.deleteDataAttributeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataAttribute: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAttributeBindingAsync(@Nullable DataAttributeBindingName name) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAttributeBindingAsync(@Nullable DataAttributeBindingName name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataAttributeBindingName name =
           DataAttributeBindingName.of("[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]");
       dataTaxonomyServiceClient.deleteDataAttributeBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataAttributeBindingName`  
Required. The resource name of the DataAttributeBinding: projects/{project_number}/locations/{location_id}/dataAttributeBindings/{data_attribute_binding_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAttributeBindingAsync(DeleteDataAttributeBindingRequest request) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAttributeBindingAsync(DeleteDataAttributeBindingRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataAttributeBindingRequest request =
           DeleteDataAttributeBindingRequest.newBuilder()
               .setName(
                   DataAttributeBindingName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       dataTaxonomyServiceClient.deleteDataAttributeBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAttributeBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAttributeBindingAsync(String name) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAttributeBindingAsync(String name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String name =
           DataAttributeBindingName.of("[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]")
               .toString();
       dataTaxonomyServiceClient.deleteDataAttributeBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataAttributeBinding: projects/{project_number}/locations/{location_id}/dataAttributeBindings/{data_attribute_binding_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAttributeBindingCallable() (deprecated)
    
    
    public final UnaryCallable<DeleteDataAttributeBindingRequest,Operation> deleteDataAttributeBindingCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataAttributeBindingRequest request =
           DeleteDataAttributeBindingRequest.newBuilder()
               .setName(
                   DataAttributeBindingName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.deleteDataAttributeBindingCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAttributeBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataAttributeBindingOperationCallable() (deprecated)
    
    
    public final OperationCallable<DeleteDataAttributeBindingRequest,Empty,OperationMetadata> deleteDataAttributeBindingOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataAttributeBindingRequest request =
           DeleteDataAttributeBindingRequest.newBuilder()
               .setName(
                   DataAttributeBindingName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataTaxonomyServiceClient
               .deleteDataAttributeBindingOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAttributeBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAttributeCallable() (deprecated)
    
    
    public final UnaryCallable<DeleteDataAttributeRequest,Operation> deleteDataAttributeCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataAttributeRequest request =
           DeleteDataAttributeRequest.newBuilder()
               .setName(
                   DataAttributeName.of(
                           "[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.deleteDataAttributeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAttributeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataAttributeOperationCallable() (deprecated)
    
    
    public final OperationCallable<DeleteDataAttributeRequest,Empty,OperationMetadata> deleteDataAttributeOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataAttributeRequest request =
           DeleteDataAttributeRequest.newBuilder()
               .setName(
                   DataAttributeName.of(
                           "[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataTaxonomyServiceClient.deleteDataAttributeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAttributeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataTaxonomyAsync(@Nullable DataTaxonomyName name) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataTaxonomyAsync(@Nullable DataTaxonomyName name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataTaxonomyName name = DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]");
       dataTaxonomyServiceClient.deleteDataTaxonomyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataTaxonomyName`  
Required. The resource name of the DataTaxonomy: projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataTaxonomyAsync(DeleteDataTaxonomyRequest request) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataTaxonomyAsync(DeleteDataTaxonomyRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataTaxonomyRequest request =
           DeleteDataTaxonomyRequest.newBuilder()
               .setName(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setEtag("etag3123477")
               .build();
       dataTaxonomyServiceClient.deleteDataTaxonomyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataTaxonomyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataTaxonomyAsync(String name) (deprecated)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataTaxonomyAsync(String name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String name = DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString();
       dataTaxonomyServiceClient.deleteDataTaxonomyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataTaxonomy: projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataTaxonomyCallable() (deprecated)
    
    
    public final UnaryCallable<DeleteDataTaxonomyRequest,Operation> deleteDataTaxonomyCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataTaxonomyRequest request =
           DeleteDataTaxonomyRequest.newBuilder()
               .setName(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.deleteDataTaxonomyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataTaxonomyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataTaxonomyOperationCallable() (deprecated)
    
    
    public final OperationCallable<DeleteDataTaxonomyRequest,Empty,OperationMetadata> deleteDataTaxonomyOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DeleteDataTaxonomyRequest request =
           DeleteDataTaxonomyRequest.newBuilder()
               .setName(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataTaxonomyServiceClient.deleteDataTaxonomyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataTaxonomyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### getDataAttribute(@Nullable DataAttributeName name) (deprecated)
    
    
    public final DataAttribute getDataAttribute(@Nullable DataAttributeName name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataAttributeName name =
           DataAttributeName.of("[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]");
       DataAttribute response = dataTaxonomyServiceClient.getDataAttribute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataAttributeName`  
Required. The resource name of the dataAttribute: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute)` |   
  
### getDataAttribute(GetDataAttributeRequest request) (deprecated)
    
    
    public final DataAttribute getDataAttribute(GetDataAttributeRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetDataAttributeRequest request =
           GetDataAttributeRequest.newBuilder()
               .setName(
                   DataAttributeName.of(
                           "[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]")
                       .toString())
               .build();
       DataAttribute response = dataTaxonomyServiceClient.getDataAttribute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataAttributeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute)` |   
  
### getDataAttribute(String name) (deprecated)
    
    
    public final DataAttribute getDataAttribute(String name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String name =
           DataAttributeName.of("[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]")
               .toString();
       DataAttribute response = dataTaxonomyServiceClient.getDataAttribute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the dataAttribute: projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute)` |   
  
### getDataAttributeBinding(@Nullable DataAttributeBindingName name) (deprecated)
    
    
    public final DataAttributeBinding getDataAttributeBinding(@Nullable DataAttributeBindingName name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataAttributeBindingName name =
           DataAttributeBindingName.of("[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]");
       DataAttributeBinding response = dataTaxonomyServiceClient.getDataAttributeBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataAttributeBindingName`  
Required. The resource name of the DataAttributeBinding: projects/{project_number}/locations/{location_id}/dataAttributeBindings/{data_attribute_binding_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding)` |   
  
### getDataAttributeBinding(GetDataAttributeBindingRequest request) (deprecated)
    
    
    public final DataAttributeBinding getDataAttributeBinding(GetDataAttributeBindingRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetDataAttributeBindingRequest request =
           GetDataAttributeBindingRequest.newBuilder()
               .setName(
                   DataAttributeBindingName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]")
                       .toString())
               .build();
       DataAttributeBinding response = dataTaxonomyServiceClient.getDataAttributeBinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataAttributeBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding)` |   
  
### getDataAttributeBinding(String name) (deprecated)
    
    
    public final DataAttributeBinding getDataAttributeBinding(String name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String name =
           DataAttributeBindingName.of("[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]")
               .toString();
       DataAttributeBinding response = dataTaxonomyServiceClient.getDataAttributeBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataAttributeBinding: projects/{project_number}/locations/{location_id}/dataAttributeBindings/{data_attribute_binding_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding)` |   
  
### getDataAttributeBindingCallable() (deprecated)
    
    
    public final UnaryCallable<GetDataAttributeBindingRequest,DataAttributeBinding> getDataAttributeBindingCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetDataAttributeBindingRequest request =
           GetDataAttributeBindingRequest.newBuilder()
               .setName(
                   DataAttributeBindingName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_ATTRIBUTE_BINDING_ID]")
                       .toString())
               .build();
       ApiFuture<DataAttributeBinding> future =
           dataTaxonomyServiceClient.getDataAttributeBindingCallable().futureCall(request);
       // Do something.
       DataAttributeBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataAttributeBindingRequest),[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding)>` |   
  
### getDataAttributeCallable() (deprecated)
    
    
    public final UnaryCallable<GetDataAttributeRequest,DataAttribute> getDataAttributeCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a Data Attribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetDataAttributeRequest request =
           GetDataAttributeRequest.newBuilder()
               .setName(
                   DataAttributeName.of(
                           "[PROJECT]", "[LOCATION]", "[DATATAXONOMY]", "[DATA_ATTRIBUTE_ID]")
                       .toString())
               .build();
       ApiFuture<DataAttribute> future =
           dataTaxonomyServiceClient.getDataAttributeCallable().futureCall(request);
       // Do something.
       DataAttribute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataAttributeRequest),[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute)>` |   
  
### getDataTaxonomy(@Nullable DataTaxonomyName name) (deprecated)
    
    
    public final DataTaxonomy getDataTaxonomy(@Nullable DataTaxonomyName name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataTaxonomyName name = DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]");
       DataTaxonomy response = dataTaxonomyServiceClient.getDataTaxonomy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataTaxonomyName`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy)` |   
  
### getDataTaxonomy(GetDataTaxonomyRequest request) (deprecated)
    
    
    public final DataTaxonomy getDataTaxonomy(GetDataTaxonomyRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetDataTaxonomyRequest request =
           GetDataTaxonomyRequest.newBuilder()
               .setName(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .build();
       DataTaxonomy response = dataTaxonomyServiceClient.getDataTaxonomy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataTaxonomyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy)` |   
  
### getDataTaxonomy(String name) (deprecated)
    
    
    public final DataTaxonomy getDataTaxonomy(String name)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String name = DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString();
       DataTaxonomy response = dataTaxonomyServiceClient.getDataTaxonomy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy)` |   
  
### getDataTaxonomyCallable() (deprecated)
    
    
    public final UnaryCallable<GetDataTaxonomyRequest,DataTaxonomy> getDataTaxonomyCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Retrieves a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetDataTaxonomyRequest request =
           GetDataTaxonomyRequest.newBuilder()
               .setName(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .build();
       ApiFuture<DataTaxonomy> future =
           dataTaxonomyServiceClient.getDataTaxonomyCallable().futureCall(request);
       // Do something.
       DataTaxonomy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataTaxonomyRequest),[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy)>` |   
  
### getHttpJsonOperationsClient() (deprecated)
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request) (deprecated)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = dataTaxonomyServiceClient.getIamPolicy(request);
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
  
### getIamPolicyCallable() (deprecated)
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           dataTaxonomyServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request) (deprecated)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataTaxonomyServiceClient.getLocation(request);
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
  
### getLocationCallable() (deprecated)
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           dataTaxonomyServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient() (deprecated)
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings() (deprecated)
    
    
    public final @Nullable DataTaxonomyServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataTaxonomyServiceSettings` |   
  
### getStub() (deprecated)
    
    
    public DataTaxonomyServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataTaxonomyServiceStub)` |   
  
### isShutdown() (deprecated)
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated() (deprecated)
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listDataAttributeBindings(@Nullable LocationName parent) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse listDataAttributeBindings(@Nullable LocationName parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataAttributeBinding resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DataAttributeBinding element :
           dataTaxonomyServiceClient.listDataAttributeBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the Location: projects/{project_number}/locations/{location_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse)` |   
  
### listDataAttributeBindings(ListDataAttributeBindingsRequest request) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse listDataAttributeBindings(ListDataAttributeBindingsRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataAttributeBinding resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataAttributeBindingsRequest request =
           ListDataAttributeBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataAttributeBinding element :
           dataTaxonomyServiceClient.listDataAttributeBindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataAttributeBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAttributeBindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse)` |   
  
### listDataAttributeBindings(String parent) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse listDataAttributeBindings(String parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataAttributeBinding resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DataAttributeBinding element :
           dataTaxonomyServiceClient.listDataAttributeBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location: projects/{project_number}/locations/{location_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse)` |   
  
### listDataAttributeBindingsCallable() (deprecated)
    
    
    public final UnaryCallable<ListDataAttributeBindingsRequest,ListDataAttributeBindingsResponse> listDataAttributeBindingsCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataAttributeBinding resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataAttributeBindingsRequest request =
           ListDataAttributeBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataAttributeBindingsResponse response =
             dataTaxonomyServiceClient.listDataAttributeBindingsCallable().call(request);
         for (DataAttributeBinding element : response.getDataAttributeBindingsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataAttributeBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAttributeBindingsRequest),[ListDataAttributeBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAttributeBindingsResponse)>` |   
  
### listDataAttributeBindingsPagedCallable() (deprecated)
    
    
    public final UnaryCallable<ListDataAttributeBindingsRequest,DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse> listDataAttributeBindingsPagedCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataAttributeBinding resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataAttributeBindingsRequest request =
           ListDataAttributeBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataAttributeBinding> future =
           dataTaxonomyServiceClient.listDataAttributeBindingsPagedCallable().futureCall(request);
       // Do something.
       for (DataAttributeBinding element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataAttributeBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAttributeBindingsRequest),[ListDataAttributeBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataAttributeBindingsPagedResponse)>` |   
  
### listDataAttributes(@Nullable DataTaxonomyName parent) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataAttributesPagedResponse listDataAttributes(@Nullable DataTaxonomyName parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists Data Attribute resources in a DataTaxonomy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataTaxonomyName parent =
           DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]");
       for (DataAttribute element :
           dataTaxonomyServiceClient.listDataAttributes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataTaxonomyName`  
Required. The resource name of the DataTaxonomy: projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataAttributesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataAttributesPagedResponse)` |   
  
### listDataAttributes(ListDataAttributesRequest request) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataAttributesPagedResponse listDataAttributes(ListDataAttributesRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists Data Attribute resources in a DataTaxonomy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataAttributesRequest request =
           ListDataAttributesRequest.newBuilder()
               .setParent(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataAttribute element :
           dataTaxonomyServiceClient.listDataAttributes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataAttributesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAttributesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataAttributesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataAttributesPagedResponse)` |   
  
### listDataAttributes(String parent) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataAttributesPagedResponse listDataAttributes(String parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists Data Attribute resources in a DataTaxonomy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String parent =
           DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString();
       for (DataAttribute element :
           dataTaxonomyServiceClient.listDataAttributes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataTaxonomy: projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataAttributesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataAttributesPagedResponse)` |   
  
### listDataAttributesCallable() (deprecated)
    
    
    public final UnaryCallable<ListDataAttributesRequest,ListDataAttributesResponse> listDataAttributesCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists Data Attribute resources in a DataTaxonomy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataAttributesRequest request =
           ListDataAttributesRequest.newBuilder()
               .setParent(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataAttributesResponse response =
             dataTaxonomyServiceClient.listDataAttributesCallable().call(request);
         for (DataAttribute element : response.getDataAttributesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataAttributesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAttributesRequest),[ListDataAttributesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAttributesResponse)>` |   
  
### listDataAttributesPagedCallable() (deprecated)
    
    
    public final UnaryCallable<ListDataAttributesRequest,DataTaxonomyServiceClient.ListDataAttributesPagedResponse> listDataAttributesPagedCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists Data Attribute resources in a DataTaxonomy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataAttributesRequest request =
           ListDataAttributesRequest.newBuilder()
               .setParent(
                   DataTaxonomyName.of("[PROJECT]", "[LOCATION]", "[DATA_TAXONOMY_ID]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataAttribute> future =
           dataTaxonomyServiceClient.listDataAttributesPagedCallable().futureCall(request);
       // Do something.
       for (DataAttribute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataAttributesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAttributesRequest),[ListDataAttributesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataAttributesPagedResponse)>` |   
  
### listDataTaxonomies(@Nullable LocationName parent) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse listDataTaxonomies(@Nullable LocationName parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataTaxonomy resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DataTaxonomy element :
           dataTaxonomyServiceClient.listDataTaxonomies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the DataTaxonomy location, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse)` |   
  
### listDataTaxonomies(ListDataTaxonomiesRequest request) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse listDataTaxonomies(ListDataTaxonomiesRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataTaxonomy resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataTaxonomiesRequest request =
           ListDataTaxonomiesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataTaxonomy element :
           dataTaxonomyServiceClient.listDataTaxonomies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataTaxonomiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataTaxonomiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse)` |   
  
### listDataTaxonomies(String parent) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse listDataTaxonomies(String parent)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataTaxonomy resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DataTaxonomy element :
           dataTaxonomyServiceClient.listDataTaxonomies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the DataTaxonomy location, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse)` |   
  
### listDataTaxonomiesCallable() (deprecated)
    
    
    public final UnaryCallable<ListDataTaxonomiesRequest,ListDataTaxonomiesResponse> listDataTaxonomiesCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataTaxonomy resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataTaxonomiesRequest request =
           ListDataTaxonomiesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataTaxonomiesResponse response =
             dataTaxonomyServiceClient.listDataTaxonomiesCallable().call(request);
         for (DataTaxonomy element : response.getDataTaxonomiesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataTaxonomiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataTaxonomiesRequest),[ListDataTaxonomiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataTaxonomiesResponse)>` |   
  
### listDataTaxonomiesPagedCallable() (deprecated)
    
    
    public final UnaryCallable<ListDataTaxonomiesRequest,DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse> listDataTaxonomiesPagedCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Lists DataTaxonomy resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListDataTaxonomiesRequest request =
           ListDataTaxonomiesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataTaxonomy> future =
           dataTaxonomyServiceClient.listDataTaxonomiesPagedCallable().futureCall(request);
       // Do something.
       for (DataTaxonomy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataTaxonomiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataTaxonomiesRequest),[ListDataTaxonomiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListDataTaxonomiesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request) (deprecated)
    
    
    public final DataTaxonomyServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataTaxonomyServiceClient.listLocations(request).iterateAll()) {
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
`[DataTaxonomyServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable() (deprecated)
    
    
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
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataTaxonomyServiceClient.listLocationsCallable().call(request);
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
  
### listLocationsPagedCallable() (deprecated)
    
    
    public final UnaryCallable<ListLocationsRequest,DataTaxonomyServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataTaxonomyServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomyServiceClient.ListLocationsPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request) (deprecated)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = dataTaxonomyServiceClient.setIamPolicy(request);
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
  
### setIamPolicyCallable() (deprecated)
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           dataTaxonomyServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown() (deprecated)
    
    
    public void shutdown()

### shutdownNow() (deprecated)
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request) (deprecated)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = dataTaxonomyServiceClient.testIamPermissions(request);
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
  
### testIamPermissionsCallable() (deprecated)
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           dataTaxonomyServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateDataAttributeAsync(DataAttribute dataAttribute, FieldMask updateMask) (deprecated)
    
    
    public final OperationFuture<DataAttribute,OperationMetadata> updateDataAttributeAsync(DataAttribute dataAttribute, FieldMask updateMask)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataAttribute dataAttribute = DataAttribute.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataAttribute response =
           dataTaxonomyServiceClient.updateDataAttributeAsync(dataAttribute, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataAttribute` | `[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute)`  
Required. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataAttributeAsync(UpdateDataAttributeRequest request) (deprecated)
    
    
    public final OperationFuture<DataAttribute,OperationMetadata> updateDataAttributeAsync(UpdateDataAttributeRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataAttributeRequest request =
           UpdateDataAttributeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataAttribute(DataAttribute.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataAttribute response = dataTaxonomyServiceClient.updateDataAttributeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAttributeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataAttributeBindingAsync(DataAttributeBinding dataAttributeBinding, FieldMask updateMask) (deprecated)
    
    
    public final OperationFuture<DataAttributeBinding,OperationMetadata> updateDataAttributeBindingAsync(DataAttributeBinding dataAttributeBinding, FieldMask updateMask)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataAttributeBinding dataAttributeBinding = DataAttributeBinding.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataAttributeBinding response =
           dataTaxonomyServiceClient
               .updateDataAttributeBindingAsync(dataAttributeBinding, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataAttributeBinding` | `[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding)`  
Required. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataAttributeBindingAsync(UpdateDataAttributeBindingRequest request) (deprecated)
    
    
    public final OperationFuture<DataAttributeBinding,OperationMetadata> updateDataAttributeBindingAsync(UpdateDataAttributeBindingRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataAttributeBindingRequest request =
           UpdateDataAttributeBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataAttributeBinding(DataAttributeBinding.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataAttributeBinding response =
           dataTaxonomyServiceClient.updateDataAttributeBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAttributeBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataAttributeBindingCallable() (deprecated)
    
    
    public final UnaryCallable<UpdateDataAttributeBindingRequest,Operation> updateDataAttributeBindingCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataAttributeBindingRequest request =
           UpdateDataAttributeBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataAttributeBinding(DataAttributeBinding.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.updateDataAttributeBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAttributeBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataAttributeBindingOperationCallable() (deprecated)
    
    
    public final OperationCallable<UpdateDataAttributeBindingRequest,DataAttributeBinding,OperationMetadata> updateDataAttributeBindingOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataAttributeBinding resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataAttributeBindingRequest request =
           UpdateDataAttributeBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataAttributeBinding(DataAttributeBinding.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataAttributeBinding, OperationMetadata> future =
           dataTaxonomyServiceClient
               .updateDataAttributeBindingOperationCallable()
               .futureCall(request);
       // Do something.
       DataAttributeBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDataAttributeBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAttributeBindingRequest),[DataAttributeBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttributeBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataAttributeCallable() (deprecated)
    
    
    public final UnaryCallable<UpdateDataAttributeRequest,Operation> updateDataAttributeCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataAttributeRequest request =
           UpdateDataAttributeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataAttribute(DataAttribute.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.updateDataAttributeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAttributeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataAttributeOperationCallable() (deprecated)
    
    
    public final OperationCallable<UpdateDataAttributeRequest,DataAttribute,OperationMetadata> updateDataAttributeOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataAttribute resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataAttributeRequest request =
           UpdateDataAttributeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataAttribute(DataAttribute.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataAttribute, OperationMetadata> future =
           dataTaxonomyServiceClient.updateDataAttributeOperationCallable().futureCall(request);
       // Do something.
       DataAttribute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDataAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAttributeRequest),[DataAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAttribute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataTaxonomyAsync(DataTaxonomy dataTaxonomy, FieldMask updateMask) (deprecated)
    
    
    public final OperationFuture<DataTaxonomy,OperationMetadata> updateDataTaxonomyAsync(DataTaxonomy dataTaxonomy, FieldMask updateMask)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       DataTaxonomy dataTaxonomy = DataTaxonomy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataTaxonomy response =
           dataTaxonomyServiceClient.updateDataTaxonomyAsync(dataTaxonomy, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataTaxonomy` | `[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy)`  
Required. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataTaxonomyAsync(UpdateDataTaxonomyRequest request) (deprecated)
    
    
    public final OperationFuture<DataTaxonomy,OperationMetadata> updateDataTaxonomyAsync(UpdateDataTaxonomyRequest request)

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataTaxonomyRequest request =
           UpdateDataTaxonomyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataTaxonomy(DataTaxonomy.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataTaxonomy response = dataTaxonomyServiceClient.updateDataTaxonomyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataTaxonomyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataTaxonomyCallable() (deprecated)
    
    
    public final UnaryCallable<UpdateDataTaxonomyRequest,Operation> updateDataTaxonomyCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataTaxonomyRequest request =
           UpdateDataTaxonomyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataTaxonomy(DataTaxonomy.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataTaxonomyServiceClient.updateDataTaxonomyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataTaxonomyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataTaxonomyOperationCallable() (deprecated)
    
    
    public final OperationCallable<UpdateDataTaxonomyRequest,DataTaxonomy,OperationMetadata> updateDataTaxonomyOperationCallable()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Updates a DataTaxonomy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataTaxonomyServiceClient dataTaxonomyServiceClient = DataTaxonomyServiceClient.create()) {
       UpdateDataTaxonomyRequest request =
           UpdateDataTaxonomyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataTaxonomy(DataTaxonomy.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataTaxonomy, OperationMetadata> future =
           dataTaxonomyServiceClient.updateDataTaxonomyOperationCallable().futureCall(request);
       // Do something.
       DataTaxonomy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDataTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataTaxonomyRequest),[DataTaxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataTaxonomy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
