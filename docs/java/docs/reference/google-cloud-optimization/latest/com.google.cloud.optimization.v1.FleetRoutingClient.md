---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.FleetRoutingClient
title: Class FleetRoutingClient (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:27.861926+00:00
---

# Class FleetRoutingClient (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.FleetRoutingClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FleetRoutingClient (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.14  0.1.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-optimization/google-cloud-optimization/src/main/java/com/google/cloud/optimization/v1/FleetRoutingClient.java)| [Product Reference](https://cloud.google.com/optimization/docs)| [REST Documentation](https://cloud.google.com/optimization/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/optimization/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for optimizing vehicle tours.

Validity of certain types of fields:

* `google.protobuf.Timestamp` * Times are in Unix time: seconds since 1970-01-01T00:00:00+00:00. * seconds must be in [0, 253402300799], i.e. in [1970-01-01T00:00:00+00:00, 9999-12-31T23:59:59+00:00]. * nanos must be unset or set to 0. * `google.protobuf.Duration` * seconds must be in [0, 253402300799], i.e. in [1970-01-01T00:00:00+00:00, 9999-12-31T23:59:59+00:00]. * nanos must be unset or set to 0. * `google.type.LatLng` * latitude must be in [-90.0, 90.0]. * longitude must be in [-180.0, 180.0]. * at least one of latitude and longitude must be non-zero.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create()) {
       OptimizeToursRequest request =
           OptimizeToursRequest.newBuilder()
               .setParent("parent-995424086")
               .setTimeout(Duration.newBuilder().build())
               .setModel(ShipmentModel.newBuilder().build())
               .addAllInjectedFirstSolutionRoutes(new ArrayList<ShipmentRoute>())
               .setInjectedSolutionConstraint(InjectedSolutionConstraint.newBuilder().build())
               .addAllRefreshDetailsRoutes(new ArrayList<ShipmentRoute>())
               .setInterpretInjectedSolutionsUsingLabels(true)
               .setConsiderRoadTraffic(true)
               .setPopulatePolylines(true)
               .setPopulateTransitionPolylines(true)
               .setAllowLargeDeadlineDespiteInterruptionRisk(true)
               .setUseGeodesicDistances(true)
               .setGeodesicMetersPerSecond(-2129658905)
               .setMaxValidationErrors(-1367418922)
               .setLabel("label102727412")
               .setPopulateTravelStepPolylines(true)
               .build();
       OptimizeToursResponse response = fleetRoutingClient.optimizeTours(request);
     }
     

