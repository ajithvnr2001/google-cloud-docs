---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient
title: Class DataProductServiceClient (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:32:09.027511+00:00
---

# Class DataProductServiceClient (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataProductServiceClient (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataplex/google-cloud-dataplex/src/main/java/com/google/cloud/dataplex/v1/DataProductServiceClient.java)| [Product Reference](https://cloud.google.com/dataplex)| [REST Documentation](https://cloud.google.com/dataplex/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataplex/docs/reference/rpc)  
---|---|---|---  
  
Service Description: `DataProductService` provides APIs for managing data products and the underlying data assets.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataProductName name = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]");
       DataProduct response = dataProductServiceClient.getDataProduct(name);
     }
     

Note: close() needs to be called on the DataProductServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDataProduct |  Creates a data product. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataProductAsync(CreateDataProductRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDataProductAsync(LocationName parent, DataProduct dataProduct, String dataProductId) 
  * createDataProductAsync(String parent, DataProduct dataProduct, String dataProductId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataProductOperationCallable() 
  * createDataProductCallable() 

  
DeleteDataProduct |  Deletes a data product. The deletion will fail if the data product is not empty (i.e. contains at least one data asset). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataProductAsync(DeleteDataProductRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDataProductAsync(DataProductName name) 
  * deleteDataProductAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataProductOperationCallable() 
  * deleteDataProductCallable() 

  
GetDataProduct |  Gets a data product. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataProduct(GetDataProductRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataProduct(DataProductName name) 
  * getDataProduct(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataProductCallable() 

  
ListDataProducts |  Lists data products for a given project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataProducts(ListDataProductsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataProducts(LocationName parent) 
  * listDataProducts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataProductsPagedCallable() 
  * listDataProductsCallable() 

  
UpdateDataProduct |  Updates a data product. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataProductAsync(UpdateDataProductRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDataProductAsync(DataProduct dataProduct, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataProductOperationCallable() 
  * updateDataProductCallable() 

  
RequestDataProductAccess |  Requests access to a data product. This will trigger an access approval workflow, and the requester will need to wait for the approval to be granted before they will be able to access the data product assets. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * requestDataProductAccess(DataProductName parent, ChangeRequest changeRequest) 
  * requestDataProductAccess(String parent, ChangeRequest changeRequest) 
  * requestDataProductAccess(RequestDataProductAccessRequest request) 
  * requestDataProductAccessCallable() 

  
CreateDataAsset |  Creates a data asset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataAssetAsync(CreateDataAssetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDataAssetAsync(DataProductName parent, DataAsset dataAsset, String dataAssetId) 
  * createDataAssetAsync(String parent, DataAsset dataAsset, String dataAssetId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataAssetOperationCallable() 
  * createDataAssetCallable() 

  
UpdateDataAsset |  Updates a data asset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataAssetAsync(UpdateDataAssetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDataAssetAsync(DataAsset dataAsset, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataAssetOperationCallable() 
  * updateDataAssetCallable() 

  
DeleteDataAsset |  Deletes a data asset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataAssetAsync(DeleteDataAssetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDataAssetAsync(DataAssetName name) 
  * deleteDataAssetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataAssetOperationCallable() 
  * deleteDataAssetCallable() 

  
GetDataAsset |  Gets a data asset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataAsset(GetDataAssetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataAsset(DataAssetName name) 
  * getDataAsset(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataAssetCallable() 

  
ListDataAssets |  Lists data assets for a given data product. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataAssets(ListDataAssetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataAssets(DataProductName parent) 
  * listDataAssets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataAssetsPagedCallable() 
  * listDataAssetsCallable() 

  
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

This class can be customized by passing in a custom instance of DataProductServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataProductServiceSettings dataProductServiceSettings =
         DataProductServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataProductServiceClient dataProductServiceClient =
         DataProductServiceClient.create(dataProductServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataProductServiceSettings dataProductServiceSettings =
         DataProductServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataProductServiceClient dataProductServiceClient =
         DataProductServiceClient.create(dataProductServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataProductServiceSettings dataProductServiceSettings =
         DataProductServiceSettings.newHttpJsonBuilder().build();
     DataProductServiceClient dataProductServiceClient =
         DataProductServiceClient.create(dataProductServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataProductServiceClient

## Static Methods 

### create()
    
    
    public static final DataProductServiceClient create()

Constructs an instance of DataProductServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataProductServiceSettings settings)
    
    
    public static final DataProductServiceClient create(DataProductServiceSettings settings)

Constructs an instance of DataProductServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataProductServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataProductServiceStub stub)
    
    
    public static final DataProductServiceClient create(DataProductServiceStub stub)

Constructs an instance of DataProductServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataProductServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataProductServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataProductServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient)` |   
  
## Constructors 

### DataProductServiceClient(DataProductServiceSettings settings)
    
    
    protected DataProductServiceClient(DataProductServiceSettings settings)

Constructs an instance of DataProductServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataProductServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceSettings)`  
  
  
### DataProductServiceClient(DataProductServiceStub stub)
    
    
    protected DataProductServiceClient(DataProductServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataProductServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataProductServiceStub)`  
  
  
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

### createDataAssetAsync(@Nullable DataProductName parent, DataAsset dataAsset, String dataAssetId)
    
    
    public final OperationFuture<DataAsset,OperationMetadata> createDataAssetAsync(@Nullable DataProductName parent, DataAsset dataAsset, String dataAssetId)

Creates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataProductName parent = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]");
       DataAsset dataAsset = DataAsset.newBuilder().build();
       String dataAssetId = "dataAssetId2108984609";
       DataAsset response =
           dataProductServiceClient.createDataAssetAsync(parent, dataAsset, dataAssetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataProductName`  
Required. The parent resource where this data asset will be created. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}  
`dataAsset` | `[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset)`  
Required. The data asset to create.  
`dataAssetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID of the data asset to create. The ID must conform to RFC-1034 and contain only lower-case letters (a-z), numbers (0-9), or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum. Characters outside of ASCII are not permitted. Valid format regex: `^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$` If not provided, a system generated ID will be used.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAssetAsync(CreateDataAssetRequest request)
    
    
    public final OperationFuture<DataAsset,OperationMetadata> createDataAssetAsync(CreateDataAssetRequest request)

Creates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       CreateDataAssetRequest request =
           CreateDataAssetRequest.newBuilder()
               .setParent(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setDataAssetId("dataAssetId2108984609")
               .setDataAsset(DataAsset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataAsset response = dataProductServiceClient.createDataAssetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAssetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAssetAsync(String parent, DataAsset dataAsset, String dataAssetId)
    
    
    public final OperationFuture<DataAsset,OperationMetadata> createDataAssetAsync(String parent, DataAsset dataAsset, String dataAssetId)

Creates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String parent = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString();
       DataAsset dataAsset = DataAsset.newBuilder().build();
       String dataAssetId = "dataAssetId2108984609";
       DataAsset response =
           dataProductServiceClient.createDataAssetAsync(parent, dataAsset, dataAssetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this data asset will be created. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}  
`dataAsset` | `[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset)`  
Required. The data asset to create.  
`dataAssetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID of the data asset to create. The ID must conform to RFC-1034 and contain only lower-case letters (a-z), numbers (0-9), or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum. Characters outside of ASCII are not permitted. Valid format regex: `^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$` If not provided, a system generated ID will be used.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataAssetCallable()
    
    
    public final UnaryCallable<CreateDataAssetRequest,Operation> createDataAssetCallable()

Creates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       CreateDataAssetRequest request =
           CreateDataAssetRequest.newBuilder()
               .setParent(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setDataAssetId("dataAssetId2108984609")
               .setDataAsset(DataAsset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataProductServiceClient.createDataAssetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataAssetOperationCallable()
    
    
    public final OperationCallable<CreateDataAssetRequest,DataAsset,OperationMetadata> createDataAssetOperationCallable()

Creates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       CreateDataAssetRequest request =
           CreateDataAssetRequest.newBuilder()
               .setParent(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setDataAssetId("dataAssetId2108984609")
               .setDataAsset(DataAsset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataAsset, OperationMetadata> future =
           dataProductServiceClient.createDataAssetOperationCallable().futureCall(request);
       // Do something.
       DataAsset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAssetRequest),[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataProductAsync(@Nullable LocationName parent, DataProduct dataProduct, String dataProductId)
    
    
    public final OperationFuture<DataProduct,OperationMetadata> createDataProductAsync(@Nullable LocationName parent, DataProduct dataProduct, String dataProductId)

Creates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DataProduct dataProduct = DataProduct.newBuilder().build();
       String dataProductId = "dataProductId1437828576";
       DataProduct response =
           dataProductServiceClient.createDataProductAsync(parent, dataProduct, dataProductId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The parent resource where this data product will be created. Format: projects/{project_id_or_number}/locations/{location_id}  
`dataProduct` | `[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct)`  
Required. The data product to create.  
`dataProductId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID of the data product to create. The ID must conform to RFC-1034 and contain only lower-case letters (a-z), numbers (0-9), or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum. Characters outside of ASCII are not permitted. Valid format regex: `^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$` If not provided, a system generated ID will be used.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataProductAsync(CreateDataProductRequest request)
    
    
    public final OperationFuture<DataProduct,OperationMetadata> createDataProductAsync(CreateDataProductRequest request)

Creates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       CreateDataProductRequest request =
           CreateDataProductRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataProductId("dataProductId1437828576")
               .setDataProduct(DataProduct.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataProduct response = dataProductServiceClient.createDataProductAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataProductAsync(String parent, DataProduct dataProduct, String dataProductId)
    
    
    public final OperationFuture<DataProduct,OperationMetadata> createDataProductAsync(String parent, DataProduct dataProduct, String dataProductId)

Creates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DataProduct dataProduct = DataProduct.newBuilder().build();
       String dataProductId = "dataProductId1437828576";
       DataProduct response =
           dataProductServiceClient.createDataProductAsync(parent, dataProduct, dataProductId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this data product will be created. Format: projects/{project_id_or_number}/locations/{location_id}  
`dataProduct` | `[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct)`  
Required. The data product to create.  
`dataProductId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID of the data product to create. The ID must conform to RFC-1034 and contain only lower-case letters (a-z), numbers (0-9), or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum. Characters outside of ASCII are not permitted. Valid format regex: `^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$` If not provided, a system generated ID will be used.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createDataProductCallable()
    
    
    public final UnaryCallable<CreateDataProductRequest,Operation> createDataProductCallable()

Creates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       CreateDataProductRequest request =
           CreateDataProductRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataProductId("dataProductId1437828576")
               .setDataProduct(DataProduct.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataProductServiceClient.createDataProductCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataProductRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataProductOperationCallable()
    
    
    public final OperationCallable<CreateDataProductRequest,DataProduct,OperationMetadata> createDataProductOperationCallable()

Creates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       CreateDataProductRequest request =
           CreateDataProductRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataProductId("dataProductId1437828576")
               .setDataProduct(DataProduct.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataProduct, OperationMetadata> future =
           dataProductServiceClient.createDataProductOperationCallable().futureCall(request);
       // Do something.
       DataProduct response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataProductRequest),[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAssetAsync(@Nullable DataAssetName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAssetAsync(@Nullable DataAssetName name)

Deletes a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataAssetName name =
           DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]");
       dataProductServiceClient.deleteDataAssetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataAssetName`  
Required. The name of the data asset to delete. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAssetAsync(DeleteDataAssetRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAssetAsync(DeleteDataAssetRequest request)

Deletes a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DeleteDataAssetRequest request =
           DeleteDataAssetRequest.newBuilder()
               .setName(
                   DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]")
                       .toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       dataProductServiceClient.deleteDataAssetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAssetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAssetAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataAssetAsync(String name)

Deletes a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String name =
           DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]").toString();
       dataProductServiceClient.deleteDataAssetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the data asset to delete. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataAssetCallable()
    
    
    public final UnaryCallable<DeleteDataAssetRequest,Operation> deleteDataAssetCallable()

Deletes a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DeleteDataAssetRequest request =
           DeleteDataAssetRequest.newBuilder()
               .setName(
                   DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]")
                       .toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataProductServiceClient.deleteDataAssetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataAssetOperationCallable()
    
    
    public final OperationCallable<DeleteDataAssetRequest,Empty,OperationMetadata> deleteDataAssetOperationCallable()

Deletes a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DeleteDataAssetRequest request =
           DeleteDataAssetRequest.newBuilder()
               .setName(
                   DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]")
                       .toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataProductServiceClient.deleteDataAssetOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAssetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataProductAsync(@Nullable DataProductName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataProductAsync(@Nullable DataProductName name)

Deletes a data product. The deletion will fail if the data product is not empty (i.e. contains at least one data asset).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataProductName name = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]");
       dataProductServiceClient.deleteDataProductAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataProductName`  
Required. The name of the data product to delete. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataProductAsync(DeleteDataProductRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataProductAsync(DeleteDataProductRequest request)

Deletes a data product. The deletion will fail if the data product is not empty (i.e. contains at least one data asset).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DeleteDataProductRequest request =
           DeleteDataProductRequest.newBuilder()
               .setName(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       dataProductServiceClient.deleteDataProductAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataProductAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteDataProductAsync(String name)

Deletes a data product. The deletion will fail if the data product is not empty (i.e. contains at least one data asset).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String name = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString();
       dataProductServiceClient.deleteDataProductAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the data product to delete. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteDataProductCallable()
    
    
    public final UnaryCallable<DeleteDataProductRequest,Operation> deleteDataProductCallable()

Deletes a data product. The deletion will fail if the data product is not empty (i.e. contains at least one data asset).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DeleteDataProductRequest request =
           DeleteDataProductRequest.newBuilder()
               .setName(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataProductServiceClient.deleteDataProductCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataProductRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataProductOperationCallable()
    
    
    public final OperationCallable<DeleteDataProductRequest,Empty,OperationMetadata> deleteDataProductOperationCallable()

Deletes a data product. The deletion will fail if the data product is not empty (i.e. contains at least one data asset).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DeleteDataProductRequest request =
           DeleteDataProductRequest.newBuilder()
               .setName(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataProductServiceClient.deleteDataProductOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataProductRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### getDataAsset(@Nullable DataAssetName name)
    
    
    public final DataAsset getDataAsset(@Nullable DataAssetName name)

Gets a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataAssetName name =
           DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]");
       DataAsset response = dataProductServiceClient.getDataAsset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataAssetName`  
Required. The name of the data asset to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset)` |   
  
### getDataAsset(GetDataAssetRequest request)
    
    
    public final DataAsset getDataAsset(GetDataAssetRequest request)

Gets a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       GetDataAssetRequest request =
           GetDataAssetRequest.newBuilder()
               .setName(
                   DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]")
                       .toString())
               .build();
       DataAsset response = dataProductServiceClient.getDataAsset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataAssetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset)` |   
  
### getDataAsset(String name)
    
    
    public final DataAsset getDataAsset(String name)

Gets a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String name =
           DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]").toString();
       DataAsset response = dataProductServiceClient.getDataAsset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the data asset to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset)` |   
  
### getDataAssetCallable()
    
    
    public final UnaryCallable<GetDataAssetRequest,DataAsset> getDataAssetCallable()

Gets a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       GetDataAssetRequest request =
           GetDataAssetRequest.newBuilder()
               .setName(
                   DataAssetName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]")
                       .toString())
               .build();
       ApiFuture<DataAsset> future =
           dataProductServiceClient.getDataAssetCallable().futureCall(request);
       // Do something.
       DataAsset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataAssetRequest),[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset)>` |   
  
### getDataProduct(@Nullable DataProductName name)
    
    
    public final DataProduct getDataProduct(@Nullable DataProductName name)

Gets a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataProductName name = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]");
       DataProduct response = dataProductServiceClient.getDataProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataProductName`  
Required. The name of the data product to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct)` |   
  
### getDataProduct(GetDataProductRequest request)
    
    
    public final DataProduct getDataProduct(GetDataProductRequest request)

Gets a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       GetDataProductRequest request =
           GetDataProductRequest.newBuilder()
               .setName(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .build();
       DataProduct response = dataProductServiceClient.getDataProduct(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct)` |   
  
### getDataProduct(String name)
    
    
    public final DataProduct getDataProduct(String name)

Gets a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String name = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString();
       DataProduct response = dataProductServiceClient.getDataProduct(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the data product to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct)` |   
  
### getDataProductCallable()
    
    
    public final UnaryCallable<GetDataProductRequest,DataProduct> getDataProductCallable()

Gets a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       GetDataProductRequest request =
           GetDataProductRequest.newBuilder()
               .setName(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .build();
       ApiFuture<DataProduct> future =
           dataProductServiceClient.getDataProductCallable().futureCall(request);
       // Do something.
       DataProduct response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetDataProductRequest),[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct)>` |   
  
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = dataProductServiceClient.getIamPolicy(request);
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           dataProductServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataProductServiceClient.getLocation(request);
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           dataProductServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable DataProductServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataProductServiceSettings` |   
  
### getStub()
    
    
    public DataProductServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataProductServiceStub)` |   
  
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
  
### listDataAssets(@Nullable DataProductName parent)
    
    
    public final DataProductServiceClient.ListDataAssetsPagedResponse listDataAssets(@Nullable DataProductName parent)

Lists data assets for a given data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataProductName parent = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]");
       for (DataAsset element : dataProductServiceClient.listDataAssets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataProductName`  
Required. The parent, which has this collection of data assets. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient.ListDataAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListDataAssetsPagedResponse)` |   
  
### listDataAssets(ListDataAssetsRequest request)
    
    
    public final DataProductServiceClient.ListDataAssetsPagedResponse listDataAssets(ListDataAssetsRequest request)

Lists data assets for a given data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListDataAssetsRequest request =
           ListDataAssetsRequest.newBuilder()
               .setParent(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DataAsset element : dataProductServiceClient.listDataAssets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAssetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient.ListDataAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListDataAssetsPagedResponse)` |   
  
### listDataAssets(String parent)
    
    
    public final DataProductServiceClient.ListDataAssetsPagedResponse listDataAssets(String parent)

Lists data assets for a given data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String parent = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString();
       for (DataAsset element : dataProductServiceClient.listDataAssets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which has this collection of data assets. Format: projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}  
**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient.ListDataAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListDataAssetsPagedResponse)` |   
  
### listDataAssetsCallable()
    
    
    public final UnaryCallable<ListDataAssetsRequest,ListDataAssetsResponse> listDataAssetsCallable()

Lists data assets for a given data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListDataAssetsRequest request =
           ListDataAssetsRequest.newBuilder()
               .setParent(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDataAssetsResponse response =
             dataProductServiceClient.listDataAssetsCallable().call(request);
         for (DataAsset element : response.getDataAssetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAssetsRequest),[ListDataAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAssetsResponse)>` |   
  
### listDataAssetsPagedCallable()
    
    
    public final UnaryCallable<ListDataAssetsRequest,DataProductServiceClient.ListDataAssetsPagedResponse> listDataAssetsPagedCallable()

Lists data assets for a given data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListDataAssetsRequest request =
           ListDataAssetsRequest.newBuilder()
               .setParent(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DataAsset> future =
           dataProductServiceClient.listDataAssetsPagedCallable().futureCall(request);
       // Do something.
       for (DataAsset element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataAssetsRequest),[ListDataAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListDataAssetsPagedResponse)>` |   
  
### listDataProducts(@Nullable LocationName parent)
    
    
    public final DataProductServiceClient.ListDataProductsPagedResponse listDataProducts(@Nullable LocationName parent)

Lists data products for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DataProduct element : dataProductServiceClient.listDataProducts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The parent, which has this collection of data products. Format: `projects/{project_id_or_number}/locations/{location_id}`. Supports listing across all locations with the wildcard `-` (hyphen) character. Example: `projects/{project_id_or_number}/locations/-`  
**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient.ListDataProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListDataProductsPagedResponse)` |   
  
### listDataProducts(ListDataProductsRequest request)
    
    
    public final DataProductServiceClient.ListDataProductsPagedResponse listDataProducts(ListDataProductsRequest request)

Lists data products for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListDataProductsRequest request =
           ListDataProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataProduct element : dataProductServiceClient.listDataProducts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataProductsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient.ListDataProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListDataProductsPagedResponse)` |   
  
### listDataProducts(String parent)
    
    
    public final DataProductServiceClient.ListDataProductsPagedResponse listDataProducts(String parent)

Lists data products for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DataProduct element : dataProductServiceClient.listDataProducts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which has this collection of data products. Format: `projects/{project_id_or_number}/locations/{location_id}`. Supports listing across all locations with the wildcard `-` (hyphen) character. Example: `projects/{project_id_or_number}/locations/-`  
**Returns**  
---  
**Type** | **Description**  
`[DataProductServiceClient.ListDataProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListDataProductsPagedResponse)` |   
  
### listDataProductsCallable()
    
    
    public final UnaryCallable<ListDataProductsRequest,ListDataProductsResponse> listDataProductsCallable()

Lists data products for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListDataProductsRequest request =
           ListDataProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataProductsResponse response =
             dataProductServiceClient.listDataProductsCallable().call(request);
         for (DataProduct element : response.getDataProductsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataProductsRequest),[ListDataProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataProductsResponse)>` |   
  
### listDataProductsPagedCallable()
    
    
    public final UnaryCallable<ListDataProductsRequest,DataProductServiceClient.ListDataProductsPagedResponse> listDataProductsPagedCallable()

Lists data products for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListDataProductsRequest request =
           ListDataProductsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataProduct> future =
           dataProductServiceClient.listDataProductsPagedCallable().futureCall(request);
       // Do something.
       for (DataProduct element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListDataProductsRequest),[ListDataProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListDataProductsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DataProductServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataProductServiceClient.listLocations(request).iterateAll()) {
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
`[DataProductServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataProductServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DataProductServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataProductServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.ListLocationsPagedResponse)>` |   
  
### requestDataProductAccess(@Nullable DataProductName parent, ChangeRequest changeRequest)
    
    
    public final RequestDataProductAccessResponse requestDataProductAccess(@Nullable DataProductName parent, ChangeRequest changeRequest)

Requests access to a data product. This will trigger an access approval workflow, and the requester will need to wait for the approval to be granted before they will be able to access the data product assets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataProductName parent = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]");
       ChangeRequest changeRequest = ChangeRequest.newBuilder().build();
       RequestDataProductAccessResponse response =
           dataProductServiceClient.requestDataProductAccess(parent, changeRequest);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataProductName`  
Required. The resource name of the data product. Format: projects/{project_number}/locations/{location_id}/dataProducts/{data_product_id}  
`changeRequest` | `[ChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ChangeRequest)`  
Required. The change request for the data product access request.  
**Returns**  
---  
**Type** | **Description**  
`[RequestDataProductAccessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RequestDataProductAccessResponse)` |   
  
### requestDataProductAccess(RequestDataProductAccessRequest request)
    
    
    public final RequestDataProductAccessResponse requestDataProductAccess(RequestDataProductAccessRequest request)

Requests access to a data product. This will trigger an access approval workflow, and the requester will need to wait for the approval to be granted before they will be able to access the data product assets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       RequestDataProductAccessRequest request =
           RequestDataProductAccessRequest.newBuilder()
               .setParent(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setChangeRequest(ChangeRequest.newBuilder().build())
               .setValidateOnly(true)
               .build();
       RequestDataProductAccessResponse response =
           dataProductServiceClient.requestDataProductAccess(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RequestDataProductAccessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RequestDataProductAccessRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RequestDataProductAccessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RequestDataProductAccessResponse)` |   
  
### requestDataProductAccess(String parent, ChangeRequest changeRequest)
    
    
    public final RequestDataProductAccessResponse requestDataProductAccess(String parent, ChangeRequest changeRequest)

Requests access to a data product. This will trigger an access approval workflow, and the requester will need to wait for the approval to be granted before they will be able to access the data product assets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       String parent = DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString();
       ChangeRequest changeRequest = ChangeRequest.newBuilder().build();
       RequestDataProductAccessResponse response =
           dataProductServiceClient.requestDataProductAccess(parent, changeRequest);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the data product. Format: projects/{project_number}/locations/{location_id}/dataProducts/{data_product_id}  
`changeRequest` | `[ChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ChangeRequest)`  
Required. The change request for the data product access request.  
**Returns**  
---  
**Type** | **Description**  
`[RequestDataProductAccessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RequestDataProductAccessResponse)` |   
  
### requestDataProductAccessCallable()
    
    
    public final UnaryCallable<RequestDataProductAccessRequest,RequestDataProductAccessResponse> requestDataProductAccessCallable()

Requests access to a data product. This will trigger an access approval workflow, and the requester will need to wait for the approval to be granted before they will be able to access the data product assets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       RequestDataProductAccessRequest request =
           RequestDataProductAccessRequest.newBuilder()
               .setParent(DataProductName.of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
               .setChangeRequest(ChangeRequest.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<RequestDataProductAccessResponse> future =
           dataProductServiceClient.requestDataProductAccessCallable().futureCall(request);
       // Do something.
       RequestDataProductAccessResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RequestDataProductAccessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RequestDataProductAccessRequest),[RequestDataProductAccessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RequestDataProductAccessResponse)>` |   
  
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = dataProductServiceClient.setIamPolicy(request);
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           dataProductServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = dataProductServiceClient.testIamPermissions(request);
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
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           dataProductServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateDataAssetAsync(DataAsset dataAsset, FieldMask updateMask)
    
    
    public final OperationFuture<DataAsset,OperationMetadata> updateDataAssetAsync(DataAsset dataAsset, FieldMask updateMask)

Updates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataAsset dataAsset = DataAsset.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataAsset response =
           dataProductServiceClient.updateDataAssetAsync(dataAsset, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataAsset` | `[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset)`  
Required. The data asset to update. The data asset's `name` field is used to identify the data asset to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update. If this is empty or not set, then all the fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataAssetAsync(UpdateDataAssetRequest request)
    
    
    public final OperationFuture<DataAsset,OperationMetadata> updateDataAssetAsync(UpdateDataAssetRequest request)

Updates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       UpdateDataAssetRequest request =
           UpdateDataAssetRequest.newBuilder()
               .setDataAsset(DataAsset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataAsset response = dataProductServiceClient.updateDataAssetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAssetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataAssetCallable()
    
    
    public final UnaryCallable<UpdateDataAssetRequest,Operation> updateDataAssetCallable()

Updates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       UpdateDataAssetRequest request =
           UpdateDataAssetRequest.newBuilder()
               .setDataAsset(DataAsset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataProductServiceClient.updateDataAssetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataAssetOperationCallable()
    
    
    public final OperationCallable<UpdateDataAssetRequest,DataAsset,OperationMetadata> updateDataAssetOperationCallable()

Updates a data asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       UpdateDataAssetRequest request =
           UpdateDataAssetRequest.newBuilder()
               .setDataAsset(DataAsset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataAsset, OperationMetadata> future =
           dataProductServiceClient.updateDataAssetOperationCallable().futureCall(request);
       // Do something.
       DataAsset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAssetRequest),[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataProductAsync(DataProduct dataProduct, FieldMask updateMask)
    
    
    public final OperationFuture<DataProduct,OperationMetadata> updateDataProductAsync(DataProduct dataProduct, FieldMask updateMask)

Updates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       DataProduct dataProduct = DataProduct.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataProduct response =
           dataProductServiceClient.updateDataProductAsync(dataProduct, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataProduct` | `[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct)`  
Required. The data product to update. The data product's `name` field is used to identify the data product to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update. If this is empty or not set, then all the fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataProductAsync(UpdateDataProductRequest request)
    
    
    public final OperationFuture<DataProduct,OperationMetadata> updateDataProductAsync(UpdateDataProductRequest request)

Updates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       UpdateDataProductRequest request =
           UpdateDataProductRequest.newBuilder()
               .setDataProduct(DataProduct.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       DataProduct response = dataProductServiceClient.updateDataProductAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataProductRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateDataProductCallable()
    
    
    public final UnaryCallable<UpdateDataProductRequest,Operation> updateDataProductCallable()

Updates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       UpdateDataProductRequest request =
           UpdateDataProductRequest.newBuilder()
               .setDataProduct(DataProduct.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           dataProductServiceClient.updateDataProductCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataProductRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataProductOperationCallable()
    
    
    public final OperationCallable<UpdateDataProductRequest,DataProduct,OperationMetadata> updateDataProductOperationCallable()

Updates a data product.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataProductServiceClient dataProductServiceClient = DataProductServiceClient.create()) {
       UpdateDataProductRequest request =
           UpdateDataProductRequest.newBuilder()
               .setDataProduct(DataProduct.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<DataProduct, OperationMetadata> future =
           dataProductServiceClient.updateDataProductOperationCallable().futureCall(request);
       // Do something.
       DataProduct response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataProductRequest),[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
