---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient
title: Class IcebergCatalogServiceClient (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:02.997707+00:00
---

# Class IcebergCatalogServiceClient (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class IcebergCatalogServiceClient (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-biglake/google-cloud-biglake/src/main/java/com/google/cloud/biglake/v1/IcebergCatalogServiceClient.java)| [Product Reference](https://cloud.google.com/biglake)  
---|---  
  
Service Description: Lakehouse runtime catalog supports the following catalog management methods:

  * GetIcebergCatalog - ListIcebergCatalogs - DeleteIcebergCatalog - UpdateIcebergCatalog - CreateIcebergCatalog - FailoverIcebergCatalog

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (IcebergCatalogServiceClient icebergCatalogServiceClient =
          IcebergCatalogServiceClient.create()) {
        CatalogName name = CatalogName.of("[PROJECT]", "[CATALOG]");
        IcebergCatalog response = icebergCatalogServiceClient.getIcebergCatalog(name);
        }
        

Note: close() needs to be called on the IcebergCatalogServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetIcebergCatalog |  Returns the Iceberg REST Catalog configuration options. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
    * getIcebergCatalog(GetIcebergCatalogRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
    * getIcebergCatalog(CatalogName name) 
    * getIcebergCatalog(String name) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
    * getIcebergCatalogCallable()   
ListIcebergCatalogs |  Lists the Iceberg REST Catalogs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
    * listIcebergCatalogs(ListIcebergCatalogsRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
    * listIcebergCatalogs(ProjectName parent) 
    * listIcebergCatalogs(String parent) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
    * listIcebergCatalogsPagedCallable() 
    * listIcebergCatalogsCallable()   
UpdateIcebergCatalog |  Update the Iceberg REST Catalog configuration options. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
    * updateIcebergCatalog(UpdateIcebergCatalogRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
    * updateIcebergCatalog(IcebergCatalog icebergCatalog, FieldMask updateMask) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
    * updateIcebergCatalogCallable()   
CreateIcebergCatalog |  Creates the Iceberg REST Catalog. Google Cloud Storage Bucket catalog id is the bucket for which the catalog is created (e.g. `my-catalog` for `gs://my-catalog`).  If the bucket does not exist, of the caller does not have bucket metadata permissions, the catalog will not be created. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
    * createIcebergCatalog(CreateIcebergCatalogRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
    * createIcebergCatalog(ProjectName parent, IcebergCatalog icebergCatalog, String icebergCatalogId) 
    * createIcebergCatalog(String parent, IcebergCatalog icebergCatalog, String icebergCatalogId) 
    * createIcebergCatalog(ProjectName parent, IcebergCatalog icebergCatalog, String icebergCatalogId, String primaryLocation) 
    * createIcebergCatalog(String parent, IcebergCatalog icebergCatalog, String icebergCatalogId, String primaryLocation) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
    * createIcebergCatalogCallable()   
FailoverIcebergCatalog |  Failover the catalog to a new primary replica region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.
    * failoverIcebergCatalog(FailoverIcebergCatalogRequest request) 
"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.
    * failoverIcebergCatalog(String name, String primaryReplica) 
Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.
    * failoverIcebergCatalogCallable()   
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of IcebergCatalogServiceSettings to create(). For example:

To customize credentials:
    
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    IcebergCatalogServiceSettings icebergCatalogServiceSettings =
      IcebergCatalogServiceSettings.newBuilder()
          .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
          .build();
    IcebergCatalogServiceClient icebergCatalogServiceClient =
      IcebergCatalogServiceClient.create(icebergCatalogServiceSettings);
    

To customize the endpoint:
    
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    IcebergCatalogServiceSettings icebergCatalogServiceSettings =
      IcebergCatalogServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
    IcebergCatalogServiceClient icebergCatalogServiceClient =
      IcebergCatalogServiceClient.create(icebergCatalogServiceSettings);
    

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    IcebergCatalogServiceSettings icebergCatalogServiceSettings =
      IcebergCatalogServiceSettings.newHttpJsonBuilder().build();
    IcebergCatalogServiceClient icebergCatalogServiceClient =
      IcebergCatalogServiceClient.create(icebergCatalogServiceSettings);
    

Please refer to the GitHub repository's samples for more quickstart code snippets.




## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > IcebergCatalogServiceClient

## Static Methods 

### create()
    
    
    public static final IcebergCatalogServiceClient create()

Constructs an instance of IcebergCatalogServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IcebergCatalogServiceSettings settings)
    
    
    public static final IcebergCatalogServiceClient create(IcebergCatalogServiceSettings settings)

Constructs an instance of IcebergCatalogServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IcebergCatalogServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IcebergCatalogServiceStub stub)
    
    
    public static final IcebergCatalogServiceClient create(IcebergCatalogServiceStub stub)

Constructs an instance of IcebergCatalogServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(IcebergCatalogServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IcebergCatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.stub.IcebergCatalogServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient)` |   
  
## Constructors 

### IcebergCatalogServiceClient(IcebergCatalogServiceSettings settings)
    
    
    protected IcebergCatalogServiceClient(IcebergCatalogServiceSettings settings)

Constructs an instance of IcebergCatalogServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IcebergCatalogServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceSettings)`  
  
  
### IcebergCatalogServiceClient(IcebergCatalogServiceStub stub)
    
    
    protected IcebergCatalogServiceClient(IcebergCatalogServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IcebergCatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.stub.IcebergCatalogServiceStub)`  
  
  
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

### createIcebergCatalog(@Nullable ProjectName parent, IcebergCatalog icebergCatalog, String icebergCatalogId)
    
    
    public final IcebergCatalog createIcebergCatalog(@Nullable ProjectName parent, IcebergCatalog icebergCatalog, String icebergCatalogId)

Creates the Iceberg REST Catalog. Google Cloud Storage Bucket catalog id is the bucket for which the catalog is created (e.g. `my-catalog` for `gs://my-catalog`).

If the bucket does not exist, of the caller does not have bucket metadata permissions, the catalog will not be created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       IcebergCatalog icebergCatalog = IcebergCatalog.newBuilder().build();
       String icebergCatalogId = "icebergCatalogId504062865";
       IcebergCatalog response =
           icebergCatalogServiceClient.createIcebergCatalog(
               parent, icebergCatalog, icebergCatalogId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.v1.ProjectName`  
Required. The parent resource where this catalog will be created. Format: projects/{project_id}  
`icebergCatalog` | `[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)`  
Required. The catalog to create. The required fields for creation are: - catalog_type. Optionally: credential_mode can be provided, if Credential Vending is desired.  
`icebergCatalogId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the catalog.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### createIcebergCatalog(@Nullable ProjectName parent, IcebergCatalog icebergCatalog, String icebergCatalogId, String primaryLocation)
    
    
    public final IcebergCatalog createIcebergCatalog(@Nullable ProjectName parent, IcebergCatalog icebergCatalog, String icebergCatalogId, String primaryLocation)

Creates the Iceberg REST Catalog. Google Cloud Storage Bucket catalog id is the bucket for which the catalog is created (e.g. `my-catalog` for `gs://my-catalog`).

If the bucket does not exist, of the caller does not have bucket metadata permissions, the catalog will not be created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       IcebergCatalog icebergCatalog = IcebergCatalog.newBuilder().build();
       String icebergCatalogId = "icebergCatalogId504062865";
       String primaryLocation = "primaryLocation-1140723753";
       IcebergCatalog response =
           icebergCatalogServiceClient.createIcebergCatalog(
               parent, icebergCatalog, icebergCatalogId, primaryLocation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.v1.ProjectName`  
Required. The parent resource where this catalog will be created. Format: projects/{project_id}  
`icebergCatalog` | `[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)`  
Required. The catalog to create. The required fields for creation are: - catalog_type. Optionally: credential_mode can be provided, if Credential Vending is desired.  
`icebergCatalogId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the catalog.  
`primaryLocation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The primary location where the catalog metadata will be stored. For Google Cloud Storage bucket catalogs and BigLake catalogs, if this is not specified, then the region is inferred from the bucket's region (`default_location` bucket for BigLake catalogs). If specified, the region must be in jurisdiction (near the `default_location` bucket's region and the `restricted_locations` buckets' regions for BigLake catalogs). For federated catalogs, this must be specified and be a Lakehouse-supported location (<https://docs.cloud.google.com/lakehouse/docs/locations>). It should be close to the remote catalog's location for the best performance and cost.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### createIcebergCatalog(CreateIcebergCatalogRequest request)
    
    
    public final IcebergCatalog createIcebergCatalog(CreateIcebergCatalogRequest request)

Creates the Iceberg REST Catalog. Google Cloud Storage Bucket catalog id is the bucket for which the catalog is created (e.g. `my-catalog` for `gs://my-catalog`).

If the bucket does not exist, of the caller does not have bucket metadata permissions, the catalog will not be created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       CreateIcebergCatalogRequest request =
           CreateIcebergCatalogRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setIcebergCatalogId("icebergCatalogId504062865")
               .setIcebergCatalog(IcebergCatalog.newBuilder().build())
               .setPrimaryLocation("primaryLocation-1140723753")
               .build();
       IcebergCatalog response = icebergCatalogServiceClient.createIcebergCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateIcebergCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.CreateIcebergCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### createIcebergCatalog(String parent, IcebergCatalog icebergCatalog, String icebergCatalogId)
    
    
    public final IcebergCatalog createIcebergCatalog(String parent, IcebergCatalog icebergCatalog, String icebergCatalogId)

Creates the Iceberg REST Catalog. Google Cloud Storage Bucket catalog id is the bucket for which the catalog is created (e.g. `my-catalog` for `gs://my-catalog`).

If the bucket does not exist, of the caller does not have bucket metadata permissions, the catalog will not be created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       IcebergCatalog icebergCatalog = IcebergCatalog.newBuilder().build();
       String icebergCatalogId = "icebergCatalogId504062865";
       IcebergCatalog response =
           icebergCatalogServiceClient.createIcebergCatalog(
               parent, icebergCatalog, icebergCatalogId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this catalog will be created. Format: projects/{project_id}  
`icebergCatalog` | `[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)`  
Required. The catalog to create. The required fields for creation are: - catalog_type. Optionally: credential_mode can be provided, if Credential Vending is desired.  
`icebergCatalogId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the catalog.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### createIcebergCatalog(String parent, IcebergCatalog icebergCatalog, String icebergCatalogId, String primaryLocation)
    
    
    public final IcebergCatalog createIcebergCatalog(String parent, IcebergCatalog icebergCatalog, String icebergCatalogId, String primaryLocation)

Creates the Iceberg REST Catalog. Google Cloud Storage Bucket catalog id is the bucket for which the catalog is created (e.g. `my-catalog` for `gs://my-catalog`).

If the bucket does not exist, of the caller does not have bucket metadata permissions, the catalog will not be created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       IcebergCatalog icebergCatalog = IcebergCatalog.newBuilder().build();
       String icebergCatalogId = "icebergCatalogId504062865";
       String primaryLocation = "primaryLocation-1140723753";
       IcebergCatalog response =
           icebergCatalogServiceClient.createIcebergCatalog(
               parent, icebergCatalog, icebergCatalogId, primaryLocation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this catalog will be created. Format: projects/{project_id}  
`icebergCatalog` | `[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)`  
Required. The catalog to create. The required fields for creation are: - catalog_type. Optionally: credential_mode can be provided, if Credential Vending is desired.  
`icebergCatalogId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the catalog.  
`primaryLocation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The primary location where the catalog metadata will be stored. For Google Cloud Storage bucket catalogs and BigLake catalogs, if this is not specified, then the region is inferred from the bucket's region (`default_location` bucket for BigLake catalogs). If specified, the region must be in jurisdiction (near the `default_location` bucket's region and the `restricted_locations` buckets' regions for BigLake catalogs). For federated catalogs, this must be specified and be a Lakehouse-supported location (<https://docs.cloud.google.com/lakehouse/docs/locations>). It should be close to the remote catalog's location for the best performance and cost.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### createIcebergCatalogCallable()
    
    
    public final UnaryCallable<CreateIcebergCatalogRequest,IcebergCatalog> createIcebergCatalogCallable()

Creates the Iceberg REST Catalog. Google Cloud Storage Bucket catalog id is the bucket for which the catalog is created (e.g. `my-catalog` for `gs://my-catalog`).

If the bucket does not exist, of the caller does not have bucket metadata permissions, the catalog will not be created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       CreateIcebergCatalogRequest request =
           CreateIcebergCatalogRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setIcebergCatalogId("icebergCatalogId504062865")
               .setIcebergCatalog(IcebergCatalog.newBuilder().build())
               .setPrimaryLocation("primaryLocation-1140723753")
               .build();
       ApiFuture<IcebergCatalog> future =
           icebergCatalogServiceClient.createIcebergCatalogCallable().futureCall(request);
       // Do something.
       IcebergCatalog response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateIcebergCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.CreateIcebergCatalogRequest),[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)>` |   
  
### failoverIcebergCatalog(FailoverIcebergCatalogRequest request)
    
    
    public final FailoverIcebergCatalogResponse failoverIcebergCatalog(FailoverIcebergCatalogRequest request)

Failover the catalog to a new primary replica region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       FailoverIcebergCatalogRequest request =
           FailoverIcebergCatalogRequest.newBuilder()
               .setName("name3373707")
               .setPrimaryReplica("primaryReplica-389090218")
               .setValidateOnly(true)
               .setConditionalFailoverReplicationTime(Timestamp.newBuilder().build())
               .build();
       FailoverIcebergCatalogResponse response =
           icebergCatalogServiceClient.failoverIcebergCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FailoverIcebergCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.FailoverIcebergCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FailoverIcebergCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.FailoverIcebergCatalogResponse)` |   
  
### failoverIcebergCatalog(String name, String primaryReplica)
    
    
    public final FailoverIcebergCatalogResponse failoverIcebergCatalog(String name, String primaryReplica)

Failover the catalog to a new primary replica region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       String name = "name3373707";
       String primaryReplica = "primaryReplica-389090218";
       FailoverIcebergCatalogResponse response =
           icebergCatalogServiceClient.failoverIcebergCatalog(name, primaryReplica);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the catalog in the form "projects/{project_id}/catalogs/{catalog_id}"  
`primaryReplica` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The region being assigned as the new primary replica region. For example "us-east1". This must be one of the replica regions in the catalog's list of replicas marked as a "secondary".  
**Returns**  
---  
**Type** | **Description**  
`[FailoverIcebergCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.FailoverIcebergCatalogResponse)` |   
  
### failoverIcebergCatalogCallable()
    
    
    public final UnaryCallable<FailoverIcebergCatalogRequest,FailoverIcebergCatalogResponse> failoverIcebergCatalogCallable()

Failover the catalog to a new primary replica region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       FailoverIcebergCatalogRequest request =
           FailoverIcebergCatalogRequest.newBuilder()
               .setName("name3373707")
               .setPrimaryReplica("primaryReplica-389090218")
               .setValidateOnly(true)
               .setConditionalFailoverReplicationTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<FailoverIcebergCatalogResponse> future =
           icebergCatalogServiceClient.failoverIcebergCatalogCallable().futureCall(request);
       // Do something.
       FailoverIcebergCatalogResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FailoverIcebergCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.FailoverIcebergCatalogRequest),[FailoverIcebergCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.FailoverIcebergCatalogResponse)>` |   
  
### getIcebergCatalog(@Nullable CatalogName name)
    
    
    public final IcebergCatalog getIcebergCatalog(@Nullable CatalogName name)

Returns the Iceberg REST Catalog configuration options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       CatalogName name = CatalogName.of("[PROJECT]", "[CATALOG]");
       IcebergCatalog response = icebergCatalogServiceClient.getIcebergCatalog(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.v1.CatalogName`  
Required. The catalog to get.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### getIcebergCatalog(GetIcebergCatalogRequest request)
    
    
    public final IcebergCatalog getIcebergCatalog(GetIcebergCatalogRequest request)

Returns the Iceberg REST Catalog configuration options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       GetIcebergCatalogRequest request =
           GetIcebergCatalogRequest.newBuilder()
               .setName(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .build();
       IcebergCatalog response = icebergCatalogServiceClient.getIcebergCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIcebergCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.GetIcebergCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### getIcebergCatalog(String name)
    
    
    public final IcebergCatalog getIcebergCatalog(String name)

Returns the Iceberg REST Catalog configuration options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       String name = CatalogName.of("[PROJECT]", "[CATALOG]").toString();
       IcebergCatalog response = icebergCatalogServiceClient.getIcebergCatalog(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The catalog to get.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### getIcebergCatalogCallable()
    
    
    public final UnaryCallable<GetIcebergCatalogRequest,IcebergCatalog> getIcebergCatalogCallable()

Returns the Iceberg REST Catalog configuration options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       GetIcebergCatalogRequest request =
           GetIcebergCatalogRequest.newBuilder()
               .setName(CatalogName.of("[PROJECT]", "[CATALOG]").toString())
               .build();
       ApiFuture<IcebergCatalog> future =
           icebergCatalogServiceClient.getIcebergCatalogCallable().futureCall(request);
       // Do something.
       IcebergCatalog response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIcebergCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.GetIcebergCatalogRequest),[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)>` |   
  
### getSettings()
    
    
    public final @Nullable IcebergCatalogServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.biglake.v1.IcebergCatalogServiceSettings` |   
  
### getStub()
    
    
    public IcebergCatalogServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.stub.IcebergCatalogServiceStub)` |   
  
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
  
### listIcebergCatalogs(@Nullable ProjectName parent)
    
    
    public final IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse listIcebergCatalogs(@Nullable ProjectName parent)

Lists the Iceberg REST Catalogs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (IcebergCatalog element :
           icebergCatalogServiceClient.listIcebergCatalogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.biglake.v1.ProjectName`  
Required. The parent resource where this catalog will be created. Format: projects/{project_id}  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse)` |   
  
### listIcebergCatalogs(ListIcebergCatalogsRequest request)
    
    
    public final IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse listIcebergCatalogs(ListIcebergCatalogsRequest request)

Lists the Iceberg REST Catalogs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       ListIcebergCatalogsRequest request =
           ListIcebergCatalogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (IcebergCatalog element :
           icebergCatalogServiceClient.listIcebergCatalogs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListIcebergCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.ListIcebergCatalogsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse)` |   
  
### listIcebergCatalogs(String parent)
    
    
    public final IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse listIcebergCatalogs(String parent)

Lists the Iceberg REST Catalogs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (IcebergCatalog element :
           icebergCatalogServiceClient.listIcebergCatalogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this catalog will be created. Format: projects/{project_id}  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse)` |   
  
### listIcebergCatalogsCallable()
    
    
    public final UnaryCallable<ListIcebergCatalogsRequest,ListIcebergCatalogsResponse> listIcebergCatalogsCallable()

Lists the Iceberg REST Catalogs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       ListIcebergCatalogsRequest request =
           ListIcebergCatalogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListIcebergCatalogsResponse response =
             icebergCatalogServiceClient.listIcebergCatalogsCallable().call(request);
         for (IcebergCatalog element : response.getIcebergCatalogsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIcebergCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.ListIcebergCatalogsRequest),[ListIcebergCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.ListIcebergCatalogsResponse)>` |   
  
### listIcebergCatalogsPagedCallable()
    
    
    public final UnaryCallable<ListIcebergCatalogsRequest,IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse> listIcebergCatalogsPagedCallable()

Lists the Iceberg REST Catalogs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       ListIcebergCatalogsRequest request =
           ListIcebergCatalogsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<IcebergCatalog> future =
           icebergCatalogServiceClient.listIcebergCatalogsPagedCallable().futureCall(request);
       // Do something.
       for (IcebergCatalog element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIcebergCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.ListIcebergCatalogsRequest),[ListIcebergCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalogServiceClient.ListIcebergCatalogsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateIcebergCatalog(IcebergCatalog icebergCatalog, FieldMask updateMask)
    
    
    public final IcebergCatalog updateIcebergCatalog(IcebergCatalog icebergCatalog, FieldMask updateMask)

Update the Iceberg REST Catalog configuration options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       IcebergCatalog icebergCatalog = IcebergCatalog.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       IcebergCatalog response =
           icebergCatalogServiceClient.updateIcebergCatalog(icebergCatalog, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`icebergCatalog` | `[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)`  
Required. The catalog to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### updateIcebergCatalog(UpdateIcebergCatalogRequest request)
    
    
    public final IcebergCatalog updateIcebergCatalog(UpdateIcebergCatalogRequest request)

Update the Iceberg REST Catalog configuration options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       UpdateIcebergCatalogRequest request =
           UpdateIcebergCatalogRequest.newBuilder()
               .setIcebergCatalog(IcebergCatalog.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       IcebergCatalog response = icebergCatalogServiceClient.updateIcebergCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateIcebergCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.UpdateIcebergCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)` |   
  
### updateIcebergCatalogCallable()
    
    
    public final UnaryCallable<UpdateIcebergCatalogRequest,IcebergCatalog> updateIcebergCatalogCallable()

Update the Iceberg REST Catalog configuration options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IcebergCatalogServiceClient icebergCatalogServiceClient =
         IcebergCatalogServiceClient.create()) {
       UpdateIcebergCatalogRequest request =
           UpdateIcebergCatalogRequest.newBuilder()
               .setIcebergCatalog(IcebergCatalog.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<IcebergCatalog> future =
           icebergCatalogServiceClient.updateIcebergCatalogCallable().futureCall(request);
       // Do something.
       IcebergCatalog response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateIcebergCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.UpdateIcebergCatalogRequest),[IcebergCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1.IcebergCatalog)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