Note: close() needs to be called on the FleetRoutingClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
OptimizeTours |  Sends an `OptimizeToursRequest` containing a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost.  A `ShipmentModel` model consists mainly of `Shipment`s that need to be carried out and `Vehicle`s that can be used to transport the `Shipment`s. The `ShipmentRoute`s assign `Shipment`s to `Vehicle`s. More specifically, they assign a series of `Visit`s to each vehicle, where a `Visit` corresponds to a `VisitRequest`, which is a pickup or delivery for a `Shipment`.  The goal is to provide an assignment of `ShipmentRoute`s to `Vehicle`s that minimizes the total cost where cost has many components defined in the `ShipmentModel`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * optimizeTours(OptimizeToursRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * optimizeToursCallable() 

  
BatchOptimizeTours |  Optimizes vehicle tours for one or more `OptimizeToursRequest` messages as a batch.  This method is a Long Running Operation (LRO). The inputs for optimization (`OptimizeToursRequest` messages) and outputs (`OptimizeToursResponse` messages) are read/written from/to Cloud Storage in user-specified format. Like the `OptimizeTours` method, each `OptimizeToursRequest` contains a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchOptimizeToursAsync(BatchOptimizeToursRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchOptimizeToursOperationCallable() 
  * batchOptimizeToursCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of FleetRoutingSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FleetRoutingSettings fleetRoutingSettings =
         FleetRoutingSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create(fleetRoutingSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FleetRoutingSettings fleetRoutingSettings =
         FleetRoutingSettings.newBuilder().setEndpoint(myEndpoint).build();
     FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create(fleetRoutingSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FleetRoutingSettings fleetRoutingSettings = FleetRoutingSettings.newHttpJsonBuilder().build();
     FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create(fleetRoutingSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FleetRoutingClient

## Static Methods 

### create()
    
    
    public static final FleetRoutingClient create()

Constructs an instance of FleetRoutingClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FleetRoutingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.FleetRoutingClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FleetRoutingSettings settings)
    
    
    public static final FleetRoutingClient create(FleetRoutingSettings settings)

Constructs an instance of FleetRoutingClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FleetRoutingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.FleetRoutingSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FleetRoutingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.FleetRoutingClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FleetRoutingStub stub)
    
    
    public static final FleetRoutingClient create(FleetRoutingStub stub)

Constructs an instance of FleetRoutingClient, using the given stub for making calls. This is for advanced usage - prefer using create(FleetRoutingSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FleetRoutingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.stub.FleetRoutingStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FleetRoutingClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.FleetRoutingClient)` |   
  
## Constructors 

### FleetRoutingClient(FleetRoutingSettings settings)
    
    
    protected FleetRoutingClient(FleetRoutingSettings settings)

Constructs an instance of FleetRoutingClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FleetRoutingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.FleetRoutingSettings)`  
  
  
### FleetRoutingClient(FleetRoutingStub stub)
    
    
    protected FleetRoutingClient(FleetRoutingStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FleetRoutingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.stub.FleetRoutingStub)`  
  
  
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
  
### batchOptimizeToursAsync(BatchOptimizeToursRequest request)
    
    
    public final OperationFuture<BatchOptimizeToursResponse,AsyncModelMetadata> batchOptimizeToursAsync(BatchOptimizeToursRequest request)

Optimizes vehicle tours for one or more `OptimizeToursRequest` messages as a batch.

This method is a Long Running Operation (LRO). The inputs for optimization (`OptimizeToursRequest` messages) and outputs (`OptimizeToursResponse` messages) are read/written from/to Cloud Storage in user-specified format. Like the `OptimizeTours` method, each `OptimizeToursRequest` contains a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create()) {
       BatchOptimizeToursRequest request =
           BatchOptimizeToursRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllModelConfigs(new ArrayList<BatchOptimizeToursRequest.AsyncModelConfig>())
               .build();
       BatchOptimizeToursResponse response =
           fleetRoutingClient.batchOptimizeToursAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchOptimizeToursRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.BatchOptimizeToursRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchOptimizeToursResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.BatchOptimizeToursResponse),[AsyncModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.AsyncModelMetadata)>` |   
  
### batchOptimizeToursCallable()
    
    
    public final UnaryCallable<BatchOptimizeToursRequest,Operation> batchOptimizeToursCallable()

Optimizes vehicle tours for one or more `OptimizeToursRequest` messages as a batch.

This method is a Long Running Operation (LRO). The inputs for optimization (`OptimizeToursRequest` messages) and outputs (`OptimizeToursResponse` messages) are read/written from/to Cloud Storage in user-specified format. Like the `OptimizeTours` method, each `OptimizeToursRequest` contains a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create()) {
       BatchOptimizeToursRequest request =
           BatchOptimizeToursRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllModelConfigs(new ArrayList<BatchOptimizeToursRequest.AsyncModelConfig>())
               .build();
       ApiFuture<Operation> future =
           fleetRoutingClient.batchOptimizeToursCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchOptimizeToursRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.BatchOptimizeToursRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchOptimizeToursOperationCallable()
    
    
    public final OperationCallable<BatchOptimizeToursRequest,BatchOptimizeToursResponse,AsyncModelMetadata> batchOptimizeToursOperationCallable()

Optimizes vehicle tours for one or more `OptimizeToursRequest` messages as a batch.

This method is a Long Running Operation (LRO). The inputs for optimization (`OptimizeToursRequest` messages) and outputs (`OptimizeToursResponse` messages) are read/written from/to Cloud Storage in user-specified format. Like the `OptimizeTours` method, each `OptimizeToursRequest` contains a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create()) {
       BatchOptimizeToursRequest request =
           BatchOptimizeToursRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllModelConfigs(new ArrayList<BatchOptimizeToursRequest.AsyncModelConfig>())
               .build();
       OperationFuture<BatchOptimizeToursResponse, AsyncModelMetadata> future =
           fleetRoutingClient.batchOptimizeToursOperationCallable().futureCall(request);
       // Do something.
       BatchOptimizeToursResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchOptimizeToursRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.BatchOptimizeToursRequest),[BatchOptimizeToursResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.BatchOptimizeToursResponse),[AsyncModelMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.AsyncModelMetadata)>` |   
  
### close()
    
    
    public final void close()

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
    
    
    public final @Nullable FleetRoutingSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.optimization.v1.FleetRoutingSettings` |   
  
### getStub()
    
    
    public FleetRoutingStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FleetRoutingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.stub.FleetRoutingStub)` |   
  
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
  
### optimizeTours(OptimizeToursRequest request)
    
    
    public final OptimizeToursResponse optimizeTours(OptimizeToursRequest request)

Sends an `OptimizeToursRequest` containing a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost.

A `ShipmentModel` model consists mainly of `Shipment`s that need to be carried out and `Vehicle`s that can be used to transport the `Shipment`s. The `ShipmentRoute`s assign `Shipment`s to `Vehicle`s. More specifically, they assign a series of `Visit`s to each vehicle, where a `Visit` corresponds to a `VisitRequest`, which is a pickup or delivery for a `Shipment`.

The goal is to provide an assignment of `ShipmentRoute`s to `Vehicle`s that minimizes the total cost where cost has many components defined in the `ShipmentModel`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create()) {
       OptimizeToursRequest request =
           OptimizeToursRequest.newBuilder()
               .setParent("parent-995424086")
               .setTimeout(Duration.newBuilder().build())
               .setModel(ShipmentModel.newBuilder().build())
               .addAllInjectedFirstSolutionRoutes(new ArrayList<ShipmentRoute>())
               .setInjectedSolutionConstraint(InjectedSolutionConstraint.newBuilder().build())
               .addAllRefreshDetailsRoutes(new ArrayList<ShipmentRoute>())
               .setInterpretInjectedSolutionsUsingLabels(true)
               .setConsiderRoadTraffic(true)
               .setPopulatePolylines(true)
               .setPopulateTransitionPolylines(true)
               .setAllowLargeDeadlineDespiteInterruptionRisk(true)
               .setUseGeodesicDistances(true)
               .setGeodesicMetersPerSecond(-2129658905)
               .setMaxValidationErrors(-1367418922)
               .setLabel("label102727412")
               .setPopulateTravelStepPolylines(true)
               .build();
       OptimizeToursResponse response = fleetRoutingClient.optimizeTours(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[OptimizeToursRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.OptimizeToursRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OptimizeToursResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.OptimizeToursResponse)` |   
  
### optimizeToursCallable()
    
    
    public final UnaryCallable<OptimizeToursRequest,OptimizeToursResponse> optimizeToursCallable()

Sends an `OptimizeToursRequest` containing a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost.

A `ShipmentModel` model consists mainly of `Shipment`s that need to be carried out and `Vehicle`s that can be used to transport the `Shipment`s. The `ShipmentRoute`s assign `Shipment`s to `Vehicle`s. More specifically, they assign a series of `Visit`s to each vehicle, where a `Visit` corresponds to a `VisitRequest`, which is a pickup or delivery for a `Shipment`.

The goal is to provide an assignment of `ShipmentRoute`s to `Vehicle`s that minimizes the total cost where cost has many components defined in the `ShipmentModel`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FleetRoutingClient fleetRoutingClient = FleetRoutingClient.create()) {
       OptimizeToursRequest request =
           OptimizeToursRequest.newBuilder()
               .setParent("parent-995424086")
               .setTimeout(Duration.newBuilder().build())
               .setModel(ShipmentModel.newBuilder().build())
               .addAllInjectedFirstSolutionRoutes(new ArrayList<ShipmentRoute>())
               .setInjectedSolutionConstraint(InjectedSolutionConstraint.newBuilder().build())
               .addAllRefreshDetailsRoutes(new ArrayList<ShipmentRoute>())
               .setInterpretInjectedSolutionsUsingLabels(true)
               .setConsiderRoadTraffic(true)
               .setPopulatePolylines(true)
               .setPopulateTransitionPolylines(true)
               .setAllowLargeDeadlineDespiteInterruptionRisk(true)
               .setUseGeodesicDistances(true)
               .setGeodesicMetersPerSecond(-2129658905)
               .setMaxValidationErrors(-1367418922)
               .setLabel("label102727412")
               .setPopulateTravelStepPolylines(true)
               .build();
       ApiFuture<OptimizeToursResponse> future =
           fleetRoutingClient.optimizeToursCallable().futureCall(request);
       // Do something.
       OptimizeToursResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[OptimizeToursRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.OptimizeToursRequest),[OptimizeToursResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-optimization/latest/com.google.cloud.optimization.v1.OptimizeToursResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
