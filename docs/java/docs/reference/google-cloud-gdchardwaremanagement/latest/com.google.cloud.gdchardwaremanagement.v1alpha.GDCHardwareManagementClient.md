---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient
title: Class GDCHardwareManagementClient (0.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:01.174588+00:00
---

# Class GDCHardwareManagementClient (0.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GDCHardwareManagementClient (0.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.54.0 (latest)  0.50.0  0.49.0  0.48.0  0.46.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.19.0  0.18.0  0.17.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-gdchardwaremanagement/google-cloud-gdchardwaremanagement/src/main/java/com/google/cloud/gdchardwaremanagement/v1alpha/GDCHardwareManagementClient.java)| [Product Reference](https://cloud.google.com/distributed-cloud/edge/latest/docs)| [RPC Documentation](https://cloud.google.com/distributed-cloud/edge/latest/docs/reference/hardware/rpc)  
---|---|---  
  
Service Description: The GDC Hardware Management service.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       Order response = gDCHardwareManagementClient.getOrder(name);
     }
     

Note: close() needs to be called on the GDCHardwareManagementClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListOrders |  Lists orders in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOrders(ListOrdersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOrders(LocationName parent) 
  * listOrders(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOrdersPagedCallable() 
  * listOrdersCallable() 

  
GetOrder |  Gets details of an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOrder(GetOrderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOrder(OrderName name) 
  * getOrder(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOrderCallable() 

  
CreateOrder |  Creates a new order in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createOrderAsync(CreateOrderRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createOrderAsync(LocationName parent, Order order, String orderId) 
  * createOrderAsync(String parent, Order order, String orderId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createOrderOperationCallable() 
  * createOrderCallable() 

  
UpdateOrder |  Updates the parameters of an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateOrderAsync(UpdateOrderRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateOrderAsync(Order order, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOrderOperationCallable() 
  * updateOrderCallable() 

  
DeleteOrder |  Deletes an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteOrderAsync(DeleteOrderRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteOrderAsync(OrderName name) 
  * deleteOrderAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOrderOperationCallable() 
  * deleteOrderCallable() 

  
SubmitOrder |  Submits an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * submitOrderAsync(SubmitOrderRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * submitOrderAsync(OrderName name) 
  * submitOrderAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * submitOrderOperationCallable() 
  * submitOrderCallable() 

  
CancelOrder |  Cancels an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelOrderAsync(CancelOrderRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cancelOrderAsync(OrderName name) 
  * cancelOrderAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelOrderOperationCallable() 
  * cancelOrderCallable() 

  
ListSites |  Lists sites in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSites(ListSitesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSites(LocationName parent) 
  * listSites(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSitesPagedCallable() 
  * listSitesCallable() 

  
GetSite |  Gets details of a site. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSite(GetSiteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSite(SiteName name) 
  * getSite(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSiteCallable() 

  
CreateSite |  Creates a new site in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSiteAsync(CreateSiteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSiteAsync(LocationName parent, Site site, String siteId) 
  * createSiteAsync(String parent, Site site, String siteId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSiteOperationCallable() 
  * createSiteCallable() 

  
UpdateSite |  Updates the parameters of a site. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSiteAsync(UpdateSiteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateSiteAsync(Site site, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSiteOperationCallable() 
  * updateSiteCallable() 

  
DeleteSite |  Deletes a site. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSiteAsync(DeleteSiteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSiteAsync(SiteName name) 
  * deleteSiteAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSiteOperationCallable() 
  * deleteSiteCallable() 

  
ListHardwareGroups |  Lists hardware groups in a given order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHardwareGroups(ListHardwareGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHardwareGroups(OrderName parent) 
  * listHardwareGroups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHardwareGroupsPagedCallable() 
  * listHardwareGroupsCallable() 

  
GetHardwareGroup |  Gets details of a hardware group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHardwareGroup(GetHardwareGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHardwareGroup(HardwareGroupName name) 
  * getHardwareGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHardwareGroupCallable() 

  
CreateHardwareGroup |  Creates a new hardware group in a given order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHardwareGroupAsync(CreateHardwareGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createHardwareGroupAsync(OrderName parent, HardwareGroup hardwareGroup, String hardwareGroupId) 
  * createHardwareGroupAsync(String parent, HardwareGroup hardwareGroup, String hardwareGroupId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHardwareGroupOperationCallable() 
  * createHardwareGroupCallable() 

  
UpdateHardwareGroup |  Updates the parameters of a hardware group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateHardwareGroupAsync(UpdateHardwareGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateHardwareGroupAsync(HardwareGroup hardwareGroup, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateHardwareGroupOperationCallable() 
  * updateHardwareGroupCallable() 

  
DeleteHardwareGroup |  Deletes a hardware group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteHardwareGroupAsync(DeleteHardwareGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteHardwareGroupAsync(HardwareGroupName name) 
  * deleteHardwareGroupAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteHardwareGroupOperationCallable() 
  * deleteHardwareGroupCallable() 

  
ListHardware |  Lists hardware in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHardware(ListHardwareRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHardware(LocationName parent) 
  * listHardware(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHardwarePagedCallable() 
  * listHardwareCallable() 

  
GetHardware |  Gets hardware details. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHardware(GetHardwareRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHardware(HardwareName name) 
  * getHardware(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHardwareCallable() 

  
CreateHardware |  Creates new hardware in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHardwareAsync(CreateHardwareRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createHardwareAsync(LocationName parent, Hardware hardware, String hardwareId) 
  * createHardwareAsync(String parent, Hardware hardware, String hardwareId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHardwareOperationCallable() 
  * createHardwareCallable() 

  
UpdateHardware |  Updates hardware parameters. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateHardwareAsync(UpdateHardwareRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateHardwareAsync(Hardware hardware, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateHardwareOperationCallable() 
  * updateHardwareCallable() 

  
DeleteHardware |  Deletes hardware. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteHardwareAsync(DeleteHardwareRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteHardwareAsync(HardwareName name) 
  * deleteHardwareAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteHardwareOperationCallable() 
  * deleteHardwareCallable() 

  
ListComments |  Lists the comments on an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listComments(ListCommentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listComments(OrderName parent) 
  * listComments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCommentsPagedCallable() 
  * listCommentsCallable() 

  
GetComment |  Gets the content of a comment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getComment(GetCommentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getComment(CommentName name) 
  * getComment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCommentCallable() 

  
CreateComment |  Creates a new comment on an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCommentAsync(CreateCommentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createCommentAsync(OrderName parent, Comment comment, String commentId) 
  * createCommentAsync(String parent, Comment comment, String commentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCommentOperationCallable() 
  * createCommentCallable() 

  
RecordActionOnComment |  Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * recordActionOnComment(RecordActionOnCommentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * recordActionOnComment(CommentName name, RecordActionOnCommentRequest.ActionType actionType) 
  * recordActionOnComment(String name, RecordActionOnCommentRequest.ActionType actionType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * recordActionOnCommentCallable() 

  
ListChangeLogEntries |  Lists the changes made to an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listChangeLogEntries(ListChangeLogEntriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listChangeLogEntries(OrderName parent) 
  * listChangeLogEntries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listChangeLogEntriesPagedCallable() 
  * listChangeLogEntriesCallable() 

  
GetChangeLogEntry |  Gets details of a change to an order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getChangeLogEntry(GetChangeLogEntryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getChangeLogEntry(ChangeLogEntryName name) 
  * getChangeLogEntry(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getChangeLogEntryCallable() 

  
ListSkus |  Lists SKUs for a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSkus(ListSkusRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSkus(LocationName parent) 
  * listSkus(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSkusPagedCallable() 
  * listSkusCallable() 

  
GetSku |  Gets details of an SKU. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSku(GetSkuRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSku(SkuName name) 
  * getSku(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSkuCallable() 

  
ListZones |  Lists zones in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listZones(ListZonesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listZones(LocationName parent) 
  * listZones(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listZonesPagedCallable() 
  * listZonesCallable() 

  
GetZone |  Gets details of a zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getZone(GetZoneRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getZone(ZoneName name) 
  * getZone(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getZoneCallable() 

  
CreateZone |  Creates a new zone in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createZoneAsync(CreateZoneRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createZoneAsync(LocationName parent, Zone zone, String zoneId) 
  * createZoneAsync(String parent, Zone zone, String zoneId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createZoneOperationCallable() 
  * createZoneCallable() 

  
UpdateZone |  Updates the parameters of a zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateZoneAsync(UpdateZoneRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateZoneAsync(Zone zone, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateZoneOperationCallable() 
  * updateZoneCallable() 

  
DeleteZone |  Deletes a zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteZoneAsync(DeleteZoneRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteZoneAsync(ZoneName name) 
  * deleteZoneAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteZoneOperationCallable() 
  * deleteZoneCallable() 

  
SignalZoneState |  Signals the state of a zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * signalZoneStateAsync(SignalZoneStateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * signalZoneStateAsync(ZoneName name, SignalZoneStateRequest.StateSignal stateSignal) 
  * signalZoneStateAsync(String name, SignalZoneStateRequest.StateSignal stateSignal) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * signalZoneStateOperationCallable() 
  * signalZoneStateCallable() 

  
RequestOrderDateChange |  Updates the requested date change of a single Order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * requestOrderDateChangeAsync(OrderName name, Date requestedDate) 
  * requestOrderDateChangeAsync(String name, Date requestedDate) 
  * requestOrderDateChangeAsync(RequestOrderDateChangeRequest request) 
  * requestOrderDateChangeOperationCallable() 
  * requestOrderDateChangeCallable() 

  
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

This class can be customized by passing in a custom instance of GDCHardwareManagementSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GDCHardwareManagementSettings gDCHardwareManagementSettings =
         GDCHardwareManagementSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create(gDCHardwareManagementSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GDCHardwareManagementSettings gDCHardwareManagementSettings =
         GDCHardwareManagementSettings.newBuilder().setEndpoint(myEndpoint).build();
     GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create(gDCHardwareManagementSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GDCHardwareManagementSettings gDCHardwareManagementSettings =
         GDCHardwareManagementSettings.newHttpJsonBuilder().build();
     GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create(gDCHardwareManagementSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GDCHardwareManagementClient

## Static Methods 

### create()
    
    
    public static final GDCHardwareManagementClient create()

Constructs an instance of GDCHardwareManagementClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GDCHardwareManagementSettings settings)
    
    
    public static final GDCHardwareManagementClient create(GDCHardwareManagementSettings settings)

Constructs an instance of GDCHardwareManagementClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GDCHardwareManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GDCHardwareManagementStub stub)
    
    
    public static final GDCHardwareManagementClient create(GDCHardwareManagementStub stub)

Constructs an instance of GDCHardwareManagementClient, using the given stub for making calls. This is for advanced usage - prefer using create(GDCHardwareManagementSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GDCHardwareManagementStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.stub.GDCHardwareManagementStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient)` |   
  
## Constructors 

### GDCHardwareManagementClient(GDCHardwareManagementSettings settings)
    
    
    protected GDCHardwareManagementClient(GDCHardwareManagementSettings settings)

Constructs an instance of GDCHardwareManagementClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GDCHardwareManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings)`  
  
  
### GDCHardwareManagementClient(GDCHardwareManagementStub stub)
    
    
    protected GDCHardwareManagementClient(GDCHardwareManagementStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GDCHardwareManagementStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.stub.GDCHardwareManagementStub)`  
  
  
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
  
### cancelOrderAsync(@Nullable OrderName name)
    
    
    public final OperationFuture<Order,OperationMetadata> cancelOrderAsync(@Nullable OrderName name)

Cancels an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       Order response = gDCHardwareManagementClient.cancelOrderAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### cancelOrderAsync(CancelOrderRequest request)
    
    
    public final OperationFuture<Order,OperationMetadata> cancelOrderAsync(CancelOrderRequest request)

Cancels an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CancelOrderRequest request =
           CancelOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       Order response = gDCHardwareManagementClient.cancelOrderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CancelOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### cancelOrderAsync(String name)
    
    
    public final OperationFuture<Order,OperationMetadata> cancelOrderAsync(String name)

Cancels an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       Order response = gDCHardwareManagementClient.cancelOrderAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### cancelOrderCallable()
    
    
    public final UnaryCallable<CancelOrderRequest,Operation> cancelOrderCallable()

Cancels an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CancelOrderRequest request =
           CancelOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.cancelOrderCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CancelOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### cancelOrderOperationCallable()
    
    
    public final OperationCallable<CancelOrderRequest,Order,OperationMetadata> cancelOrderOperationCallable()

Cancels an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CancelOrderRequest request =
           CancelOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Order, OperationMetadata> future =
           gDCHardwareManagementClient.cancelOrderOperationCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CancelOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CancelOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createCommentAsync(@Nullable OrderName parent, Comment comment, String commentId)
    
    
    public final OperationFuture<Comment,OperationMetadata> createCommentAsync(@Nullable OrderName parent, Comment comment, String commentId)

Creates a new comment on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       Comment comment = Comment.newBuilder().build();
       String commentId = "commentId-1495016486";
       Comment response =
           gDCHardwareManagementClient.createCommentAsync(parent, comment, commentId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The order to create the comment on. Format: `projects/{project}/locations/{location}/orders/{order}`  
`comment` | `[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)`  
Required. The comment to create.  
`commentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Comment within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The comment.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createCommentAsync(CreateCommentRequest request)
    
    
    public final OperationFuture<Comment,OperationMetadata> createCommentAsync(CreateCommentRequest request)

Creates a new comment on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateCommentRequest request =
           CreateCommentRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setCommentId("commentId-1495016486")
               .setComment(Comment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Comment response = gDCHardwareManagementClient.createCommentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateCommentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createCommentAsync(String parent, Comment comment, String commentId)
    
    
    public final OperationFuture<Comment,OperationMetadata> createCommentAsync(String parent, Comment comment, String commentId)

Creates a new comment on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       Comment comment = Comment.newBuilder().build();
       String commentId = "commentId-1495016486";
       Comment response =
           gDCHardwareManagementClient.createCommentAsync(parent, comment, commentId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The order to create the comment on. Format: `projects/{project}/locations/{location}/orders/{order}`  
`comment` | `[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)`  
Required. The comment to create.  
`commentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Comment within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The comment.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createCommentCallable()
    
    
    public final UnaryCallable<CreateCommentRequest,Operation> createCommentCallable()

Creates a new comment on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateCommentRequest request =
           CreateCommentRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setCommentId("commentId-1495016486")
               .setComment(Comment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.createCommentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateCommentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCommentOperationCallable()
    
    
    public final OperationCallable<CreateCommentRequest,Comment,OperationMetadata> createCommentOperationCallable()

Creates a new comment on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateCommentRequest request =
           CreateCommentRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setCommentId("commentId-1495016486")
               .setComment(Comment.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Comment, OperationMetadata> future =
           gDCHardwareManagementClient.createCommentOperationCallable().futureCall(request);
       // Do something.
       Comment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateCommentRequest),[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareAsync(@Nullable LocationName parent, Hardware hardware, String hardwareId)
    
    
    public final OperationFuture<Hardware,OperationMetadata> createHardwareAsync(@Nullable LocationName parent, Hardware hardware, String hardwareId)

Creates new hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Hardware hardware = Hardware.newBuilder().build();
       String hardwareId = "hardwareId680924451";
       Hardware response =
           gDCHardwareManagementClient.createHardwareAsync(parent, hardware, hardwareId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to create hardware in. Format: `projects/{project}/locations/{location}`  
`hardware` | `[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)`  
Required. The resource to create.  
`hardwareId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Hardware within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The hardware.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareAsync(CreateHardwareRequest request)
    
    
    public final OperationFuture<Hardware,OperationMetadata> createHardwareAsync(CreateHardwareRequest request)

Creates new hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateHardwareRequest request =
           CreateHardwareRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHardwareId("hardwareId680924451")
               .setHardware(Hardware.newBuilder().build())
               .build();
       Hardware response = gDCHardwareManagementClient.createHardwareAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareAsync(String parent, Hardware hardware, String hardwareId)
    
    
    public final OperationFuture<Hardware,OperationMetadata> createHardwareAsync(String parent, Hardware hardware, String hardwareId)

Creates new hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Hardware hardware = Hardware.newBuilder().build();
       String hardwareId = "hardwareId680924451";
       Hardware response =
           gDCHardwareManagementClient.createHardwareAsync(parent, hardware, hardwareId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to create hardware in. Format: `projects/{project}/locations/{location}`  
`hardware` | `[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)`  
Required. The resource to create.  
`hardwareId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Hardware within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The hardware.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareCallable()
    
    
    public final UnaryCallable<CreateHardwareRequest,Operation> createHardwareCallable()

Creates new hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateHardwareRequest request =
           CreateHardwareRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHardwareId("hardwareId680924451")
               .setHardware(Hardware.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.createHardwareCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHardwareGroupAsync(@Nullable OrderName parent, HardwareGroup hardwareGroup, String hardwareGroupId)
    
    
    public final OperationFuture<HardwareGroup,OperationMetadata> createHardwareGroupAsync(@Nullable OrderName parent, HardwareGroup hardwareGroup, String hardwareGroupId)

Creates a new hardware group in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       HardwareGroup hardwareGroup = HardwareGroup.newBuilder().build();
       String hardwareGroupId = "hardwareGroupId-1961682702";
       HardwareGroup response =
           gDCHardwareManagementClient
               .createHardwareGroupAsync(parent, hardwareGroup, hardwareGroupId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The order to create the hardware group in. Format: `projects/{project}/locations/{location}/orders/{order}`  
`hardwareGroup` | `[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)`  
Required. The hardware group to create.  
`hardwareGroupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the HardwareGroup within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The hardware_group.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareGroupAsync(CreateHardwareGroupRequest request)
    
    
    public final OperationFuture<HardwareGroup,OperationMetadata> createHardwareGroupAsync(CreateHardwareGroupRequest request)

Creates a new hardware group in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateHardwareGroupRequest request =
           CreateHardwareGroupRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setHardwareGroupId("hardwareGroupId-1961682702")
               .setHardwareGroup(HardwareGroup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       HardwareGroup response = gDCHardwareManagementClient.createHardwareGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareGroupAsync(String parent, HardwareGroup hardwareGroup, String hardwareGroupId)
    
    
    public final OperationFuture<HardwareGroup,OperationMetadata> createHardwareGroupAsync(String parent, HardwareGroup hardwareGroup, String hardwareGroupId)

Creates a new hardware group in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       HardwareGroup hardwareGroup = HardwareGroup.newBuilder().build();
       String hardwareGroupId = "hardwareGroupId-1961682702";
       HardwareGroup response =
           gDCHardwareManagementClient
               .createHardwareGroupAsync(parent, hardwareGroup, hardwareGroupId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The order to create the hardware group in. Format: `projects/{project}/locations/{location}/orders/{order}`  
`hardwareGroup` | `[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)`  
Required. The hardware group to create.  
`hardwareGroupId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the HardwareGroup within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The hardware_group.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareGroupCallable()
    
    
    public final UnaryCallable<CreateHardwareGroupRequest,Operation> createHardwareGroupCallable()

Creates a new hardware group in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateHardwareGroupRequest request =
           CreateHardwareGroupRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setHardwareGroupId("hardwareGroupId-1961682702")
               .setHardwareGroup(HardwareGroup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.createHardwareGroupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHardwareGroupOperationCallable()
    
    
    public final OperationCallable<CreateHardwareGroupRequest,HardwareGroup,OperationMetadata> createHardwareGroupOperationCallable()

Creates a new hardware group in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateHardwareGroupRequest request =
           CreateHardwareGroupRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setHardwareGroupId("hardwareGroupId-1961682702")
               .setHardwareGroup(HardwareGroup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<HardwareGroup, OperationMetadata> future =
           gDCHardwareManagementClient.createHardwareGroupOperationCallable().futureCall(request);
       // Do something.
       HardwareGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareGroupRequest),[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareOperationCallable()
    
    
    public final OperationCallable<CreateHardwareRequest,Hardware,OperationMetadata> createHardwareOperationCallable()

Creates new hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateHardwareRequest request =
           CreateHardwareRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHardwareId("hardwareId680924451")
               .setHardware(Hardware.newBuilder().build())
               .build();
       OperationFuture<Hardware, OperationMetadata> future =
           gDCHardwareManagementClient.createHardwareOperationCallable().futureCall(request);
       // Do something.
       Hardware response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareRequest),[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createOrderAsync(@Nullable LocationName parent, Order order, String orderId)
    
    
    public final OperationFuture<Order,OperationMetadata> createOrderAsync(@Nullable LocationName parent, Order order, String orderId)

Creates a new order in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Order order = Order.newBuilder().build();
       String orderId = "orderId-1207110391";
       Order response = gDCHardwareManagementClient.createOrderAsync(parent, order, orderId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to create the order in. Format: `projects/{project}/locations/{location}`  
`order` | `[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)`  
Required. The order to create.  
`orderId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Order within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The order.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createOrderAsync(CreateOrderRequest request)
    
    
    public final OperationFuture<Order,OperationMetadata> createOrderAsync(CreateOrderRequest request)

Creates a new order in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateOrderRequest request =
           CreateOrderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOrderId("orderId-1207110391")
               .setOrder(Order.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Order response = gDCHardwareManagementClient.createOrderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createOrderAsync(String parent, Order order, String orderId)
    
    
    public final OperationFuture<Order,OperationMetadata> createOrderAsync(String parent, Order order, String orderId)

Creates a new order in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Order order = Order.newBuilder().build();
       String orderId = "orderId-1207110391";
       Order response = gDCHardwareManagementClient.createOrderAsync(parent, order, orderId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to create the order in. Format: `projects/{project}/locations/{location}`  
`order` | `[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)`  
Required. The order to create.  
`orderId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Order within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The order.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createOrderCallable()
    
    
    public final UnaryCallable<CreateOrderRequest,Operation> createOrderCallable()

Creates a new order in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateOrderRequest request =
           CreateOrderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOrderId("orderId-1207110391")
               .setOrder(Order.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.createOrderCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createOrderOperationCallable()
    
    
    public final OperationCallable<CreateOrderRequest,Order,OperationMetadata> createOrderOperationCallable()

Creates a new order in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateOrderRequest request =
           CreateOrderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setOrderId("orderId-1207110391")
               .setOrder(Order.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Order, OperationMetadata> future =
           gDCHardwareManagementClient.createOrderOperationCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createSiteAsync(@Nullable LocationName parent, Site site, String siteId)
    
    
    public final OperationFuture<Site,OperationMetadata> createSiteAsync(@Nullable LocationName parent, Site site, String siteId)

Creates a new site in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Site site = Site.newBuilder().build();
       String siteId = "siteId-902090046";
       Site response = gDCHardwareManagementClient.createSiteAsync(parent, site, siteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to create the site in. Format: `projects/{project}/locations/{location}`  
`site` | `[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)`  
Required. The site to create.  
`siteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Site within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The site.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createSiteAsync(CreateSiteRequest request)
    
    
    public final OperationFuture<Site,OperationMetadata> createSiteAsync(CreateSiteRequest request)

Creates a new site in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateSiteRequest request =
           CreateSiteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSiteId("siteId-902090046")
               .setSite(Site.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Site response = gDCHardwareManagementClient.createSiteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createSiteAsync(String parent, Site site, String siteId)
    
    
    public final OperationFuture<Site,OperationMetadata> createSiteAsync(String parent, Site site, String siteId)

Creates a new site in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Site site = Site.newBuilder().build();
       String siteId = "siteId-902090046";
       Site response = gDCHardwareManagementClient.createSiteAsync(parent, site, siteId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to create the site in. Format: `projects/{project}/locations/{location}`  
`site` | `[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)`  
Required. The site to create.  
`siteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Site within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The site.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createSiteCallable()
    
    
    public final UnaryCallable<CreateSiteRequest,Operation> createSiteCallable()

Creates a new site in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateSiteRequest request =
           CreateSiteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSiteId("siteId-902090046")
               .setSite(Site.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.createSiteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSiteOperationCallable()
    
    
    public final OperationCallable<CreateSiteRequest,Site,OperationMetadata> createSiteOperationCallable()

Creates a new site in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateSiteRequest request =
           CreateSiteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSiteId("siteId-902090046")
               .setSite(Site.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Site, OperationMetadata> future =
           gDCHardwareManagementClient.createSiteOperationCallable().futureCall(request);
       // Do something.
       Site response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createZoneAsync(@Nullable LocationName parent, Zone zone, String zoneId)
    
    
    public final OperationFuture<Zone,OperationMetadata> createZoneAsync(@Nullable LocationName parent, Zone zone, String zoneId)

Creates a new zone in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Zone zone = Zone.newBuilder().build();
       String zoneId = "zoneId-696323609";
       Zone response = gDCHardwareManagementClient.createZoneAsync(parent, zone, zoneId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to create the zone in. Format: `projects/{project}/locations/{location}`  
`zone` | `[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)`  
Required. The zone to create.  
`zoneId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Zone within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The zone.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createZoneAsync(CreateZoneRequest request)
    
    
    public final OperationFuture<Zone,OperationMetadata> createZoneAsync(CreateZoneRequest request)

Creates a new zone in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateZoneRequest request =
           CreateZoneRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setZoneId("zoneId-696323609")
               .setZone(Zone.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Zone response = gDCHardwareManagementClient.createZoneAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createZoneAsync(String parent, Zone zone, String zoneId)
    
    
    public final OperationFuture<Zone,OperationMetadata> createZoneAsync(String parent, Zone zone, String zoneId)

Creates a new zone in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Zone zone = Zone.newBuilder().build();
       String zoneId = "zoneId-696323609";
       Zone response = gDCHardwareManagementClient.createZoneAsync(parent, zone, zoneId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to create the zone in. Format: `projects/{project}/locations/{location}`  
`zone` | `[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)`  
Required. The zone to create.  
`zoneId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. ID used to uniquely identify the Zone within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The zone.name field in the request will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createZoneCallable()
    
    
    public final UnaryCallable<CreateZoneRequest,Operation> createZoneCallable()

Creates a new zone in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateZoneRequest request =
           CreateZoneRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setZoneId("zoneId-696323609")
               .setZone(Zone.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.createZoneCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createZoneOperationCallable()
    
    
    public final OperationCallable<CreateZoneRequest,Zone,OperationMetadata> createZoneOperationCallable()

Creates a new zone in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CreateZoneRequest request =
           CreateZoneRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setZoneId("zoneId-696323609")
               .setZone(Zone.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Zone, OperationMetadata> future =
           gDCHardwareManagementClient.createZoneOperationCallable().futureCall(request);
       // Do something.
       Zone response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareAsync(@Nullable HardwareName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHardwareAsync(@Nullable HardwareName name)

Deletes hardware.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       HardwareName name = HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]");
       gDCHardwareManagementClient.deleteHardwareAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.HardwareName`  
Required. The name of the hardware. Format: `projects/{project}/locations/{location}/hardware/{hardware}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareAsync(DeleteHardwareRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHardwareAsync(DeleteHardwareRequest request)

Deletes hardware.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteHardwareRequest request =
           DeleteHardwareRequest.newBuilder()
               .setName(HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]").toString())
               .setRequestId("requestId693933066")
               .build();
       gDCHardwareManagementClient.deleteHardwareAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHardwareAsync(String name)

Deletes hardware.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]").toString();
       gDCHardwareManagementClient.deleteHardwareAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hardware. Format: `projects/{project}/locations/{location}/hardware/{hardware}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareCallable()
    
    
    public final UnaryCallable<DeleteHardwareRequest,Operation> deleteHardwareCallable()

Deletes hardware.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteHardwareRequest request =
           DeleteHardwareRequest.newBuilder()
               .setName(HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.deleteHardwareCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHardwareGroupAsync(@Nullable HardwareGroupName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHardwareGroupAsync(@Nullable HardwareGroupName name)

Deletes a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       HardwareGroupName name =
           HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]");
       gDCHardwareManagementClient.deleteHardwareGroupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroupName`  
Required. The name of the hardware group. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareGroupAsync(DeleteHardwareGroupRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHardwareGroupAsync(DeleteHardwareGroupRequest request)

Deletes a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteHardwareGroupRequest request =
           DeleteHardwareGroupRequest.newBuilder()
               .setName(
                   HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       gDCHardwareManagementClient.deleteHardwareGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareGroupAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteHardwareGroupAsync(String name)

Deletes a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name =
           HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]").toString();
       gDCHardwareManagementClient.deleteHardwareGroupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hardware group. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareGroupCallable()
    
    
    public final UnaryCallable<DeleteHardwareGroupRequest,Operation> deleteHardwareGroupCallable()

Deletes a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteHardwareGroupRequest request =
           DeleteHardwareGroupRequest.newBuilder()
               .setName(
                   HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.deleteHardwareGroupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHardwareGroupOperationCallable()
    
    
    public final OperationCallable<DeleteHardwareGroupRequest,Empty,OperationMetadata> deleteHardwareGroupOperationCallable()

Deletes a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteHardwareGroupRequest request =
           DeleteHardwareGroupRequest.newBuilder()
               .setName(
                   HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           gDCHardwareManagementClient.deleteHardwareGroupOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareOperationCallable()
    
    
    public final OperationCallable<DeleteHardwareRequest,Empty,OperationMetadata> deleteHardwareOperationCallable()

Deletes hardware.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteHardwareRequest request =
           DeleteHardwareRequest.newBuilder()
               .setName(HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           gDCHardwareManagementClient.deleteHardwareOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteOrderAsync(@Nullable OrderName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOrderAsync(@Nullable OrderName name)

Deletes an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       gDCHardwareManagementClient.deleteOrderAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteOrderAsync(DeleteOrderRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOrderAsync(DeleteOrderRequest request)

Deletes an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteOrderRequest request =
           DeleteOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       gDCHardwareManagementClient.deleteOrderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteOrderAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteOrderAsync(String name)

Deletes an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       gDCHardwareManagementClient.deleteOrderAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteOrderCallable()
    
    
    public final UnaryCallable<DeleteOrderRequest,Operation> deleteOrderCallable()

Deletes an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteOrderRequest request =
           DeleteOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.deleteOrderCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteOrderOperationCallable()
    
    
    public final OperationCallable<DeleteOrderRequest,Empty,OperationMetadata> deleteOrderOperationCallable()

Deletes an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteOrderRequest request =
           DeleteOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           gDCHardwareManagementClient.deleteOrderOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteOrderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteSiteAsync(@Nullable SiteName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSiteAsync(@Nullable SiteName name)

Deletes a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SiteName name = SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]");
       gDCHardwareManagementClient.deleteSiteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.SiteName`  
Required. The name of the site. Format: `projects/{project}/locations/{location}/sites/{site}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteSiteAsync(DeleteSiteRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSiteAsync(DeleteSiteRequest request)

Deletes a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteSiteRequest request =
           DeleteSiteRequest.newBuilder()
               .setName(SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]").toString())
               .setRequestId("requestId693933066")
               .build();
       gDCHardwareManagementClient.deleteSiteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteSiteAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSiteAsync(String name)

Deletes a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]").toString();
       gDCHardwareManagementClient.deleteSiteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the site. Format: `projects/{project}/locations/{location}/sites/{site}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteSiteCallable()
    
    
    public final UnaryCallable<DeleteSiteRequest,Operation> deleteSiteCallable()

Deletes a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteSiteRequest request =
           DeleteSiteRequest.newBuilder()
               .setName(SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.deleteSiteCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSiteOperationCallable()
    
    
    public final OperationCallable<DeleteSiteRequest,Empty,OperationMetadata> deleteSiteOperationCallable()

Deletes a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteSiteRequest request =
           DeleteSiteRequest.newBuilder()
               .setName(SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           gDCHardwareManagementClient.deleteSiteOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteSiteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteZoneAsync(@Nullable ZoneName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteZoneAsync(@Nullable ZoneName name)

Deletes a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ZoneName name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       gDCHardwareManagementClient.deleteZoneAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.ZoneName`  
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteZoneAsync(DeleteZoneRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteZoneAsync(DeleteZoneRequest request)

Deletes a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteZoneRequest request =
           DeleteZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRequestId("requestId693933066")
               .build();
       gDCHardwareManagementClient.deleteZoneAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteZoneAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteZoneAsync(String name)

Deletes a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       gDCHardwareManagementClient.deleteZoneAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteZoneCallable()
    
    
    public final UnaryCallable<DeleteZoneRequest,Operation> deleteZoneCallable()

Deletes a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteZoneRequest request =
           DeleteZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.deleteZoneCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteZoneOperationCallable()
    
    
    public final OperationCallable<DeleteZoneRequest,Empty,OperationMetadata> deleteZoneOperationCallable()

Deletes a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       DeleteZoneRequest request =
           DeleteZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           gDCHardwareManagementClient.deleteZoneOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteZoneRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### getChangeLogEntry(@Nullable ChangeLogEntryName name)
    
    
    public final ChangeLogEntry getChangeLogEntry(@Nullable ChangeLogEntryName name)

Gets details of a change to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ChangeLogEntryName name =
           ChangeLogEntryName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[CHANGE_LOG_ENTRY]");
       ChangeLogEntry response = gDCHardwareManagementClient.getChangeLogEntry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.ChangeLogEntryName`  
Required. The name of the change log entry. Format: `projects/{project}/locations/{location}/orders/{order}/changeLogEntries/{change_log_entry}`  
**Returns**  
---  
**Type** | **Description**  
`[ChangeLogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ChangeLogEntry)` |   
  
### getChangeLogEntry(GetChangeLogEntryRequest request)
    
    
    public final ChangeLogEntry getChangeLogEntry(GetChangeLogEntryRequest request)

Gets details of a change to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetChangeLogEntryRequest request =
           GetChangeLogEntryRequest.newBuilder()
               .setName(
                   ChangeLogEntryName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[CHANGE_LOG_ENTRY]")
                       .toString())
               .build();
       ChangeLogEntry response = gDCHardwareManagementClient.getChangeLogEntry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChangeLogEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetChangeLogEntryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChangeLogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ChangeLogEntry)` |   
  
### getChangeLogEntry(String name)
    
    
    public final ChangeLogEntry getChangeLogEntry(String name)

Gets details of a change to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name =
           ChangeLogEntryName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[CHANGE_LOG_ENTRY]")
               .toString();
       ChangeLogEntry response = gDCHardwareManagementClient.getChangeLogEntry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the change log entry. Format: `projects/{project}/locations/{location}/orders/{order}/changeLogEntries/{change_log_entry}`  
**Returns**  
---  
**Type** | **Description**  
`[ChangeLogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ChangeLogEntry)` |   
  
### getChangeLogEntryCallable()
    
    
    public final UnaryCallable<GetChangeLogEntryRequest,ChangeLogEntry> getChangeLogEntryCallable()

Gets details of a change to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetChangeLogEntryRequest request =
           GetChangeLogEntryRequest.newBuilder()
               .setName(
                   ChangeLogEntryName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[CHANGE_LOG_ENTRY]")
                       .toString())
               .build();
       ApiFuture<ChangeLogEntry> future =
           gDCHardwareManagementClient.getChangeLogEntryCallable().futureCall(request);
       // Do something.
       ChangeLogEntry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetChangeLogEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetChangeLogEntryRequest),[ChangeLogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ChangeLogEntry)>` |   
  
### getComment(@Nullable CommentName name)
    
    
    public final Comment getComment(@Nullable CommentName name)

Gets the content of a comment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CommentName name = CommentName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[COMMENT]");
       Comment response = gDCHardwareManagementClient.getComment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.CommentName`  
Required. The name of the comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`  
**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)` |   
  
### getComment(GetCommentRequest request)
    
    
    public final Comment getComment(GetCommentRequest request)

Gets the content of a comment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetCommentRequest request =
           GetCommentRequest.newBuilder()
               .setName(CommentName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[COMMENT]").toString())
               .build();
       Comment response = gDCHardwareManagementClient.getComment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetCommentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)` |   
  
### getComment(String name)
    
    
    public final Comment getComment(String name)

Gets the content of a comment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = CommentName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[COMMENT]").toString();
       Comment response = gDCHardwareManagementClient.getComment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`  
**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)` |   
  
### getCommentCallable()
    
    
    public final UnaryCallable<GetCommentRequest,Comment> getCommentCallable()

Gets the content of a comment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetCommentRequest request =
           GetCommentRequest.newBuilder()
               .setName(CommentName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[COMMENT]").toString())
               .build();
       ApiFuture<Comment> future =
           gDCHardwareManagementClient.getCommentCallable().futureCall(request);
       // Do something.
       Comment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetCommentRequest),[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)>` |   
  
### getHardware(@Nullable HardwareName name)
    
    
    public final Hardware getHardware(@Nullable HardwareName name)

Gets hardware details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       HardwareName name = HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]");
       Hardware response = gDCHardwareManagementClient.getHardware(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.HardwareName`  
Required. The name of the hardware. Format: `projects/{project}/locations/{location}/hardware/{hardware}`  
**Returns**  
---  
**Type** | **Description**  
`[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)` |   
  
### getHardware(GetHardwareRequest request)
    
    
    public final Hardware getHardware(GetHardwareRequest request)

Gets hardware details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetHardwareRequest request =
           GetHardwareRequest.newBuilder()
               .setName(HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]").toString())
               .build();
       Hardware response = gDCHardwareManagementClient.getHardware(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)` |   
  
### getHardware(String name)
    
    
    public final Hardware getHardware(String name)

Gets hardware details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]").toString();
       Hardware response = gDCHardwareManagementClient.getHardware(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hardware. Format: `projects/{project}/locations/{location}/hardware/{hardware}`  
**Returns**  
---  
**Type** | **Description**  
`[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)` |   
  
### getHardwareCallable()
    
    
    public final UnaryCallable<GetHardwareRequest,Hardware> getHardwareCallable()

Gets hardware details.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetHardwareRequest request =
           GetHardwareRequest.newBuilder()
               .setName(HardwareName.of("[PROJECT]", "[LOCATION]", "[HARDWARE]").toString())
               .build();
       ApiFuture<Hardware> future =
           gDCHardwareManagementClient.getHardwareCallable().futureCall(request);
       // Do something.
       Hardware response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareRequest),[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)>` |   
  
### getHardwareGroup(@Nullable HardwareGroupName name)
    
    
    public final HardwareGroup getHardwareGroup(@Nullable HardwareGroupName name)

Gets details of a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       HardwareGroupName name =
           HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]");
       HardwareGroup response = gDCHardwareManagementClient.getHardwareGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroupName`  
Required. The name of the hardware group. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`  
**Returns**  
---  
**Type** | **Description**  
`[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)` |   
  
### getHardwareGroup(GetHardwareGroupRequest request)
    
    
    public final HardwareGroup getHardwareGroup(GetHardwareGroupRequest request)

Gets details of a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetHardwareGroupRequest request =
           GetHardwareGroupRequest.newBuilder()
               .setName(
                   HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]")
                       .toString())
               .build();
       HardwareGroup response = gDCHardwareManagementClient.getHardwareGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)` |   
  
### getHardwareGroup(String name)
    
    
    public final HardwareGroup getHardwareGroup(String name)

Gets details of a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name =
           HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]").toString();
       HardwareGroup response = gDCHardwareManagementClient.getHardwareGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the hardware group. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`  
**Returns**  
---  
**Type** | **Description**  
`[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)` |   
  
### getHardwareGroupCallable()
    
    
    public final UnaryCallable<GetHardwareGroupRequest,HardwareGroup> getHardwareGroupCallable()

Gets details of a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetHardwareGroupRequest request =
           GetHardwareGroupRequest.newBuilder()
               .setName(
                   HardwareGroupName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[HARDWARE_GROUP]")
                       .toString())
               .build();
       ApiFuture<HardwareGroup> future =
           gDCHardwareManagementClient.getHardwareGroupCallable().futureCall(request);
       // Do something.
       HardwareGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareGroupRequest),[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)>` |   
  
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
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = gDCHardwareManagementClient.getLocation(request);
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
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           gDCHardwareManagementClient.getLocationCallable().futureCall(request);
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
  
### getOrder(@Nullable OrderName name)
    
    
    public final Order getOrder(@Nullable OrderName name)

Gets details of an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       Order response = gDCHardwareManagementClient.getOrder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)` |   
  
### getOrder(GetOrderRequest request)
    
    
    public final Order getOrder(GetOrderRequest request)

Gets details of an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetOrderRequest request =
           GetOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .build();
       Order response = gDCHardwareManagementClient.getOrder(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)` |   
  
### getOrder(String name)
    
    
    public final Order getOrder(String name)

Gets details of an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       Order response = gDCHardwareManagementClient.getOrder(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)` |   
  
### getOrderCallable()
    
    
    public final UnaryCallable<GetOrderRequest,Order> getOrderCallable()

Gets details of an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetOrderRequest request =
           GetOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .build();
       ApiFuture<Order> future = gDCHardwareManagementClient.getOrderCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)>` |   
  
### getSettings()
    
    
    public final @Nullable GDCHardwareManagementSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings` |   
  
### getSite(@Nullable SiteName name)
    
    
    public final Site getSite(@Nullable SiteName name)

Gets details of a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SiteName name = SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]");
       Site response = gDCHardwareManagementClient.getSite(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.SiteName`  
Required. The name of the site. Format: `projects/{project}/locations/{location}/sites/{site}`  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)` |   
  
### getSite(GetSiteRequest request)
    
    
    public final Site getSite(GetSiteRequest request)

Gets details of a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetSiteRequest request =
           GetSiteRequest.newBuilder()
               .setName(SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]").toString())
               .build();
       Site response = gDCHardwareManagementClient.getSite(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)` |   
  
### getSite(String name)
    
    
    public final Site getSite(String name)

Gets details of a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]").toString();
       Site response = gDCHardwareManagementClient.getSite(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the site. Format: `projects/{project}/locations/{location}/sites/{site}`  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)` |   
  
### getSiteCallable()
    
    
    public final UnaryCallable<GetSiteRequest,Site> getSiteCallable()

Gets details of a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetSiteRequest request =
           GetSiteRequest.newBuilder()
               .setName(SiteName.of("[PROJECT]", "[LOCATION]", "[SITE]").toString())
               .build();
       ApiFuture<Site> future = gDCHardwareManagementClient.getSiteCallable().futureCall(request);
       // Do something.
       Site response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)>` |   
  
### getSku(@Nullable SkuName name)
    
    
    public final Sku getSku(@Nullable SkuName name)

Gets details of an SKU.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SkuName name = SkuName.of("[PROJECT]", "[LOCATION]", "[SKU]");
       Sku response = gDCHardwareManagementClient.getSku(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.SkuName`  
Required. The name of the SKU. Format: `projects/{project}/locations/{location}/skus/{sku}`  
**Returns**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Sku)` |   
  
### getSku(GetSkuRequest request)
    
    
    public final Sku getSku(GetSkuRequest request)

Gets details of an SKU.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetSkuRequest request =
           GetSkuRequest.newBuilder()
               .setName(SkuName.of("[PROJECT]", "[LOCATION]", "[SKU]").toString())
               .build();
       Sku response = gDCHardwareManagementClient.getSku(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSkuRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSkuRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Sku)` |   
  
### getSku(String name)
    
    
    public final Sku getSku(String name)

Gets details of an SKU.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = SkuName.of("[PROJECT]", "[LOCATION]", "[SKU]").toString();
       Sku response = gDCHardwareManagementClient.getSku(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the SKU. Format: `projects/{project}/locations/{location}/skus/{sku}`  
**Returns**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Sku)` |   
  
### getSkuCallable()
    
    
    public final UnaryCallable<GetSkuRequest,Sku> getSkuCallable()

Gets details of an SKU.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetSkuRequest request =
           GetSkuRequest.newBuilder()
               .setName(SkuName.of("[PROJECT]", "[LOCATION]", "[SKU]").toString())
               .build();
       ApiFuture<Sku> future = gDCHardwareManagementClient.getSkuCallable().futureCall(request);
       // Do something.
       Sku response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSkuRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSkuRequest),[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Sku)>` |   
  
### getStub()
    
    
    public GDCHardwareManagementStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.stub.GDCHardwareManagementStub)` |   
  
### getZone(@Nullable ZoneName name)
    
    
    public final Zone getZone(@Nullable ZoneName name)

Gets details of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ZoneName name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       Zone response = gDCHardwareManagementClient.getZone(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.ZoneName`  
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)` |   
  
### getZone(GetZoneRequest request)
    
    
    public final Zone getZone(GetZoneRequest request)

Gets details of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetZoneRequest request =
           GetZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .build();
       Zone response = gDCHardwareManagementClient.getZone(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)` |   
  
### getZone(String name)
    
    
    public final Zone getZone(String name)

Gets details of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       Zone response = gDCHardwareManagementClient.getZone(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)` |   
  
### getZoneCallable()
    
    
    public final UnaryCallable<GetZoneRequest,Zone> getZoneCallable()

Gets details of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       GetZoneRequest request =
           GetZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .build();
       ApiFuture<Zone> future = gDCHardwareManagementClient.getZoneCallable().futureCall(request);
       // Do something.
       Zone response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)>` |   
  
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
  
### listChangeLogEntries(@Nullable OrderName parent)
    
    
    public final GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse listChangeLogEntries(@Nullable OrderName parent)

Lists the changes made to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       for (ChangeLogEntry element :
           gDCHardwareManagementClient.listChangeLogEntries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The order to list change log entries for. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse)` |   
  
### listChangeLogEntries(ListChangeLogEntriesRequest request)
    
    
    public final GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse listChangeLogEntries(ListChangeLogEntriesRequest request)

Lists the changes made to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListChangeLogEntriesRequest request =
           ListChangeLogEntriesRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ChangeLogEntry element :
           gDCHardwareManagementClient.listChangeLogEntries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChangeLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse)` |   
  
### listChangeLogEntries(String parent)
    
    
    public final GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse listChangeLogEntries(String parent)

Lists the changes made to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       for (ChangeLogEntry element :
           gDCHardwareManagementClient.listChangeLogEntries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The order to list change log entries for. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse)` |   
  
### listChangeLogEntriesCallable()
    
    
    public final UnaryCallable<ListChangeLogEntriesRequest,ListChangeLogEntriesResponse> listChangeLogEntriesCallable()

Lists the changes made to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListChangeLogEntriesRequest request =
           ListChangeLogEntriesRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListChangeLogEntriesResponse response =
             gDCHardwareManagementClient.listChangeLogEntriesCallable().call(request);
         for (ChangeLogEntry element : response.getChangeLogEntriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChangeLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesRequest),[ListChangeLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesResponse)>` |   
  
### listChangeLogEntriesPagedCallable()
    
    
    public final UnaryCallable<ListChangeLogEntriesRequest,GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse> listChangeLogEntriesPagedCallable()

Lists the changes made to an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListChangeLogEntriesRequest request =
           ListChangeLogEntriesRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ChangeLogEntry> future =
           gDCHardwareManagementClient.listChangeLogEntriesPagedCallable().futureCall(request);
       // Do something.
       for (ChangeLogEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChangeLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesRequest),[ListChangeLogEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse)>` |   
  
### listComments(@Nullable OrderName parent)
    
    
    public final GDCHardwareManagementClient.ListCommentsPagedResponse listComments(@Nullable OrderName parent)

Lists the comments on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       for (Comment element : gDCHardwareManagementClient.listComments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The order to list comments on. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListCommentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListCommentsPagedResponse)` |   
  
### listComments(ListCommentsRequest request)
    
    
    public final GDCHardwareManagementClient.ListCommentsPagedResponse listComments(ListCommentsRequest request)

Lists the comments on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListCommentsRequest request =
           ListCommentsRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Comment element : gDCHardwareManagementClient.listComments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCommentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListCommentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListCommentsPagedResponse)` |   
  
### listComments(String parent)
    
    
    public final GDCHardwareManagementClient.ListCommentsPagedResponse listComments(String parent)

Lists the comments on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       for (Comment element : gDCHardwareManagementClient.listComments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The order to list comments on. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListCommentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListCommentsPagedResponse)` |   
  
### listCommentsCallable()
    
    
    public final UnaryCallable<ListCommentsRequest,ListCommentsResponse> listCommentsCallable()

Lists the comments on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListCommentsRequest request =
           ListCommentsRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListCommentsResponse response =
             gDCHardwareManagementClient.listCommentsCallable().call(request);
         for (Comment element : response.getCommentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCommentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsRequest),[ListCommentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsResponse)>` |   
  
### listCommentsPagedCallable()
    
    
    public final UnaryCallable<ListCommentsRequest,GDCHardwareManagementClient.ListCommentsPagedResponse> listCommentsPagedCallable()

Lists the comments on an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListCommentsRequest request =
           ListCommentsRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Comment> future =
           gDCHardwareManagementClient.listCommentsPagedCallable().futureCall(request);
       // Do something.
       for (Comment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCommentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsRequest),[ListCommentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListCommentsPagedResponse)>` |   
  
### listHardware(@Nullable LocationName parent)
    
    
    public final GDCHardwareManagementClient.ListHardwarePagedResponse listHardware(@Nullable LocationName parent)

Lists hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Hardware element : gDCHardwareManagementClient.listHardware(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to list hardware in. Format: `projects/{project}/locations/{location}` To list hardware across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListHardwarePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwarePagedResponse)` |   
  
### listHardware(ListHardwareRequest request)
    
    
    public final GDCHardwareManagementClient.ListHardwarePagedResponse listHardware(ListHardwareRequest request)

Lists hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListHardwareRequest request =
           ListHardwareRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Hardware element : gDCHardwareManagementClient.listHardware(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListHardwarePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwarePagedResponse)` |   
  
### listHardware(String parent)
    
    
    public final GDCHardwareManagementClient.ListHardwarePagedResponse listHardware(String parent)

Lists hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Hardware element : gDCHardwareManagementClient.listHardware(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to list hardware in. Format: `projects/{project}/locations/{location}` To list hardware across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListHardwarePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwarePagedResponse)` |   
  
### listHardwareCallable()
    
    
    public final UnaryCallable<ListHardwareRequest,ListHardwareResponse> listHardwareCallable()

Lists hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListHardwareRequest request =
           ListHardwareRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListHardwareResponse response =
             gDCHardwareManagementClient.listHardwareCallable().call(request);
         for (Hardware element : response.getHardwareList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareRequest),[ListHardwareResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareResponse)>` |   
  
### listHardwareGroups(@Nullable OrderName parent)
    
    
    public final GDCHardwareManagementClient.ListHardwareGroupsPagedResponse listHardwareGroups(@Nullable OrderName parent)

Lists hardware groups in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       for (HardwareGroup element :
           gDCHardwareManagementClient.listHardwareGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The order to list hardware groups in. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListHardwareGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwareGroupsPagedResponse)` |   
  
### listHardwareGroups(ListHardwareGroupsRequest request)
    
    
    public final GDCHardwareManagementClient.ListHardwareGroupsPagedResponse listHardwareGroups(ListHardwareGroupsRequest request)

Lists hardware groups in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListHardwareGroupsRequest request =
           ListHardwareGroupsRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (HardwareGroup element :
           gDCHardwareManagementClient.listHardwareGroups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHardwareGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListHardwareGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwareGroupsPagedResponse)` |   
  
### listHardwareGroups(String parent)
    
    
    public final GDCHardwareManagementClient.ListHardwareGroupsPagedResponse listHardwareGroups(String parent)

Lists hardware groups in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       for (HardwareGroup element :
           gDCHardwareManagementClient.listHardwareGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The order to list hardware groups in. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListHardwareGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwareGroupsPagedResponse)` |   
  
### listHardwareGroupsCallable()
    
    
    public final UnaryCallable<ListHardwareGroupsRequest,ListHardwareGroupsResponse> listHardwareGroupsCallable()

Lists hardware groups in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListHardwareGroupsRequest request =
           ListHardwareGroupsRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListHardwareGroupsResponse response =
             gDCHardwareManagementClient.listHardwareGroupsCallable().call(request);
         for (HardwareGroup element : response.getHardwareGroupsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHardwareGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsRequest),[ListHardwareGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsResponse)>` |   
  
### listHardwareGroupsPagedCallable()
    
    
    public final UnaryCallable<ListHardwareGroupsRequest,GDCHardwareManagementClient.ListHardwareGroupsPagedResponse> listHardwareGroupsPagedCallable()

Lists hardware groups in a given order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListHardwareGroupsRequest request =
           ListHardwareGroupsRequest.newBuilder()
               .setParent(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<HardwareGroup> future =
           gDCHardwareManagementClient.listHardwareGroupsPagedCallable().futureCall(request);
       // Do something.
       for (HardwareGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHardwareGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsRequest),[ListHardwareGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwareGroupsPagedResponse)>` |   
  
### listHardwarePagedCallable()
    
    
    public final UnaryCallable<ListHardwareRequest,GDCHardwareManagementClient.ListHardwarePagedResponse> listHardwarePagedCallable()

Lists hardware in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListHardwareRequest request =
           ListHardwareRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Hardware> future =
           gDCHardwareManagementClient.listHardwarePagedCallable().futureCall(request);
       // Do something.
       for (Hardware element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareRequest),[ListHardwarePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwarePagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final GDCHardwareManagementClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : gDCHardwareManagementClient.listLocations(request).iterateAll()) {
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
`[GDCHardwareManagementClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             gDCHardwareManagementClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,GDCHardwareManagementClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           gDCHardwareManagementClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListLocationsPagedResponse)>` |   
  
### listOrders(@Nullable LocationName parent)
    
    
    public final GDCHardwareManagementClient.ListOrdersPagedResponse listOrders(@Nullable LocationName parent)

Lists orders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Order element : gDCHardwareManagementClient.listOrders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to list orders in. Format: `projects/{project}/locations/{location}` To list orders across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListOrdersPagedResponse)` |   
  
### listOrders(ListOrdersRequest request)
    
    
    public final GDCHardwareManagementClient.ListOrdersPagedResponse listOrders(ListOrdersRequest request)

Lists orders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Order element : gDCHardwareManagementClient.listOrders(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListOrdersPagedResponse)` |   
  
### listOrders(String parent)
    
    
    public final GDCHardwareManagementClient.ListOrdersPagedResponse listOrders(String parent)

Lists orders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Order element : gDCHardwareManagementClient.listOrders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to list orders in. Format: `projects/{project}/locations/{location}` To list orders across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListOrdersPagedResponse)` |   
  
### listOrdersCallable()
    
    
    public final UnaryCallable<ListOrdersRequest,ListOrdersResponse> listOrdersCallable()

Lists orders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListOrdersResponse response =
             gDCHardwareManagementClient.listOrdersCallable().call(request);
         for (Order element : response.getOrdersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersRequest),[ListOrdersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersResponse)>` |   
  
### listOrdersPagedCallable()
    
    
    public final UnaryCallable<ListOrdersRequest,GDCHardwareManagementClient.ListOrdersPagedResponse> listOrdersPagedCallable()

Lists orders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListOrdersRequest request =
           ListOrdersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Order> future =
           gDCHardwareManagementClient.listOrdersPagedCallable().futureCall(request);
       // Do something.
       for (Order element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersRequest),[ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListOrdersPagedResponse)>` |   
  
### listSites(@Nullable LocationName parent)
    
    
    public final GDCHardwareManagementClient.ListSitesPagedResponse listSites(@Nullable LocationName parent)

Lists sites in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Site element : gDCHardwareManagementClient.listSites(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to list sites in. Format: `projects/{project}/locations/{location}` To list sites across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSitesPagedResponse)` |   
  
### listSites(ListSitesRequest request)
    
    
    public final GDCHardwareManagementClient.ListSitesPagedResponse listSites(ListSitesRequest request)

Lists sites in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListSitesRequest request =
           ListSitesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Site element : gDCHardwareManagementClient.listSites(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSitesPagedResponse)` |   
  
### listSites(String parent)
    
    
    public final GDCHardwareManagementClient.ListSitesPagedResponse listSites(String parent)

Lists sites in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Site element : gDCHardwareManagementClient.listSites(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to list sites in. Format: `projects/{project}/locations/{location}` To list sites across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSitesPagedResponse)` |   
  
### listSitesCallable()
    
    
    public final UnaryCallable<ListSitesRequest,ListSitesResponse> listSitesCallable()

Lists sites in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListSitesRequest request =
           ListSitesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSitesResponse response = gDCHardwareManagementClient.listSitesCallable().call(request);
         for (Site element : response.getSitesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesRequest),[ListSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesResponse)>` |   
  
### listSitesPagedCallable()
    
    
    public final UnaryCallable<ListSitesRequest,GDCHardwareManagementClient.ListSitesPagedResponse> listSitesPagedCallable()

Lists sites in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListSitesRequest request =
           ListSitesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Site> future =
           gDCHardwareManagementClient.listSitesPagedCallable().futureCall(request);
       // Do something.
       for (Site element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesRequest),[ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSitesPagedResponse)>` |   
  
### listSkus(@Nullable LocationName parent)
    
    
    public final GDCHardwareManagementClient.ListSkusPagedResponse listSkus(@Nullable LocationName parent)

Lists SKUs for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Sku element : gDCHardwareManagementClient.listSkus(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to list SKUs in. Format: `projects/{project}/locations/{location}` To list SKUs across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSkusPagedResponse)` |   
  
### listSkus(ListSkusRequest request)
    
    
    public final GDCHardwareManagementClient.ListSkusPagedResponse listSkus(ListSkusRequest request)

Lists SKUs for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Sku element : gDCHardwareManagementClient.listSkus(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSkusPagedResponse)` |   
  
### listSkus(String parent)
    
    
    public final GDCHardwareManagementClient.ListSkusPagedResponse listSkus(String parent)

Lists SKUs for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Sku element : gDCHardwareManagementClient.listSkus(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to list SKUs in. Format: `projects/{project}/locations/{location}` To list SKUs across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSkusPagedResponse)` |   
  
### listSkusCallable()
    
    
    public final UnaryCallable<ListSkusRequest,ListSkusResponse> listSkusCallable()

Lists SKUs for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSkusResponse response = gDCHardwareManagementClient.listSkusCallable().call(request);
         for (Sku element : response.getSkusList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusRequest),[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusResponse)>` |   
  
### listSkusPagedCallable()
    
    
    public final UnaryCallable<ListSkusRequest,GDCHardwareManagementClient.ListSkusPagedResponse> listSkusPagedCallable()

Lists SKUs for a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListSkusRequest request =
           ListSkusRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Sku> future =
           gDCHardwareManagementClient.listSkusPagedCallable().futureCall(request);
       // Do something.
       for (Sku element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusRequest),[ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSkusPagedResponse)>` |   
  
### listZones(@Nullable LocationName parent)
    
    
    public final GDCHardwareManagementClient.ListZonesPagedResponse listZones(@Nullable LocationName parent)

Lists zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Zone element : gDCHardwareManagementClient.listZones(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.LocationName`  
Required. The project and location to list zones in. Format: `projects/{project}/locations/{location}` To list zones across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListZonesPagedResponse)` |   
  
### listZones(ListZonesRequest request)
    
    
    public final GDCHardwareManagementClient.ListZonesPagedResponse listZones(ListZonesRequest request)

Lists zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Zone element : gDCHardwareManagementClient.listZones(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListZonesPagedResponse)` |   
  
### listZones(String parent)
    
    
    public final GDCHardwareManagementClient.ListZonesPagedResponse listZones(String parent)

Lists zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Zone element : gDCHardwareManagementClient.listZones(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to list zones in. Format: `projects/{project}/locations/{location}` To list zones across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message.  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListZonesPagedResponse)` |   
  
### listZonesCallable()
    
    
    public final UnaryCallable<ListZonesRequest,ListZonesResponse> listZonesCallable()

Lists zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListZonesResponse response = gDCHardwareManagementClient.listZonesCallable().call(request);
         for (Zone element : response.getZonesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesRequest),[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesResponse)>` |   
  
### listZonesPagedCallable()
    
    
    public final UnaryCallable<ListZonesRequest,GDCHardwareManagementClient.ListZonesPagedResponse> listZonesPagedCallable()

Lists zones in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Zone> future =
           gDCHardwareManagementClient.listZonesPagedCallable().futureCall(request);
       // Do something.
       for (Zone element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesRequest),[ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListZonesPagedResponse)>` |   
  
### recordActionOnComment(@Nullable CommentName name, RecordActionOnCommentRequest.ActionType actionType)
    
    
    public final Comment recordActionOnComment(@Nullable CommentName name, RecordActionOnCommentRequest.ActionType actionType)

Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       CommentName name = CommentName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[COMMENT]");
       RecordActionOnCommentRequest.ActionType actionType =
           RecordActionOnCommentRequest.ActionType.forNumber(0);
       Comment response = gDCHardwareManagementClient.recordActionOnComment(name, actionType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.CommentName`  
Required. The name of the comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`  
`actionType` | `[RecordActionOnCommentRequest.ActionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RecordActionOnCommentRequest.ActionType)`  
Required. The action type of the recorded action.  
**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)` |   
  
### recordActionOnComment(RecordActionOnCommentRequest request)
    
    
    public final Comment recordActionOnComment(RecordActionOnCommentRequest request)

Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       RecordActionOnCommentRequest request =
           RecordActionOnCommentRequest.newBuilder()
               .setName(CommentName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[COMMENT]").toString())
               .build();
       Comment response = gDCHardwareManagementClient.recordActionOnComment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RecordActionOnCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RecordActionOnCommentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)` |   
  
### recordActionOnComment(String name, RecordActionOnCommentRequest.ActionType actionType)
    
    
    public final Comment recordActionOnComment(String name, RecordActionOnCommentRequest.ActionType actionType)

Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = CommentName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[COMMENT]").toString();
       RecordActionOnCommentRequest.ActionType actionType =
           RecordActionOnCommentRequest.ActionType.forNumber(0);
       Comment response = gDCHardwareManagementClient.recordActionOnComment(name, actionType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`  
`actionType` | `[RecordActionOnCommentRequest.ActionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RecordActionOnCommentRequest.ActionType)`  
Required. The action type of the recorded action.  
**Returns**  
---  
**Type** | **Description**  
`[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)` |   
  
### recordActionOnCommentCallable()
    
    
    public final UnaryCallable<RecordActionOnCommentRequest,Comment> recordActionOnCommentCallable()

Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       RecordActionOnCommentRequest request =
           RecordActionOnCommentRequest.newBuilder()
               .setName(CommentName.of("[PROJECT]", "[LOCATION]", "[ORDER]", "[COMMENT]").toString())
               .build();
       ApiFuture<Comment> future =
           gDCHardwareManagementClient.recordActionOnCommentCallable().futureCall(request);
       // Do something.
       Comment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RecordActionOnCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RecordActionOnCommentRequest),[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)>` |   
  
### requestOrderDateChangeAsync(@Nullable OrderName name, Date requestedDate)
    
    
    public final OperationFuture<Order,OperationMetadata> requestOrderDateChangeAsync(@Nullable OrderName name, Date requestedDate)

Updates the requested date change of a single Order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       Date requestedDate = Date.newBuilder().build();
       Order response =
           gDCHardwareManagementClient.requestOrderDateChangeAsync(name, requestedDate).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The name of the order to update. Format: projects/{project}/locations/{location}/orders/{order}  
`requestedDate` | `com.google.type.Date`  
Required. The date to which the customer or Google wants to set the scheduled installation date.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### requestOrderDateChangeAsync(RequestOrderDateChangeRequest request)
    
    
    public final OperationFuture<Order,OperationMetadata> requestOrderDateChangeAsync(RequestOrderDateChangeRequest request)

Updates the requested date change of a single Order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       RequestOrderDateChangeRequest request =
           RequestOrderDateChangeRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestedDate(Date.newBuilder().build())
               .build();
       Order response = gDCHardwareManagementClient.requestOrderDateChangeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RequestOrderDateChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RequestOrderDateChangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### requestOrderDateChangeAsync(String name, Date requestedDate)
    
    
    public final OperationFuture<Order,OperationMetadata> requestOrderDateChangeAsync(String name, Date requestedDate)

Updates the requested date change of a single Order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       Date requestedDate = Date.newBuilder().build();
       Order response =
           gDCHardwareManagementClient.requestOrderDateChangeAsync(name, requestedDate).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the order to update. Format: projects/{project}/locations/{location}/orders/{order}  
`requestedDate` | `com.google.type.Date`  
Required. The date to which the customer or Google wants to set the scheduled installation date.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### requestOrderDateChangeCallable()
    
    
    public final UnaryCallable<RequestOrderDateChangeRequest,Operation> requestOrderDateChangeCallable()

Updates the requested date change of a single Order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       RequestOrderDateChangeRequest request =
           RequestOrderDateChangeRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestedDate(Date.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.requestOrderDateChangeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RequestOrderDateChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RequestOrderDateChangeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### requestOrderDateChangeOperationCallable()
    
    
    public final OperationCallable<RequestOrderDateChangeRequest,Order,OperationMetadata> requestOrderDateChangeOperationCallable()

Updates the requested date change of a single Order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       RequestOrderDateChangeRequest request =
           RequestOrderDateChangeRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestedDate(Date.newBuilder().build())
               .build();
       OperationFuture<Order, OperationMetadata> future =
           gDCHardwareManagementClient.requestOrderDateChangeOperationCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RequestOrderDateChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RequestOrderDateChangeRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### signalZoneStateAsync(@Nullable ZoneName name, SignalZoneStateRequest.StateSignal stateSignal)
    
    
    public final OperationFuture<Zone,OperationMetadata> signalZoneStateAsync(@Nullable ZoneName name, SignalZoneStateRequest.StateSignal stateSignal)

Signals the state of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       ZoneName name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]");
       SignalZoneStateRequest.StateSignal stateSignal =
           SignalZoneStateRequest.StateSignal.forNumber(0);
       Zone response = gDCHardwareManagementClient.signalZoneStateAsync(name, stateSignal).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.ZoneName`  
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
`stateSignal` | `[SignalZoneStateRequest.StateSignal](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest.StateSignal)`  
Optional. The state signal to send for this zone. Either state_signal or provisioning_state_signal must be set, but not both.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### signalZoneStateAsync(SignalZoneStateRequest request)
    
    
    public final OperationFuture<Zone,OperationMetadata> signalZoneStateAsync(SignalZoneStateRequest request)

Signals the state of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SignalZoneStateRequest request =
           SignalZoneStateRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRequestId("requestId693933066")
               .setStep("step3540684")
               .setDetails("details1557721666")
               .build();
       Zone response = gDCHardwareManagementClient.signalZoneStateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SignalZoneStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### signalZoneStateAsync(String name, SignalZoneStateRequest.StateSignal stateSignal)
    
    
    public final OperationFuture<Zone,OperationMetadata> signalZoneStateAsync(String name, SignalZoneStateRequest.StateSignal stateSignal)

Signals the state of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString();
       SignalZoneStateRequest.StateSignal stateSignal =
           SignalZoneStateRequest.StateSignal.forNumber(0);
       Zone response = gDCHardwareManagementClient.signalZoneStateAsync(name, stateSignal).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
`stateSignal` | `[SignalZoneStateRequest.StateSignal](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest.StateSignal)`  
Optional. The state signal to send for this zone. Either state_signal or provisioning_state_signal must be set, but not both.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### signalZoneStateCallable()
    
    
    public final UnaryCallable<SignalZoneStateRequest,Operation> signalZoneStateCallable()

Signals the state of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SignalZoneStateRequest request =
           SignalZoneStateRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRequestId("requestId693933066")
               .setStep("step3540684")
               .setDetails("details1557721666")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.signalZoneStateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SignalZoneStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### signalZoneStateOperationCallable()
    
    
    public final OperationCallable<SignalZoneStateRequest,Zone,OperationMetadata> signalZoneStateOperationCallable()

Signals the state of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SignalZoneStateRequest request =
           SignalZoneStateRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[ZONE]").toString())
               .setRequestId("requestId693933066")
               .setStep("step3540684")
               .setDetails("details1557721666")
               .build();
       OperationFuture<Zone, OperationMetadata> future =
           gDCHardwareManagementClient.signalZoneStateOperationCallable().futureCall(request);
       // Do something.
       Zone response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SignalZoneStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### submitOrderAsync(@Nullable OrderName name)
    
    
    public final OperationFuture<Order,OperationMetadata> submitOrderAsync(@Nullable OrderName name)

Submits an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       OrderName name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]");
       Order response = gDCHardwareManagementClient.submitOrderAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.gdchardwaremanagement.v1alpha.OrderName`  
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### submitOrderAsync(SubmitOrderRequest request)
    
    
    public final OperationFuture<Order,OperationMetadata> submitOrderAsync(SubmitOrderRequest request)

Submits an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SubmitOrderRequest request =
           SubmitOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       Order response = gDCHardwareManagementClient.submitOrderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SubmitOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SubmitOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### submitOrderAsync(String name)
    
    
    public final OperationFuture<Order,OperationMetadata> submitOrderAsync(String name)

Submits an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       String name = OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString();
       Order response = gDCHardwareManagementClient.submitOrderAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### submitOrderCallable()
    
    
    public final UnaryCallable<SubmitOrderRequest,Operation> submitOrderCallable()

Submits an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SubmitOrderRequest request =
           SubmitOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.submitOrderCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SubmitOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SubmitOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### submitOrderOperationCallable()
    
    
    public final OperationCallable<SubmitOrderRequest,Order,OperationMetadata> submitOrderOperationCallable()

Submits an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       SubmitOrderRequest request =
           SubmitOrderRequest.newBuilder()
               .setName(OrderName.of("[PROJECT]", "[LOCATION]", "[ORDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Order, OperationMetadata> future =
           gDCHardwareManagementClient.submitOrderOperationCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SubmitOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SubmitOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateHardwareAsync(Hardware hardware, FieldMask updateMask)
    
    
    public final OperationFuture<Hardware,OperationMetadata> updateHardwareAsync(Hardware hardware, FieldMask updateMask)

Updates hardware parameters.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       Hardware hardware = Hardware.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Hardware response =
           gDCHardwareManagementClient.updateHardwareAsync(hardware, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`hardware` | `[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)`  
Required. The hardware to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A mask to specify the fields in the Hardware to overwrite with this update. The fields specified in the update_mask are relative to the hardware, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateHardwareAsync(UpdateHardwareRequest request)
    
    
    public final OperationFuture<Hardware,OperationMetadata> updateHardwareAsync(UpdateHardwareRequest request)

Updates hardware parameters.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateHardwareRequest request =
           UpdateHardwareRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHardware(Hardware.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Hardware response = gDCHardwareManagementClient.updateHardwareAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateHardwareCallable()
    
    
    public final UnaryCallable<UpdateHardwareRequest,Operation> updateHardwareCallable()

Updates hardware parameters.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateHardwareRequest request =
           UpdateHardwareRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHardware(Hardware.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.updateHardwareCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHardwareGroupAsync(HardwareGroup hardwareGroup, FieldMask updateMask)
    
    
    public final OperationFuture<HardwareGroup,OperationMetadata> updateHardwareGroupAsync(HardwareGroup hardwareGroup, FieldMask updateMask)

Updates the parameters of a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       HardwareGroup hardwareGroup = HardwareGroup.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       HardwareGroup response =
           gDCHardwareManagementClient.updateHardwareGroupAsync(hardwareGroup, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`hardwareGroup` | `[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)`  
Required. The hardware group to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A mask to specify the fields in the HardwareGroup to overwrite with this update. The fields specified in the update_mask are relative to the hardware group, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateHardwareGroupAsync(UpdateHardwareGroupRequest request)
    
    
    public final OperationFuture<HardwareGroup,OperationMetadata> updateHardwareGroupAsync(UpdateHardwareGroupRequest request)

Updates the parameters of a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateHardwareGroupRequest request =
           UpdateHardwareGroupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHardwareGroup(HardwareGroup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       HardwareGroup response = gDCHardwareManagementClient.updateHardwareGroupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateHardwareGroupCallable()
    
    
    public final UnaryCallable<UpdateHardwareGroupRequest,Operation> updateHardwareGroupCallable()

Updates the parameters of a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateHardwareGroupRequest request =
           UpdateHardwareGroupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHardwareGroup(HardwareGroup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.updateHardwareGroupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHardwareGroupOperationCallable()
    
    
    public final OperationCallable<UpdateHardwareGroupRequest,HardwareGroup,OperationMetadata> updateHardwareGroupOperationCallable()

Updates the parameters of a hardware group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateHardwareGroupRequest request =
           UpdateHardwareGroupRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHardwareGroup(HardwareGroup.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<HardwareGroup, OperationMetadata> future =
           gDCHardwareManagementClient.updateHardwareGroupOperationCallable().futureCall(request);
       // Do something.
       HardwareGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareGroupRequest),[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateHardwareOperationCallable()
    
    
    public final OperationCallable<UpdateHardwareRequest,Hardware,OperationMetadata> updateHardwareOperationCallable()

Updates hardware parameters.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateHardwareRequest request =
           UpdateHardwareRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setHardware(Hardware.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Hardware, OperationMetadata> future =
           gDCHardwareManagementClient.updateHardwareOperationCallable().futureCall(request);
       // Do something.
       Hardware response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareRequest),[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateOrderAsync(Order order, FieldMask updateMask)
    
    
    public final OperationFuture<Order,OperationMetadata> updateOrderAsync(Order order, FieldMask updateMask)

Updates the parameters of an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       Order order = Order.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Order response = gDCHardwareManagementClient.updateOrderAsync(order, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`order` | `[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)`  
Required. The order to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A mask to specify the fields in the Order to overwrite with this update. The fields specified in the update_mask are relative to the order, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateOrderAsync(UpdateOrderRequest request)
    
    
    public final OperationFuture<Order,OperationMetadata> updateOrderAsync(UpdateOrderRequest request)

Updates the parameters of an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateOrderRequest request =
           UpdateOrderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setOrder(Order.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Order response = gDCHardwareManagementClient.updateOrderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateOrderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateOrderCallable()
    
    
    public final UnaryCallable<UpdateOrderRequest,Operation> updateOrderCallable()

Updates the parameters of an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateOrderRequest request =
           UpdateOrderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setOrder(Order.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.updateOrderCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateOrderOperationCallable()
    
    
    public final OperationCallable<UpdateOrderRequest,Order,OperationMetadata> updateOrderOperationCallable()

Updates the parameters of an order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateOrderRequest request =
           UpdateOrderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setOrder(Order.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Order, OperationMetadata> future =
           gDCHardwareManagementClient.updateOrderOperationCallable().futureCall(request);
       // Do something.
       Order response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateSiteAsync(Site site, FieldMask updateMask)
    
    
    public final OperationFuture<Site,OperationMetadata> updateSiteAsync(Site site, FieldMask updateMask)

Updates the parameters of a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       Site site = Site.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Site response = gDCHardwareManagementClient.updateSiteAsync(site, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`site` | `[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)`  
Required. The site to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A mask to specify the fields in the Site to overwrite with this update. The fields specified in the update_mask are relative to the site, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateSiteAsync(UpdateSiteRequest request)
    
    
    public final OperationFuture<Site,OperationMetadata> updateSiteAsync(UpdateSiteRequest request)

Updates the parameters of a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateSiteRequest request =
           UpdateSiteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSite(Site.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Site response = gDCHardwareManagementClient.updateSiteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateSiteCallable()
    
    
    public final UnaryCallable<UpdateSiteRequest,Operation> updateSiteCallable()

Updates the parameters of a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateSiteRequest request =
           UpdateSiteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSite(Site.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.updateSiteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSiteOperationCallable()
    
    
    public final OperationCallable<UpdateSiteRequest,Site,OperationMetadata> updateSiteOperationCallable()

Updates the parameters of a site.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateSiteRequest request =
           UpdateSiteRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSite(Site.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Site, OperationMetadata> future =
           gDCHardwareManagementClient.updateSiteOperationCallable().futureCall(request);
       // Do something.
       Site response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateZoneAsync(UpdateZoneRequest request)
    
    
    public final OperationFuture<Zone,OperationMetadata> updateZoneAsync(UpdateZoneRequest request)

Updates the parameters of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateZoneRequest request =
           UpdateZoneRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setZone(Zone.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Zone response = gDCHardwareManagementClient.updateZoneAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateZoneAsync(Zone zone, FieldMask updateMask)
    
    
    public final OperationFuture<Zone,OperationMetadata> updateZoneAsync(Zone zone, FieldMask updateMask)

Updates the parameters of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       Zone zone = Zone.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Zone response = gDCHardwareManagementClient.updateZoneAsync(zone, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`zone` | `[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)`  
Required. The zone to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A mask to specify the fields in the Zone to overwrite with this update. The fields specified in the update_mask are relative to the zone, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateZoneCallable()
    
    
    public final UnaryCallable<UpdateZoneRequest,Operation> updateZoneCallable()

Updates the parameters of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateZoneRequest request =
           UpdateZoneRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setZone(Zone.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           gDCHardwareManagementClient.updateZoneCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateZoneOperationCallable()
    
    
    public final OperationCallable<UpdateZoneRequest,Zone,OperationMetadata> updateZoneOperationCallable()

Updates the parameters of a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GDCHardwareManagementClient gDCHardwareManagementClient =
         GDCHardwareManagementClient.create()) {
       UpdateZoneRequest request =
           UpdateZoneRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setZone(Zone.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Zone, OperationMetadata> future =
           gDCHardwareManagementClient.updateZoneOperationCallable().futureCall(request);
       // Do something.
       Zone response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
