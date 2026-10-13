---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient
title: Class NetworkServicesClient (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:36:09.025100+00:00
---

# Class NetworkServicesClient (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkServicesClient (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-networkservices/google-cloud-networkservices/src/main/java/com/google/cloud/networkservices/v1/NetworkServicesClient.java)| [Product Reference](https://cloud.google.com/products/networking)  
---|---  
  
Service Description: Service describing handlers for resources.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       EndpointPolicyName name =
           EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]");
       EndpointPolicy response = networkServicesClient.getEndpointPolicy(name);
     }
     

Note: close() needs to be called on the NetworkServicesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListEndpointPolicies |  Lists EndpointPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEndpointPolicies(ListEndpointPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEndpointPolicies(LocationName parent) 
  * listEndpointPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEndpointPoliciesPagedCallable() 
  * listEndpointPoliciesCallable() 

  
GetEndpointPolicy |  Gets details of a single EndpointPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEndpointPolicy(GetEndpointPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEndpointPolicy(EndpointPolicyName name) 
  * getEndpointPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEndpointPolicyCallable() 

  
CreateEndpointPolicy |  Creates a new EndpointPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEndpointPolicyAsync(CreateEndpointPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEndpointPolicyAsync(LocationName parent, EndpointPolicy endpointPolicy, String endpointPolicyId) 
  * createEndpointPolicyAsync(String parent, EndpointPolicy endpointPolicy, String endpointPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEndpointPolicyOperationCallable() 
  * createEndpointPolicyCallable() 

  
UpdateEndpointPolicy |  Updates the parameters of a single EndpointPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEndpointPolicyAsync(UpdateEndpointPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateEndpointPolicyAsync(EndpointPolicy endpointPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEndpointPolicyOperationCallable() 
  * updateEndpointPolicyCallable() 

  
DeleteEndpointPolicy |  Deletes a single EndpointPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEndpointPolicyAsync(DeleteEndpointPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEndpointPolicyAsync(EndpointPolicyName name) 
  * deleteEndpointPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEndpointPolicyOperationCallable() 
  * deleteEndpointPolicyCallable() 

  
ListWasmPluginVersions |  Lists `WasmPluginVersion` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWasmPluginVersions(ListWasmPluginVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWasmPluginVersions(WasmPluginName parent) 
  * listWasmPluginVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWasmPluginVersionsPagedCallable() 
  * listWasmPluginVersionsCallable() 

  
GetWasmPluginVersion |  Gets details of the specified `WasmPluginVersion` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWasmPluginVersion(GetWasmPluginVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWasmPluginVersion(WasmPluginVersionName name) 
  * getWasmPluginVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWasmPluginVersionCallable() 

  
CreateWasmPluginVersion |  Creates a new `WasmPluginVersion` resource in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWasmPluginVersionAsync(CreateWasmPluginVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createWasmPluginVersionAsync(WasmPluginName parent, WasmPluginVersion wasmPluginVersion, String wasmPluginVersionId) 
  * createWasmPluginVersionAsync(String parent, WasmPluginVersion wasmPluginVersion, String wasmPluginVersionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWasmPluginVersionOperationCallable() 
  * createWasmPluginVersionCallable() 

  
DeleteWasmPluginVersion |  Deletes the specified `WasmPluginVersion` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteWasmPluginVersionAsync(DeleteWasmPluginVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteWasmPluginVersionAsync(WasmPluginVersionName name) 
  * deleteWasmPluginVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteWasmPluginVersionOperationCallable() 
  * deleteWasmPluginVersionCallable() 

  
ListWasmPlugins |  Lists `WasmPlugin` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWasmPlugins(ListWasmPluginsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWasmPlugins(LocationName parent) 
  * listWasmPlugins(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWasmPluginsPagedCallable() 
  * listWasmPluginsCallable() 

  
GetWasmPlugin |  Gets details of the specified `WasmPlugin` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWasmPlugin(GetWasmPluginRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWasmPlugin(WasmPluginName name) 
  * getWasmPlugin(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWasmPluginCallable() 

  
CreateWasmPlugin |  Creates a new `WasmPlugin` resource in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWasmPluginAsync(CreateWasmPluginRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createWasmPluginAsync(LocationName parent, WasmPlugin wasmPlugin, String wasmPluginId) 
  * createWasmPluginAsync(String parent, WasmPlugin wasmPlugin, String wasmPluginId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWasmPluginOperationCallable() 
  * createWasmPluginCallable() 

  
UpdateWasmPlugin |  Updates the parameters of the specified `WasmPlugin` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateWasmPluginAsync(UpdateWasmPluginRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateWasmPluginAsync(WasmPlugin wasmPlugin, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateWasmPluginOperationCallable() 
  * updateWasmPluginCallable() 

  
DeleteWasmPlugin |  Deletes the specified `WasmPlugin` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteWasmPluginAsync(DeleteWasmPluginRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteWasmPluginAsync(WasmPluginName name) 
  * deleteWasmPluginAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteWasmPluginOperationCallable() 
  * deleteWasmPluginCallable() 

  
ListGateways |  Lists Gateways in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGateways(ListGatewaysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGateways(LocationName parent) 
  * listGateways(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGatewaysPagedCallable() 
  * listGatewaysCallable() 

  
GetGateway |  Gets details of a single Gateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGateway(GetGatewayRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGateway(GatewayName name) 
  * getGateway(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGatewayCallable() 

  
CreateGateway |  Creates a new Gateway in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGatewayAsync(CreateGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createGatewayAsync(LocationName parent, Gateway gateway, String gatewayId) 
  * createGatewayAsync(String parent, Gateway gateway, String gatewayId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGatewayOperationCallable() 
  * createGatewayCallable() 

  
UpdateGateway |  Updates the parameters of a single Gateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGatewayAsync(UpdateGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateGatewayAsync(Gateway gateway, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGatewayOperationCallable() 
  * updateGatewayCallable() 

  
DeleteGateway |  Deletes a single Gateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGatewayAsync(DeleteGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteGatewayAsync(GatewayName name) 
  * deleteGatewayAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGatewayOperationCallable() 
  * deleteGatewayCallable() 

  
ListGrpcRoutes |  Lists GrpcRoutes in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGrpcRoutes(ListGrpcRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGrpcRoutes(LocationName parent) 
  * listGrpcRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGrpcRoutesPagedCallable() 
  * listGrpcRoutesCallable() 

  
GetGrpcRoute |  Gets details of a single GrpcRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGrpcRoute(GetGrpcRouteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGrpcRoute(GrpcRouteName name) 
  * getGrpcRoute(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGrpcRouteCallable() 

  
CreateGrpcRoute |  Creates a new GrpcRoute in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGrpcRouteAsync(CreateGrpcRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createGrpcRouteAsync(LocationName parent, GrpcRoute grpcRoute, String grpcRouteId) 
  * createGrpcRouteAsync(String parent, GrpcRoute grpcRoute, String grpcRouteId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGrpcRouteOperationCallable() 
  * createGrpcRouteCallable() 

  
UpdateGrpcRoute |  Updates the parameters of a single GrpcRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGrpcRouteAsync(UpdateGrpcRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateGrpcRouteAsync(GrpcRoute grpcRoute, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGrpcRouteOperationCallable() 
  * updateGrpcRouteCallable() 

  
DeleteGrpcRoute |  Deletes a single GrpcRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGrpcRouteAsync(DeleteGrpcRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteGrpcRouteAsync(GrpcRouteName name) 
  * deleteGrpcRouteAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGrpcRouteOperationCallable() 
  * deleteGrpcRouteCallable() 

  
ListHttpRoutes |  Lists HttpRoute in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHttpRoutes(ListHttpRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHttpRoutes(LocationName parent) 
  * listHttpRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHttpRoutesPagedCallable() 
  * listHttpRoutesCallable() 

  
GetHttpRoute |  Gets details of a single HttpRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHttpRoute(GetHttpRouteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHttpRoute(HttpRouteName name) 
  * getHttpRoute(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHttpRouteCallable() 

  
CreateHttpRoute |  Creates a new HttpRoute in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHttpRouteAsync(CreateHttpRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createHttpRouteAsync(LocationName parent, HttpRoute httpRoute, String httpRouteId) 
  * createHttpRouteAsync(String parent, HttpRoute httpRoute, String httpRouteId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHttpRouteOperationCallable() 
  * createHttpRouteCallable() 

  
UpdateHttpRoute |  Updates the parameters of a single HttpRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateHttpRouteAsync(UpdateHttpRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateHttpRouteAsync(HttpRoute httpRoute, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateHttpRouteOperationCallable() 
  * updateHttpRouteCallable() 

  
DeleteHttpRoute |  Deletes a single HttpRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteHttpRouteAsync(DeleteHttpRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteHttpRouteAsync(HttpRouteName name) 
  * deleteHttpRouteAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteHttpRouteOperationCallable() 
  * deleteHttpRouteCallable() 

  
ListTcpRoutes |  Lists TcpRoute in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTcpRoutes(ListTcpRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTcpRoutes(LocationName parent) 
  * listTcpRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTcpRoutesPagedCallable() 
  * listTcpRoutesCallable() 

  
GetTcpRoute |  Gets details of a single TcpRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTcpRoute(GetTcpRouteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTcpRoute(TcpRouteName name) 
  * getTcpRoute(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTcpRouteCallable() 

  
CreateTcpRoute |  Creates a new TcpRoute in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTcpRouteAsync(CreateTcpRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createTcpRouteAsync(LocationName parent, TcpRoute tcpRoute, String tcpRouteId) 
  * createTcpRouteAsync(String parent, TcpRoute tcpRoute, String tcpRouteId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTcpRouteOperationCallable() 
  * createTcpRouteCallable() 

  
UpdateTcpRoute |  Updates the parameters of a single TcpRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTcpRouteAsync(UpdateTcpRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateTcpRouteAsync(TcpRoute tcpRoute, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTcpRouteOperationCallable() 
  * updateTcpRouteCallable() 

  
DeleteTcpRoute |  Deletes a single TcpRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTcpRouteAsync(DeleteTcpRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTcpRouteAsync(TcpRouteName name) 
  * deleteTcpRouteAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTcpRouteOperationCallable() 
  * deleteTcpRouteCallable() 

  
ListTlsRoutes |  Lists TlsRoute in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTlsRoutes(ListTlsRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTlsRoutes(LocationName parent) 
  * listTlsRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTlsRoutesPagedCallable() 
  * listTlsRoutesCallable() 

  
GetTlsRoute |  Gets details of a single TlsRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTlsRoute(GetTlsRouteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTlsRoute(TlsRouteName name) 
  * getTlsRoute(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTlsRouteCallable() 

  
CreateTlsRoute |  Creates a new TlsRoute in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTlsRouteAsync(CreateTlsRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createTlsRouteAsync(LocationName parent, TlsRoute tlsRoute, String tlsRouteId) 
  * createTlsRouteAsync(String parent, TlsRoute tlsRoute, String tlsRouteId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTlsRouteOperationCallable() 
  * createTlsRouteCallable() 

  
UpdateTlsRoute |  Updates the parameters of a single TlsRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTlsRouteAsync(UpdateTlsRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateTlsRouteAsync(TlsRoute tlsRoute, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTlsRouteOperationCallable() 
  * updateTlsRouteCallable() 

  
DeleteTlsRoute |  Deletes a single TlsRoute. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTlsRouteAsync(DeleteTlsRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTlsRouteAsync(TlsRouteName name) 
  * deleteTlsRouteAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTlsRouteOperationCallable() 
  * deleteTlsRouteCallable() 

  
ListServiceBindings |  Lists ServiceBinding in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServiceBindings(ListServiceBindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServiceBindings(LocationName parent) 
  * listServiceBindings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServiceBindingsPagedCallable() 
  * listServiceBindingsCallable() 

  
GetServiceBinding |  Gets details of a single ServiceBinding. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServiceBinding(GetServiceBindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServiceBinding(ServiceBindingName name) 
  * getServiceBinding(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceBindingCallable() 

  
CreateServiceBinding |  Creates a new ServiceBinding in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServiceBindingAsync(CreateServiceBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createServiceBindingAsync(LocationName parent, ServiceBinding serviceBinding, String serviceBindingId) 
  * createServiceBindingAsync(String parent, ServiceBinding serviceBinding, String serviceBindingId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServiceBindingOperationCallable() 
  * createServiceBindingCallable() 

  
UpdateServiceBinding |  Updates the parameters of a single ServiceBinding. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServiceBindingAsync(UpdateServiceBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateServiceBindingAsync(ServiceBinding serviceBinding, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServiceBindingOperationCallable() 
  * updateServiceBindingCallable() 

  
DeleteServiceBinding |  Deletes a single ServiceBinding. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServiceBindingAsync(DeleteServiceBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServiceBindingAsync(ServiceBindingName name) 
  * deleteServiceBindingAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceBindingOperationCallable() 
  * deleteServiceBindingCallable() 

  
ListMeshes |  Lists Meshes in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMeshes(ListMeshesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMeshes(LocationName parent) 
  * listMeshes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMeshesPagedCallable() 
  * listMeshesCallable() 

  
GetMesh |  Gets details of a single Mesh. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMesh(GetMeshRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMesh(MeshName name) 
  * getMesh(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMeshCallable() 

  
CreateMesh |  Creates a new Mesh in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMeshAsync(CreateMeshRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createMeshAsync(LocationName parent, Mesh mesh, String meshId) 
  * createMeshAsync(String parent, Mesh mesh, String meshId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMeshOperationCallable() 
  * createMeshCallable() 

  
UpdateMesh |  Updates the parameters of a single Mesh. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMeshAsync(UpdateMeshRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateMeshAsync(Mesh mesh, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMeshOperationCallable() 
  * updateMeshCallable() 

  
DeleteMesh |  Deletes a single Mesh. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMeshAsync(DeleteMeshRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteMeshAsync(MeshName name) 
  * deleteMeshAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMeshOperationCallable() 
  * deleteMeshCallable() 

  
ListServiceLbPolicies |  Lists ServiceLbPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServiceLbPolicies(ListServiceLbPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServiceLbPolicies(LocationName parent) 
  * listServiceLbPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServiceLbPoliciesPagedCallable() 
  * listServiceLbPoliciesCallable() 

  
GetServiceLbPolicy |  Gets details of a single ServiceLbPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServiceLbPolicy(GetServiceLbPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServiceLbPolicy(ServiceLbPolicyName name) 
  * getServiceLbPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceLbPolicyCallable() 

  
CreateServiceLbPolicy |  Creates a new ServiceLbPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServiceLbPolicyAsync(CreateServiceLbPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createServiceLbPolicyAsync(LocationName parent, ServiceLbPolicy serviceLbPolicy, String serviceLbPolicyId) 
  * createServiceLbPolicyAsync(String parent, ServiceLbPolicy serviceLbPolicy, String serviceLbPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServiceLbPolicyOperationCallable() 
  * createServiceLbPolicyCallable() 

  
UpdateServiceLbPolicy |  Updates the parameters of a single ServiceLbPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServiceLbPolicyAsync(UpdateServiceLbPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateServiceLbPolicyAsync(ServiceLbPolicy serviceLbPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServiceLbPolicyOperationCallable() 
  * updateServiceLbPolicyCallable() 

  
DeleteServiceLbPolicy |  Deletes a single ServiceLbPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServiceLbPolicyAsync(DeleteServiceLbPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServiceLbPolicyAsync(ServiceLbPolicyName name) 
  * deleteServiceLbPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceLbPolicyOperationCallable() 
  * deleteServiceLbPolicyCallable() 

  
GetGatewayRouteView |  Get a single RouteView of a Gateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGatewayRouteView(GetGatewayRouteViewRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGatewayRouteView(GatewayRouteViewName name) 
  * getGatewayRouteView(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGatewayRouteViewCallable() 

  
GetMeshRouteView |  Get a single RouteView of a Mesh. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMeshRouteView(GetMeshRouteViewRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMeshRouteView(MeshRouteViewName name) 
  * getMeshRouteView(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMeshRouteViewCallable() 

  
ListGatewayRouteViews |  Lists RouteViews |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGatewayRouteViews(ListGatewayRouteViewsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGatewayRouteViews(GatewayName parent) 
  * listGatewayRouteViews(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGatewayRouteViewsPagedCallable() 
  * listGatewayRouteViewsCallable() 

  
ListMeshRouteViews |  Lists RouteViews |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMeshRouteViews(ListMeshRouteViewsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMeshRouteViews(MeshName parent) 
  * listMeshRouteViews(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMeshRouteViewsPagedCallable() 
  * listMeshRouteViewsCallable() 

  
ListAgentGateways |  Lists AgentGateways in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAgentGateways(ListAgentGatewaysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAgentGateways(LocationName parent) 
  * listAgentGateways(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAgentGatewaysPagedCallable() 
  * listAgentGatewaysCallable() 

  
GetAgentGateway |  Gets details of a single AgentGateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAgentGateway(GetAgentGatewayRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAgentGateway(AgentGatewayName name) 
  * getAgentGateway(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAgentGatewayCallable() 

  
CreateAgentGateway |  Creates a new AgentGateway in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAgentGatewayAsync(CreateAgentGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAgentGatewayAsync(LocationName parent, AgentGateway agentGateway, String agentGatewayId) 
  * createAgentGatewayAsync(String parent, AgentGateway agentGateway, String agentGatewayId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAgentGatewayOperationCallable() 
  * createAgentGatewayCallable() 

  
UpdateAgentGateway |  Updates the parameters of a single AgentGateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAgentGatewayAsync(UpdateAgentGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAgentGatewayAsync(AgentGateway agentGateway, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAgentGatewayOperationCallable() 
  * updateAgentGatewayCallable() 

  
DeleteAgentGateway |  Deletes a single AgentGateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAgentGatewayAsync(DeleteAgentGatewayRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAgentGatewayAsync(AgentGatewayName name) 
  * deleteAgentGatewayAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAgentGatewayOperationCallable() 
  * deleteAgentGatewayCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of NetworkServicesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkServicesSettings networkServicesSettings =
         NetworkServicesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NetworkServicesClient networkServicesClient =
         NetworkServicesClient.create(networkServicesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkServicesSettings networkServicesSettings =
         NetworkServicesSettings.newBuilder().setEndpoint(myEndpoint).build();
     NetworkServicesClient networkServicesClient =
         NetworkServicesClient.create(networkServicesSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkServicesSettings networkServicesSettings =
         NetworkServicesSettings.newHttpJsonBuilder().build();
     NetworkServicesClient networkServicesClient =
         NetworkServicesClient.create(networkServicesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NetworkServicesClient

## Static Methods 

### create()
    
    
    public static final NetworkServicesClient create()

Constructs an instance of NetworkServicesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkServicesSettings settings)
    
    
    public static final NetworkServicesClient create(NetworkServicesSettings settings)

Constructs an instance of NetworkServicesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkServicesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkServicesStub stub)
    
    
    public static final NetworkServicesClient create(NetworkServicesStub stub)

Constructs an instance of NetworkServicesClient, using the given stub for making calls. This is for advanced usage - prefer using create(NetworkServicesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.stub.NetworkServicesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient)` |   
  
## Constructors 

### NetworkServicesClient(NetworkServicesSettings settings)
    
    
    protected NetworkServicesClient(NetworkServicesSettings settings)

Constructs an instance of NetworkServicesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkServicesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings)`  
  
  
### NetworkServicesClient(NetworkServicesStub stub)
    
    
    protected NetworkServicesClient(NetworkServicesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.stub.NetworkServicesStub)`  
  
  
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

### createAgentGatewayAsync(@Nullable LocationName parent, AgentGateway agentGateway, String agentGatewayId)
    
    
    public final OperationFuture<AgentGateway,OperationMetadata> createAgentGatewayAsync(@Nullable LocationName parent, AgentGateway agentGateway, String agentGatewayId)

Creates a new AgentGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AgentGateway agentGateway = AgentGateway.newBuilder().build();
       String agentGatewayId = "agentGatewayId1729577210";
       AgentGateway response =
           networkServicesClient.createAgentGatewayAsync(parent, agentGateway, agentGatewayId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the AgentGateway. Must be in the format `projects/*/locations/*`.  
`agentGateway` | `[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)`  
Required. AgentGateway resource to be created.  
`agentGatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the AgentGateway resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createAgentGatewayAsync(CreateAgentGatewayRequest request)
    
    
    public final OperationFuture<AgentGateway,OperationMetadata> createAgentGatewayAsync(CreateAgentGatewayRequest request)

Creates a new AgentGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateAgentGatewayRequest request =
           CreateAgentGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAgentGatewayId("agentGatewayId1729577210")
               .setAgentGateway(AgentGateway.newBuilder().build())
               .build();
       AgentGateway response = networkServicesClient.createAgentGatewayAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAgentGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createAgentGatewayAsync(String parent, AgentGateway agentGateway, String agentGatewayId)
    
    
    public final OperationFuture<AgentGateway,OperationMetadata> createAgentGatewayAsync(String parent, AgentGateway agentGateway, String agentGatewayId)

Creates a new AgentGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AgentGateway agentGateway = AgentGateway.newBuilder().build();
       String agentGatewayId = "agentGatewayId1729577210";
       AgentGateway response =
           networkServicesClient.createAgentGatewayAsync(parent, agentGateway, agentGatewayId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the AgentGateway. Must be in the format `projects/*/locations/*`.  
`agentGateway` | `[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)`  
Required. AgentGateway resource to be created.  
`agentGatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the AgentGateway resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createAgentGatewayCallable()
    
    
    public final UnaryCallable<CreateAgentGatewayRequest,Operation> createAgentGatewayCallable()

Creates a new AgentGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateAgentGatewayRequest request =
           CreateAgentGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAgentGatewayId("agentGatewayId1729577210")
               .setAgentGateway(AgentGateway.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createAgentGatewayCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAgentGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAgentGatewayOperationCallable()
    
    
    public final OperationCallable<CreateAgentGatewayRequest,AgentGateway,OperationMetadata> createAgentGatewayOperationCallable()

Creates a new AgentGateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateAgentGatewayRequest request =
           CreateAgentGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAgentGatewayId("agentGatewayId1729577210")
               .setAgentGateway(AgentGateway.newBuilder().build())
               .build();
       OperationFuture<AgentGateway, OperationMetadata> future =
           networkServicesClient.createAgentGatewayOperationCallable().futureCall(request);
       // Do something.
       AgentGateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAgentGatewayRequest),[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createEndpointPolicyAsync(@Nullable LocationName parent, EndpointPolicy endpointPolicy, String endpointPolicyId)
    
    
    public final OperationFuture<EndpointPolicy,OperationMetadata> createEndpointPolicyAsync(@Nullable LocationName parent, EndpointPolicy endpointPolicy, String endpointPolicyId)

Creates a new EndpointPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       EndpointPolicy endpointPolicy = EndpointPolicy.newBuilder().build();
       String endpointPolicyId = "endpointPolicyId-509458782";
       EndpointPolicy response =
           networkServicesClient
               .createEndpointPolicyAsync(parent, endpointPolicy, endpointPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the EndpointPolicy. Must be in the format `projects/*/locations/*`.  
`endpointPolicy` | `[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)`  
Required. EndpointPolicy resource to be created.  
`endpointPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the EndpointPolicy resource to be created. E.g. "CustomECS".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createEndpointPolicyAsync(CreateEndpointPolicyRequest request)
    
    
    public final OperationFuture<EndpointPolicy,OperationMetadata> createEndpointPolicyAsync(CreateEndpointPolicyRequest request)

Creates a new EndpointPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateEndpointPolicyRequest request =
           CreateEndpointPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEndpointPolicyId("endpointPolicyId-509458782")
               .setEndpointPolicy(EndpointPolicy.newBuilder().build())
               .build();
       EndpointPolicy response = networkServicesClient.createEndpointPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateEndpointPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createEndpointPolicyAsync(String parent, EndpointPolicy endpointPolicy, String endpointPolicyId)
    
    
    public final OperationFuture<EndpointPolicy,OperationMetadata> createEndpointPolicyAsync(String parent, EndpointPolicy endpointPolicy, String endpointPolicyId)

Creates a new EndpointPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       EndpointPolicy endpointPolicy = EndpointPolicy.newBuilder().build();
       String endpointPolicyId = "endpointPolicyId-509458782";
       EndpointPolicy response =
           networkServicesClient
               .createEndpointPolicyAsync(parent, endpointPolicy, endpointPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the EndpointPolicy. Must be in the format `projects/*/locations/*`.  
`endpointPolicy` | `[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)`  
Required. EndpointPolicy resource to be created.  
`endpointPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the EndpointPolicy resource to be created. E.g. "CustomECS".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createEndpointPolicyCallable()
    
    
    public final UnaryCallable<CreateEndpointPolicyRequest,Operation> createEndpointPolicyCallable()

Creates a new EndpointPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateEndpointPolicyRequest request =
           CreateEndpointPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEndpointPolicyId("endpointPolicyId-509458782")
               .setEndpointPolicy(EndpointPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createEndpointPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateEndpointPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEndpointPolicyOperationCallable()
    
    
    public final OperationCallable<CreateEndpointPolicyRequest,EndpointPolicy,OperationMetadata> createEndpointPolicyOperationCallable()

Creates a new EndpointPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateEndpointPolicyRequest request =
           CreateEndpointPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEndpointPolicyId("endpointPolicyId-509458782")
               .setEndpointPolicy(EndpointPolicy.newBuilder().build())
               .build();
       OperationFuture<EndpointPolicy, OperationMetadata> future =
           networkServicesClient.createEndpointPolicyOperationCallable().futureCall(request);
       // Do something.
       EndpointPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateEndpointPolicyRequest),[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGatewayAsync(@Nullable LocationName parent, Gateway gateway, String gatewayId)
    
    
    public final OperationFuture<Gateway,OperationMetadata> createGatewayAsync(@Nullable LocationName parent, Gateway gateway, String gatewayId)

Creates a new Gateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Gateway gateway = Gateway.newBuilder().build();
       String gatewayId = "gatewayId-1354641793";
       Gateway response = networkServicesClient.createGatewayAsync(parent, gateway, gatewayId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the Gateway. Must be in the format `projects/*/locations/*`.  
`gateway` | `[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)`  
Required. Gateway resource to be created.  
`gatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the Gateway resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGatewayAsync(CreateGatewayRequest request)
    
    
    public final OperationFuture<Gateway,OperationMetadata> createGatewayAsync(CreateGatewayRequest request)

Creates a new Gateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateGatewayRequest request =
           CreateGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGatewayId("gatewayId-1354641793")
               .setGateway(Gateway.newBuilder().build())
               .build();
       Gateway response = networkServicesClient.createGatewayAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGatewayAsync(String parent, Gateway gateway, String gatewayId)
    
    
    public final OperationFuture<Gateway,OperationMetadata> createGatewayAsync(String parent, Gateway gateway, String gatewayId)

Creates a new Gateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Gateway gateway = Gateway.newBuilder().build();
       String gatewayId = "gatewayId-1354641793";
       Gateway response = networkServicesClient.createGatewayAsync(parent, gateway, gatewayId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the Gateway. Must be in the format `projects/*/locations/*`.  
`gateway` | `[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)`  
Required. Gateway resource to be created.  
`gatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the Gateway resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGatewayCallable()
    
    
    public final UnaryCallable<CreateGatewayRequest,Operation> createGatewayCallable()

Creates a new Gateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateGatewayRequest request =
           CreateGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGatewayId("gatewayId-1354641793")
               .setGateway(Gateway.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createGatewayCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGatewayOperationCallable()
    
    
    public final OperationCallable<CreateGatewayRequest,Gateway,OperationMetadata> createGatewayOperationCallable()

Creates a new Gateway in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateGatewayRequest request =
           CreateGatewayRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGatewayId("gatewayId-1354641793")
               .setGateway(Gateway.newBuilder().build())
               .build();
       OperationFuture<Gateway, OperationMetadata> future =
           networkServicesClient.createGatewayOperationCallable().futureCall(request);
       // Do something.
       Gateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGatewayRequest),[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGrpcRouteAsync(@Nullable LocationName parent, GrpcRoute grpcRoute, String grpcRouteId)
    
    
    public final OperationFuture<GrpcRoute,OperationMetadata> createGrpcRouteAsync(@Nullable LocationName parent, GrpcRoute grpcRoute, String grpcRouteId)

Creates a new GrpcRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       GrpcRoute grpcRoute = GrpcRoute.newBuilder().build();
       String grpcRouteId = "grpcRouteId1888295750";
       GrpcRoute response =
           networkServicesClient.createGrpcRouteAsync(parent, grpcRoute, grpcRouteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the GrpcRoute. Must be in the format `projects/*/locations/*`.  
`grpcRoute` | `[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)`  
Required. GrpcRoute resource to be created.  
`grpcRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the GrpcRoute resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGrpcRouteAsync(CreateGrpcRouteRequest request)
    
    
    public final OperationFuture<GrpcRoute,OperationMetadata> createGrpcRouteAsync(CreateGrpcRouteRequest request)

Creates a new GrpcRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateGrpcRouteRequest request =
           CreateGrpcRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGrpcRouteId("grpcRouteId1888295750")
               .setGrpcRoute(GrpcRoute.newBuilder().build())
               .build();
       GrpcRoute response = networkServicesClient.createGrpcRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGrpcRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGrpcRouteAsync(String parent, GrpcRoute grpcRoute, String grpcRouteId)
    
    
    public final OperationFuture<GrpcRoute,OperationMetadata> createGrpcRouteAsync(String parent, GrpcRoute grpcRoute, String grpcRouteId)

Creates a new GrpcRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       GrpcRoute grpcRoute = GrpcRoute.newBuilder().build();
       String grpcRouteId = "grpcRouteId1888295750";
       GrpcRoute response =
           networkServicesClient.createGrpcRouteAsync(parent, grpcRoute, grpcRouteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the GrpcRoute. Must be in the format `projects/*/locations/*`.  
`grpcRoute` | `[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)`  
Required. GrpcRoute resource to be created.  
`grpcRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the GrpcRoute resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGrpcRouteCallable()
    
    
    public final UnaryCallable<CreateGrpcRouteRequest,Operation> createGrpcRouteCallable()

Creates a new GrpcRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateGrpcRouteRequest request =
           CreateGrpcRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGrpcRouteId("grpcRouteId1888295750")
               .setGrpcRoute(GrpcRoute.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createGrpcRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGrpcRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGrpcRouteOperationCallable()
    
    
    public final OperationCallable<CreateGrpcRouteRequest,GrpcRoute,OperationMetadata> createGrpcRouteOperationCallable()

Creates a new GrpcRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateGrpcRouteRequest request =
           CreateGrpcRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGrpcRouteId("grpcRouteId1888295750")
               .setGrpcRoute(GrpcRoute.newBuilder().build())
               .build();
       OperationFuture<GrpcRoute, OperationMetadata> future =
           networkServicesClient.createGrpcRouteOperationCallable().futureCall(request);
       // Do something.
       GrpcRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGrpcRouteRequest),[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createHttpRouteAsync(@Nullable LocationName parent, HttpRoute httpRoute, String httpRouteId)
    
    
    public final OperationFuture<HttpRoute,OperationMetadata> createHttpRouteAsync(@Nullable LocationName parent, HttpRoute httpRoute, String httpRouteId)

Creates a new HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       HttpRoute httpRoute = HttpRoute.newBuilder().build();
       String httpRouteId = "httpRouteId-2054835300";
       HttpRoute response =
           networkServicesClient.createHttpRouteAsync(parent, httpRoute, httpRouteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the HttpRoute. Must be in the format `projects/*/locations/*`.  
`httpRoute` | `[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)`  
Required. HttpRoute resource to be created.  
`httpRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the HttpRoute resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createHttpRouteAsync(CreateHttpRouteRequest request)
    
    
    public final OperationFuture<HttpRoute,OperationMetadata> createHttpRouteAsync(CreateHttpRouteRequest request)

Creates a new HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateHttpRouteRequest request =
           CreateHttpRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHttpRouteId("httpRouteId-2054835300")
               .setHttpRoute(HttpRoute.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       HttpRoute response = networkServicesClient.createHttpRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateHttpRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createHttpRouteAsync(String parent, HttpRoute httpRoute, String httpRouteId)
    
    
    public final OperationFuture<HttpRoute,OperationMetadata> createHttpRouteAsync(String parent, HttpRoute httpRoute, String httpRouteId)

Creates a new HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       HttpRoute httpRoute = HttpRoute.newBuilder().build();
       String httpRouteId = "httpRouteId-2054835300";
       HttpRoute response =
           networkServicesClient.createHttpRouteAsync(parent, httpRoute, httpRouteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the HttpRoute. Must be in the format `projects/*/locations/*`.  
`httpRoute` | `[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)`  
Required. HttpRoute resource to be created.  
`httpRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the HttpRoute resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createHttpRouteCallable()
    
    
    public final UnaryCallable<CreateHttpRouteRequest,Operation> createHttpRouteCallable()

Creates a new HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateHttpRouteRequest request =
           CreateHttpRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHttpRouteId("httpRouteId-2054835300")
               .setHttpRoute(HttpRoute.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createHttpRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateHttpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHttpRouteOperationCallable()
    
    
    public final OperationCallable<CreateHttpRouteRequest,HttpRoute,OperationMetadata> createHttpRouteOperationCallable()

Creates a new HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateHttpRouteRequest request =
           CreateHttpRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHttpRouteId("httpRouteId-2054835300")
               .setHttpRoute(HttpRoute.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<HttpRoute, OperationMetadata> future =
           networkServicesClient.createHttpRouteOperationCallable().futureCall(request);
       // Do something.
       HttpRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateHttpRouteRequest),[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createMeshAsync(@Nullable LocationName parent, Mesh mesh, String meshId)
    
    
    public final OperationFuture<Mesh,OperationMetadata> createMeshAsync(@Nullable LocationName parent, Mesh mesh, String meshId)

Creates a new Mesh in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Mesh mesh = Mesh.newBuilder().build();
       String meshId = "meshId-1077585944";
       Mesh response = networkServicesClient.createMeshAsync(parent, mesh, meshId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the Mesh. Must be in the format `projects/*/locations/*`.  
`mesh` | `[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)`  
Required. Mesh resource to be created.  
`meshId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the Mesh resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createMeshAsync(CreateMeshRequest request)
    
    
    public final OperationFuture<Mesh,OperationMetadata> createMeshAsync(CreateMeshRequest request)

Creates a new Mesh in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateMeshRequest request =
           CreateMeshRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMeshId("meshId-1077585944")
               .setMesh(Mesh.newBuilder().build())
               .build();
       Mesh response = networkServicesClient.createMeshAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateMeshRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createMeshAsync(String parent, Mesh mesh, String meshId)
    
    
    public final OperationFuture<Mesh,OperationMetadata> createMeshAsync(String parent, Mesh mesh, String meshId)

Creates a new Mesh in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Mesh mesh = Mesh.newBuilder().build();
       String meshId = "meshId-1077585944";
       Mesh response = networkServicesClient.createMeshAsync(parent, mesh, meshId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the Mesh. Must be in the format `projects/*/locations/*`.  
`mesh` | `[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)`  
Required. Mesh resource to be created.  
`meshId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the Mesh resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createMeshCallable()
    
    
    public final UnaryCallable<CreateMeshRequest,Operation> createMeshCallable()

Creates a new Mesh in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateMeshRequest request =
           CreateMeshRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMeshId("meshId-1077585944")
               .setMesh(Mesh.newBuilder().build())
               .build();
       ApiFuture<Operation> future = networkServicesClient.createMeshCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateMeshRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMeshOperationCallable()
    
    
    public final OperationCallable<CreateMeshRequest,Mesh,OperationMetadata> createMeshOperationCallable()

Creates a new Mesh in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateMeshRequest request =
           CreateMeshRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setMeshId("meshId-1077585944")
               .setMesh(Mesh.newBuilder().build())
               .build();
       OperationFuture<Mesh, OperationMetadata> future =
           networkServicesClient.createMeshOperationCallable().futureCall(request);
       // Do something.
       Mesh response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateMeshRequest),[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceBindingAsync(@Nullable LocationName parent, ServiceBinding serviceBinding, String serviceBindingId)
    
    
    public final OperationFuture<ServiceBinding,OperationMetadata> createServiceBindingAsync(@Nullable LocationName parent, ServiceBinding serviceBinding, String serviceBindingId)

Creates a new ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ServiceBinding serviceBinding = ServiceBinding.newBuilder().build();
       String serviceBindingId = "serviceBindingId-1424670901";
       ServiceBinding response =
           networkServicesClient
               .createServiceBindingAsync(parent, serviceBinding, serviceBindingId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the ServiceBinding. Must be in the format `projects/*/locations/*`.  
`serviceBinding` | `[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)`  
Required. ServiceBinding resource to be created.  
`serviceBindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the ServiceBinding resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceBindingAsync(CreateServiceBindingRequest request)
    
    
    public final OperationFuture<ServiceBinding,OperationMetadata> createServiceBindingAsync(CreateServiceBindingRequest request)

Creates a new ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateServiceBindingRequest request =
           CreateServiceBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceBindingId("serviceBindingId-1424670901")
               .setServiceBinding(ServiceBinding.newBuilder().build())
               .build();
       ServiceBinding response = networkServicesClient.createServiceBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceBindingAsync(String parent, ServiceBinding serviceBinding, String serviceBindingId)
    
    
    public final OperationFuture<ServiceBinding,OperationMetadata> createServiceBindingAsync(String parent, ServiceBinding serviceBinding, String serviceBindingId)

Creates a new ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ServiceBinding serviceBinding = ServiceBinding.newBuilder().build();
       String serviceBindingId = "serviceBindingId-1424670901";
       ServiceBinding response =
           networkServicesClient
               .createServiceBindingAsync(parent, serviceBinding, serviceBindingId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the ServiceBinding. Must be in the format `projects/*/locations/*`.  
`serviceBinding` | `[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)`  
Required. ServiceBinding resource to be created.  
`serviceBindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the ServiceBinding resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceBindingCallable()
    
    
    public final UnaryCallable<CreateServiceBindingRequest,Operation> createServiceBindingCallable()

Creates a new ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateServiceBindingRequest request =
           CreateServiceBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceBindingId("serviceBindingId-1424670901")
               .setServiceBinding(ServiceBinding.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createServiceBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceBindingOperationCallable()
    
    
    public final OperationCallable<CreateServiceBindingRequest,ServiceBinding,OperationMetadata> createServiceBindingOperationCallable()

Creates a new ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateServiceBindingRequest request =
           CreateServiceBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceBindingId("serviceBindingId-1424670901")
               .setServiceBinding(ServiceBinding.newBuilder().build())
               .build();
       OperationFuture<ServiceBinding, OperationMetadata> future =
           networkServicesClient.createServiceBindingOperationCallable().futureCall(request);
       // Do something.
       ServiceBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceBindingRequest),[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceLbPolicyAsync(@Nullable LocationName parent, ServiceLbPolicy serviceLbPolicy, String serviceLbPolicyId)
    
    
    public final OperationFuture<ServiceLbPolicy,OperationMetadata> createServiceLbPolicyAsync(@Nullable LocationName parent, ServiceLbPolicy serviceLbPolicy, String serviceLbPolicyId)

Creates a new ServiceLbPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ServiceLbPolicy serviceLbPolicy = ServiceLbPolicy.newBuilder().build();
       String serviceLbPolicyId = "serviceLbPolicyId1391086104";
       ServiceLbPolicy response =
           networkServicesClient
               .createServiceLbPolicyAsync(parent, serviceLbPolicy, serviceLbPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the ServiceLbPolicy. Must be in the format `projects/{project}/locations/{location}`.  
`serviceLbPolicy` | `[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)`  
Required. ServiceLbPolicy resource to be created.  
`serviceLbPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the ServiceLbPolicy resource to be created. E.g. for resource name `projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}`. the id is value of {service_lb_policy_name}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceLbPolicyAsync(CreateServiceLbPolicyRequest request)
    
    
    public final OperationFuture<ServiceLbPolicy,OperationMetadata> createServiceLbPolicyAsync(CreateServiceLbPolicyRequest request)

Creates a new ServiceLbPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateServiceLbPolicyRequest request =
           CreateServiceLbPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceLbPolicyId("serviceLbPolicyId1391086104")
               .setServiceLbPolicy(ServiceLbPolicy.newBuilder().build())
               .build();
       ServiceLbPolicy response = networkServicesClient.createServiceLbPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceLbPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceLbPolicyAsync(String parent, ServiceLbPolicy serviceLbPolicy, String serviceLbPolicyId)
    
    
    public final OperationFuture<ServiceLbPolicy,OperationMetadata> createServiceLbPolicyAsync(String parent, ServiceLbPolicy serviceLbPolicy, String serviceLbPolicyId)

Creates a new ServiceLbPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ServiceLbPolicy serviceLbPolicy = ServiceLbPolicy.newBuilder().build();
       String serviceLbPolicyId = "serviceLbPolicyId1391086104";
       ServiceLbPolicy response =
           networkServicesClient
               .createServiceLbPolicyAsync(parent, serviceLbPolicy, serviceLbPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the ServiceLbPolicy. Must be in the format `projects/{project}/locations/{location}`.  
`serviceLbPolicy` | `[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)`  
Required. ServiceLbPolicy resource to be created.  
`serviceLbPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the ServiceLbPolicy resource to be created. E.g. for resource name `projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}`. the id is value of {service_lb_policy_name}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceLbPolicyCallable()
    
    
    public final UnaryCallable<CreateServiceLbPolicyRequest,Operation> createServiceLbPolicyCallable()

Creates a new ServiceLbPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateServiceLbPolicyRequest request =
           CreateServiceLbPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceLbPolicyId("serviceLbPolicyId1391086104")
               .setServiceLbPolicy(ServiceLbPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createServiceLbPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceLbPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceLbPolicyOperationCallable()
    
    
    public final OperationCallable<CreateServiceLbPolicyRequest,ServiceLbPolicy,OperationMetadata> createServiceLbPolicyOperationCallable()

Creates a new ServiceLbPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateServiceLbPolicyRequest request =
           CreateServiceLbPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceLbPolicyId("serviceLbPolicyId1391086104")
               .setServiceLbPolicy(ServiceLbPolicy.newBuilder().build())
               .build();
       OperationFuture<ServiceLbPolicy, OperationMetadata> future =
           networkServicesClient.createServiceLbPolicyOperationCallable().futureCall(request);
       // Do something.
       ServiceLbPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceLbPolicyRequest),[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTcpRouteAsync(@Nullable LocationName parent, TcpRoute tcpRoute, String tcpRouteId)
    
    
    public final OperationFuture<TcpRoute,OperationMetadata> createTcpRouteAsync(@Nullable LocationName parent, TcpRoute tcpRoute, String tcpRouteId)

Creates a new TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       TcpRoute tcpRoute = TcpRoute.newBuilder().build();
       String tcpRouteId = "tcpRouteId806467107";
       TcpRoute response =
           networkServicesClient.createTcpRouteAsync(parent, tcpRoute, tcpRouteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the TcpRoute. Must be in the format `projects/*/locations/*`.  
`tcpRoute` | `[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)`  
Required. TcpRoute resource to be created.  
`tcpRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the TcpRoute resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTcpRouteAsync(CreateTcpRouteRequest request)
    
    
    public final OperationFuture<TcpRoute,OperationMetadata> createTcpRouteAsync(CreateTcpRouteRequest request)

Creates a new TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateTcpRouteRequest request =
           CreateTcpRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTcpRouteId("tcpRouteId806467107")
               .setTcpRoute(TcpRoute.newBuilder().build())
               .build();
       TcpRoute response = networkServicesClient.createTcpRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTcpRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTcpRouteAsync(String parent, TcpRoute tcpRoute, String tcpRouteId)
    
    
    public final OperationFuture<TcpRoute,OperationMetadata> createTcpRouteAsync(String parent, TcpRoute tcpRoute, String tcpRouteId)

Creates a new TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       TcpRoute tcpRoute = TcpRoute.newBuilder().build();
       String tcpRouteId = "tcpRouteId806467107";
       TcpRoute response =
           networkServicesClient.createTcpRouteAsync(parent, tcpRoute, tcpRouteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the TcpRoute. Must be in the format `projects/*/locations/*`.  
`tcpRoute` | `[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)`  
Required. TcpRoute resource to be created.  
`tcpRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the TcpRoute resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTcpRouteCallable()
    
    
    public final UnaryCallable<CreateTcpRouteRequest,Operation> createTcpRouteCallable()

Creates a new TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateTcpRouteRequest request =
           CreateTcpRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTcpRouteId("tcpRouteId806467107")
               .setTcpRoute(TcpRoute.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createTcpRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTcpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTcpRouteOperationCallable()
    
    
    public final OperationCallable<CreateTcpRouteRequest,TcpRoute,OperationMetadata> createTcpRouteOperationCallable()

Creates a new TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateTcpRouteRequest request =
           CreateTcpRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTcpRouteId("tcpRouteId806467107")
               .setTcpRoute(TcpRoute.newBuilder().build())
               .build();
       OperationFuture<TcpRoute, OperationMetadata> future =
           networkServicesClient.createTcpRouteOperationCallable().futureCall(request);
       // Do something.
       TcpRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTcpRouteRequest),[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTlsRouteAsync(@Nullable LocationName parent, TlsRoute tlsRoute, String tlsRouteId)
    
    
    public final OperationFuture<TlsRoute,OperationMetadata> createTlsRouteAsync(@Nullable LocationName parent, TlsRoute tlsRoute, String tlsRouteId)

Creates a new TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       TlsRoute tlsRoute = TlsRoute.newBuilder().build();
       String tlsRouteId = "tlsRouteId-1642257463";
       TlsRoute response =
           networkServicesClient.createTlsRouteAsync(parent, tlsRoute, tlsRouteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the TlsRoute. Must be in the format `projects/*/locations/*`.  
`tlsRoute` | `[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)`  
Required. TlsRoute resource to be created.  
`tlsRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the TlsRoute resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTlsRouteAsync(CreateTlsRouteRequest request)
    
    
    public final OperationFuture<TlsRoute,OperationMetadata> createTlsRouteAsync(CreateTlsRouteRequest request)

Creates a new TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateTlsRouteRequest request =
           CreateTlsRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTlsRouteId("tlsRouteId-1642257463")
               .setTlsRoute(TlsRoute.newBuilder().build())
               .build();
       TlsRoute response = networkServicesClient.createTlsRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTlsRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTlsRouteAsync(String parent, TlsRoute tlsRoute, String tlsRouteId)
    
    
    public final OperationFuture<TlsRoute,OperationMetadata> createTlsRouteAsync(String parent, TlsRoute tlsRoute, String tlsRouteId)

Creates a new TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       TlsRoute tlsRoute = TlsRoute.newBuilder().build();
       String tlsRouteId = "tlsRouteId-1642257463";
       TlsRoute response =
           networkServicesClient.createTlsRouteAsync(parent, tlsRoute, tlsRouteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the TlsRoute. Must be in the format `projects/*/locations/*`.  
`tlsRoute` | `[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)`  
Required. TlsRoute resource to be created.  
`tlsRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the TlsRoute resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTlsRouteCallable()
    
    
    public final UnaryCallable<CreateTlsRouteRequest,Operation> createTlsRouteCallable()

Creates a new TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateTlsRouteRequest request =
           CreateTlsRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTlsRouteId("tlsRouteId-1642257463")
               .setTlsRoute(TlsRoute.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createTlsRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTlsRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTlsRouteOperationCallable()
    
    
    public final OperationCallable<CreateTlsRouteRequest,TlsRoute,OperationMetadata> createTlsRouteOperationCallable()

Creates a new TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateTlsRouteRequest request =
           CreateTlsRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTlsRouteId("tlsRouteId-1642257463")
               .setTlsRoute(TlsRoute.newBuilder().build())
               .build();
       OperationFuture<TlsRoute, OperationMetadata> future =
           networkServicesClient.createTlsRouteOperationCallable().futureCall(request);
       // Do something.
       TlsRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTlsRouteRequest),[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginAsync(@Nullable LocationName parent, WasmPlugin wasmPlugin, String wasmPluginId)
    
    
    public final OperationFuture<WasmPlugin,OperationMetadata> createWasmPluginAsync(@Nullable LocationName parent, WasmPlugin wasmPlugin, String wasmPluginId)

Creates a new `WasmPlugin` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       WasmPlugin wasmPlugin = WasmPlugin.newBuilder().build();
       String wasmPluginId = "wasmPluginId1902086770";
       WasmPlugin response =
           networkServicesClient.createWasmPluginAsync(parent, wasmPlugin, wasmPluginId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the `WasmPlugin` resource. Must be in the format `projects/{project}/locations/global`.  
`wasmPlugin` | `[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)`  
Required. `WasmPlugin` resource to be created.  
`wasmPluginId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `WasmPlugin` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginAsync(CreateWasmPluginRequest request)
    
    
    public final OperationFuture<WasmPlugin,OperationMetadata> createWasmPluginAsync(CreateWasmPluginRequest request)

Creates a new `WasmPlugin` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateWasmPluginRequest request =
           CreateWasmPluginRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWasmPluginId("wasmPluginId1902086770")
               .setWasmPlugin(WasmPlugin.newBuilder().build())
               .build();
       WasmPlugin response = networkServicesClient.createWasmPluginAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginAsync(String parent, WasmPlugin wasmPlugin, String wasmPluginId)
    
    
    public final OperationFuture<WasmPlugin,OperationMetadata> createWasmPluginAsync(String parent, WasmPlugin wasmPlugin, String wasmPluginId)

Creates a new `WasmPlugin` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       WasmPlugin wasmPlugin = WasmPlugin.newBuilder().build();
       String wasmPluginId = "wasmPluginId1902086770";
       WasmPlugin response =
           networkServicesClient.createWasmPluginAsync(parent, wasmPlugin, wasmPluginId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `WasmPlugin` resource. Must be in the format `projects/{project}/locations/global`.  
`wasmPlugin` | `[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)`  
Required. `WasmPlugin` resource to be created.  
`wasmPluginId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `WasmPlugin` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginCallable()
    
    
    public final UnaryCallable<CreateWasmPluginRequest,Operation> createWasmPluginCallable()

Creates a new `WasmPlugin` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateWasmPluginRequest request =
           CreateWasmPluginRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWasmPluginId("wasmPluginId1902086770")
               .setWasmPlugin(WasmPlugin.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createWasmPluginCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWasmPluginOperationCallable()
    
    
    public final OperationCallable<CreateWasmPluginRequest,WasmPlugin,OperationMetadata> createWasmPluginOperationCallable()

Creates a new `WasmPlugin` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateWasmPluginRequest request =
           CreateWasmPluginRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWasmPluginId("wasmPluginId1902086770")
               .setWasmPlugin(WasmPlugin.newBuilder().build())
               .build();
       OperationFuture<WasmPlugin, OperationMetadata> future =
           networkServicesClient.createWasmPluginOperationCallable().futureCall(request);
       // Do something.
       WasmPlugin response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginRequest),[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginVersionAsync(@Nullable WasmPluginName parent, WasmPluginVersion wasmPluginVersion, String wasmPluginVersionId)
    
    
    public final OperationFuture<WasmPluginVersion,OperationMetadata> createWasmPluginVersionAsync(@Nullable WasmPluginName parent, WasmPluginVersion wasmPluginVersion, String wasmPluginVersionId)

Creates a new `WasmPluginVersion` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       WasmPluginName parent = WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]");
       WasmPluginVersion wasmPluginVersion = WasmPluginVersion.newBuilder().build();
       String wasmPluginVersionId = "wasmPluginVersionId38892252";
       WasmPluginVersion response =
           networkServicesClient
               .createWasmPluginVersionAsync(parent, wasmPluginVersion, wasmPluginVersionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.WasmPluginName`  
Required. The parent resource of the `WasmPluginVersion` resource. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}`.  
`wasmPluginVersion` | `[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)`  
Required. `WasmPluginVersion` resource to be created.  
`wasmPluginVersionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `WasmPluginVersion` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginVersionAsync(CreateWasmPluginVersionRequest request)
    
    
    public final OperationFuture<WasmPluginVersion,OperationMetadata> createWasmPluginVersionAsync(CreateWasmPluginVersionRequest request)

Creates a new `WasmPluginVersion` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateWasmPluginVersionRequest request =
           CreateWasmPluginVersionRequest.newBuilder()
               .setParent(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .setWasmPluginVersionId("wasmPluginVersionId38892252")
               .setWasmPluginVersion(WasmPluginVersion.newBuilder().build())
               .build();
       WasmPluginVersion response =
           networkServicesClient.createWasmPluginVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginVersionAsync(String parent, WasmPluginVersion wasmPluginVersion, String wasmPluginVersionId)
    
    
    public final OperationFuture<WasmPluginVersion,OperationMetadata> createWasmPluginVersionAsync(String parent, WasmPluginVersion wasmPluginVersion, String wasmPluginVersionId)

Creates a new `WasmPluginVersion` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString();
       WasmPluginVersion wasmPluginVersion = WasmPluginVersion.newBuilder().build();
       String wasmPluginVersionId = "wasmPluginVersionId38892252";
       WasmPluginVersion response =
           networkServicesClient
               .createWasmPluginVersionAsync(parent, wasmPluginVersion, wasmPluginVersionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `WasmPluginVersion` resource. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}`.  
`wasmPluginVersion` | `[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)`  
Required. `WasmPluginVersion` resource to be created.  
`wasmPluginVersionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `WasmPluginVersion` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginVersionCallable()
    
    
    public final UnaryCallable<CreateWasmPluginVersionRequest,Operation> createWasmPluginVersionCallable()

Creates a new `WasmPluginVersion` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateWasmPluginVersionRequest request =
           CreateWasmPluginVersionRequest.newBuilder()
               .setParent(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .setWasmPluginVersionId("wasmPluginVersionId38892252")
               .setWasmPluginVersion(WasmPluginVersion.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.createWasmPluginVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWasmPluginVersionOperationCallable()
    
    
    public final OperationCallable<CreateWasmPluginVersionRequest,WasmPluginVersion,OperationMetadata> createWasmPluginVersionOperationCallable()

Creates a new `WasmPluginVersion` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       CreateWasmPluginVersionRequest request =
           CreateWasmPluginVersionRequest.newBuilder()
               .setParent(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .setWasmPluginVersionId("wasmPluginVersionId38892252")
               .setWasmPluginVersion(WasmPluginVersion.newBuilder().build())
               .build();
       OperationFuture<WasmPluginVersion, OperationMetadata> future =
           networkServicesClient.createWasmPluginVersionOperationCallable().futureCall(request);
       // Do something.
       WasmPluginVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest),[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAgentGatewayAsync(@Nullable AgentGatewayName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAgentGatewayAsync(@Nullable AgentGatewayName name)

Deletes a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       AgentGatewayName name = AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]");
       networkServicesClient.deleteAgentGatewayAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.AgentGatewayName`  
Required. A name of the AgentGateway to delete. Must be in the format `projects/*/locations/*/agentGateways/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAgentGatewayAsync(DeleteAgentGatewayRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAgentGatewayAsync(DeleteAgentGatewayRequest request)

Deletes a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteAgentGatewayRequest request =
           DeleteAgentGatewayRequest.newBuilder()
               .setName(AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]").toString())
               .setEtag("etag3123477")
               .build();
       networkServicesClient.deleteAgentGatewayAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAgentGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAgentGatewayAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAgentGatewayAsync(String name)

Deletes a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]").toString();
       networkServicesClient.deleteAgentGatewayAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the AgentGateway to delete. Must be in the format `projects/*/locations/*/agentGateways/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAgentGatewayCallable()
    
    
    public final UnaryCallable<DeleteAgentGatewayRequest,Operation> deleteAgentGatewayCallable()

Deletes a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteAgentGatewayRequest request =
           DeleteAgentGatewayRequest.newBuilder()
               .setName(AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteAgentGatewayCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAgentGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAgentGatewayOperationCallable()
    
    
    public final OperationCallable<DeleteAgentGatewayRequest,Empty,OperationMetadata> deleteAgentGatewayOperationCallable()

Deletes a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteAgentGatewayRequest request =
           DeleteAgentGatewayRequest.newBuilder()
               .setName(AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteAgentGatewayOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAgentGatewayRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteEndpointPolicyAsync(@Nullable EndpointPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEndpointPolicyAsync(@Nullable EndpointPolicyName name)

Deletes a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       EndpointPolicyName name =
           EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]");
       networkServicesClient.deleteEndpointPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.EndpointPolicyName`  
Required. A name of the EndpointPolicy to delete. Must be in the format `projects/*/locations/*/endpointPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteEndpointPolicyAsync(DeleteEndpointPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEndpointPolicyAsync(DeleteEndpointPolicyRequest request)

Deletes a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteEndpointPolicyRequest request =
           DeleteEndpointPolicyRequest.newBuilder()
               .setName(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .build();
       networkServicesClient.deleteEndpointPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteEndpointPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteEndpointPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEndpointPolicyAsync(String name)

Deletes a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString();
       networkServicesClient.deleteEndpointPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the EndpointPolicy to delete. Must be in the format `projects/*/locations/*/endpointPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteEndpointPolicyCallable()
    
    
    public final UnaryCallable<DeleteEndpointPolicyRequest,Operation> deleteEndpointPolicyCallable()

Deletes a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteEndpointPolicyRequest request =
           DeleteEndpointPolicyRequest.newBuilder()
               .setName(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteEndpointPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteEndpointPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEndpointPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteEndpointPolicyRequest,Empty,OperationMetadata> deleteEndpointPolicyOperationCallable()

Deletes a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteEndpointPolicyRequest request =
           DeleteEndpointPolicyRequest.newBuilder()
               .setName(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteEndpointPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteEndpointPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGatewayAsync(@Nullable GatewayName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewayAsync(@Nullable GatewayName name)

Deletes a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GatewayName name = GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]");
       networkServicesClient.deleteGatewayAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.GatewayName`  
Required. A name of the Gateway to delete. Must be in the format `projects/*/locations/*/gateways/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGatewayAsync(DeleteGatewayRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewayAsync(DeleteGatewayRequest request)

Deletes a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteGatewayRequest request =
           DeleteGatewayRequest.newBuilder()
               .setName(GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString())
               .build();
       networkServicesClient.deleteGatewayAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGatewayAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewayAsync(String name)

Deletes a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString();
       networkServicesClient.deleteGatewayAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the Gateway to delete. Must be in the format `projects/*/locations/*/gateways/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGatewayCallable()
    
    
    public final UnaryCallable<DeleteGatewayRequest,Operation> deleteGatewayCallable()

Deletes a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteGatewayRequest request =
           DeleteGatewayRequest.newBuilder()
               .setName(GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteGatewayCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGatewayOperationCallable()
    
    
    public final OperationCallable<DeleteGatewayRequest,Empty,OperationMetadata> deleteGatewayOperationCallable()

Deletes a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteGatewayRequest request =
           DeleteGatewayRequest.newBuilder()
               .setName(GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteGatewayOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGatewayRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGrpcRouteAsync(@Nullable GrpcRouteName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGrpcRouteAsync(@Nullable GrpcRouteName name)

Deletes a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GrpcRouteName name = GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]");
       networkServicesClient.deleteGrpcRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.GrpcRouteName`  
Required. A name of the GrpcRoute to delete. Must be in the format `projects/*/locations/*/grpcRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGrpcRouteAsync(DeleteGrpcRouteRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGrpcRouteAsync(DeleteGrpcRouteRequest request)

Deletes a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteGrpcRouteRequest request =
           DeleteGrpcRouteRequest.newBuilder()
               .setName(GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]").toString())
               .build();
       networkServicesClient.deleteGrpcRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGrpcRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGrpcRouteAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGrpcRouteAsync(String name)

Deletes a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]").toString();
       networkServicesClient.deleteGrpcRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the GrpcRoute to delete. Must be in the format `projects/*/locations/*/grpcRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGrpcRouteCallable()
    
    
    public final UnaryCallable<DeleteGrpcRouteRequest,Operation> deleteGrpcRouteCallable()

Deletes a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteGrpcRouteRequest request =
           DeleteGrpcRouteRequest.newBuilder()
               .setName(GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]").toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteGrpcRouteCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGrpcRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGrpcRouteOperationCallable()
    
    
    public final OperationCallable<DeleteGrpcRouteRequest,Empty,OperationMetadata> deleteGrpcRouteOperationCallable()

Deletes a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteGrpcRouteRequest request =
           DeleteGrpcRouteRequest.newBuilder()
               .setName(GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteGrpcRouteOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGrpcRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteHttpRouteAsync(@Nullable HttpRouteName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHttpRouteAsync(@Nullable HttpRouteName name)

Deletes a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       HttpRouteName name = HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]");
       networkServicesClient.deleteHttpRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.HttpRouteName`  
Required. A name of the HttpRoute to delete. Must be in the format `projects/*/locations/*/httpRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteHttpRouteAsync(DeleteHttpRouteRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHttpRouteAsync(DeleteHttpRouteRequest request)

Deletes a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteHttpRouteRequest request =
           DeleteHttpRouteRequest.newBuilder()
               .setName(HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]").toString())
               .build();
       networkServicesClient.deleteHttpRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteHttpRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteHttpRouteAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHttpRouteAsync(String name)

Deletes a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]").toString();
       networkServicesClient.deleteHttpRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the HttpRoute to delete. Must be in the format `projects/*/locations/*/httpRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteHttpRouteCallable()
    
    
    public final UnaryCallable<DeleteHttpRouteRequest,Operation> deleteHttpRouteCallable()

Deletes a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteHttpRouteRequest request =
           DeleteHttpRouteRequest.newBuilder()
               .setName(HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]").toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteHttpRouteCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteHttpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHttpRouteOperationCallable()
    
    
    public final OperationCallable<DeleteHttpRouteRequest,Empty,OperationMetadata> deleteHttpRouteOperationCallable()

Deletes a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteHttpRouteRequest request =
           DeleteHttpRouteRequest.newBuilder()
               .setName(HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteHttpRouteOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteHttpRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteMeshAsync(@Nullable MeshName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMeshAsync(@Nullable MeshName name)

Deletes a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       MeshName name = MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]");
       networkServicesClient.deleteMeshAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.MeshName`  
Required. A name of the Mesh to delete. Must be in the format `projects/*/locations/*/meshes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteMeshAsync(DeleteMeshRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMeshAsync(DeleteMeshRequest request)

Deletes a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteMeshRequest request =
           DeleteMeshRequest.newBuilder()
               .setName(MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString())
               .build();
       networkServicesClient.deleteMeshAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteMeshRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteMeshAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteMeshAsync(String name)

Deletes a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString();
       networkServicesClient.deleteMeshAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the Mesh to delete. Must be in the format `projects/*/locations/*/meshes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteMeshCallable()
    
    
    public final UnaryCallable<DeleteMeshRequest,Operation> deleteMeshCallable()

Deletes a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteMeshRequest request =
           DeleteMeshRequest.newBuilder()
               .setName(MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString())
               .build();
       ApiFuture<Operation> future = networkServicesClient.deleteMeshCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteMeshRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMeshOperationCallable()
    
    
    public final OperationCallable<DeleteMeshRequest,Empty,OperationMetadata> deleteMeshOperationCallable()

Deletes a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteMeshRequest request =
           DeleteMeshRequest.newBuilder()
               .setName(MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteMeshOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteMeshRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceBindingAsync(@Nullable ServiceBindingName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceBindingAsync(@Nullable ServiceBindingName name)

Deletes a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ServiceBindingName name =
           ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]");
       networkServicesClient.deleteServiceBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.ServiceBindingName`  
Required. A name of the ServiceBinding to delete. Must be in the format `projects/*/locations/*/serviceBindings/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceBindingAsync(DeleteServiceBindingRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceBindingAsync(DeleteServiceBindingRequest request)

Deletes a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteServiceBindingRequest request =
           DeleteServiceBindingRequest.newBuilder()
               .setName(
                   ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]").toString())
               .build();
       networkServicesClient.deleteServiceBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceBindingAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceBindingAsync(String name)

Deletes a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]").toString();
       networkServicesClient.deleteServiceBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the ServiceBinding to delete. Must be in the format `projects/*/locations/*/serviceBindings/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceBindingCallable()
    
    
    public final UnaryCallable<DeleteServiceBindingRequest,Operation> deleteServiceBindingCallable()

Deletes a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteServiceBindingRequest request =
           DeleteServiceBindingRequest.newBuilder()
               .setName(
                   ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]").toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteServiceBindingCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceBindingOperationCallable()
    
    
    public final OperationCallable<DeleteServiceBindingRequest,Empty,OperationMetadata> deleteServiceBindingOperationCallable()

Deletes a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteServiceBindingRequest request =
           DeleteServiceBindingRequest.newBuilder()
               .setName(
                   ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteServiceBindingOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceLbPolicyAsync(@Nullable ServiceLbPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceLbPolicyAsync(@Nullable ServiceLbPolicyName name)

Deletes a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ServiceLbPolicyName name =
           ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]");
       networkServicesClient.deleteServiceLbPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.ServiceLbPolicyName`  
Required. A name of the ServiceLbPolicy to delete. Must be in the format `projects/{project}/locations/{location}/serviceLbPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceLbPolicyAsync(DeleteServiceLbPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceLbPolicyAsync(DeleteServiceLbPolicyRequest request)

Deletes a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteServiceLbPolicyRequest request =
           DeleteServiceLbPolicyRequest.newBuilder()
               .setName(
                   ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]")
                       .toString())
               .build();
       networkServicesClient.deleteServiceLbPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceLbPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceLbPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceLbPolicyAsync(String name)

Deletes a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]").toString();
       networkServicesClient.deleteServiceLbPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the ServiceLbPolicy to delete. Must be in the format `projects/{project}/locations/{location}/serviceLbPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceLbPolicyCallable()
    
    
    public final UnaryCallable<DeleteServiceLbPolicyRequest,Operation> deleteServiceLbPolicyCallable()

Deletes a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteServiceLbPolicyRequest request =
           DeleteServiceLbPolicyRequest.newBuilder()
               .setName(
                   ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteServiceLbPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceLbPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceLbPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteServiceLbPolicyRequest,Empty,OperationMetadata> deleteServiceLbPolicyOperationCallable()

Deletes a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteServiceLbPolicyRequest request =
           DeleteServiceLbPolicyRequest.newBuilder()
               .setName(
                   ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteServiceLbPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceLbPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTcpRouteAsync(@Nullable TcpRouteName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTcpRouteAsync(@Nullable TcpRouteName name)

Deletes a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       TcpRouteName name = TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]");
       networkServicesClient.deleteTcpRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.TcpRouteName`  
Required. A name of the TcpRoute to delete. Must be in the format `projects/*/locations/*/tcpRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTcpRouteAsync(DeleteTcpRouteRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTcpRouteAsync(DeleteTcpRouteRequest request)

Deletes a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteTcpRouteRequest request =
           DeleteTcpRouteRequest.newBuilder()
               .setName(TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]").toString())
               .build();
       networkServicesClient.deleteTcpRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTcpRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTcpRouteAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTcpRouteAsync(String name)

Deletes a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]").toString();
       networkServicesClient.deleteTcpRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the TcpRoute to delete. Must be in the format `projects/*/locations/*/tcpRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTcpRouteCallable()
    
    
    public final UnaryCallable<DeleteTcpRouteRequest,Operation> deleteTcpRouteCallable()

Deletes a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteTcpRouteRequest request =
           DeleteTcpRouteRequest.newBuilder()
               .setName(TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]").toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteTcpRouteCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTcpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTcpRouteOperationCallable()
    
    
    public final OperationCallable<DeleteTcpRouteRequest,Empty,OperationMetadata> deleteTcpRouteOperationCallable()

Deletes a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteTcpRouteRequest request =
           DeleteTcpRouteRequest.newBuilder()
               .setName(TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteTcpRouteOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTcpRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTlsRouteAsync(@Nullable TlsRouteName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTlsRouteAsync(@Nullable TlsRouteName name)

Deletes a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       TlsRouteName name = TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]");
       networkServicesClient.deleteTlsRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.TlsRouteName`  
Required. A name of the TlsRoute to delete. Must be in the format `projects/*/locations/*/tlsRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTlsRouteAsync(DeleteTlsRouteRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTlsRouteAsync(DeleteTlsRouteRequest request)

Deletes a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteTlsRouteRequest request =
           DeleteTlsRouteRequest.newBuilder()
               .setName(TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]").toString())
               .build();
       networkServicesClient.deleteTlsRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTlsRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTlsRouteAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTlsRouteAsync(String name)

Deletes a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]").toString();
       networkServicesClient.deleteTlsRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the TlsRoute to delete. Must be in the format `projects/*/locations/*/tlsRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTlsRouteCallable()
    
    
    public final UnaryCallable<DeleteTlsRouteRequest,Operation> deleteTlsRouteCallable()

Deletes a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteTlsRouteRequest request =
           DeleteTlsRouteRequest.newBuilder()
               .setName(TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]").toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteTlsRouteCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTlsRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTlsRouteOperationCallable()
    
    
    public final OperationCallable<DeleteTlsRouteRequest,Empty,OperationMetadata> deleteTlsRouteOperationCallable()

Deletes a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteTlsRouteRequest request =
           DeleteTlsRouteRequest.newBuilder()
               .setName(TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteTlsRouteOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTlsRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginAsync(@Nullable WasmPluginName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteWasmPluginAsync(@Nullable WasmPluginName name)

Deletes the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       WasmPluginName name = WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]");
       networkServicesClient.deleteWasmPluginAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.WasmPluginName`  
Required. A name of the `WasmPlugin` resource to delete. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginAsync(DeleteWasmPluginRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteWasmPluginAsync(DeleteWasmPluginRequest request)

Deletes the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteWasmPluginRequest request =
           DeleteWasmPluginRequest.newBuilder()
               .setName(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .build();
       networkServicesClient.deleteWasmPluginAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteWasmPluginAsync(String name)

Deletes the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString();
       networkServicesClient.deleteWasmPluginAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `WasmPlugin` resource to delete. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginCallable()
    
    
    public final UnaryCallable<DeleteWasmPluginRequest,Operation> deleteWasmPluginCallable()

Deletes the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteWasmPluginRequest request =
           DeleteWasmPluginRequest.newBuilder()
               .setName(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteWasmPluginCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWasmPluginOperationCallable()
    
    
    public final OperationCallable<DeleteWasmPluginRequest,Empty,OperationMetadata> deleteWasmPluginOperationCallable()

Deletes the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteWasmPluginRequest request =
           DeleteWasmPluginRequest.newBuilder()
               .setName(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteWasmPluginOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginVersionAsync(@Nullable WasmPluginVersionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteWasmPluginVersionAsync(@Nullable WasmPluginVersionName name)

Deletes the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       WasmPluginVersionName name =
           WasmPluginVersionName.of(
               "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]");
       networkServicesClient.deleteWasmPluginVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.WasmPluginVersionName`  
Required. A name of the `WasmPluginVersion` resource to delete. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}/versions/{wasm_plugin_version}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginVersionAsync(DeleteWasmPluginVersionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteWasmPluginVersionAsync(DeleteWasmPluginVersionRequest request)

Deletes the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteWasmPluginVersionRequest request =
           DeleteWasmPluginVersionRequest.newBuilder()
               .setName(
                   WasmPluginVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]")
                       .toString())
               .build();
       networkServicesClient.deleteWasmPluginVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginVersionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteWasmPluginVersionAsync(String name)

Deletes the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           WasmPluginVersionName.of(
                   "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]")
               .toString();
       networkServicesClient.deleteWasmPluginVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `WasmPluginVersion` resource to delete. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}/versions/{wasm_plugin_version}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginVersionCallable()
    
    
    public final UnaryCallable<DeleteWasmPluginVersionRequest,Operation> deleteWasmPluginVersionCallable()

Deletes the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteWasmPluginVersionRequest request =
           DeleteWasmPluginVersionRequest.newBuilder()
               .setName(
                   WasmPluginVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.deleteWasmPluginVersionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWasmPluginVersionOperationCallable()
    
    
    public final OperationCallable<DeleteWasmPluginVersionRequest,Empty,OperationMetadata> deleteWasmPluginVersionOperationCallable()

Deletes the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       DeleteWasmPluginVersionRequest request =
           DeleteWasmPluginVersionRequest.newBuilder()
               .setName(
                   WasmPluginVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkServicesClient.deleteWasmPluginVersionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### getAgentGateway(@Nullable AgentGatewayName name)
    
    
    public final AgentGateway getAgentGateway(@Nullable AgentGatewayName name)

Gets details of a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       AgentGatewayName name = AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]");
       AgentGateway response = networkServicesClient.getAgentGateway(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.AgentGatewayName`  
Required. A name of the AgentGateway to get. Must be in the format `projects/*/locations/*/agentGateways/*`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)` |   
  
### getAgentGateway(GetAgentGatewayRequest request)
    
    
    public final AgentGateway getAgentGateway(GetAgentGatewayRequest request)

Gets details of a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetAgentGatewayRequest request =
           GetAgentGatewayRequest.newBuilder()
               .setName(AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]").toString())
               .build();
       AgentGateway response = networkServicesClient.getAgentGateway(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetAgentGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)` |   
  
### getAgentGateway(String name)
    
    
    public final AgentGateway getAgentGateway(String name)

Gets details of a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]").toString();
       AgentGateway response = networkServicesClient.getAgentGateway(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the AgentGateway to get. Must be in the format `projects/*/locations/*/agentGateways/*`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)` |   
  
### getAgentGatewayCallable()
    
    
    public final UnaryCallable<GetAgentGatewayRequest,AgentGateway> getAgentGatewayCallable()

Gets details of a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetAgentGatewayRequest request =
           GetAgentGatewayRequest.newBuilder()
               .setName(AgentGatewayName.of("[PROJECT]", "[LOCATION]", "[AGENT_GATEWAY]").toString())
               .build();
       ApiFuture<AgentGateway> future =
           networkServicesClient.getAgentGatewayCallable().futureCall(request);
       // Do something.
       AgentGateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetAgentGatewayRequest),[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)>` |   
  
### getEndpointPolicy(@Nullable EndpointPolicyName name)
    
    
    public final EndpointPolicy getEndpointPolicy(@Nullable EndpointPolicyName name)

Gets details of a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       EndpointPolicyName name =
           EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]");
       EndpointPolicy response = networkServicesClient.getEndpointPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.EndpointPolicyName`  
Required. A name of the EndpointPolicy to get. Must be in the format `projects/*/locations/*/endpointPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)` |   
  
### getEndpointPolicy(GetEndpointPolicyRequest request)
    
    
    public final EndpointPolicy getEndpointPolicy(GetEndpointPolicyRequest request)

Gets details of a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetEndpointPolicyRequest request =
           GetEndpointPolicyRequest.newBuilder()
               .setName(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .build();
       EndpointPolicy response = networkServicesClient.getEndpointPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetEndpointPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)` |   
  
### getEndpointPolicy(String name)
    
    
    public final EndpointPolicy getEndpointPolicy(String name)

Gets details of a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString();
       EndpointPolicy response = networkServicesClient.getEndpointPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the EndpointPolicy to get. Must be in the format `projects/*/locations/*/endpointPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)` |   
  
### getEndpointPolicyCallable()
    
    
    public final UnaryCallable<GetEndpointPolicyRequest,EndpointPolicy> getEndpointPolicyCallable()

Gets details of a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetEndpointPolicyRequest request =
           GetEndpointPolicyRequest.newBuilder()
               .setName(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .build();
       ApiFuture<EndpointPolicy> future =
           networkServicesClient.getEndpointPolicyCallable().futureCall(request);
       // Do something.
       EndpointPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetEndpointPolicyRequest),[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)>` |   
  
### getGateway(@Nullable GatewayName name)
    
    
    public final Gateway getGateway(@Nullable GatewayName name)

Gets details of a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GatewayName name = GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]");
       Gateway response = networkServicesClient.getGateway(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.GatewayName`  
Required. A name of the Gateway to get. Must be in the format `projects/*/locations/*/gateways/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)` |   
  
### getGateway(GetGatewayRequest request)
    
    
    public final Gateway getGateway(GetGatewayRequest request)

Gets details of a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetGatewayRequest request =
           GetGatewayRequest.newBuilder()
               .setName(GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString())
               .build();
       Gateway response = networkServicesClient.getGateway(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)` |   
  
### getGateway(String name)
    
    
    public final Gateway getGateway(String name)

Gets details of a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString();
       Gateway response = networkServicesClient.getGateway(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the Gateway to get. Must be in the format `projects/*/locations/*/gateways/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)` |   
  
### getGatewayCallable()
    
    
    public final UnaryCallable<GetGatewayRequest,Gateway> getGatewayCallable()

Gets details of a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetGatewayRequest request =
           GetGatewayRequest.newBuilder()
               .setName(GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString())
               .build();
       ApiFuture<Gateway> future = networkServicesClient.getGatewayCallable().futureCall(request);
       // Do something.
       Gateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRequest),[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)>` |   
  
### getGatewayRouteView(@Nullable GatewayRouteViewName name)
    
    
    public final GatewayRouteView getGatewayRouteView(@Nullable GatewayRouteViewName name)

Get a single RouteView of a Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GatewayRouteViewName name =
           GatewayRouteViewName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]", "[ROUTE_VIEW]");
       GatewayRouteView response = networkServicesClient.getGatewayRouteView(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.GatewayRouteViewName`  
Required. Name of the GatewayRouteView resource. Formats: projects/{project}/locations/{location}/gateways/{gateway}/routeViews/{route_view}  
**Returns**  
---  
**Type** | **Description**  
`[GatewayRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GatewayRouteView)` |   
  
### getGatewayRouteView(GetGatewayRouteViewRequest request)
    
    
    public final GatewayRouteView getGatewayRouteView(GetGatewayRouteViewRequest request)

Get a single RouteView of a Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetGatewayRouteViewRequest request =
           GetGatewayRouteViewRequest.newBuilder()
               .setName(
                   GatewayRouteViewName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]", "[ROUTE_VIEW]")
                       .toString())
               .build();
       GatewayRouteView response = networkServicesClient.getGatewayRouteView(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGatewayRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRouteViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GatewayRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GatewayRouteView)` |   
  
### getGatewayRouteView(String name)
    
    
    public final GatewayRouteView getGatewayRouteView(String name)

Get a single RouteView of a Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           GatewayRouteViewName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]", "[ROUTE_VIEW]")
               .toString();
       GatewayRouteView response = networkServicesClient.getGatewayRouteView(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the GatewayRouteView resource. Formats: projects/{project}/locations/{location}/gateways/{gateway}/routeViews/{route_view}  
**Returns**  
---  
**Type** | **Description**  
`[GatewayRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GatewayRouteView)` |   
  
### getGatewayRouteViewCallable()
    
    
    public final UnaryCallable<GetGatewayRouteViewRequest,GatewayRouteView> getGatewayRouteViewCallable()

Get a single RouteView of a Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetGatewayRouteViewRequest request =
           GetGatewayRouteViewRequest.newBuilder()
               .setName(
                   GatewayRouteViewName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]", "[ROUTE_VIEW]")
                       .toString())
               .build();
       ApiFuture<GatewayRouteView> future =
           networkServicesClient.getGatewayRouteViewCallable().futureCall(request);
       // Do something.
       GatewayRouteView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGatewayRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRouteViewRequest),[GatewayRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GatewayRouteView)>` |   
  
### getGrpcRoute(@Nullable GrpcRouteName name)
    
    
    public final GrpcRoute getGrpcRoute(@Nullable GrpcRouteName name)

Gets details of a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GrpcRouteName name = GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]");
       GrpcRoute response = networkServicesClient.getGrpcRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.GrpcRouteName`  
Required. A name of the GrpcRoute to get. Must be in the format `projects/*/locations/*/grpcRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)` |   
  
### getGrpcRoute(GetGrpcRouteRequest request)
    
    
    public final GrpcRoute getGrpcRoute(GetGrpcRouteRequest request)

Gets details of a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetGrpcRouteRequest request =
           GetGrpcRouteRequest.newBuilder()
               .setName(GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]").toString())
               .build();
       GrpcRoute response = networkServicesClient.getGrpcRoute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGrpcRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)` |   
  
### getGrpcRoute(String name)
    
    
    public final GrpcRoute getGrpcRoute(String name)

Gets details of a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]").toString();
       GrpcRoute response = networkServicesClient.getGrpcRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the GrpcRoute to get. Must be in the format `projects/*/locations/*/grpcRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)` |   
  
### getGrpcRouteCallable()
    
    
    public final UnaryCallable<GetGrpcRouteRequest,GrpcRoute> getGrpcRouteCallable()

Gets details of a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetGrpcRouteRequest request =
           GetGrpcRouteRequest.newBuilder()
               .setName(GrpcRouteName.of("[PROJECT]", "[LOCATION]", "[GRPC_ROUTE]").toString())
               .build();
       ApiFuture<GrpcRoute> future =
           networkServicesClient.getGrpcRouteCallable().futureCall(request);
       // Do something.
       GrpcRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGrpcRouteRequest),[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getHttpRoute(@Nullable HttpRouteName name)
    
    
    public final HttpRoute getHttpRoute(@Nullable HttpRouteName name)

Gets details of a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       HttpRouteName name = HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]");
       HttpRoute response = networkServicesClient.getHttpRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.HttpRouteName`  
Required. A name of the HttpRoute to get. Must be in the format `projects/*/locations/*/httpRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)` |   
  
### getHttpRoute(GetHttpRouteRequest request)
    
    
    public final HttpRoute getHttpRoute(GetHttpRouteRequest request)

Gets details of a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetHttpRouteRequest request =
           GetHttpRouteRequest.newBuilder()
               .setName(HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]").toString())
               .build();
       HttpRoute response = networkServicesClient.getHttpRoute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetHttpRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)` |   
  
### getHttpRoute(String name)
    
    
    public final HttpRoute getHttpRoute(String name)

Gets details of a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]").toString();
       HttpRoute response = networkServicesClient.getHttpRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the HttpRoute to get. Must be in the format `projects/*/locations/*/httpRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)` |   
  
### getHttpRouteCallable()
    
    
    public final UnaryCallable<GetHttpRouteRequest,HttpRoute> getHttpRouteCallable()

Gets details of a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetHttpRouteRequest request =
           GetHttpRouteRequest.newBuilder()
               .setName(HttpRouteName.of("[PROJECT]", "[LOCATION]", "[HTTP_ROUTE]").toString())
               .build();
       ApiFuture<HttpRoute> future =
           networkServicesClient.getHttpRouteCallable().futureCall(request);
       // Do something.
       HttpRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetHttpRouteRequest),[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = networkServicesClient.getIamPolicy(request);
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
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = networkServicesClient.getIamPolicyCallable().futureCall(request);
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
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = networkServicesClient.getLocation(request);
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
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = networkServicesClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMesh(@Nullable MeshName name)
    
    
    public final Mesh getMesh(@Nullable MeshName name)

Gets details of a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       MeshName name = MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]");
       Mesh response = networkServicesClient.getMesh(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.MeshName`  
Required. A name of the Mesh to get. Must be in the format `projects/*/locations/*/meshes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)` |   
  
### getMesh(GetMeshRequest request)
    
    
    public final Mesh getMesh(GetMeshRequest request)

Gets details of a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetMeshRequest request =
           GetMeshRequest.newBuilder()
               .setName(MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString())
               .build();
       Mesh response = networkServicesClient.getMesh(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)` |   
  
### getMesh(String name)
    
    
    public final Mesh getMesh(String name)

Gets details of a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString();
       Mesh response = networkServicesClient.getMesh(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the Mesh to get. Must be in the format `projects/*/locations/*/meshes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)` |   
  
### getMeshCallable()
    
    
    public final UnaryCallable<GetMeshRequest,Mesh> getMeshCallable()

Gets details of a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetMeshRequest request =
           GetMeshRequest.newBuilder()
               .setName(MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString())
               .build();
       ApiFuture<Mesh> future = networkServicesClient.getMeshCallable().futureCall(request);
       // Do something.
       Mesh response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRequest),[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)>` |   
  
### getMeshRouteView(@Nullable MeshRouteViewName name)
    
    
    public final MeshRouteView getMeshRouteView(@Nullable MeshRouteViewName name)

Get a single RouteView of a Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       MeshRouteViewName name =
           MeshRouteViewName.of("[PROJECT]", "[LOCATION]", "[MESH]", "[ROUTE_VIEW]");
       MeshRouteView response = networkServicesClient.getMeshRouteView(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.MeshRouteViewName`  
Required. Name of the MeshRouteView resource. Format: projects/{project}/locations/{location}/meshes/{mesh}/routeViews/{route_view}  
**Returns**  
---  
**Type** | **Description**  
`[MeshRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.MeshRouteView)` |   
  
### getMeshRouteView(GetMeshRouteViewRequest request)
    
    
    public final MeshRouteView getMeshRouteView(GetMeshRouteViewRequest request)

Get a single RouteView of a Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetMeshRouteViewRequest request =
           GetMeshRouteViewRequest.newBuilder()
               .setName(
                   MeshRouteViewName.of("[PROJECT]", "[LOCATION]", "[MESH]", "[ROUTE_VIEW]")
                       .toString())
               .build();
       MeshRouteView response = networkServicesClient.getMeshRouteView(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMeshRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRouteViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MeshRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.MeshRouteView)` |   
  
### getMeshRouteView(String name)
    
    
    public final MeshRouteView getMeshRouteView(String name)

Get a single RouteView of a Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           MeshRouteViewName.of("[PROJECT]", "[LOCATION]", "[MESH]", "[ROUTE_VIEW]").toString();
       MeshRouteView response = networkServicesClient.getMeshRouteView(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the MeshRouteView resource. Format: projects/{project}/locations/{location}/meshes/{mesh}/routeViews/{route_view}  
**Returns**  
---  
**Type** | **Description**  
`[MeshRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.MeshRouteView)` |   
  
### getMeshRouteViewCallable()
    
    
    public final UnaryCallable<GetMeshRouteViewRequest,MeshRouteView> getMeshRouteViewCallable()

Get a single RouteView of a Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetMeshRouteViewRequest request =
           GetMeshRouteViewRequest.newBuilder()
               .setName(
                   MeshRouteViewName.of("[PROJECT]", "[LOCATION]", "[MESH]", "[ROUTE_VIEW]")
                       .toString())
               .build();
       ApiFuture<MeshRouteView> future =
           networkServicesClient.getMeshRouteViewCallable().futureCall(request);
       // Do something.
       MeshRouteView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMeshRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRouteViewRequest),[MeshRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.MeshRouteView)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getServiceBinding(@Nullable ServiceBindingName name)
    
    
    public final ServiceBinding getServiceBinding(@Nullable ServiceBindingName name)

Gets details of a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ServiceBindingName name =
           ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]");
       ServiceBinding response = networkServicesClient.getServiceBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.ServiceBindingName`  
Required. A name of the ServiceBinding to get. Must be in the format `projects/*/locations/*/serviceBindings/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)` |   
  
### getServiceBinding(GetServiceBindingRequest request)
    
    
    public final ServiceBinding getServiceBinding(GetServiceBindingRequest request)

Gets details of a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetServiceBindingRequest request =
           GetServiceBindingRequest.newBuilder()
               .setName(
                   ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]").toString())
               .build();
       ServiceBinding response = networkServicesClient.getServiceBinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)` |   
  
### getServiceBinding(String name)
    
    
    public final ServiceBinding getServiceBinding(String name)

Gets details of a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]").toString();
       ServiceBinding response = networkServicesClient.getServiceBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the ServiceBinding to get. Must be in the format `projects/*/locations/*/serviceBindings/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)` |   
  
### getServiceBindingCallable()
    
    
    public final UnaryCallable<GetServiceBindingRequest,ServiceBinding> getServiceBindingCallable()

Gets details of a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetServiceBindingRequest request =
           GetServiceBindingRequest.newBuilder()
               .setName(
                   ServiceBindingName.of("[PROJECT]", "[LOCATION]", "[SERVICE_BINDING]").toString())
               .build();
       ApiFuture<ServiceBinding> future =
           networkServicesClient.getServiceBindingCallable().futureCall(request);
       // Do something.
       ServiceBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceBindingRequest),[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)>` |   
  
### getServiceLbPolicy(@Nullable ServiceLbPolicyName name)
    
    
    public final ServiceLbPolicy getServiceLbPolicy(@Nullable ServiceLbPolicyName name)

Gets details of a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ServiceLbPolicyName name =
           ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]");
       ServiceLbPolicy response = networkServicesClient.getServiceLbPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.ServiceLbPolicyName`  
Required. A name of the ServiceLbPolicy to get. Must be in the format `projects/{project}/locations/{location}/serviceLbPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)` |   
  
### getServiceLbPolicy(GetServiceLbPolicyRequest request)
    
    
    public final ServiceLbPolicy getServiceLbPolicy(GetServiceLbPolicyRequest request)

Gets details of a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetServiceLbPolicyRequest request =
           GetServiceLbPolicyRequest.newBuilder()
               .setName(
                   ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]")
                       .toString())
               .build();
       ServiceLbPolicy response = networkServicesClient.getServiceLbPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceLbPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)` |   
  
### getServiceLbPolicy(String name)
    
    
    public final ServiceLbPolicy getServiceLbPolicy(String name)

Gets details of a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]").toString();
       ServiceLbPolicy response = networkServicesClient.getServiceLbPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the ServiceLbPolicy to get. Must be in the format `projects/{project}/locations/{location}/serviceLbPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)` |   
  
### getServiceLbPolicyCallable()
    
    
    public final UnaryCallable<GetServiceLbPolicyRequest,ServiceLbPolicy> getServiceLbPolicyCallable()

Gets details of a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetServiceLbPolicyRequest request =
           GetServiceLbPolicyRequest.newBuilder()
               .setName(
                   ServiceLbPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_LB_POLICY]")
                       .toString())
               .build();
       ApiFuture<ServiceLbPolicy> future =
           networkServicesClient.getServiceLbPolicyCallable().futureCall(request);
       // Do something.
       ServiceLbPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceLbPolicyRequest),[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)>` |   
  
### getSettings()
    
    
    public final @Nullable NetworkServicesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.NetworkServicesSettings` |   
  
### getStub()
    
    
    public NetworkServicesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.stub.NetworkServicesStub)` |   
  
### getTcpRoute(@Nullable TcpRouteName name)
    
    
    public final TcpRoute getTcpRoute(@Nullable TcpRouteName name)

Gets details of a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       TcpRouteName name = TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]");
       TcpRoute response = networkServicesClient.getTcpRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.TcpRouteName`  
Required. A name of the TcpRoute to get. Must be in the format `projects/*/locations/*/tcpRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)` |   
  
### getTcpRoute(GetTcpRouteRequest request)
    
    
    public final TcpRoute getTcpRoute(GetTcpRouteRequest request)

Gets details of a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetTcpRouteRequest request =
           GetTcpRouteRequest.newBuilder()
               .setName(TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]").toString())
               .build();
       TcpRoute response = networkServicesClient.getTcpRoute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTcpRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)` |   
  
### getTcpRoute(String name)
    
    
    public final TcpRoute getTcpRoute(String name)

Gets details of a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]").toString();
       TcpRoute response = networkServicesClient.getTcpRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the TcpRoute to get. Must be in the format `projects/*/locations/*/tcpRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)` |   
  
### getTcpRouteCallable()
    
    
    public final UnaryCallable<GetTcpRouteRequest,TcpRoute> getTcpRouteCallable()

Gets details of a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetTcpRouteRequest request =
           GetTcpRouteRequest.newBuilder()
               .setName(TcpRouteName.of("[PROJECT]", "[LOCATION]", "[TCP_ROUTE]").toString())
               .build();
       ApiFuture<TcpRoute> future = networkServicesClient.getTcpRouteCallable().futureCall(request);
       // Do something.
       TcpRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTcpRouteRequest),[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)>` |   
  
### getTlsRoute(@Nullable TlsRouteName name)
    
    
    public final TlsRoute getTlsRoute(@Nullable TlsRouteName name)

Gets details of a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       TlsRouteName name = TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]");
       TlsRoute response = networkServicesClient.getTlsRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.TlsRouteName`  
Required. A name of the TlsRoute to get. Must be in the format `projects/*/locations/*/tlsRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)` |   
  
### getTlsRoute(GetTlsRouteRequest request)
    
    
    public final TlsRoute getTlsRoute(GetTlsRouteRequest request)

Gets details of a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetTlsRouteRequest request =
           GetTlsRouteRequest.newBuilder()
               .setName(TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]").toString())
               .build();
       TlsRoute response = networkServicesClient.getTlsRoute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTlsRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)` |   
  
### getTlsRoute(String name)
    
    
    public final TlsRoute getTlsRoute(String name)

Gets details of a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]").toString();
       TlsRoute response = networkServicesClient.getTlsRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the TlsRoute to get. Must be in the format `projects/*/locations/*/tlsRoutes/*`.  
**Returns**  
---  
**Type** | **Description**  
`[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)` |   
  
### getTlsRouteCallable()
    
    
    public final UnaryCallable<GetTlsRouteRequest,TlsRoute> getTlsRouteCallable()

Gets details of a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetTlsRouteRequest request =
           GetTlsRouteRequest.newBuilder()
               .setName(TlsRouteName.of("[PROJECT]", "[LOCATION]", "[TLS_ROUTE]").toString())
               .build();
       ApiFuture<TlsRoute> future = networkServicesClient.getTlsRouteCallable().futureCall(request);
       // Do something.
       TlsRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTlsRouteRequest),[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)>` |   
  
### getWasmPlugin(@Nullable WasmPluginName name)
    
    
    public final WasmPlugin getWasmPlugin(@Nullable WasmPluginName name)

Gets details of the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       WasmPluginName name = WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]");
       WasmPlugin response = networkServicesClient.getWasmPlugin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.WasmPluginName`  
Required. A name of the `WasmPlugin` resource to get. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)` |   
  
### getWasmPlugin(GetWasmPluginRequest request)
    
    
    public final WasmPlugin getWasmPlugin(GetWasmPluginRequest request)

Gets details of the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetWasmPluginRequest request =
           GetWasmPluginRequest.newBuilder()
               .setName(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .setView(WasmPluginView.forNumber(0))
               .build();
       WasmPlugin response = networkServicesClient.getWasmPlugin(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)` |   
  
### getWasmPlugin(String name)
    
    
    public final WasmPlugin getWasmPlugin(String name)

Gets details of the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name = WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString();
       WasmPlugin response = networkServicesClient.getWasmPlugin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `WasmPlugin` resource to get. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)` |   
  
### getWasmPluginCallable()
    
    
    public final UnaryCallable<GetWasmPluginRequest,WasmPlugin> getWasmPluginCallable()

Gets details of the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetWasmPluginRequest request =
           GetWasmPluginRequest.newBuilder()
               .setName(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .setView(WasmPluginView.forNumber(0))
               .build();
       ApiFuture<WasmPlugin> future =
           networkServicesClient.getWasmPluginCallable().futureCall(request);
       // Do something.
       WasmPlugin response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginRequest),[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)>` |   
  
### getWasmPluginVersion(@Nullable WasmPluginVersionName name)
    
    
    public final WasmPluginVersion getWasmPluginVersion(@Nullable WasmPluginVersionName name)

Gets details of the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       WasmPluginVersionName name =
           WasmPluginVersionName.of(
               "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]");
       WasmPluginVersion response = networkServicesClient.getWasmPluginVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.WasmPluginVersionName`  
Required. A name of the `WasmPluginVersion` resource to get. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}/versions/{wasm_plugin_version}`.  
**Returns**  
---  
**Type** | **Description**  
`[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)` |   
  
### getWasmPluginVersion(GetWasmPluginVersionRequest request)
    
    
    public final WasmPluginVersion getWasmPluginVersion(GetWasmPluginVersionRequest request)

Gets details of the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetWasmPluginVersionRequest request =
           GetWasmPluginVersionRequest.newBuilder()
               .setName(
                   WasmPluginVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]")
                       .toString())
               .build();
       WasmPluginVersion response = networkServicesClient.getWasmPluginVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)` |   
  
### getWasmPluginVersion(String name)
    
    
    public final WasmPluginVersion getWasmPluginVersion(String name)

Gets details of the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String name =
           WasmPluginVersionName.of(
                   "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]")
               .toString();
       WasmPluginVersion response = networkServicesClient.getWasmPluginVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `WasmPluginVersion` resource to get. Must be in the format `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}/versions/{wasm_plugin_version}`.  
**Returns**  
---  
**Type** | **Description**  
`[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)` |   
  
### getWasmPluginVersionCallable()
    
    
    public final UnaryCallable<GetWasmPluginVersionRequest,WasmPluginVersion> getWasmPluginVersionCallable()

Gets details of the specified `WasmPluginVersion` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GetWasmPluginVersionRequest request =
           GetWasmPluginVersionRequest.newBuilder()
               .setName(
                   WasmPluginVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]", "[WASM_PLUGIN_VERSION]")
                       .toString())
               .build();
       ApiFuture<WasmPluginVersion> future =
           networkServicesClient.getWasmPluginVersionCallable().futureCall(request);
       // Do something.
       WasmPluginVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginVersionRequest),[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)>` |   
  
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
  
### listAgentGateways(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListAgentGatewaysPagedResponse listAgentGateways(@Nullable LocationName parent)

Lists AgentGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AgentGateway element : networkServicesClient.listAgentGateways(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the AgentGateways should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListAgentGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListAgentGatewaysPagedResponse)` |   
  
### listAgentGateways(ListAgentGatewaysRequest request)
    
    
    public final NetworkServicesClient.ListAgentGatewaysPagedResponse listAgentGateways(ListAgentGatewaysRequest request)

Lists AgentGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListAgentGatewaysRequest request =
           ListAgentGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       for (AgentGateway element : networkServicesClient.listAgentGateways(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAgentGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListAgentGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListAgentGatewaysPagedResponse)` |   
  
### listAgentGateways(String parent)
    
    
    public final NetworkServicesClient.ListAgentGatewaysPagedResponse listAgentGateways(String parent)

Lists AgentGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AgentGateway element : networkServicesClient.listAgentGateways(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the AgentGateways should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListAgentGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListAgentGatewaysPagedResponse)` |   
  
### listAgentGatewaysCallable()
    
    
    public final UnaryCallable<ListAgentGatewaysRequest,ListAgentGatewaysResponse> listAgentGatewaysCallable()

Lists AgentGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListAgentGatewaysRequest request =
           ListAgentGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListAgentGatewaysResponse response =
             networkServicesClient.listAgentGatewaysCallable().call(request);
         for (AgentGateway element : response.getAgentGatewaysList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAgentGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysRequest),[ListAgentGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysResponse)>` |   
  
### listAgentGatewaysPagedCallable()
    
    
    public final UnaryCallable<ListAgentGatewaysRequest,NetworkServicesClient.ListAgentGatewaysPagedResponse> listAgentGatewaysPagedCallable()

Lists AgentGateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListAgentGatewaysRequest request =
           ListAgentGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<AgentGateway> future =
           networkServicesClient.listAgentGatewaysPagedCallable().futureCall(request);
       // Do something.
       for (AgentGateway element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAgentGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysRequest),[ListAgentGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListAgentGatewaysPagedResponse)>` |   
  
### listEndpointPolicies(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListEndpointPoliciesPagedResponse listEndpointPolicies(@Nullable LocationName parent)

Lists EndpointPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (EndpointPolicy element :
           networkServicesClient.listEndpointPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the EndpointPolicies should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListEndpointPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListEndpointPoliciesPagedResponse)` |   
  
### listEndpointPolicies(ListEndpointPoliciesRequest request)
    
    
    public final NetworkServicesClient.ListEndpointPoliciesPagedResponse listEndpointPolicies(ListEndpointPoliciesRequest request)

Lists EndpointPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListEndpointPoliciesRequest request =
           ListEndpointPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       for (EndpointPolicy element :
           networkServicesClient.listEndpointPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEndpointPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListEndpointPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListEndpointPoliciesPagedResponse)` |   
  
### listEndpointPolicies(String parent)
    
    
    public final NetworkServicesClient.ListEndpointPoliciesPagedResponse listEndpointPolicies(String parent)

Lists EndpointPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (EndpointPolicy element :
           networkServicesClient.listEndpointPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the EndpointPolicies should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListEndpointPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListEndpointPoliciesPagedResponse)` |   
  
### listEndpointPoliciesCallable()
    
    
    public final UnaryCallable<ListEndpointPoliciesRequest,ListEndpointPoliciesResponse> listEndpointPoliciesCallable()

Lists EndpointPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListEndpointPoliciesRequest request =
           ListEndpointPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListEndpointPoliciesResponse response =
             networkServicesClient.listEndpointPoliciesCallable().call(request);
         for (EndpointPolicy element : response.getEndpointPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEndpointPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesRequest),[ListEndpointPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesResponse)>` |   
  
### listEndpointPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListEndpointPoliciesRequest,NetworkServicesClient.ListEndpointPoliciesPagedResponse> listEndpointPoliciesPagedCallable()

Lists EndpointPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListEndpointPoliciesRequest request =
           ListEndpointPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<EndpointPolicy> future =
           networkServicesClient.listEndpointPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (EndpointPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEndpointPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesRequest),[ListEndpointPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListEndpointPoliciesPagedResponse)>` |   
  
### listGatewayRouteViews(@Nullable GatewayName parent)
    
    
    public final NetworkServicesClient.ListGatewayRouteViewsPagedResponse listGatewayRouteViews(@Nullable GatewayName parent)

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GatewayName parent = GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]");
       for (GatewayRouteView element :
           networkServicesClient.listGatewayRouteViews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.GatewayName`  
Required. The Gateway to which a Route is associated. Formats: projects/{project}/locations/{location}/gateways/{gateway}  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGatewayRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewayRouteViewsPagedResponse)` |   
  
### listGatewayRouteViews(ListGatewayRouteViewsRequest request)
    
    
    public final NetworkServicesClient.ListGatewayRouteViewsPagedResponse listGatewayRouteViews(ListGatewayRouteViewsRequest request)

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGatewayRouteViewsRequest request =
           ListGatewayRouteViewsRequest.newBuilder()
               .setParent(GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (GatewayRouteView element :
           networkServicesClient.listGatewayRouteViews(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGatewayRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewayRouteViewsPagedResponse)` |   
  
### listGatewayRouteViews(String parent)
    
    
    public final NetworkServicesClient.ListGatewayRouteViewsPagedResponse listGatewayRouteViews(String parent)

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString();
       for (GatewayRouteView element :
           networkServicesClient.listGatewayRouteViews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Gateway to which a Route is associated. Formats: projects/{project}/locations/{location}/gateways/{gateway}  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGatewayRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewayRouteViewsPagedResponse)` |   
  
### listGatewayRouteViewsCallable()
    
    
    public final UnaryCallable<ListGatewayRouteViewsRequest,ListGatewayRouteViewsResponse> listGatewayRouteViewsCallable()

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGatewayRouteViewsRequest request =
           ListGatewayRouteViewsRequest.newBuilder()
               .setParent(GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListGatewayRouteViewsResponse response =
             networkServicesClient.listGatewayRouteViewsCallable().call(request);
         for (GatewayRouteView element : response.getGatewayRouteViewsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest),[ListGatewayRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsResponse)>` |   
  
### listGatewayRouteViewsPagedCallable()
    
    
    public final UnaryCallable<ListGatewayRouteViewsRequest,NetworkServicesClient.ListGatewayRouteViewsPagedResponse> listGatewayRouteViewsPagedCallable()

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGatewayRouteViewsRequest request =
           ListGatewayRouteViewsRequest.newBuilder()
               .setParent(GatewayName.of("[PROJECT]", "[LOCATION]", "[GATEWAY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<GatewayRouteView> future =
           networkServicesClient.listGatewayRouteViewsPagedCallable().futureCall(request);
       // Do something.
       for (GatewayRouteView element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest),[ListGatewayRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewayRouteViewsPagedResponse)>` |   
  
### listGateways(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListGatewaysPagedResponse listGateways(@Nullable LocationName parent)

Lists Gateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Gateway element : networkServicesClient.listGateways(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the Gateways should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewaysPagedResponse)` |   
  
### listGateways(ListGatewaysRequest request)
    
    
    public final NetworkServicesClient.ListGatewaysPagedResponse listGateways(ListGatewaysRequest request)

Lists Gateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGatewaysRequest request =
           ListGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Gateway element : networkServicesClient.listGateways(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewaysPagedResponse)` |   
  
### listGateways(String parent)
    
    
    public final NetworkServicesClient.ListGatewaysPagedResponse listGateways(String parent)

Lists Gateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Gateway element : networkServicesClient.listGateways(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the Gateways should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewaysPagedResponse)` |   
  
### listGatewaysCallable()
    
    
    public final UnaryCallable<ListGatewaysRequest,ListGatewaysResponse> listGatewaysCallable()

Lists Gateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGatewaysRequest request =
           ListGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListGatewaysResponse response = networkServicesClient.listGatewaysCallable().call(request);
         for (Gateway element : response.getGatewaysList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysRequest),[ListGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysResponse)>` |   
  
### listGatewaysPagedCallable()
    
    
    public final UnaryCallable<ListGatewaysRequest,NetworkServicesClient.ListGatewaysPagedResponse> listGatewaysPagedCallable()

Lists Gateways in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGatewaysRequest request =
           ListGatewaysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Gateway> future =
           networkServicesClient.listGatewaysPagedCallable().futureCall(request);
       // Do something.
       for (Gateway element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysRequest),[ListGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewaysPagedResponse)>` |   
  
### listGrpcRoutes(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListGrpcRoutesPagedResponse listGrpcRoutes(@Nullable LocationName parent)

Lists GrpcRoutes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GrpcRoute element : networkServicesClient.listGrpcRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the GrpcRoutes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGrpcRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGrpcRoutesPagedResponse)` |   
  
### listGrpcRoutes(ListGrpcRoutesRequest request)
    
    
    public final NetworkServicesClient.ListGrpcRoutesPagedResponse listGrpcRoutes(ListGrpcRoutesRequest request)

Lists GrpcRoutes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGrpcRoutesRequest request =
           ListGrpcRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       for (GrpcRoute element : networkServicesClient.listGrpcRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGrpcRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGrpcRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGrpcRoutesPagedResponse)` |   
  
### listGrpcRoutes(String parent)
    
    
    public final NetworkServicesClient.ListGrpcRoutesPagedResponse listGrpcRoutes(String parent)

Lists GrpcRoutes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GrpcRoute element : networkServicesClient.listGrpcRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the GrpcRoutes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListGrpcRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGrpcRoutesPagedResponse)` |   
  
### listGrpcRoutesCallable()
    
    
    public final UnaryCallable<ListGrpcRoutesRequest,ListGrpcRoutesResponse> listGrpcRoutesCallable()

Lists GrpcRoutes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGrpcRoutesRequest request =
           ListGrpcRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListGrpcRoutesResponse response =
             networkServicesClient.listGrpcRoutesCallable().call(request);
         for (GrpcRoute element : response.getGrpcRoutesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGrpcRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesRequest),[ListGrpcRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesResponse)>` |   
  
### listGrpcRoutesPagedCallable()
    
    
    public final UnaryCallable<ListGrpcRoutesRequest,NetworkServicesClient.ListGrpcRoutesPagedResponse> listGrpcRoutesPagedCallable()

Lists GrpcRoutes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListGrpcRoutesRequest request =
           ListGrpcRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<GrpcRoute> future =
           networkServicesClient.listGrpcRoutesPagedCallable().futureCall(request);
       // Do something.
       for (GrpcRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGrpcRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesRequest),[ListGrpcRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGrpcRoutesPagedResponse)>` |   
  
### listHttpRoutes(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListHttpRoutesPagedResponse listHttpRoutes(@Nullable LocationName parent)

Lists HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (HttpRoute element : networkServicesClient.listHttpRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the HttpRoutes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListHttpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListHttpRoutesPagedResponse)` |   
  
### listHttpRoutes(ListHttpRoutesRequest request)
    
    
    public final NetworkServicesClient.ListHttpRoutesPagedResponse listHttpRoutes(ListHttpRoutesRequest request)

Lists HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListHttpRoutesRequest request =
           ListHttpRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .setFilter("filter-1274492040")
               .build();
       for (HttpRoute element : networkServicesClient.listHttpRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHttpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListHttpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListHttpRoutesPagedResponse)` |   
  
### listHttpRoutes(String parent)
    
    
    public final NetworkServicesClient.ListHttpRoutesPagedResponse listHttpRoutes(String parent)

Lists HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (HttpRoute element : networkServicesClient.listHttpRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the HttpRoutes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListHttpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListHttpRoutesPagedResponse)` |   
  
### listHttpRoutesCallable()
    
    
    public final UnaryCallable<ListHttpRoutesRequest,ListHttpRoutesResponse> listHttpRoutesCallable()

Lists HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListHttpRoutesRequest request =
           ListHttpRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListHttpRoutesResponse response =
             networkServicesClient.listHttpRoutesCallable().call(request);
         for (HttpRoute element : response.getHttpRoutesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHttpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesRequest),[ListHttpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesResponse)>` |   
  
### listHttpRoutesPagedCallable()
    
    
    public final UnaryCallable<ListHttpRoutesRequest,NetworkServicesClient.ListHttpRoutesPagedResponse> listHttpRoutesPagedCallable()

Lists HttpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListHttpRoutesRequest request =
           ListHttpRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<HttpRoute> future =
           networkServicesClient.listHttpRoutesPagedCallable().futureCall(request);
       // Do something.
       for (HttpRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHttpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesRequest),[ListHttpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListHttpRoutesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final NetworkServicesClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : networkServicesClient.listLocations(request).iterateAll()) {
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
`[NetworkServicesClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             networkServicesClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,NetworkServicesClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           networkServicesClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListLocationsPagedResponse)>` |   
  
### listMeshRouteViews(@Nullable MeshName parent)
    
    
    public final NetworkServicesClient.ListMeshRouteViewsPagedResponse listMeshRouteViews(@Nullable MeshName parent)

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       MeshName parent = MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]");
       for (MeshRouteView element : networkServicesClient.listMeshRouteViews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.MeshName`  
Required. The Mesh to which a Route is associated. Format: projects/{project}/locations/{location}/meshes/{mesh}  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListMeshRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshRouteViewsPagedResponse)` |   
  
### listMeshRouteViews(ListMeshRouteViewsRequest request)
    
    
    public final NetworkServicesClient.ListMeshRouteViewsPagedResponse listMeshRouteViews(ListMeshRouteViewsRequest request)

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListMeshRouteViewsRequest request =
           ListMeshRouteViewsRequest.newBuilder()
               .setParent(MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (MeshRouteView element : networkServicesClient.listMeshRouteViews(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMeshRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListMeshRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshRouteViewsPagedResponse)` |   
  
### listMeshRouteViews(String parent)
    
    
    public final NetworkServicesClient.ListMeshRouteViewsPagedResponse listMeshRouteViews(String parent)

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString();
       for (MeshRouteView element : networkServicesClient.listMeshRouteViews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Mesh to which a Route is associated. Format: projects/{project}/locations/{location}/meshes/{mesh}  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListMeshRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshRouteViewsPagedResponse)` |   
  
### listMeshRouteViewsCallable()
    
    
    public final UnaryCallable<ListMeshRouteViewsRequest,ListMeshRouteViewsResponse> listMeshRouteViewsCallable()

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListMeshRouteViewsRequest request =
           ListMeshRouteViewsRequest.newBuilder()
               .setParent(MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListMeshRouteViewsResponse response =
             networkServicesClient.listMeshRouteViewsCallable().call(request);
         for (MeshRouteView element : response.getMeshRouteViewsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMeshRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsRequest),[ListMeshRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsResponse)>` |   
  
### listMeshRouteViewsPagedCallable()
    
    
    public final UnaryCallable<ListMeshRouteViewsRequest,NetworkServicesClient.ListMeshRouteViewsPagedResponse> listMeshRouteViewsPagedCallable()

Lists RouteViews

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListMeshRouteViewsRequest request =
           ListMeshRouteViewsRequest.newBuilder()
               .setParent(MeshName.of("[PROJECT]", "[LOCATION]", "[MESH]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<MeshRouteView> future =
           networkServicesClient.listMeshRouteViewsPagedCallable().futureCall(request);
       // Do something.
       for (MeshRouteView element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMeshRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsRequest),[ListMeshRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshRouteViewsPagedResponse)>` |   
  
### listMeshes(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListMeshesPagedResponse listMeshes(@Nullable LocationName parent)

Lists Meshes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Mesh element : networkServicesClient.listMeshes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the Meshes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListMeshesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshesPagedResponse)` |   
  
### listMeshes(ListMeshesRequest request)
    
    
    public final NetworkServicesClient.ListMeshesPagedResponse listMeshes(ListMeshesRequest request)

Lists Meshes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListMeshesRequest request =
           ListMeshesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       for (Mesh element : networkServicesClient.listMeshes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMeshesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListMeshesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshesPagedResponse)` |   
  
### listMeshes(String parent)
    
    
    public final NetworkServicesClient.ListMeshesPagedResponse listMeshes(String parent)

Lists Meshes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Mesh element : networkServicesClient.listMeshes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the Meshes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListMeshesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshesPagedResponse)` |   
  
### listMeshesCallable()
    
    
    public final UnaryCallable<ListMeshesRequest,ListMeshesResponse> listMeshesCallable()

Lists Meshes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListMeshesRequest request =
           ListMeshesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListMeshesResponse response = networkServicesClient.listMeshesCallable().call(request);
         for (Mesh element : response.getMeshesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMeshesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesRequest),[ListMeshesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesResponse)>` |   
  
### listMeshesPagedCallable()
    
    
    public final UnaryCallable<ListMeshesRequest,NetworkServicesClient.ListMeshesPagedResponse> listMeshesPagedCallable()

Lists Meshes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListMeshesRequest request =
           ListMeshesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<Mesh> future = networkServicesClient.listMeshesPagedCallable().futureCall(request);
       // Do something.
       for (Mesh element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMeshesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesRequest),[ListMeshesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshesPagedResponse)>` |   
  
### listServiceBindings(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListServiceBindingsPagedResponse listServiceBindings(@Nullable LocationName parent)

Lists ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ServiceBinding element :
           networkServicesClient.listServiceBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the ServiceBindings should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListServiceBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceBindingsPagedResponse)` |   
  
### listServiceBindings(ListServiceBindingsRequest request)
    
    
    public final NetworkServicesClient.ListServiceBindingsPagedResponse listServiceBindings(ListServiceBindingsRequest request)

Lists ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListServiceBindingsRequest request =
           ListServiceBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ServiceBinding element :
           networkServicesClient.listServiceBindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListServiceBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceBindingsPagedResponse)` |   
  
### listServiceBindings(String parent)
    
    
    public final NetworkServicesClient.ListServiceBindingsPagedResponse listServiceBindings(String parent)

Lists ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ServiceBinding element :
           networkServicesClient.listServiceBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the ServiceBindings should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListServiceBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceBindingsPagedResponse)` |   
  
### listServiceBindingsCallable()
    
    
    public final UnaryCallable<ListServiceBindingsRequest,ListServiceBindingsResponse> listServiceBindingsCallable()

Lists ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListServiceBindingsRequest request =
           ListServiceBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListServiceBindingsResponse response =
             networkServicesClient.listServiceBindingsCallable().call(request);
         for (ServiceBinding element : response.getServiceBindingsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsRequest),[ListServiceBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsResponse)>` |   
  
### listServiceBindingsPagedCallable()
    
    
    public final UnaryCallable<ListServiceBindingsRequest,NetworkServicesClient.ListServiceBindingsPagedResponse> listServiceBindingsPagedCallable()

Lists ServiceBinding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListServiceBindingsRequest request =
           ListServiceBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ServiceBinding> future =
           networkServicesClient.listServiceBindingsPagedCallable().futureCall(request);
       // Do something.
       for (ServiceBinding element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsRequest),[ListServiceBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceBindingsPagedResponse)>` |   
  
### listServiceLbPolicies(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListServiceLbPoliciesPagedResponse listServiceLbPolicies(@Nullable LocationName parent)

Lists ServiceLbPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ServiceLbPolicy element :
           networkServicesClient.listServiceLbPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the ServiceLbPolicies should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListServiceLbPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceLbPoliciesPagedResponse)` |   
  
### listServiceLbPolicies(ListServiceLbPoliciesRequest request)
    
    
    public final NetworkServicesClient.ListServiceLbPoliciesPagedResponse listServiceLbPolicies(ListServiceLbPoliciesRequest request)

Lists ServiceLbPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListServiceLbPoliciesRequest request =
           ListServiceLbPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ServiceLbPolicy element :
           networkServicesClient.listServiceLbPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceLbPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListServiceLbPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceLbPoliciesPagedResponse)` |   
  
### listServiceLbPolicies(String parent)
    
    
    public final NetworkServicesClient.ListServiceLbPoliciesPagedResponse listServiceLbPolicies(String parent)

Lists ServiceLbPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ServiceLbPolicy element :
           networkServicesClient.listServiceLbPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the ServiceLbPolicies should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListServiceLbPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceLbPoliciesPagedResponse)` |   
  
### listServiceLbPoliciesCallable()
    
    
    public final UnaryCallable<ListServiceLbPoliciesRequest,ListServiceLbPoliciesResponse> listServiceLbPoliciesCallable()

Lists ServiceLbPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListServiceLbPoliciesRequest request =
           ListServiceLbPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListServiceLbPoliciesResponse response =
             networkServicesClient.listServiceLbPoliciesCallable().call(request);
         for (ServiceLbPolicy element : response.getServiceLbPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceLbPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesRequest),[ListServiceLbPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesResponse)>` |   
  
### listServiceLbPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListServiceLbPoliciesRequest,NetworkServicesClient.ListServiceLbPoliciesPagedResponse> listServiceLbPoliciesPagedCallable()

Lists ServiceLbPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListServiceLbPoliciesRequest request =
           ListServiceLbPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ServiceLbPolicy> future =
           networkServicesClient.listServiceLbPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (ServiceLbPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceLbPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesRequest),[ListServiceLbPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceLbPoliciesPagedResponse)>` |   
  
### listTcpRoutes(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListTcpRoutesPagedResponse listTcpRoutes(@Nullable LocationName parent)

Lists TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (TcpRoute element : networkServicesClient.listTcpRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the TcpRoutes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListTcpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTcpRoutesPagedResponse)` |   
  
### listTcpRoutes(ListTcpRoutesRequest request)
    
    
    public final NetworkServicesClient.ListTcpRoutesPagedResponse listTcpRoutes(ListTcpRoutesRequest request)

Lists TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListTcpRoutesRequest request =
           ListTcpRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       for (TcpRoute element : networkServicesClient.listTcpRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTcpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListTcpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTcpRoutesPagedResponse)` |   
  
### listTcpRoutes(String parent)
    
    
    public final NetworkServicesClient.ListTcpRoutesPagedResponse listTcpRoutes(String parent)

Lists TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (TcpRoute element : networkServicesClient.listTcpRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the TcpRoutes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListTcpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTcpRoutesPagedResponse)` |   
  
### listTcpRoutesCallable()
    
    
    public final UnaryCallable<ListTcpRoutesRequest,ListTcpRoutesResponse> listTcpRoutesCallable()

Lists TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListTcpRoutesRequest request =
           ListTcpRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListTcpRoutesResponse response =
             networkServicesClient.listTcpRoutesCallable().call(request);
         for (TcpRoute element : response.getTcpRoutesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTcpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesRequest),[ListTcpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesResponse)>` |   
  
### listTcpRoutesPagedCallable()
    
    
    public final UnaryCallable<ListTcpRoutesRequest,NetworkServicesClient.ListTcpRoutesPagedResponse> listTcpRoutesPagedCallable()

Lists TcpRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListTcpRoutesRequest request =
           ListTcpRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<TcpRoute> future =
           networkServicesClient.listTcpRoutesPagedCallable().futureCall(request);
       // Do something.
       for (TcpRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTcpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesRequest),[ListTcpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTcpRoutesPagedResponse)>` |   
  
### listTlsRoutes(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListTlsRoutesPagedResponse listTlsRoutes(@Nullable LocationName parent)

Lists TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (TlsRoute element : networkServicesClient.listTlsRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the TlsRoutes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListTlsRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTlsRoutesPagedResponse)` |   
  
### listTlsRoutes(ListTlsRoutesRequest request)
    
    
    public final NetworkServicesClient.ListTlsRoutesPagedResponse listTlsRoutes(ListTlsRoutesRequest request)

Lists TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListTlsRoutesRequest request =
           ListTlsRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       for (TlsRoute element : networkServicesClient.listTlsRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTlsRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListTlsRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTlsRoutesPagedResponse)` |   
  
### listTlsRoutes(String parent)
    
    
    public final NetworkServicesClient.ListTlsRoutesPagedResponse listTlsRoutes(String parent)

Lists TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (TlsRoute element : networkServicesClient.listTlsRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the TlsRoutes should be listed, specified in the format `projects/*/locations/*`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListTlsRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTlsRoutesPagedResponse)` |   
  
### listTlsRoutesCallable()
    
    
    public final UnaryCallable<ListTlsRoutesRequest,ListTlsRoutesResponse> listTlsRoutesCallable()

Lists TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListTlsRoutesRequest request =
           ListTlsRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListTlsRoutesResponse response =
             networkServicesClient.listTlsRoutesCallable().call(request);
         for (TlsRoute element : response.getTlsRoutesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTlsRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesRequest),[ListTlsRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesResponse)>` |   
  
### listTlsRoutesPagedCallable()
    
    
    public final UnaryCallable<ListTlsRoutesRequest,NetworkServicesClient.ListTlsRoutesPagedResponse> listTlsRoutesPagedCallable()

Lists TlsRoute in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListTlsRoutesRequest request =
           ListTlsRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<TlsRoute> future =
           networkServicesClient.listTlsRoutesPagedCallable().futureCall(request);
       // Do something.
       for (TlsRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTlsRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesRequest),[ListTlsRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTlsRoutesPagedResponse)>` |   
  
### listWasmPluginVersions(@Nullable WasmPluginName parent)
    
    
    public final NetworkServicesClient.ListWasmPluginVersionsPagedResponse listWasmPluginVersions(@Nullable WasmPluginName parent)

Lists `WasmPluginVersion` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       WasmPluginName parent = WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]");
       for (WasmPluginVersion element :
           networkServicesClient.listWasmPluginVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.WasmPluginName`  
Required. The `WasmPlugin` resource whose `WasmPluginVersion`s are listed, specified in the following format: `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListWasmPluginVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginVersionsPagedResponse)` |   
  
### listWasmPluginVersions(ListWasmPluginVersionsRequest request)
    
    
    public final NetworkServicesClient.ListWasmPluginVersionsPagedResponse listWasmPluginVersions(ListWasmPluginVersionsRequest request)

Lists `WasmPluginVersion` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListWasmPluginVersionsRequest request =
           ListWasmPluginVersionsRequest.newBuilder()
               .setParent(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (WasmPluginVersion element :
           networkServicesClient.listWasmPluginVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWasmPluginVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListWasmPluginVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginVersionsPagedResponse)` |   
  
### listWasmPluginVersions(String parent)
    
    
    public final NetworkServicesClient.ListWasmPluginVersionsPagedResponse listWasmPluginVersions(String parent)

Lists `WasmPluginVersion` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString();
       for (WasmPluginVersion element :
           networkServicesClient.listWasmPluginVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The `WasmPlugin` resource whose `WasmPluginVersion`s are listed, specified in the following format: `projects/{project}/locations/global/wasmPlugins/{wasm_plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListWasmPluginVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginVersionsPagedResponse)` |   
  
### listWasmPluginVersionsCallable()
    
    
    public final UnaryCallable<ListWasmPluginVersionsRequest,ListWasmPluginVersionsResponse> listWasmPluginVersionsCallable()

Lists `WasmPluginVersion` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListWasmPluginVersionsRequest request =
           ListWasmPluginVersionsRequest.newBuilder()
               .setParent(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListWasmPluginVersionsResponse response =
             networkServicesClient.listWasmPluginVersionsCallable().call(request);
         for (WasmPluginVersion element : response.getWasmPluginVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWasmPluginVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsRequest),[ListWasmPluginVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsResponse)>` |   
  
### listWasmPluginVersionsPagedCallable()
    
    
    public final UnaryCallable<ListWasmPluginVersionsRequest,NetworkServicesClient.ListWasmPluginVersionsPagedResponse> listWasmPluginVersionsPagedCallable()

Lists `WasmPluginVersion` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListWasmPluginVersionsRequest request =
           ListWasmPluginVersionsRequest.newBuilder()
               .setParent(WasmPluginName.of("[PROJECT]", "[LOCATION]", "[WASM_PLUGIN]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<WasmPluginVersion> future =
           networkServicesClient.listWasmPluginVersionsPagedCallable().futureCall(request);
       // Do something.
       for (WasmPluginVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWasmPluginVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsRequest),[ListWasmPluginVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginVersionsPagedResponse)>` |   
  
### listWasmPlugins(@Nullable LocationName parent)
    
    
    public final NetworkServicesClient.ListWasmPluginsPagedResponse listWasmPlugins(@Nullable LocationName parent)

Lists `WasmPlugin` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (WasmPlugin element : networkServicesClient.listWasmPlugins(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the `WasmPlugin` resources are listed, specified in the following format: `projects/{project}/locations/global`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListWasmPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginsPagedResponse)` |   
  
### listWasmPlugins(ListWasmPluginsRequest request)
    
    
    public final NetworkServicesClient.ListWasmPluginsPagedResponse listWasmPlugins(ListWasmPluginsRequest request)

Lists `WasmPlugin` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListWasmPluginsRequest request =
           ListWasmPluginsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (WasmPlugin element : networkServicesClient.listWasmPlugins(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWasmPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListWasmPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginsPagedResponse)` |   
  
### listWasmPlugins(String parent)
    
    
    public final NetworkServicesClient.ListWasmPluginsPagedResponse listWasmPlugins(String parent)

Lists `WasmPlugin` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (WasmPlugin element : networkServicesClient.listWasmPlugins(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the `WasmPlugin` resources are listed, specified in the following format: `projects/{project}/locations/global`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesClient.ListWasmPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginsPagedResponse)` |   
  
### listWasmPluginsCallable()
    
    
    public final UnaryCallable<ListWasmPluginsRequest,ListWasmPluginsResponse> listWasmPluginsCallable()

Lists `WasmPlugin` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListWasmPluginsRequest request =
           ListWasmPluginsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListWasmPluginsResponse response =
             networkServicesClient.listWasmPluginsCallable().call(request);
         for (WasmPlugin element : response.getWasmPluginsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWasmPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsRequest),[ListWasmPluginsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsResponse)>` |   
  
### listWasmPluginsPagedCallable()
    
    
    public final UnaryCallable<ListWasmPluginsRequest,NetworkServicesClient.ListWasmPluginsPagedResponse> listWasmPluginsPagedCallable()

Lists `WasmPlugin` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ListWasmPluginsRequest request =
           ListWasmPluginsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<WasmPlugin> future =
           networkServicesClient.listWasmPluginsPagedCallable().futureCall(request);
       // Do something.
       for (WasmPlugin element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWasmPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsRequest),[ListWasmPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginsPagedResponse)>` |   
  
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
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = networkServicesClient.setIamPolicy(request);
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
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = networkServicesClient.setIamPolicyCallable().futureCall(request);
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
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = networkServicesClient.testIamPermissions(request);
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
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           networkServicesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateAgentGatewayAsync(AgentGateway agentGateway, FieldMask updateMask)
    
    
    public final OperationFuture<AgentGateway,OperationMetadata> updateAgentGatewayAsync(AgentGateway agentGateway, FieldMask updateMask)

Updates the parameters of a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       AgentGateway agentGateway = AgentGateway.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AgentGateway response =
           networkServicesClient.updateAgentGatewayAsync(agentGateway, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`agentGateway` | `[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)`  
Required. Updated AgentGateway resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the AgentGateway resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateAgentGatewayAsync(UpdateAgentGatewayRequest request)
    
    
    public final OperationFuture<AgentGateway,OperationMetadata> updateAgentGatewayAsync(UpdateAgentGatewayRequest request)

Updates the parameters of a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateAgentGatewayRequest request =
           UpdateAgentGatewayRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAgentGateway(AgentGateway.newBuilder().build())
               .build();
       AgentGateway response = networkServicesClient.updateAgentGatewayAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAgentGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateAgentGatewayCallable()
    
    
    public final UnaryCallable<UpdateAgentGatewayRequest,Operation> updateAgentGatewayCallable()

Updates the parameters of a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateAgentGatewayRequest request =
           UpdateAgentGatewayRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAgentGateway(AgentGateway.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateAgentGatewayCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAgentGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAgentGatewayOperationCallable()
    
    
    public final OperationCallable<UpdateAgentGatewayRequest,AgentGateway,OperationMetadata> updateAgentGatewayOperationCallable()

Updates the parameters of a single AgentGateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateAgentGatewayRequest request =
           UpdateAgentGatewayRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAgentGateway(AgentGateway.newBuilder().build())
               .build();
       OperationFuture<AgentGateway, OperationMetadata> future =
           networkServicesClient.updateAgentGatewayOperationCallable().futureCall(request);
       // Do something.
       AgentGateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAgentGatewayRequest),[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateEndpointPolicyAsync(EndpointPolicy endpointPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<EndpointPolicy,OperationMetadata> updateEndpointPolicyAsync(EndpointPolicy endpointPolicy, FieldMask updateMask)

Updates the parameters of a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       EndpointPolicy endpointPolicy = EndpointPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       EndpointPolicy response =
           networkServicesClient.updateEndpointPolicyAsync(endpointPolicy, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpointPolicy` | `[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)`  
Required. Updated EndpointPolicy resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the EndpointPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateEndpointPolicyAsync(UpdateEndpointPolicyRequest request)
    
    
    public final OperationFuture<EndpointPolicy,OperationMetadata> updateEndpointPolicyAsync(UpdateEndpointPolicyRequest request)

Updates the parameters of a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateEndpointPolicyRequest request =
           UpdateEndpointPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setEndpointPolicy(EndpointPolicy.newBuilder().build())
               .build();
       EndpointPolicy response = networkServicesClient.updateEndpointPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateEndpointPolicyCallable()
    
    
    public final UnaryCallable<UpdateEndpointPolicyRequest,Operation> updateEndpointPolicyCallable()

Updates the parameters of a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateEndpointPolicyRequest request =
           UpdateEndpointPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setEndpointPolicy(EndpointPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateEndpointPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEndpointPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateEndpointPolicyRequest,EndpointPolicy,OperationMetadata> updateEndpointPolicyOperationCallable()

Updates the parameters of a single EndpointPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateEndpointPolicyRequest request =
           UpdateEndpointPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setEndpointPolicy(EndpointPolicy.newBuilder().build())
               .build();
       OperationFuture<EndpointPolicy, OperationMetadata> future =
           networkServicesClient.updateEndpointPolicyOperationCallable().futureCall(request);
       // Do something.
       EndpointPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest),[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateGatewayAsync(Gateway gateway, FieldMask updateMask)
    
    
    public final OperationFuture<Gateway,OperationMetadata> updateGatewayAsync(Gateway gateway, FieldMask updateMask)

Updates the parameters of a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       Gateway gateway = Gateway.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Gateway response = networkServicesClient.updateGatewayAsync(gateway, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`gateway` | `[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)`  
Required. Updated Gateway resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Gateway resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateGatewayAsync(UpdateGatewayRequest request)
    
    
    public final OperationFuture<Gateway,OperationMetadata> updateGatewayAsync(UpdateGatewayRequest request)

Updates the parameters of a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateGatewayRequest request =
           UpdateGatewayRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGateway(Gateway.newBuilder().build())
               .build();
       Gateway response = networkServicesClient.updateGatewayAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateGatewayCallable()
    
    
    public final UnaryCallable<UpdateGatewayRequest,Operation> updateGatewayCallable()

Updates the parameters of a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateGatewayRequest request =
           UpdateGatewayRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGateway(Gateway.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateGatewayCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGatewayOperationCallable()
    
    
    public final OperationCallable<UpdateGatewayRequest,Gateway,OperationMetadata> updateGatewayOperationCallable()

Updates the parameters of a single Gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateGatewayRequest request =
           UpdateGatewayRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGateway(Gateway.newBuilder().build())
               .build();
       OperationFuture<Gateway, OperationMetadata> future =
           networkServicesClient.updateGatewayOperationCallable().futureCall(request);
       // Do something.
       Gateway response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGatewayRequest),[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateGrpcRouteAsync(GrpcRoute grpcRoute, FieldMask updateMask)
    
    
    public final OperationFuture<GrpcRoute,OperationMetadata> updateGrpcRouteAsync(GrpcRoute grpcRoute, FieldMask updateMask)

Updates the parameters of a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       GrpcRoute grpcRoute = GrpcRoute.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GrpcRoute response = networkServicesClient.updateGrpcRouteAsync(grpcRoute, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`grpcRoute` | `[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)`  
Required. Updated GrpcRoute resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the GrpcRoute resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateGrpcRouteAsync(UpdateGrpcRouteRequest request)
    
    
    public final OperationFuture<GrpcRoute,OperationMetadata> updateGrpcRouteAsync(UpdateGrpcRouteRequest request)

Updates the parameters of a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateGrpcRouteRequest request =
           UpdateGrpcRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGrpcRoute(GrpcRoute.newBuilder().build())
               .build();
       GrpcRoute response = networkServicesClient.updateGrpcRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGrpcRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateGrpcRouteCallable()
    
    
    public final UnaryCallable<UpdateGrpcRouteRequest,Operation> updateGrpcRouteCallable()

Updates the parameters of a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateGrpcRouteRequest request =
           UpdateGrpcRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGrpcRoute(GrpcRoute.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateGrpcRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGrpcRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGrpcRouteOperationCallable()
    
    
    public final OperationCallable<UpdateGrpcRouteRequest,GrpcRoute,OperationMetadata> updateGrpcRouteOperationCallable()

Updates the parameters of a single GrpcRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateGrpcRouteRequest request =
           UpdateGrpcRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGrpcRoute(GrpcRoute.newBuilder().build())
               .build();
       OperationFuture<GrpcRoute, OperationMetadata> future =
           networkServicesClient.updateGrpcRouteOperationCallable().futureCall(request);
       // Do something.
       GrpcRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGrpcRouteRequest),[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateHttpRouteAsync(HttpRoute httpRoute, FieldMask updateMask)
    
    
    public final OperationFuture<HttpRoute,OperationMetadata> updateHttpRouteAsync(HttpRoute httpRoute, FieldMask updateMask)

Updates the parameters of a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       HttpRoute httpRoute = HttpRoute.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       HttpRoute response = networkServicesClient.updateHttpRouteAsync(httpRoute, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`httpRoute` | `[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)`  
Required. Updated HttpRoute resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the HttpRoute resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateHttpRouteAsync(UpdateHttpRouteRequest request)
    
    
    public final OperationFuture<HttpRoute,OperationMetadata> updateHttpRouteAsync(UpdateHttpRouteRequest request)

Updates the parameters of a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateHttpRouteRequest request =
           UpdateHttpRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHttpRoute(HttpRoute.newBuilder().build())
               .build();
       HttpRoute response = networkServicesClient.updateHttpRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateHttpRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateHttpRouteCallable()
    
    
    public final UnaryCallable<UpdateHttpRouteRequest,Operation> updateHttpRouteCallable()

Updates the parameters of a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateHttpRouteRequest request =
           UpdateHttpRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHttpRoute(HttpRoute.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateHttpRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateHttpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHttpRouteOperationCallable()
    
    
    public final OperationCallable<UpdateHttpRouteRequest,HttpRoute,OperationMetadata> updateHttpRouteOperationCallable()

Updates the parameters of a single HttpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateHttpRouteRequest request =
           UpdateHttpRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHttpRoute(HttpRoute.newBuilder().build())
               .build();
       OperationFuture<HttpRoute, OperationMetadata> future =
           networkServicesClient.updateHttpRouteOperationCallable().futureCall(request);
       // Do something.
       HttpRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateHttpRouteRequest),[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateMeshAsync(Mesh mesh, FieldMask updateMask)
    
    
    public final OperationFuture<Mesh,OperationMetadata> updateMeshAsync(Mesh mesh, FieldMask updateMask)

Updates the parameters of a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       Mesh mesh = Mesh.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Mesh response = networkServicesClient.updateMeshAsync(mesh, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`mesh` | `[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)`  
Required. Updated Mesh resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Mesh resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateMeshAsync(UpdateMeshRequest request)
    
    
    public final OperationFuture<Mesh,OperationMetadata> updateMeshAsync(UpdateMeshRequest request)

Updates the parameters of a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateMeshRequest request =
           UpdateMeshRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMesh(Mesh.newBuilder().build())
               .build();
       Mesh response = networkServicesClient.updateMeshAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateMeshRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateMeshCallable()
    
    
    public final UnaryCallable<UpdateMeshRequest,Operation> updateMeshCallable()

Updates the parameters of a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateMeshRequest request =
           UpdateMeshRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMesh(Mesh.newBuilder().build())
               .build();
       ApiFuture<Operation> future = networkServicesClient.updateMeshCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateMeshRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMeshOperationCallable()
    
    
    public final OperationCallable<UpdateMeshRequest,Mesh,OperationMetadata> updateMeshOperationCallable()

Updates the parameters of a single Mesh.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateMeshRequest request =
           UpdateMeshRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setMesh(Mesh.newBuilder().build())
               .build();
       OperationFuture<Mesh, OperationMetadata> future =
           networkServicesClient.updateMeshOperationCallable().futureCall(request);
       // Do something.
       Mesh response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateMeshRequest),[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateServiceBindingAsync(ServiceBinding serviceBinding, FieldMask updateMask)
    
    
    public final OperationFuture<ServiceBinding,OperationMetadata> updateServiceBindingAsync(ServiceBinding serviceBinding, FieldMask updateMask)

Updates the parameters of a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ServiceBinding serviceBinding = ServiceBinding.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ServiceBinding response =
           networkServicesClient.updateServiceBindingAsync(serviceBinding, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`serviceBinding` | `[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)`  
Required. Updated ServiceBinding resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ServiceBinding resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateServiceBindingAsync(UpdateServiceBindingRequest request)
    
    
    public final OperationFuture<ServiceBinding,OperationMetadata> updateServiceBindingAsync(UpdateServiceBindingRequest request)

Updates the parameters of a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateServiceBindingRequest request =
           UpdateServiceBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceBinding(ServiceBinding.newBuilder().build())
               .build();
       ServiceBinding response = networkServicesClient.updateServiceBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateServiceBindingCallable()
    
    
    public final UnaryCallable<UpdateServiceBindingRequest,Operation> updateServiceBindingCallable()

Updates the parameters of a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateServiceBindingRequest request =
           UpdateServiceBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceBinding(ServiceBinding.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateServiceBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceBindingOperationCallable()
    
    
    public final OperationCallable<UpdateServiceBindingRequest,ServiceBinding,OperationMetadata> updateServiceBindingOperationCallable()

Updates the parameters of a single ServiceBinding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateServiceBindingRequest request =
           UpdateServiceBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceBinding(ServiceBinding.newBuilder().build())
               .build();
       OperationFuture<ServiceBinding, OperationMetadata> future =
           networkServicesClient.updateServiceBindingOperationCallable().futureCall(request);
       // Do something.
       ServiceBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceBindingRequest),[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateServiceLbPolicyAsync(ServiceLbPolicy serviceLbPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<ServiceLbPolicy,OperationMetadata> updateServiceLbPolicyAsync(ServiceLbPolicy serviceLbPolicy, FieldMask updateMask)

Updates the parameters of a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       ServiceLbPolicy serviceLbPolicy = ServiceLbPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ServiceLbPolicy response =
           networkServicesClient.updateServiceLbPolicyAsync(serviceLbPolicy, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`serviceLbPolicy` | `[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)`  
Required. Updated ServiceLbPolicy resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ServiceLbPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateServiceLbPolicyAsync(UpdateServiceLbPolicyRequest request)
    
    
    public final OperationFuture<ServiceLbPolicy,OperationMetadata> updateServiceLbPolicyAsync(UpdateServiceLbPolicyRequest request)

Updates the parameters of a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateServiceLbPolicyRequest request =
           UpdateServiceLbPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceLbPolicy(ServiceLbPolicy.newBuilder().build())
               .build();
       ServiceLbPolicy response = networkServicesClient.updateServiceLbPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceLbPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateServiceLbPolicyCallable()
    
    
    public final UnaryCallable<UpdateServiceLbPolicyRequest,Operation> updateServiceLbPolicyCallable()

Updates the parameters of a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateServiceLbPolicyRequest request =
           UpdateServiceLbPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceLbPolicy(ServiceLbPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateServiceLbPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceLbPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceLbPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateServiceLbPolicyRequest,ServiceLbPolicy,OperationMetadata> updateServiceLbPolicyOperationCallable()

Updates the parameters of a single ServiceLbPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateServiceLbPolicyRequest request =
           UpdateServiceLbPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceLbPolicy(ServiceLbPolicy.newBuilder().build())
               .build();
       OperationFuture<ServiceLbPolicy, OperationMetadata> future =
           networkServicesClient.updateServiceLbPolicyOperationCallable().futureCall(request);
       // Do something.
       ServiceLbPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceLbPolicyRequest),[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateTcpRouteAsync(TcpRoute tcpRoute, FieldMask updateMask)
    
    
    public final OperationFuture<TcpRoute,OperationMetadata> updateTcpRouteAsync(TcpRoute tcpRoute, FieldMask updateMask)

Updates the parameters of a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       TcpRoute tcpRoute = TcpRoute.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TcpRoute response = networkServicesClient.updateTcpRouteAsync(tcpRoute, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tcpRoute` | `[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)`  
Required. Updated TcpRoute resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the TcpRoute resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateTcpRouteAsync(UpdateTcpRouteRequest request)
    
    
    public final OperationFuture<TcpRoute,OperationMetadata> updateTcpRouteAsync(UpdateTcpRouteRequest request)

Updates the parameters of a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateTcpRouteRequest request =
           UpdateTcpRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTcpRoute(TcpRoute.newBuilder().build())
               .build();
       TcpRoute response = networkServicesClient.updateTcpRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTcpRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateTcpRouteCallable()
    
    
    public final UnaryCallable<UpdateTcpRouteRequest,Operation> updateTcpRouteCallable()

Updates the parameters of a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateTcpRouteRequest request =
           UpdateTcpRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTcpRoute(TcpRoute.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateTcpRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTcpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTcpRouteOperationCallable()
    
    
    public final OperationCallable<UpdateTcpRouteRequest,TcpRoute,OperationMetadata> updateTcpRouteOperationCallable()

Updates the parameters of a single TcpRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateTcpRouteRequest request =
           UpdateTcpRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTcpRoute(TcpRoute.newBuilder().build())
               .build();
       OperationFuture<TcpRoute, OperationMetadata> future =
           networkServicesClient.updateTcpRouteOperationCallable().futureCall(request);
       // Do something.
       TcpRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTcpRouteRequest),[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateTlsRouteAsync(TlsRoute tlsRoute, FieldMask updateMask)
    
    
    public final OperationFuture<TlsRoute,OperationMetadata> updateTlsRouteAsync(TlsRoute tlsRoute, FieldMask updateMask)

Updates the parameters of a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       TlsRoute tlsRoute = TlsRoute.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TlsRoute response = networkServicesClient.updateTlsRouteAsync(tlsRoute, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tlsRoute` | `[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)`  
Required. Updated TlsRoute resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the TlsRoute resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateTlsRouteAsync(UpdateTlsRouteRequest request)
    
    
    public final OperationFuture<TlsRoute,OperationMetadata> updateTlsRouteAsync(UpdateTlsRouteRequest request)

Updates the parameters of a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateTlsRouteRequest request =
           UpdateTlsRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTlsRoute(TlsRoute.newBuilder().build())
               .build();
       TlsRoute response = networkServicesClient.updateTlsRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTlsRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateTlsRouteCallable()
    
    
    public final UnaryCallable<UpdateTlsRouteRequest,Operation> updateTlsRouteCallable()

Updates the parameters of a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateTlsRouteRequest request =
           UpdateTlsRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTlsRoute(TlsRoute.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateTlsRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTlsRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTlsRouteOperationCallable()
    
    
    public final OperationCallable<UpdateTlsRouteRequest,TlsRoute,OperationMetadata> updateTlsRouteOperationCallable()

Updates the parameters of a single TlsRoute.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateTlsRouteRequest request =
           UpdateTlsRouteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTlsRoute(TlsRoute.newBuilder().build())
               .build();
       OperationFuture<TlsRoute, OperationMetadata> future =
           networkServicesClient.updateTlsRouteOperationCallable().futureCall(request);
       // Do something.
       TlsRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTlsRouteRequest),[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateWasmPluginAsync(UpdateWasmPluginRequest request)
    
    
    public final OperationFuture<WasmPlugin,OperationMetadata> updateWasmPluginAsync(UpdateWasmPluginRequest request)

Updates the parameters of the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateWasmPluginRequest request =
           UpdateWasmPluginRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setWasmPlugin(WasmPlugin.newBuilder().build())
               .build();
       WasmPlugin response = networkServicesClient.updateWasmPluginAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateWasmPluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateWasmPluginAsync(WasmPlugin wasmPlugin, FieldMask updateMask)
    
    
    public final OperationFuture<WasmPlugin,OperationMetadata> updateWasmPluginAsync(WasmPlugin wasmPlugin, FieldMask updateMask)

Updates the parameters of the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       WasmPlugin wasmPlugin = WasmPlugin.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       WasmPlugin response =
           networkServicesClient.updateWasmPluginAsync(wasmPlugin, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`wasmPlugin` | `[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)`  
Required. Updated `WasmPlugin` resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Used to specify the fields to be overwritten in the `WasmPlugin` resource by the update. The fields specified in the `update_mask` field are relative to the resource, not the full request. An omitted `update_mask` field is treated as an implied `update_mask` field equivalent to all fields that are populated (that have a non-empty value). The `update_mask` field supports a special value `*`, which means that each field in the given `WasmPlugin` resource (including the empty ones) replaces the current value.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateWasmPluginCallable()
    
    
    public final UnaryCallable<UpdateWasmPluginRequest,Operation> updateWasmPluginCallable()

Updates the parameters of the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateWasmPluginRequest request =
           UpdateWasmPluginRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setWasmPlugin(WasmPlugin.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkServicesClient.updateWasmPluginCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateWasmPluginRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateWasmPluginOperationCallable()
    
    
    public final OperationCallable<UpdateWasmPluginRequest,WasmPlugin,OperationMetadata> updateWasmPluginOperationCallable()

Updates the parameters of the specified `WasmPlugin` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkServicesClient networkServicesClient = NetworkServicesClient.create()) {
       UpdateWasmPluginRequest request =
           UpdateWasmPluginRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setWasmPlugin(WasmPlugin.newBuilder().build())
               .build();
       OperationFuture<WasmPlugin, OperationMetadata> future =
           networkServicesClient.updateWasmPluginOperationCallable().futureCall(request);
       // Do something.
       WasmPlugin response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateWasmPluginRequest),[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
