---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient
title: Class ServingConfigServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:26.098215+00:00
---

# Class ServingConfigServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ServingConfigServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/ServingConfigServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for modifying ServingConfig.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       ServingConfig servingConfig = ServingConfig.newBuilder().build();
       String servingConfigId = "servingConfigId-831052759";
       ServingConfig response =
           servingConfigServiceClient.createServingConfig(parent, servingConfig, servingConfigId);
     }
     

Note: close() needs to be called on the ServingConfigServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateServingConfig |  Creates a ServingConfig.  A maximum of 100 ServingConfigs are allowed in a Catalog, otherwise a FAILED_PRECONDITION error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServingConfig(CreateServingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createServingConfig(CatalogName parent, ServingConfig servingConfig, String servingConfigId) 
  * createServingConfig(String parent, ServingConfig servingConfig, String servingConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServingConfigCallable() 

  
DeleteServingConfig |  Deletes a ServingConfig.  Returns a NotFound error if the ServingConfig does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServingConfig(DeleteServingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteServingConfig(ServingConfigName name) 
  * deleteServingConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServingConfigCallable() 

  
UpdateServingConfig |  Updates a ServingConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServingConfig(UpdateServingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateServingConfig(ServingConfig servingConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServingConfigCallable() 

  
GetServingConfig |  Gets a ServingConfig.  Returns a NotFound error if the ServingConfig does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServingConfig(GetServingConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServingConfig(ServingConfigName name) 
  * getServingConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServingConfigCallable() 

  
ListServingConfigs |  Lists all ServingConfigs linked to this catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServingConfigs(ListServingConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServingConfigs(CatalogName parent) 
  * listServingConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServingConfigsPagedCallable() 
  * listServingConfigsCallable() 

  
AddControl |  Enables a Control on the specified ServingConfig. The control is added in the last position of the list of controls it belongs to (e.g. if it's a facet spec control it will be applied in the last position of servingConfig.facetSpecIds) Returns a ALREADY_EXISTS error if the control has already been applied. Returns a FAILED_PRECONDITION error if the addition could exceed maximum number of control allowed for that type of control. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addControl(AddControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * addControl(ServingConfigName servingConfig) 
  * addControl(String servingConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addControlCallable() 

  
RemoveControl |  Disables a Control on the specified ServingConfig. The control is removed from the ServingConfig. Returns a NOT_FOUND error if the Control is not enabled for the ServingConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeControl(RemoveControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * removeControl(ServingConfigName servingConfig) 
  * removeControl(String servingConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeControlCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ServingConfigServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ServingConfigServiceSettings servingConfigServiceSettings =
         ServingConfigServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create(servingConfigServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ServingConfigServiceSettings servingConfigServiceSettings =
         ServingConfigServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create(servingConfigServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ServingConfigServiceSettings servingConfigServiceSettings =
         ServingConfigServiceSettings.newHttpJsonBuilder().build();
     ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create(servingConfigServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ServingConfigServiceClient

## Static Methods 

### create()
    
    
    public static final ServingConfigServiceClient create()

Constructs an instance of ServingConfigServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ServingConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ServingConfigServiceSettings settings)
    
    
    public static final ServingConfigServiceClient create(ServingConfigServiceSettings settings)

Constructs an instance of ServingConfigServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ServingConfigServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ServingConfigServiceStub stub)
    
    
    public static final ServingConfigServiceClient create(ServingConfigServiceStub stub)

Constructs an instance of ServingConfigServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ServingConfigServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ServingConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ServingConfigServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient)` |   
  
## Constructors 

### ServingConfigServiceClient(ServingConfigServiceSettings settings)
    
    
    protected ServingConfigServiceClient(ServingConfigServiceSettings settings)

Constructs an instance of ServingConfigServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ServingConfigServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceSettings)`  
  
  
### ServingConfigServiceClient(ServingConfigServiceStub stub)
    
    
    protected ServingConfigServiceClient(ServingConfigServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ServingConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ServingConfigServiceStub)`  
  
  
## Methods 

### addControl(@Nullable ServingConfigName servingConfig)
    
    
    public final ServingConfig addControl(@Nullable ServingConfigName servingConfig)

Enables a Control on the specified ServingConfig. The control is added in the last position of the list of controls it belongs to (e.g. if it's a facet spec control it will be applied in the last position of servingConfig.facetSpecIds) Returns a ALREADY_EXISTS error if the control has already been applied. Returns a FAILED_PRECONDITION error if the addition could exceed maximum number of control allowed for that type of control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       ServingConfigName servingConfig =
           ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]");
       ServingConfig response = servingConfigServiceClient.addControl(servingConfig);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`servingConfig` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ServingConfigName`  
Required. The source ServingConfig resource name . Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### addControl(AddControlRequest request)
    
    
    public final ServingConfig addControl(AddControlRequest request)

Enables a Control on the specified ServingConfig. The control is added in the last position of the list of controls it belongs to (e.g. if it's a facet spec control it will be applied in the last position of servingConfig.facetSpecIds) Returns a ALREADY_EXISTS error if the control has already been applied. Returns a FAILED_PRECONDITION error if the addition could exceed maximum number of control allowed for that type of control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       AddControlRequest request =
           AddControlRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
                       .toString())
               .setControlId("controlId-395080872")
               .build();
       ServingConfig response = servingConfigServiceClient.addControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### addControl(String servingConfig)
    
    
    public final ServingConfig addControl(String servingConfig)

Enables a Control on the specified ServingConfig. The control is added in the last position of the list of controls it belongs to (e.g. if it's a facet spec control it will be applied in the last position of servingConfig.facetSpecIds) Returns a ALREADY_EXISTS error if the control has already been applied. Returns a FAILED_PRECONDITION error if the addition could exceed maximum number of control allowed for that type of control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       String servingConfig =
           ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
               .toString();
       ServingConfig response = servingConfigServiceClient.addControl(servingConfig);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`servingConfig` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The source ServingConfig resource name . Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### addControlCallable()
    
    
    public final UnaryCallable<AddControlRequest,ServingConfig> addControlCallable()

Enables a Control on the specified ServingConfig. The control is added in the last position of the list of controls it belongs to (e.g. if it's a facet spec control it will be applied in the last position of servingConfig.facetSpecIds) Returns a ALREADY_EXISTS error if the control has already been applied. Returns a FAILED_PRECONDITION error if the addition could exceed maximum number of control allowed for that type of control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       AddControlRequest request =
           AddControlRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
                       .toString())
               .setControlId("controlId-395080872")
               .build();
       ApiFuture<ServingConfig> future =
           servingConfigServiceClient.addControlCallable().futureCall(request);
       // Do something.
       ServingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.AddControlRequest),[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)>` |   
  
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

### createServingConfig(@Nullable CatalogName parent, ServingConfig servingConfig, String servingConfigId)
    
    
    public final ServingConfig createServingConfig(@Nullable CatalogName parent, ServingConfig servingConfig, String servingConfigId)

Creates a ServingConfig.

A maximum of 100 ServingConfigs are allowed in a Catalog, otherwise a FAILED_PRECONDITION error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       ServingConfig servingConfig = ServingConfig.newBuilder().build();
       String servingConfigId = "servingConfigId-831052759";
       ServingConfig response =
           servingConfigServiceClient.createServingConfig(parent, servingConfig, servingConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Required. Full resource name of parent. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
`servingConfig` | `[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)`  
Required. The ServingConfig to create.  
`servingConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the ServingConfig, which will become the final component of the ServingConfig's resource name. This value should be 4-63 characters, and valid characters are /a-z-_/.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### createServingConfig(CreateServingConfigRequest request)
    
    
    public final ServingConfig createServingConfig(CreateServingConfigRequest request)

Creates a ServingConfig.

A maximum of 100 ServingConfigs are allowed in a Catalog, otherwise a FAILED_PRECONDITION error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       CreateServingConfigRequest request =
           CreateServingConfigRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setServingConfig(ServingConfig.newBuilder().build())
               .setServingConfigId("servingConfigId-831052759")
               .build();
       ServingConfig response = servingConfigServiceClient.createServingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateServingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### createServingConfig(String parent, ServingConfig servingConfig, String servingConfigId)
    
    
    public final ServingConfig createServingConfig(String parent, ServingConfig servingConfig, String servingConfigId)

Creates a ServingConfig.

A maximum of 100 ServingConfigs are allowed in a Catalog, otherwise a FAILED_PRECONDITION error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       ServingConfig servingConfig = ServingConfig.newBuilder().build();
       String servingConfigId = "servingConfigId-831052759";
       ServingConfig response =
           servingConfigServiceClient.createServingConfig(parent, servingConfig, servingConfigId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of parent. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
`servingConfig` | `[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)`  
Required. The ServingConfig to create.  
`servingConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the ServingConfig, which will become the final component of the ServingConfig's resource name. This value should be 4-63 characters, and valid characters are /a-z-_/.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### createServingConfigCallable()
    
    
    public final UnaryCallable<CreateServingConfigRequest,ServingConfig> createServingConfigCallable()

Creates a ServingConfig.

A maximum of 100 ServingConfigs are allowed in a Catalog, otherwise a FAILED_PRECONDITION error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       CreateServingConfigRequest request =
           CreateServingConfigRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setServingConfig(ServingConfig.newBuilder().build())
               .setServingConfigId("servingConfigId-831052759")
               .build();
       ApiFuture<ServingConfig> future =
           servingConfigServiceClient.createServingConfigCallable().futureCall(request);
       // Do something.
       ServingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.CreateServingConfigRequest),[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)>` |   
  
### deleteServingConfig(@Nullable ServingConfigName name)
    
    
    public final void deleteServingConfig(@Nullable ServingConfigName name)

Deletes a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       ServingConfigName name =
           ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]");
       servingConfigServiceClient.deleteServingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ServingConfigName`  
Required. The resource name of the ServingConfig to delete. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}`  
  
### deleteServingConfig(DeleteServingConfigRequest request)
    
    
    public final void deleteServingConfig(DeleteServingConfigRequest request)

Deletes a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       DeleteServingConfigRequest request =
           DeleteServingConfigRequest.newBuilder()
               .setName(
                   ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
                       .toString())
               .build();
       servingConfigServiceClient.deleteServingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.DeleteServingConfigRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteServingConfig(String name)
    
    
    public final void deleteServingConfig(String name)

Deletes a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       String name =
           ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
               .toString();
       servingConfigServiceClient.deleteServingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ServingConfig to delete. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}`  
  
### deleteServingConfigCallable()
    
    
    public final UnaryCallable<DeleteServingConfigRequest,Empty> deleteServingConfigCallable()

Deletes a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       DeleteServingConfigRequest request =
           DeleteServingConfigRequest.newBuilder()
               .setName(
                   ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           servingConfigServiceClient.deleteServingConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.DeleteServingConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getServingConfig(@Nullable ServingConfigName name)
    
    
    public final ServingConfig getServingConfig(@Nullable ServingConfigName name)

Gets a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       ServingConfigName name =
           ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]");
       ServingConfig response = servingConfigServiceClient.getServingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ServingConfigName`  
Required. The resource name of the ServingConfig to get. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### getServingConfig(GetServingConfigRequest request)
    
    
    public final ServingConfig getServingConfig(GetServingConfigRequest request)

Gets a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       GetServingConfigRequest request =
           GetServingConfigRequest.newBuilder()
               .setName(
                   ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
                       .toString())
               .build();
       ServingConfig response = servingConfigServiceClient.getServingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetServingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### getServingConfig(String name)
    
    
    public final ServingConfig getServingConfig(String name)

Gets a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       String name =
           ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
               .toString();
       ServingConfig response = servingConfigServiceClient.getServingConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ServingConfig to get. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### getServingConfigCallable()
    
    
    public final UnaryCallable<GetServingConfigRequest,ServingConfig> getServingConfigCallable()

Gets a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       GetServingConfigRequest request =
           GetServingConfigRequest.newBuilder()
               .setName(
                   ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
                       .toString())
               .build();
       ApiFuture<ServingConfig> future =
           servingConfigServiceClient.getServingConfigCallable().futureCall(request);
       // Do something.
       ServingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetServingConfigRequest),[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)>` |   
  
### getSettings()
    
    
    public final @Nullable ServingConfigServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ServingConfigServiceSettings` |   
  
### getStub()
    
    
    public ServingConfigServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ServingConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.ServingConfigServiceStub)` |   
  
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
  
### listServingConfigs(@Nullable CatalogName parent)
    
    
    public final ServingConfigServiceClient.ListServingConfigsPagedResponse listServingConfigs(@Nullable CatalogName parent)

Lists all ServingConfigs linked to this catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       for (ServingConfig element :
           servingConfigServiceClient.listServingConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Required. The catalog resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfigServiceClient.ListServingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient.ListServingConfigsPagedResponse)` |   
  
### listServingConfigs(ListServingConfigsRequest request)
    
    
    public final ServingConfigServiceClient.ListServingConfigsPagedResponse listServingConfigs(ListServingConfigsRequest request)

Lists all ServingConfigs linked to this catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       ListServingConfigsRequest request =
           ListServingConfigsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ServingConfig element :
           servingConfigServiceClient.listServingConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListServingConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfigServiceClient.ListServingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient.ListServingConfigsPagedResponse)` |   
  
### listServingConfigs(String parent)
    
    
    public final ServingConfigServiceClient.ListServingConfigsPagedResponse listServingConfigs(String parent)

Lists all ServingConfigs linked to this catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       for (ServingConfig element :
           servingConfigServiceClient.listServingConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The catalog resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfigServiceClient.ListServingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient.ListServingConfigsPagedResponse)` |   
  
### listServingConfigsCallable()
    
    
    public final UnaryCallable<ListServingConfigsRequest,ListServingConfigsResponse> listServingConfigsCallable()

Lists all ServingConfigs linked to this catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       ListServingConfigsRequest request =
           ListServingConfigsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListServingConfigsResponse response =
             servingConfigServiceClient.listServingConfigsCallable().call(request);
         for (ServingConfig element : response.getServingConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListServingConfigsRequest),[ListServingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListServingConfigsResponse)>` |   
  
### listServingConfigsPagedCallable()
    
    
    public final UnaryCallable<ListServingConfigsRequest,ServingConfigServiceClient.ListServingConfigsPagedResponse> listServingConfigsPagedCallable()

Lists all ServingConfigs linked to this catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       ListServingConfigsRequest request =
           ListServingConfigsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ServingConfig> future =
           servingConfigServiceClient.listServingConfigsPagedCallable().futureCall(request);
       // Do something.
       for (ServingConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListServingConfigsRequest),[ListServingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfigServiceClient.ListServingConfigsPagedResponse)>` |   
  
### removeControl(@Nullable ServingConfigName servingConfig)
    
    
    public final ServingConfig removeControl(@Nullable ServingConfigName servingConfig)

Disables a Control on the specified ServingConfig. The control is removed from the ServingConfig. Returns a NOT_FOUND error if the Control is not enabled for the ServingConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       ServingConfigName servingConfig =
           ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]");
       ServingConfig response = servingConfigServiceClient.removeControl(servingConfig);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`servingConfig` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.ServingConfigName`  
Required. The source ServingConfig resource name . Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### removeControl(RemoveControlRequest request)
    
    
    public final ServingConfig removeControl(RemoveControlRequest request)

Disables a Control on the specified ServingConfig. The control is removed from the ServingConfig. Returns a NOT_FOUND error if the Control is not enabled for the ServingConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       RemoveControlRequest request =
           RemoveControlRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
                       .toString())
               .setControlId("controlId-395080872")
               .build();
       ServingConfig response = servingConfigServiceClient.removeControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### removeControl(String servingConfig)
    
    
    public final ServingConfig removeControl(String servingConfig)

Disables a Control on the specified ServingConfig. The control is removed from the ServingConfig. Returns a NOT_FOUND error if the Control is not enabled for the ServingConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       String servingConfig =
           ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
               .toString();
       ServingConfig response = servingConfigServiceClient.removeControl(servingConfig);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`servingConfig` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The source ServingConfig resource name . Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### removeControlCallable()
    
    
    public final UnaryCallable<RemoveControlRequest,ServingConfig> removeControlCallable()

Disables a Control on the specified ServingConfig. The control is removed from the ServingConfig. Returns a NOT_FOUND error if the Control is not enabled for the ServingConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       RemoveControlRequest request =
           RemoveControlRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.of("[PROJECT]", "[LOCATION]", "[CATALOG]", "[SERVING_CONFIG]")
                       .toString())
               .setControlId("controlId-395080872")
               .build();
       ApiFuture<ServingConfig> future =
           servingConfigServiceClient.removeControlCallable().futureCall(request);
       // Do something.
       ServingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.RemoveControlRequest),[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateServingConfig(ServingConfig servingConfig, FieldMask updateMask)
    
    
    public final ServingConfig updateServingConfig(ServingConfig servingConfig, FieldMask updateMask)

Updates a ServingConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       ServingConfig servingConfig = ServingConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ServingConfig response =
           servingConfigServiceClient.updateServingConfig(servingConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`servingConfig` | `[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)`  
Required. The ServingConfig to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided ServingConfig to update. The following are NOT supported: 

  * ServingConfig.name

If not set, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### updateServingConfig(UpdateServingConfigRequest request)
    
    
    public final ServingConfig updateServingConfig(UpdateServingConfigRequest request)

Updates a ServingConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       UpdateServingConfigRequest request =
           UpdateServingConfigRequest.newBuilder()
               .setServingConfig(ServingConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ServingConfig response = servingConfigServiceClient.updateServingConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateServingConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)` |   
  
### updateServingConfigCallable()
    
    
    public final UnaryCallable<UpdateServingConfigRequest,ServingConfig> updateServingConfigCallable()

Updates a ServingConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ServingConfigServiceClient servingConfigServiceClient =
         ServingConfigServiceClient.create()) {
       UpdateServingConfigRequest request =
           UpdateServingConfigRequest.newBuilder()
               .setServingConfig(ServingConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ServingConfig> future =
           servingConfigServiceClient.updateServingConfigCallable().futureCall(request);
       // Do something.
       ServingConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateServingConfigRequest),[ServingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ServingConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
