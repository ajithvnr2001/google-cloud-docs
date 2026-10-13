---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient
title: Class CatalogServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:18.785989+00:00
---

# Class CatalogServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CatalogServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/CatalogServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for managing catalog configuration.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       Catalog catalog = Catalog.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Catalog response = catalogServiceClient.updateCatalog(catalog, updateMask);
     }
     

Note: close() needs to be called on the CatalogServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListCatalogs |  Lists all the Catalogs associated with the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCatalogs(ListCatalogsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCatalogs(LocationName parent) 
  * listCatalogs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCatalogsPagedCallable() 
  * listCatalogsCallable() 

  
UpdateCatalog |  Updates the Catalogs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCatalog(UpdateCatalogRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCatalog(Catalog catalog, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCatalogCallable() 

  
SetDefaultBranch |  Set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default.  For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`.  Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as SearchRequest.branch to route the traffic to this staging branch.  CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one.  More specifically: 

  * PredictionService will only return product IDs from branch {newBranch}. 
  * SearchService will only return product IDs from branch {newBranch} (if branch is not explicitly set). 
  * UserEventService will only join events with products from branch {newBranch}. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setDefaultBranch(SetDefaultBranchRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setDefaultBranch(CatalogName catalog) 
  * setDefaultBranch(String catalog) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setDefaultBranchCallable() 

  
GetDefaultBranch |  Get which branch is currently default branch set by CatalogService.SetDefaultBranch method under a specified parent catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDefaultBranch(GetDefaultBranchRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDefaultBranch(CatalogName catalog) 
  * getDefaultBranch(String catalog) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDefaultBranchCallable() 

  
GetCompletionConfig |  Gets a CompletionConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCompletionConfig(GetCompletionConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCompletionConfig(CompletionConfigName name) 
  * getCompletionConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCompletionConfigCallable() 

  
UpdateCompletionConfig |  Updates the CompletionConfigs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCompletionConfig(UpdateCompletionConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCompletionConfig(CompletionConfig completionConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCompletionConfigCallable() 

  
GetAttributesConfig |  Gets an AttributesConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAttributesConfig(GetAttributesConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAttributesConfig(AttributesConfigName name) 
  * getAttributesConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAttributesConfigCallable() 

  
UpdateAttributesConfig |  Updates the AttributesConfig.  The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAttributesConfig(UpdateAttributesConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAttributesConfig(AttributesConfig attributesConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAttributesConfigCallable() 

  
AddCatalogAttribute |  Adds the specified CatalogAttribute to the AttributesConfig.  If the CatalogAttribute to add already exists, an ALREADY_EXISTS error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addCatalogAttribute(AddCatalogAttributeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addCatalogAttributeCallable() 

  
RemoveCatalogAttribute |  Removes the specified CatalogAttribute from the AttributesConfig.  If the CatalogAttribute to remove does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeCatalogAttribute(RemoveCatalogAttributeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeCatalogAttributeCallable() 

  
ReplaceCatalogAttribute |  Replaces the specified CatalogAttribute in the AttributesConfig by updating the catalog attribute with the same CatalogAttribute.key.  If the CatalogAttribute to replace does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * replaceCatalogAttribute(ReplaceCatalogAttributeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * replaceCatalogAttributeCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CatalogServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CatalogServiceSettings catalogServiceSettings =
         CatalogServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CatalogServiceClient catalogServiceClient = CatalogServiceClient.create(catalogServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CatalogServiceSettings catalogServiceSettings =
         CatalogServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CatalogServiceClient catalogServiceClient = CatalogServiceClient.create(catalogServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CatalogServiceSettings catalogServiceSettings =
         CatalogServiceSettings.newHttpJsonBuilder().build();
     CatalogServiceClient catalogServiceClient = CatalogServiceClient.create(catalogServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CatalogServiceClient

## Static Methods 

### create()
    
    
    public static final CatalogServiceClient create()

Constructs an instance of CatalogServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CatalogServiceSettings settings)
    
    
    public static final CatalogServiceClient create(CatalogServiceSettings settings)

Constructs an instance of CatalogServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CatalogServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CatalogServiceStub stub)
    
    
    public static final CatalogServiceClient create(CatalogServiceStub stub)

Constructs an instance of CatalogServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CatalogServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.CatalogServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient)` |   
  
## Constructors 

### CatalogServiceClient(CatalogServiceSettings settings)
    
    
    protected CatalogServiceClient(CatalogServiceSettings settings)

Constructs an instance of CatalogServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CatalogServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceSettings)`  
  
  
### CatalogServiceClient(CatalogServiceStub stub)
    
    
    protected CatalogServiceClient(CatalogServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.CatalogServiceStub)`  
  
  
## Methods 

### addCatalogAttribute(AddCatalogAttributeRequest request)
    
    
    public final AttributesConfig addCatalogAttribute(AddCatalogAttributeRequest request)

Adds the specified CatalogAttribute to the AttributesConfig.

If the CatalogAttribute to add already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       AddCatalogAttributeRequest request =
           AddCatalogAttributeRequest.newBuilder()
               .setAttributesConfig(
                   AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setCatalogAttribute(CatalogAttribute.newBuilder().build())
               .build();
       AttributesConfig response = catalogServiceClient.addCatalogAttribute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddCatalogAttributeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)` |   
  
### addCatalogAttributeCallable()
    
    
    public final UnaryCallable<AddCatalogAttributeRequest,AttributesConfig> addCatalogAttributeCallable()

Adds the specified CatalogAttribute to the AttributesConfig.

If the CatalogAttribute to add already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       AddCatalogAttributeRequest request =
           AddCatalogAttributeRequest.newBuilder()
               .setAttributesConfig(
                   AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setCatalogAttribute(CatalogAttribute.newBuilder().build())
               .build();
       ApiFuture<AttributesConfig> future =
           catalogServiceClient.addCatalogAttributeCallable().futureCall(request);
       // Do something.
       AttributesConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddCatalogAttributeRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
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

### getAttributesConfig(@Nullable AttributesConfigName name)
    
    
    public final AttributesConfig getAttributesConfig(@Nullable AttributesConfigName name)

Gets an AttributesConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       AttributesConfigName name = AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       AttributesConfig response = catalogServiceClient.getAttributesConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.AttributesConfigName`  
Required. Full AttributesConfig resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/attributesConfig`  
**Returns**  
---  
**Type** | **Description**  
`[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)` |   
  
### getAttributesConfig(GetAttributesConfigRequest request)
    
    
    public final AttributesConfig getAttributesConfig(GetAttributesConfigRequest request)

Gets an AttributesConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetAttributesConfigRequest request =
           GetAttributesConfigRequest.newBuilder()
               .setName(AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       AttributesConfig response = catalogServiceClient.getAttributesConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAttributesConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetAttributesConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)` |   
  
### getAttributesConfig(String name)
    
    
    public final AttributesConfig getAttributesConfig(String name)

Gets an AttributesConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       AttributesConfig response = catalogServiceClient.getAttributesConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full AttributesConfig resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/attributesConfig`  
**Returns**  
---  
**Type** | **Description**  
`[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)` |   
  
### getAttributesConfigCallable()
    
    
    public final UnaryCallable<GetAttributesConfigRequest,AttributesConfig> getAttributesConfigCallable()

Gets an AttributesConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetAttributesConfigRequest request =
           GetAttributesConfigRequest.newBuilder()
               .setName(AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       ApiFuture<AttributesConfig> future =
           catalogServiceClient.getAttributesConfigCallable().futureCall(request);
       // Do something.
       AttributesConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAttributesConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetAttributesConfigRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### getCompletionConfig(@Nullable CompletionConfigName name)
    
    
    public final CompletionConfig getCompletionConfig(@Nullable CompletionConfigName name)

Gets a CompletionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CompletionConfigName name = CompletionConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       CompletionConfig response = catalogServiceClient.getCompletionConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CompletionConfigName`  
Required. Full CompletionConfig resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/completionConfig`  
**Returns**  
---  
**Type** | **Description**  
`[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)` |   
  
### getCompletionConfig(GetCompletionConfigRequest request)
    
    
    public final CompletionConfig getCompletionConfig(GetCompletionConfigRequest request)

Gets a CompletionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetCompletionConfigRequest request =
           GetCompletionConfigRequest.newBuilder()
               .setName(CompletionConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       CompletionConfig response = catalogServiceClient.getCompletionConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCompletionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetCompletionConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)` |   
  
### getCompletionConfig(String name)
    
    
    public final CompletionConfig getCompletionConfig(String name)

Gets a CompletionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String name = CompletionConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       CompletionConfig response = catalogServiceClient.getCompletionConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full CompletionConfig resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/completionConfig`  
**Returns**  
---  
**Type** | **Description**  
`[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)` |   
  
### getCompletionConfigCallable()
    
    
    public final UnaryCallable<GetCompletionConfigRequest,CompletionConfig> getCompletionConfigCallable()

Gets a CompletionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetCompletionConfigRequest request =
           GetCompletionConfigRequest.newBuilder()
               .setName(CompletionConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       ApiFuture<CompletionConfig> future =
           catalogServiceClient.getCompletionConfigCallable().futureCall(request);
       // Do something.
       CompletionConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCompletionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetCompletionConfigRequest),[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)>` |   
  
### getDefaultBranch(@Nullable CatalogName catalog)
    
    
    public final GetDefaultBranchResponse getDefaultBranch(@Nullable CatalogName catalog)

Get which branch is currently default branch set by CatalogService.SetDefaultBranch method under a specified parent catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CatalogName catalog = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       GetDefaultBranchResponse response = catalogServiceClient.getDefaultBranch(catalog);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`catalog` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
The parent catalog resource name, such as `projects/*/locations/global/catalogs/default_catalog`.  
**Returns**  
---  
**Type** | **Description**  
`[GetDefaultBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetDefaultBranchResponse)` |   
  
### getDefaultBranch(GetDefaultBranchRequest request)
    
    
    public final GetDefaultBranchResponse getDefaultBranch(GetDefaultBranchRequest request)

Get which branch is currently default branch set by CatalogService.SetDefaultBranch method under a specified parent catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetDefaultBranchRequest request =
           GetDefaultBranchRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       GetDefaultBranchResponse response = catalogServiceClient.getDefaultBranch(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDefaultBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetDefaultBranchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GetDefaultBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetDefaultBranchResponse)` |   
  
### getDefaultBranch(String catalog)
    
    
    public final GetDefaultBranchResponse getDefaultBranch(String catalog)

Get which branch is currently default branch set by CatalogService.SetDefaultBranch method under a specified parent catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String catalog = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       GetDefaultBranchResponse response = catalogServiceClient.getDefaultBranch(catalog);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`catalog` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent catalog resource name, such as `projects/*/locations/global/catalogs/default_catalog`.  
**Returns**  
---  
**Type** | **Description**  
`[GetDefaultBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetDefaultBranchResponse)` |   
  
### getDefaultBranchCallable()
    
    
    public final UnaryCallable<GetDefaultBranchRequest,GetDefaultBranchResponse> getDefaultBranchCallable()

Get which branch is currently default branch set by CatalogService.SetDefaultBranch method under a specified parent catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       GetDefaultBranchRequest request =
           GetDefaultBranchRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       ApiFuture<GetDefaultBranchResponse> future =
           catalogServiceClient.getDefaultBranchCallable().futureCall(request);
       // Do something.
       GetDefaultBranchResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDefaultBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetDefaultBranchRequest),[GetDefaultBranchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetDefaultBranchResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable CatalogServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogServiceSettings` |   
  
### getStub()
    
    
    public CatalogServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.CatalogServiceStub)` |   
  
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
  
### listCatalogs(@Nullable LocationName parent)
    
    
    public final CatalogServiceClient.ListCatalogsPagedResponse listCatalogs(@Nullable LocationName parent)

Lists all the Catalogs associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Catalog element : catalogServiceClient.listCatalogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.LocationName`  
Required. The account resource name with an associated location. If the caller does not have permission to list Catalogs under this location, regardless of whether or not this location exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient.ListCatalogsPagedResponse)` |   
  
### listCatalogs(ListCatalogsRequest request)
    
    
    public final CatalogServiceClient.ListCatalogsPagedResponse listCatalogs(ListCatalogsRequest request)

Lists all the Catalogs associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListCatalogsRequest request =
           ListCatalogsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Catalog element : catalogServiceClient.listCatalogs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListCatalogsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient.ListCatalogsPagedResponse)` |   
  
### listCatalogs(String parent)
    
    
    public final CatalogServiceClient.ListCatalogsPagedResponse listCatalogs(String parent)

Lists all the Catalogs associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Catalog element : catalogServiceClient.listCatalogs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The account resource name with an associated location. If the caller does not have permission to list Catalogs under this location, regardless of whether or not this location exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[CatalogServiceClient.ListCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient.ListCatalogsPagedResponse)` |   
  
### listCatalogsCallable()
    
    
    public final UnaryCallable<ListCatalogsRequest,ListCatalogsResponse> listCatalogsCallable()

Lists all the Catalogs associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListCatalogsRequest request =
           ListCatalogsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListCatalogsResponse response = catalogServiceClient.listCatalogsCallable().call(request);
         for (Catalog element : response.getCatalogsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListCatalogsRequest),[ListCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListCatalogsResponse)>` |   
  
### listCatalogsPagedCallable()
    
    
    public final UnaryCallable<ListCatalogsRequest,CatalogServiceClient.ListCatalogsPagedResponse> listCatalogsPagedCallable()

Lists all the Catalogs associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ListCatalogsRequest request =
           ListCatalogsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Catalog> future =
           catalogServiceClient.listCatalogsPagedCallable().futureCall(request);
       // Do something.
       for (Catalog element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListCatalogsRequest),[ListCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CatalogServiceClient.ListCatalogsPagedResponse)>` |   
  
### removeCatalogAttribute(RemoveCatalogAttributeRequest request)
    
    
    public final AttributesConfig removeCatalogAttribute(RemoveCatalogAttributeRequest request)

Removes the specified CatalogAttribute from the AttributesConfig.

If the CatalogAttribute to remove does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       RemoveCatalogAttributeRequest request =
           RemoveCatalogAttributeRequest.newBuilder()
               .setAttributesConfig(
                   AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setKey("key106079")
               .build();
       AttributesConfig response = catalogServiceClient.removeCatalogAttribute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveCatalogAttributeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)` |   
  
### removeCatalogAttributeCallable()
    
    
    public final UnaryCallable<RemoveCatalogAttributeRequest,AttributesConfig> removeCatalogAttributeCallable()

Removes the specified CatalogAttribute from the AttributesConfig.

If the CatalogAttribute to remove does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       RemoveCatalogAttributeRequest request =
           RemoveCatalogAttributeRequest.newBuilder()
               .setAttributesConfig(
                   AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setKey("key106079")
               .build();
       ApiFuture<AttributesConfig> future =
           catalogServiceClient.removeCatalogAttributeCallable().futureCall(request);
       // Do something.
       AttributesConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveCatalogAttributeRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### replaceCatalogAttribute(ReplaceCatalogAttributeRequest request)
    
    
    public final AttributesConfig replaceCatalogAttribute(ReplaceCatalogAttributeRequest request)

Replaces the specified CatalogAttribute in the AttributesConfig by updating the catalog attribute with the same CatalogAttribute.key.

If the CatalogAttribute to replace does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ReplaceCatalogAttributeRequest request =
           ReplaceCatalogAttributeRequest.newBuilder()
               .setAttributesConfig(
                   AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setCatalogAttribute(CatalogAttribute.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AttributesConfig response = catalogServiceClient.replaceCatalogAttribute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReplaceCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ReplaceCatalogAttributeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)` |   
  
### replaceCatalogAttributeCallable()
    
    
    public final UnaryCallable<ReplaceCatalogAttributeRequest,AttributesConfig> replaceCatalogAttributeCallable()

Replaces the specified CatalogAttribute in the AttributesConfig by updating the catalog attribute with the same CatalogAttribute.key.

If the CatalogAttribute to replace does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       ReplaceCatalogAttributeRequest request =
           ReplaceCatalogAttributeRequest.newBuilder()
               .setAttributesConfig(
                   AttributesConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setCatalogAttribute(CatalogAttribute.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AttributesConfig> future =
           catalogServiceClient.replaceCatalogAttributeCallable().futureCall(request);
       // Do something.
       AttributesConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReplaceCatalogAttributeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ReplaceCatalogAttributeRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### setDefaultBranch(@Nullable CatalogName catalog)
    
    
    public final void setDefaultBranch(@Nullable CatalogName catalog)

Set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default.

For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`.

Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as SearchRequest.branch to route the traffic to this staging branch.

CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one.

More specifically:

  * PredictionService will only return product IDs from branch {newBranch}. 
  * SearchService will only return product IDs from branch {newBranch} (if branch is not explicitly set). 
  * UserEventService will only join events with products from branch {newBranch}. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CatalogName catalog = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       catalogServiceClient.setDefaultBranch(catalog);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`catalog` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Full resource name of the catalog, such as `projects/*/locations/global/catalogs/default_catalog`.  
  
### setDefaultBranch(SetDefaultBranchRequest request)
    
    
    public final void setDefaultBranch(SetDefaultBranchRequest request)

Set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default.

For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`.

Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as SearchRequest.branch to route the traffic to this staging branch.

CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one.

More specifically:

  * PredictionService will only return product IDs from branch {newBranch}. 
  * SearchService will only return product IDs from branch {newBranch} (if branch is not explicitly set). 
  * UserEventService will only join events with products from branch {newBranch}. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       SetDefaultBranchRequest request =
           SetDefaultBranchRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setBranchId(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setNote("note3387378")
               .setForce(true)
               .build();
       catalogServiceClient.setDefaultBranch(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetDefaultBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetDefaultBranchRequest)`  
The request object containing all of the parameters for the API call.  
  
### setDefaultBranch(String catalog)
    
    
    public final void setDefaultBranch(String catalog)

Set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default.

For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`.

Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as SearchRequest.branch to route the traffic to this staging branch.

CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one.

More specifically:

  * PredictionService will only return product IDs from branch {newBranch}. 
  * SearchService will only return product IDs from branch {newBranch} (if branch is not explicitly set). 
  * UserEventService will only join events with products from branch {newBranch}. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       String catalog = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       catalogServiceClient.setDefaultBranch(catalog);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`catalog` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Full resource name of the catalog, such as `projects/*/locations/global/catalogs/default_catalog`.  
  
### setDefaultBranchCallable()
    
    
    public final UnaryCallable<SetDefaultBranchRequest,Empty> setDefaultBranchCallable()

Set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default.

For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`.

Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as SearchRequest.branch to route the traffic to this staging branch.

CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one.

More specifically:

  * PredictionService will only return product IDs from branch {newBranch}. 
  * SearchService will only return product IDs from branch {newBranch} (if branch is not explicitly set). 
  * UserEventService will only join events with products from branch {newBranch}. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       SetDefaultBranchRequest request =
           SetDefaultBranchRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setBranchId(
                   BranchName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[BRANCH]").toString())
               .setNote("note3387378")
               .setForce(true)
               .build();
       ApiFuture<Empty> future = catalogServiceClient.setDefaultBranchCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetDefaultBranchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.SetDefaultBranchRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAttributesConfig(AttributesConfig attributesConfig, FieldMask updateMask)
    
    
    public final AttributesConfig updateAttributesConfig(AttributesConfig attributesConfig, FieldMask updateMask)

Updates the AttributesConfig.

The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       AttributesConfig attributesConfig = AttributesConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AttributesConfig response =
           catalogServiceClient.updateAttributesConfig(attributesConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`attributesConfig` | `[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)`  
Required. The AttributesConfig to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided AttributesConfig to update. The following is the only supported field: 

  * AttributesConfig.catalog_attributes

If not set, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)` |   
  
### updateAttributesConfig(UpdateAttributesConfigRequest request)
    
    
    public final AttributesConfig updateAttributesConfig(UpdateAttributesConfigRequest request)

Updates the AttributesConfig.

The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateAttributesConfigRequest request =
           UpdateAttributesConfigRequest.newBuilder()
               .setAttributesConfig(AttributesConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AttributesConfig response = catalogServiceClient.updateAttributesConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAttributesConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateAttributesConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)` |   
  
### updateAttributesConfigCallable()
    
    
    public final UnaryCallable<UpdateAttributesConfigRequest,AttributesConfig> updateAttributesConfigCallable()

Updates the AttributesConfig.

The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateAttributesConfigRequest request =
           UpdateAttributesConfigRequest.newBuilder()
               .setAttributesConfig(AttributesConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AttributesConfig> future =
           catalogServiceClient.updateAttributesConfigCallable().futureCall(request);
       // Do something.
       AttributesConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAttributesConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateAttributesConfigRequest),[AttributesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AttributesConfig)>` |   
  
### updateCatalog(Catalog catalog, FieldMask updateMask)
    
    
    public final Catalog updateCatalog(Catalog catalog, FieldMask updateMask)

Updates the Catalogs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       Catalog catalog = Catalog.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Catalog response = catalogServiceClient.updateCatalog(catalog, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`catalog` | `[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Catalog)`  
Required. The Catalog to update. If the caller does not have permission to update the Catalog, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the Catalog to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided Catalog to update. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Catalog)` |   
  
### updateCatalog(UpdateCatalogRequest request)
    
    
    public final Catalog updateCatalog(UpdateCatalogRequest request)

Updates the Catalogs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateCatalogRequest request =
           UpdateCatalogRequest.newBuilder()
               .setCatalog(Catalog.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Catalog response = catalogServiceClient.updateCatalog(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateCatalogRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Catalog)` |   
  
### updateCatalogCallable()
    
    
    public final UnaryCallable<UpdateCatalogRequest,Catalog> updateCatalogCallable()

Updates the Catalogs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateCatalogRequest request =
           UpdateCatalogRequest.newBuilder()
               .setCatalog(Catalog.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Catalog> future = catalogServiceClient.updateCatalogCallable().futureCall(request);
       // Do something.
       Catalog response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateCatalogRequest),[Catalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Catalog)>` |   
  
### updateCompletionConfig(CompletionConfig completionConfig, FieldMask updateMask)
    
    
    public final CompletionConfig updateCompletionConfig(CompletionConfig completionConfig, FieldMask updateMask)

Updates the CompletionConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       CompletionConfig completionConfig = CompletionConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CompletionConfig response =
           catalogServiceClient.updateCompletionConfig(completionConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`completionConfig` | `[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)`  
Required. The CompletionConfig to update. If the caller does not have permission to update the CompletionConfig, then a PERMISSION_DENIED error is returned. If the CompletionConfig to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided CompletionConfig to update. The following are the only supported fields: 

  * CompletionConfig.matching_order
  * CompletionConfig.max_suggestions
  * CompletionConfig.min_prefix_length
  * CompletionConfig.auto_learning

If not set, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)` |   
  
### updateCompletionConfig(UpdateCompletionConfigRequest request)
    
    
    public final CompletionConfig updateCompletionConfig(UpdateCompletionConfigRequest request)

Updates the CompletionConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateCompletionConfigRequest request =
           UpdateCompletionConfigRequest.newBuilder()
               .setCompletionConfig(CompletionConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CompletionConfig response = catalogServiceClient.updateCompletionConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCompletionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateCompletionConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)` |   
  
### updateCompletionConfigCallable()
    
    
    public final UnaryCallable<UpdateCompletionConfigRequest,CompletionConfig> updateCompletionConfigCallable()

Updates the CompletionConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CatalogServiceClient catalogServiceClient = CatalogServiceClient.create()) {
       UpdateCompletionConfigRequest request =
           UpdateCompletionConfigRequest.newBuilder()
               .setCompletionConfig(CompletionConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CompletionConfig> future =
           catalogServiceClient.updateCompletionConfigCallable().futureCall(request);
       // Do something.
       CompletionConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCompletionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateCompletionConfigRequest),[CompletionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CompletionConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
