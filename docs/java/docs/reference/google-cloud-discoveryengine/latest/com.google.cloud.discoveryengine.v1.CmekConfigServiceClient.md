---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfigServiceClient
title: Class CmekConfigServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:24.556706+00:00
---

# Class CmekConfigServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfigServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CmekConfigServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/CmekConfigServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for managing CMEK related tasks

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       CmekConfigName name = CmekConfigName.ofProjectLocationName("[PROJECT]", "[LOCATION]");
       CmekConfig response = cmekConfigServiceClient.getCmekConfig(name);
     }
     

Note: close() needs to be called on the CmekConfigServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
UpdateCmekConfig |  Provisions a CMEK key for use in a location of a customer's project. This method will also conduct location validation on the provided cmekConfig to make sure the key is valid and can be used in the selected location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCmekConfigAsync(UpdateCmekConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateCmekConfigAsync(CmekConfig config) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCmekConfigOperationCallable() 
  * updateCmekConfigCallable() 

  
GetCmekConfig |  Gets the CmekConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCmekConfig(GetCmekConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCmekConfig(CmekConfigName name) 
  * getCmekConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCmekConfigCallable() 

  
ListCmekConfigs |  Lists all the CmekConfigs with the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCmekConfigs(ListCmekConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCmekConfigs(LocationName parent) 
  * listCmekConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCmekConfigsCallable() 

  
DeleteCmekConfig |  De-provisions a CmekConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCmekConfigAsync(DeleteCmekConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteCmekConfigAsync(CmekConfigName name) 
  * deleteCmekConfigAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCmekConfigOperationCallable() 
  * deleteCmekConfigCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CmekConfigServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmekConfigServiceSettings cmekConfigServiceSettings =
         CmekConfigServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CmekConfigServiceClient cmekConfigServiceClient =
         CmekConfigServiceClient.create(cmekConfigServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmekConfigServiceSettings cmekConfigServiceSettings =
         CmekConfigServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CmekConfigServiceClient cmekConfigServiceClient =
         CmekConfigServiceClient.create(cmekConfigServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmekConfigServiceSettings cmekConfigServiceSettings =
         CmekConfigServiceSettings.newHttpJsonBuilder().build();
     CmekConfigServiceClient cmekConfigServiceClient =
         CmekConfigServiceClient.create(cmekConfigServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CmekConfigServiceClient

## Static Methods 

### create()
    
    
    public static final CmekConfigServiceClient create()

Constructs an instance of CmekConfigServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CmekConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfigServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmekConfigServiceSettings settings)
    
    
    public static final CmekConfigServiceClient create(CmekConfigServiceSettings settings)

Constructs an instance of CmekConfigServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmekConfigServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfigServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfigServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmekConfigServiceStub stub)
    
    
    public static final CmekConfigServiceClient create(CmekConfigServiceStub stub)

Constructs an instance of CmekConfigServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CmekConfigServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmekConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.CmekConfigServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfigServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfigServiceClient)` |   
  
## Constructors 

### CmekConfigServiceClient(CmekConfigServiceSettings settings)
    
    
    protected CmekConfigServiceClient(CmekConfigServiceSettings settings)

Constructs an instance of CmekConfigServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmekConfigServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfigServiceSettings)`  
  
  
### CmekConfigServiceClient(CmekConfigServiceStub stub)
    
    
    protected CmekConfigServiceClient(CmekConfigServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmekConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.CmekConfigServiceStub)`  
  
  
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

### deleteCmekConfigAsync(@Nullable CmekConfigName name)
    
    
    public final OperationFuture<Empty,DeleteCmekConfigMetadata> deleteCmekConfigAsync(@Nullable CmekConfigName name)

De-provisions a CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       CmekConfigName name =
           CmekConfigName.ofProjectLocationCmekConfigName(
               "[PROJECT]", "[LOCATION]", "[CMEK_CONFIG]");
       cmekConfigServiceClient.deleteCmekConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.CmekConfigName`  
Required. The resource name of the CmekConfig to delete, such as `projects/{project}/locations/{location}/cmekConfigs/{cmek_config}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteCmekConfigMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteCmekConfigMetadata)>` |   
  
### deleteCmekConfigAsync(DeleteCmekConfigRequest request)
    
    
    public final OperationFuture<Empty,DeleteCmekConfigMetadata> deleteCmekConfigAsync(DeleteCmekConfigRequest request)

De-provisions a CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       DeleteCmekConfigRequest request =
           DeleteCmekConfigRequest.newBuilder()
               .setName(
                   CmekConfigName.ofProjectLocationCmekConfigName(
                           "[PROJECT]", "[LOCATION]", "[CMEK_CONFIG]")
                       .toString())
               .build();
       cmekConfigServiceClient.deleteCmekConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteCmekConfigMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteCmekConfigMetadata)>` |   
  
### deleteCmekConfigAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteCmekConfigMetadata> deleteCmekConfigAsync(String name)

De-provisions a CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       String name = CmekConfigName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString();
       cmekConfigServiceClient.deleteCmekConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CmekConfig to delete, such as `projects/{project}/locations/{location}/cmekConfigs/{cmek_config}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteCmekConfigMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteCmekConfigMetadata)>` |   
  
### deleteCmekConfigCallable()
    
    
    public final UnaryCallable<DeleteCmekConfigRequest,Operation> deleteCmekConfigCallable()

De-provisions a CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       DeleteCmekConfigRequest request =
           DeleteCmekConfigRequest.newBuilder()
               .setName(
                   CmekConfigName.ofProjectLocationCmekConfigName(
                           "[PROJECT]", "[LOCATION]", "[CMEK_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           cmekConfigServiceClient.deleteCmekConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteCmekConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCmekConfigOperationCallable()
    
    
    public final OperationCallable<DeleteCmekConfigRequest,Empty,DeleteCmekConfigMetadata> deleteCmekConfigOperationCallable()

De-provisions a CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       DeleteCmekConfigRequest request =
           DeleteCmekConfigRequest.newBuilder()
               .setName(
                   CmekConfigName.ofProjectLocationCmekConfigName(
                           "[PROJECT]", "[LOCATION]", "[CMEK_CONFIG]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteCmekConfigMetadata> future =
           cmekConfigServiceClient.deleteCmekConfigOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteCmekConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteCmekConfigMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteCmekConfigMetadata)>` |   
  
### getCmekConfig(@Nullable CmekConfigName name)
    
    
    public final CmekConfig getCmekConfig(@Nullable CmekConfigName name)

Gets the CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       CmekConfigName name = CmekConfigName.ofProjectLocationName("[PROJECT]", "[LOCATION]");
       CmekConfig response = cmekConfigServiceClient.getCmekConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.CmekConfigName`  
Required. Resource name of CmekConfig, such as `projects/*/locations/*/cmekConfig` or `projects/*/locations/*/cmekConfigs/*`. If the caller does not have permission to access the CmekConfig, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfig)` |   
  
### getCmekConfig(GetCmekConfigRequest request)
    
    
    public final CmekConfig getCmekConfig(GetCmekConfigRequest request)

Gets the CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       GetCmekConfigRequest request =
           GetCmekConfigRequest.newBuilder()
               .setName(CmekConfigName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString())
               .build();
       CmekConfig response = cmekConfigServiceClient.getCmekConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfig)` |   
  
### getCmekConfig(String name)
    
    
    public final CmekConfig getCmekConfig(String name)

Gets the CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       String name = CmekConfigName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString();
       CmekConfig response = cmekConfigServiceClient.getCmekConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of CmekConfig, such as `projects/*/locations/*/cmekConfig` or `projects/*/locations/*/cmekConfigs/*`. If the caller does not have permission to access the CmekConfig, regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfig)` |   
  
### getCmekConfigCallable()
    
    
    public final UnaryCallable<GetCmekConfigRequest,CmekConfig> getCmekConfigCallable()

Gets the CmekConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       GetCmekConfigRequest request =
           GetCmekConfigRequest.newBuilder()
               .setName(CmekConfigName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<CmekConfig> future =
           cmekConfigServiceClient.getCmekConfigCallable().futureCall(request);
       // Do something.
       CmekConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetCmekConfigRequest),[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfig)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable CmekConfigServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.CmekConfigServiceSettings` |   
  
### getStub()
    
    
    public CmekConfigServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CmekConfigServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.CmekConfigServiceStub)` |   
  
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
  
### listCmekConfigs(@Nullable LocationName parent)
    
    
    public final ListCmekConfigsResponse listCmekConfigs(@Nullable LocationName parent)

Lists all the CmekConfigs with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ListCmekConfigsResponse response = cmekConfigServiceClient.listCmekConfigs(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.LocationName`  
Required. The parent location resource name, such as `projects/{project}/locations/{location}`. If the caller does not have permission to list CmekConfigs under this location, regardless of whether or not a CmekConfig exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[ListCmekConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCmekConfigsResponse)` |   
  
### listCmekConfigs(ListCmekConfigsRequest request)
    
    
    public final ListCmekConfigsResponse listCmekConfigs(ListCmekConfigsRequest request)

Lists all the CmekConfigs with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       ListCmekConfigsRequest request =
           ListCmekConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ListCmekConfigsResponse response = cmekConfigServiceClient.listCmekConfigs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCmekConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCmekConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCmekConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCmekConfigsResponse)` |   
  
### listCmekConfigs(String parent)
    
    
    public final ListCmekConfigsResponse listCmekConfigs(String parent)

Lists all the CmekConfigs with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ListCmekConfigsResponse response = cmekConfigServiceClient.listCmekConfigs(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent location resource name, such as `projects/{project}/locations/{location}`. If the caller does not have permission to list CmekConfigs under this location, regardless of whether or not a CmekConfig exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[ListCmekConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCmekConfigsResponse)` |   
  
### listCmekConfigsCallable()
    
    
    public final UnaryCallable<ListCmekConfigsRequest,ListCmekConfigsResponse> listCmekConfigsCallable()

Lists all the CmekConfigs with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       ListCmekConfigsRequest request =
           ListCmekConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<ListCmekConfigsResponse> future =
           cmekConfigServiceClient.listCmekConfigsCallable().futureCall(request);
       // Do something.
       ListCmekConfigsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCmekConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCmekConfigsRequest),[ListCmekConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListCmekConfigsResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCmekConfigAsync(CmekConfig config)
    
    
    public final OperationFuture<CmekConfig,UpdateCmekConfigMetadata> updateCmekConfigAsync(CmekConfig config)

Provisions a CMEK key for use in a location of a customer's project. This method will also conduct location validation on the provided cmekConfig to make sure the key is valid and can be used in the selected location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       CmekConfig config = CmekConfig.newBuilder().build();
       CmekConfig response = cmekConfigServiceClient.updateCmekConfigAsync(config).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`config` | `[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfig)`  
Required. The CmekConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfig),[UpdateCmekConfigMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateCmekConfigMetadata)>` |   
  
### updateCmekConfigAsync(UpdateCmekConfigRequest request)
    
    
    public final OperationFuture<CmekConfig,UpdateCmekConfigMetadata> updateCmekConfigAsync(UpdateCmekConfigRequest request)

Provisions a CMEK key for use in a location of a customer's project. This method will also conduct location validation on the provided cmekConfig to make sure the key is valid and can be used in the selected location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       UpdateCmekConfigRequest request =
           UpdateCmekConfigRequest.newBuilder()
               .setConfig(CmekConfig.newBuilder().build())
               .setSetDefault(true)
               .build();
       CmekConfig response = cmekConfigServiceClient.updateCmekConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateCmekConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfig),[UpdateCmekConfigMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateCmekConfigMetadata)>` |   
  
### updateCmekConfigCallable()
    
    
    public final UnaryCallable<UpdateCmekConfigRequest,Operation> updateCmekConfigCallable()

Provisions a CMEK key for use in a location of a customer's project. This method will also conduct location validation on the provided cmekConfig to make sure the key is valid and can be used in the selected location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       UpdateCmekConfigRequest request =
           UpdateCmekConfigRequest.newBuilder()
               .setConfig(CmekConfig.newBuilder().build())
               .setSetDefault(true)
               .build();
       ApiFuture<Operation> future =
           cmekConfigServiceClient.updateCmekConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateCmekConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCmekConfigOperationCallable()
    
    
    public final OperationCallable<UpdateCmekConfigRequest,CmekConfig,UpdateCmekConfigMetadata> updateCmekConfigOperationCallable()

Provisions a CMEK key for use in a location of a customer's project. This method will also conduct location validation on the provided cmekConfig to make sure the key is valid and can be used in the selected location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekConfigServiceClient cmekConfigServiceClient = CmekConfigServiceClient.create()) {
       UpdateCmekConfigRequest request =
           UpdateCmekConfigRequest.newBuilder()
               .setConfig(CmekConfig.newBuilder().build())
               .setSetDefault(true)
               .build();
       OperationFuture<CmekConfig, UpdateCmekConfigMetadata> future =
           cmekConfigServiceClient.updateCmekConfigOperationCallable().futureCall(request);
       // Do something.
       CmekConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateCmekConfigRequest),[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CmekConfig),[UpdateCmekConfigMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateCmekConfigMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
