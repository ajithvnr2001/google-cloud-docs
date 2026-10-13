---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient
title: Class DeviceManagerClient (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:14.250252+00:00
---

# Class DeviceManagerClient (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DeviceManagerClient (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.6  2.2.1  2.1.7 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-iot/google-cloud-iot/src/main/java/com/google/cloud/iot/v1/DeviceManagerClient.java)| [Product Reference](https://cloud.google.com/iot)  
---|---  
  
Service Description: Internet of Things (IoT) service. Securely connect and manage IoT devices.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DeviceRegistry deviceRegistry = DeviceRegistry.newBuilder().build();
       DeviceRegistry response = deviceManagerClient.createDeviceRegistry(parent, deviceRegistry);
     }
     

Note: close() needs to be called on the DeviceManagerClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDeviceRegistry |  Creates a device registry that contains devices. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDeviceRegistry(CreateDeviceRegistryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDeviceRegistry(LocationName parent, DeviceRegistry deviceRegistry) 
  * createDeviceRegistry(String parent, DeviceRegistry deviceRegistry) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDeviceRegistryCallable() 

  
GetDeviceRegistry |  Gets a device registry configuration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDeviceRegistry(GetDeviceRegistryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDeviceRegistry(RegistryName name) 
  * getDeviceRegistry(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDeviceRegistryCallable() 

  
UpdateDeviceRegistry |  Updates a device registry configuration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDeviceRegistry(UpdateDeviceRegistryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDeviceRegistry(DeviceRegistry deviceRegistry, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDeviceRegistryCallable() 

  
DeleteDeviceRegistry |  Deletes a device registry configuration. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDeviceRegistry(DeleteDeviceRegistryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDeviceRegistry(RegistryName name) 
  * deleteDeviceRegistry(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDeviceRegistryCallable() 

  
ListDeviceRegistries |  Lists device registries. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDeviceRegistries(ListDeviceRegistriesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDeviceRegistries(LocationName parent) 
  * listDeviceRegistries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDeviceRegistriesPagedCallable() 
  * listDeviceRegistriesCallable() 

  
CreateDevice |  Creates a device in a device registry. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDevice(CreateDeviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDevice(RegistryName parent, Device device) 
  * createDevice(String parent, Device device) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDeviceCallable() 

  
GetDevice |  Gets details about a device. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDevice(GetDeviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDevice(DeviceName name) 
  * getDevice(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDeviceCallable() 

  
UpdateDevice |  Updates a device. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDevice(UpdateDeviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDevice(Device device, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDeviceCallable() 

  
DeleteDevice |  Deletes a device. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDevice(DeleteDeviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDevice(DeviceName name) 
  * deleteDevice(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDeviceCallable() 

  
ListDevices |  List devices in a device registry. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDevices(ListDevicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDevices(RegistryName parent) 
  * listDevices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDevicesPagedCallable() 
  * listDevicesCallable() 

  
ModifyCloudToDeviceConfig |  Modifies the configuration for the device, which is eventually sent from the Cloud IoT Core servers. Returns the modified configuration version and its metadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * modifyCloudToDeviceConfig(ModifyCloudToDeviceConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * modifyCloudToDeviceConfig(DeviceName name, ByteString binaryData) 
  * modifyCloudToDeviceConfig(String name, ByteString binaryData) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * modifyCloudToDeviceConfigCallable() 

  
ListDeviceConfigVersions |  Lists the last few versions of the device configuration in descending order (i.e.: newest first). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDeviceConfigVersions(ListDeviceConfigVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDeviceConfigVersions(DeviceName name) 
  * listDeviceConfigVersions(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDeviceConfigVersionsCallable() 

  
ListDeviceStates |  Lists the last few versions of the device state in descending order (i.e.: newest first). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDeviceStates(ListDeviceStatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDeviceStates(DeviceName name) 
  * listDeviceStates(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDeviceStatesCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(ResourceName resource, Policy policy) 
  * setIamPolicy(String resource, Policy policy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(ResourceName resource) 
  * getIamPolicy(String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(ResourceName resource, List<String> permissions) 
  * testIamPermissions(String resource, List<String> permissions) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
SendCommandToDevice |  Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * sendCommandToDevice(SendCommandToDeviceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * sendCommandToDevice(DeviceName name, ByteString binaryData) 
  * sendCommandToDevice(String name, ByteString binaryData) 
  * sendCommandToDevice(DeviceName name, ByteString binaryData, String subfolder) 
  * sendCommandToDevice(String name, ByteString binaryData, String subfolder) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * sendCommandToDeviceCallable() 

  
BindDeviceToGateway |  Associates the device with the gateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * bindDeviceToGateway(BindDeviceToGatewayRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * bindDeviceToGateway(RegistryName parent, String gatewayId, String deviceId) 
  * bindDeviceToGateway(String parent, String gatewayId, String deviceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * bindDeviceToGatewayCallable() 

  
UnbindDeviceFromGateway |  Deletes the association between the device and the gateway. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * unbindDeviceFromGateway(UnbindDeviceFromGatewayRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * unbindDeviceFromGateway(RegistryName parent, String gatewayId, String deviceId) 
  * unbindDeviceFromGateway(String parent, String gatewayId, String deviceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * unbindDeviceFromGatewayCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DeviceManagerSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeviceManagerSettings deviceManagerSettings =
         DeviceManagerSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DeviceManagerClient deviceManagerClient = DeviceManagerClient.create(deviceManagerSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeviceManagerSettings deviceManagerSettings =
         DeviceManagerSettings.newBuilder().setEndpoint(myEndpoint).build();
     DeviceManagerClient deviceManagerClient = DeviceManagerClient.create(deviceManagerSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeviceManagerSettings deviceManagerSettings =
         DeviceManagerSettings.newHttpJsonBuilder().build();
     DeviceManagerClient deviceManagerClient = DeviceManagerClient.create(deviceManagerSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DeviceManagerClient

## Static Methods 

### create()
    
    
    public static final DeviceManagerClient create()

Constructs an instance of DeviceManagerClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeviceManagerSettings settings)
    
    
    public static final DeviceManagerClient create(DeviceManagerSettings settings)

Constructs an instance of DeviceManagerClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeviceManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeviceManagerStub stub)
    
    
    public static final DeviceManagerClient create(DeviceManagerStub stub)

Constructs an instance of DeviceManagerClient, using the given stub for making calls. This is for advanced usage - prefer using create(DeviceManagerSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeviceManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.stub.DeviceManagerStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient)` |   
  
## Constructors 

### DeviceManagerClient(DeviceManagerSettings settings)
    
    
    protected DeviceManagerClient(DeviceManagerSettings settings)

Constructs an instance of DeviceManagerClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeviceManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerSettings)`  
  
  
### DeviceManagerClient(DeviceManagerStub stub)
    
    
    protected DeviceManagerClient(DeviceManagerStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeviceManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.stub.DeviceManagerStub)`  
  
  
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
  
### bindDeviceToGateway(@Nullable RegistryName parent, String gatewayId, String deviceId)
    
    
    public final BindDeviceToGatewayResponse bindDeviceToGateway(@Nullable RegistryName parent, String gatewayId, String deviceId)

Associates the device with the gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       RegistryName parent = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       String gatewayId = "gatewayId-1354641793";
       String deviceId = "deviceId1109191185";
       BindDeviceToGatewayResponse response =
           deviceManagerClient.bindDeviceToGateway(parent, gatewayId, deviceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.RegistryName`  
Required. The name of the registry. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
`gatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value of `gateway_id` can be either the device numeric ID or the user-defined device identifier.  
`deviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The device to associate with the specified gateway. The value of `device_id` can be either the device numeric ID or the user-defined device identifier.  
**Returns**  
---  
**Type** | **Description**  
`[BindDeviceToGatewayResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.BindDeviceToGatewayResponse)` |   
  
### bindDeviceToGateway(BindDeviceToGatewayRequest request)
    
    
    public final BindDeviceToGatewayResponse bindDeviceToGateway(BindDeviceToGatewayRequest request)

Associates the device with the gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       BindDeviceToGatewayRequest request =
           BindDeviceToGatewayRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setGatewayId("gatewayId-1354641793")
               .setDeviceId("deviceId1109191185")
               .build();
       BindDeviceToGatewayResponse response = deviceManagerClient.bindDeviceToGateway(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BindDeviceToGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.BindDeviceToGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BindDeviceToGatewayResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.BindDeviceToGatewayResponse)` |   
  
### bindDeviceToGateway(String parent, String gatewayId, String deviceId)
    
    
    public final BindDeviceToGatewayResponse bindDeviceToGateway(String parent, String gatewayId, String deviceId)

Associates the device with the gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String parent = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString();
       String gatewayId = "gatewayId-1354641793";
       String deviceId = "deviceId1109191185";
       BindDeviceToGatewayResponse response =
           deviceManagerClient.bindDeviceToGateway(parent, gatewayId, deviceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the registry. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
`gatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value of `gateway_id` can be either the device numeric ID or the user-defined device identifier.  
`deviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The device to associate with the specified gateway. The value of `device_id` can be either the device numeric ID or the user-defined device identifier.  
**Returns**  
---  
**Type** | **Description**  
`[BindDeviceToGatewayResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.BindDeviceToGatewayResponse)` |   
  
### bindDeviceToGatewayCallable()
    
    
    public final UnaryCallable<BindDeviceToGatewayRequest,BindDeviceToGatewayResponse> bindDeviceToGatewayCallable()

Associates the device with the gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       BindDeviceToGatewayRequest request =
           BindDeviceToGatewayRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setGatewayId("gatewayId-1354641793")
               .setDeviceId("deviceId1109191185")
               .build();
       ApiFuture<BindDeviceToGatewayResponse> future =
           deviceManagerClient.bindDeviceToGatewayCallable().futureCall(request);
       // Do something.
       BindDeviceToGatewayResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BindDeviceToGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.BindDeviceToGatewayRequest),[BindDeviceToGatewayResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.BindDeviceToGatewayResponse)>` |   
  
### close()
    
    
    public final void close()

### createDevice(@Nullable RegistryName parent, Device device)
    
    
    public final Device createDevice(@Nullable RegistryName parent, Device device)

Creates a device in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       RegistryName parent = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       Device device = Device.newBuilder().build();
       Device response = deviceManagerClient.createDevice(parent, device);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.RegistryName`  
Required. The name of the device registry where this device should be created. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
`device` | `[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)`  
Required. The device registration details. The field `name` must be empty. The server generates `name` from the device registry `id` and the `parent` field.  
**Returns**  
---  
**Type** | **Description**  
`[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)` |   
  
### createDevice(CreateDeviceRequest request)
    
    
    public final Device createDevice(CreateDeviceRequest request)

Creates a device in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       CreateDeviceRequest request =
           CreateDeviceRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setDevice(Device.newBuilder().build())
               .build();
       Device response = deviceManagerClient.createDevice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.CreateDeviceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)` |   
  
### createDevice(String parent, Device device)
    
    
    public final Device createDevice(String parent, Device device)

Creates a device in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String parent = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString();
       Device device = Device.newBuilder().build();
       Device response = deviceManagerClient.createDevice(parent, device);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device registry where this device should be created. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
`device` | `[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)`  
Required. The device registration details. The field `name` must be empty. The server generates `name` from the device registry `id` and the `parent` field.  
**Returns**  
---  
**Type** | **Description**  
`[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)` |   
  
### createDeviceCallable()
    
    
    public final UnaryCallable<CreateDeviceRequest,Device> createDeviceCallable()

Creates a device in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       CreateDeviceRequest request =
           CreateDeviceRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setDevice(Device.newBuilder().build())
               .build();
       ApiFuture<Device> future = deviceManagerClient.createDeviceCallable().futureCall(request);
       // Do something.
       Device response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.CreateDeviceRequest),[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)>` |   
  
### createDeviceRegistry(@Nullable LocationName parent, DeviceRegistry deviceRegistry)
    
    
    public final DeviceRegistry createDeviceRegistry(@Nullable LocationName parent, DeviceRegistry deviceRegistry)

Creates a device registry that contains devices.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DeviceRegistry deviceRegistry = DeviceRegistry.newBuilder().build();
       DeviceRegistry response = deviceManagerClient.createDeviceRegistry(parent, deviceRegistry);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.LocationName`  
Required. The project and cloud region where this device registry must be created. For example, `projects/example-project/locations/us-central1`.  
`deviceRegistry` | `[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)`  
Required. The device registry. The field `name` must be empty. The server will generate that field from the device registry `id` provided and the `parent` field.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)` |   
  
### createDeviceRegistry(CreateDeviceRegistryRequest request)
    
    
    public final DeviceRegistry createDeviceRegistry(CreateDeviceRegistryRequest request)

Creates a device registry that contains devices.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       CreateDeviceRegistryRequest request =
           CreateDeviceRegistryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDeviceRegistry(DeviceRegistry.newBuilder().build())
               .build();
       DeviceRegistry response = deviceManagerClient.createDeviceRegistry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDeviceRegistryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.CreateDeviceRegistryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)` |   
  
### createDeviceRegistry(String parent, DeviceRegistry deviceRegistry)
    
    
    public final DeviceRegistry createDeviceRegistry(String parent, DeviceRegistry deviceRegistry)

Creates a device registry that contains devices.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DeviceRegistry deviceRegistry = DeviceRegistry.newBuilder().build();
       DeviceRegistry response = deviceManagerClient.createDeviceRegistry(parent, deviceRegistry);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and cloud region where this device registry must be created. For example, `projects/example-project/locations/us-central1`.  
`deviceRegistry` | `[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)`  
Required. The device registry. The field `name` must be empty. The server will generate that field from the device registry `id` provided and the `parent` field.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)` |   
  
### createDeviceRegistryCallable()
    
    
    public final UnaryCallable<CreateDeviceRegistryRequest,DeviceRegistry> createDeviceRegistryCallable()

Creates a device registry that contains devices.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       CreateDeviceRegistryRequest request =
           CreateDeviceRegistryRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDeviceRegistry(DeviceRegistry.newBuilder().build())
               .build();
       ApiFuture<DeviceRegistry> future =
           deviceManagerClient.createDeviceRegistryCallable().futureCall(request);
       // Do something.
       DeviceRegistry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDeviceRegistryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.CreateDeviceRegistryRequest),[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)>` |   
  
### deleteDevice(@Nullable DeviceName name)
    
    
    public final void deleteDevice(@Nullable DeviceName name)

Deletes a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeviceName name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]");
       deviceManagerClient.deleteDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.DeviceName`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
  
### deleteDevice(DeleteDeviceRequest request)
    
    
    public final void deleteDevice(DeleteDeviceRequest request)

Deletes a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeleteDeviceRequest request =
           DeleteDeviceRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .build();
       deviceManagerClient.deleteDevice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeleteDeviceRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDevice(String name)
    
    
    public final void deleteDevice(String name)

Deletes a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       deviceManagerClient.deleteDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
  
### deleteDeviceCallable()
    
    
    public final UnaryCallable<DeleteDeviceRequest,Empty> deleteDeviceCallable()

Deletes a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeleteDeviceRequest request =
           DeleteDeviceRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .build();
       ApiFuture<Empty> future = deviceManagerClient.deleteDeviceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeleteDeviceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteDeviceRegistry(@Nullable RegistryName name)
    
    
    public final void deleteDeviceRegistry(@Nullable RegistryName name)

Deletes a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       RegistryName name = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       deviceManagerClient.deleteDeviceRegistry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.RegistryName`  
Required. The name of the device registry. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
  
### deleteDeviceRegistry(DeleteDeviceRegistryRequest request)
    
    
    public final void deleteDeviceRegistry(DeleteDeviceRegistryRequest request)

Deletes a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeleteDeviceRegistryRequest request =
           DeleteDeviceRegistryRequest.newBuilder()
               .setName(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .build();
       deviceManagerClient.deleteDeviceRegistry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDeviceRegistryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeleteDeviceRegistryRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDeviceRegistry(String name)
    
    
    public final void deleteDeviceRegistry(String name)

Deletes a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString();
       deviceManagerClient.deleteDeviceRegistry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device registry. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
  
### deleteDeviceRegistryCallable()
    
    
    public final UnaryCallable<DeleteDeviceRegistryRequest,Empty> deleteDeviceRegistryCallable()

Deletes a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeleteDeviceRegistryRequest request =
           DeleteDeviceRegistryRequest.newBuilder()
               .setName(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .build();
       ApiFuture<Empty> future =
           deviceManagerClient.deleteDeviceRegistryCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDeviceRegistryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeleteDeviceRegistryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDevice(@Nullable DeviceName name)
    
    
    public final Device getDevice(@Nullable DeviceName name)

Gets details about a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeviceName name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]");
       Device response = deviceManagerClient.getDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.DeviceName`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)` |   
  
### getDevice(GetDeviceRequest request)
    
    
    public final Device getDevice(GetDeviceRequest request)

Gets details about a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       GetDeviceRequest request =
           GetDeviceRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setFieldMask(FieldMask.newBuilder().build())
               .build();
       Device response = deviceManagerClient.getDevice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.GetDeviceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)` |   
  
### getDevice(String name)
    
    
    public final Device getDevice(String name)

Gets details about a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       Device response = deviceManagerClient.getDevice(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)` |   
  
### getDeviceCallable()
    
    
    public final UnaryCallable<GetDeviceRequest,Device> getDeviceCallable()

Gets details about a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       GetDeviceRequest request =
           GetDeviceRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setFieldMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Device> future = deviceManagerClient.getDeviceCallable().futureCall(request);
       // Do something.
       Device response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.GetDeviceRequest),[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)>` |   
  
### getDeviceRegistry(@Nullable RegistryName name)
    
    
    public final DeviceRegistry getDeviceRegistry(@Nullable RegistryName name)

Gets a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       RegistryName name = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       DeviceRegistry response = deviceManagerClient.getDeviceRegistry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.RegistryName`  
Required. The name of the device registry. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)` |   
  
### getDeviceRegistry(GetDeviceRegistryRequest request)
    
    
    public final DeviceRegistry getDeviceRegistry(GetDeviceRegistryRequest request)

Gets a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       GetDeviceRegistryRequest request =
           GetDeviceRegistryRequest.newBuilder()
               .setName(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .build();
       DeviceRegistry response = deviceManagerClient.getDeviceRegistry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDeviceRegistryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.GetDeviceRegistryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)` |   
  
### getDeviceRegistry(String name)
    
    
    public final DeviceRegistry getDeviceRegistry(String name)

Gets a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString();
       DeviceRegistry response = deviceManagerClient.getDeviceRegistry(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device registry. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)` |   
  
### getDeviceRegistryCallable()
    
    
    public final UnaryCallable<GetDeviceRegistryRequest,DeviceRegistry> getDeviceRegistryCallable()

Gets a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       GetDeviceRegistryRequest request =
           GetDeviceRegistryRequest.newBuilder()
               .setName(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .build();
       ApiFuture<DeviceRegistry> future =
           deviceManagerClient.getDeviceRegistryCallable().futureCall(request);
       // Do something.
       DeviceRegistry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDeviceRegistryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.GetDeviceRegistryRequest),[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)>` |   
  
### getIamPolicy(@Nullable ResourceName resource)
    
    
    public final Policy getIamPolicy(@Nullable ResourceName resource)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ResourceName resource = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       Policy response = deviceManagerClient.getIamPolicy(resource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = deviceManagerClient.getIamPolicy(request);
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
  
### getIamPolicy(String resource)
    
    
    public final Policy getIamPolicy(String resource)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String resource =
           DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       Policy response = deviceManagerClient.getIamPolicy(resource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = deviceManagerClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getSettings()
    
    
    public final @Nullable DeviceManagerSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.DeviceManagerSettings` |   
  
### getStub()
    
    
    public DeviceManagerStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.stub.DeviceManagerStub)` |   
  
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
  
### listDeviceConfigVersions(@Nullable DeviceName name)
    
    
    public final ListDeviceConfigVersionsResponse listDeviceConfigVersions(@Nullable DeviceName name)

Lists the last few versions of the device configuration in descending order (i.e.: newest first).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeviceName name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]");
       ListDeviceConfigVersionsResponse response =
           deviceManagerClient.listDeviceConfigVersions(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.DeviceName`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeviceConfigVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceConfigVersionsResponse)` |   
  
### listDeviceConfigVersions(ListDeviceConfigVersionsRequest request)
    
    
    public final ListDeviceConfigVersionsResponse listDeviceConfigVersions(ListDeviceConfigVersionsRequest request)

Lists the last few versions of the device configuration in descending order (i.e.: newest first).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDeviceConfigVersionsRequest request =
           ListDeviceConfigVersionsRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setNumVersions(-315385036)
               .build();
       ListDeviceConfigVersionsResponse response =
           deviceManagerClient.listDeviceConfigVersions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDeviceConfigVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceConfigVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeviceConfigVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceConfigVersionsResponse)` |   
  
### listDeviceConfigVersions(String name)
    
    
    public final ListDeviceConfigVersionsResponse listDeviceConfigVersions(String name)

Lists the last few versions of the device configuration in descending order (i.e.: newest first).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       ListDeviceConfigVersionsResponse response =
           deviceManagerClient.listDeviceConfigVersions(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeviceConfigVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceConfigVersionsResponse)` |   
  
### listDeviceConfigVersionsCallable()
    
    
    public final UnaryCallable<ListDeviceConfigVersionsRequest,ListDeviceConfigVersionsResponse> listDeviceConfigVersionsCallable()

Lists the last few versions of the device configuration in descending order (i.e.: newest first).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDeviceConfigVersionsRequest request =
           ListDeviceConfigVersionsRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setNumVersions(-315385036)
               .build();
       ApiFuture<ListDeviceConfigVersionsResponse> future =
           deviceManagerClient.listDeviceConfigVersionsCallable().futureCall(request);
       // Do something.
       ListDeviceConfigVersionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeviceConfigVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceConfigVersionsRequest),[ListDeviceConfigVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceConfigVersionsResponse)>` |   
  
### listDeviceRegistries(@Nullable LocationName parent)
    
    
    public final DeviceManagerClient.ListDeviceRegistriesPagedResponse listDeviceRegistries(@Nullable LocationName parent)

Lists device registries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DeviceRegistry element : deviceManagerClient.listDeviceRegistries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.LocationName`  
Required. The project and cloud region path. For example, `projects/example-project/locations/us-central1`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient.ListDeviceRegistriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient.ListDeviceRegistriesPagedResponse)` |   
  
### listDeviceRegistries(ListDeviceRegistriesRequest request)
    
    
    public final DeviceManagerClient.ListDeviceRegistriesPagedResponse listDeviceRegistries(ListDeviceRegistriesRequest request)

Lists device registries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDeviceRegistriesRequest request =
           ListDeviceRegistriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DeviceRegistry element :
           deviceManagerClient.listDeviceRegistries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDeviceRegistriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceRegistriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient.ListDeviceRegistriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient.ListDeviceRegistriesPagedResponse)` |   
  
### listDeviceRegistries(String parent)
    
    
    public final DeviceManagerClient.ListDeviceRegistriesPagedResponse listDeviceRegistries(String parent)

Lists device registries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DeviceRegistry element : deviceManagerClient.listDeviceRegistries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and cloud region path. For example, `projects/example-project/locations/us-central1`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient.ListDeviceRegistriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient.ListDeviceRegistriesPagedResponse)` |   
  
### listDeviceRegistriesCallable()
    
    
    public final UnaryCallable<ListDeviceRegistriesRequest,ListDeviceRegistriesResponse> listDeviceRegistriesCallable()

Lists device registries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDeviceRegistriesRequest request =
           ListDeviceRegistriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDeviceRegistriesResponse response =
             deviceManagerClient.listDeviceRegistriesCallable().call(request);
         for (DeviceRegistry element : response.getDeviceRegistriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeviceRegistriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceRegistriesRequest),[ListDeviceRegistriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceRegistriesResponse)>` |   
  
### listDeviceRegistriesPagedCallable()
    
    
    public final UnaryCallable<ListDeviceRegistriesRequest,DeviceManagerClient.ListDeviceRegistriesPagedResponse> listDeviceRegistriesPagedCallable()

Lists device registries.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDeviceRegistriesRequest request =
           ListDeviceRegistriesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DeviceRegistry> future =
           deviceManagerClient.listDeviceRegistriesPagedCallable().futureCall(request);
       // Do something.
       for (DeviceRegistry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeviceRegistriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceRegistriesRequest),[ListDeviceRegistriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient.ListDeviceRegistriesPagedResponse)>` |   
  
### listDeviceStates(@Nullable DeviceName name)
    
    
    public final ListDeviceStatesResponse listDeviceStates(@Nullable DeviceName name)

Lists the last few versions of the device state in descending order (i.e.: newest first).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeviceName name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]");
       ListDeviceStatesResponse response = deviceManagerClient.listDeviceStates(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.DeviceName`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeviceStatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceStatesResponse)` |   
  
### listDeviceStates(ListDeviceStatesRequest request)
    
    
    public final ListDeviceStatesResponse listDeviceStates(ListDeviceStatesRequest request)

Lists the last few versions of the device state in descending order (i.e.: newest first).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDeviceStatesRequest request =
           ListDeviceStatesRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setNumStates(1643330779)
               .build();
       ListDeviceStatesResponse response = deviceManagerClient.listDeviceStates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDeviceStatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceStatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeviceStatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceStatesResponse)` |   
  
### listDeviceStates(String name)
    
    
    public final ListDeviceStatesResponse listDeviceStates(String name)

Lists the last few versions of the device state in descending order (i.e.: newest first).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       ListDeviceStatesResponse response = deviceManagerClient.listDeviceStates(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeviceStatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceStatesResponse)` |   
  
### listDeviceStatesCallable()
    
    
    public final UnaryCallable<ListDeviceStatesRequest,ListDeviceStatesResponse> listDeviceStatesCallable()

Lists the last few versions of the device state in descending order (i.e.: newest first).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDeviceStatesRequest request =
           ListDeviceStatesRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setNumStates(1643330779)
               .build();
       ApiFuture<ListDeviceStatesResponse> future =
           deviceManagerClient.listDeviceStatesCallable().futureCall(request);
       // Do something.
       ListDeviceStatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeviceStatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceStatesRequest),[ListDeviceStatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDeviceStatesResponse)>` |   
  
### listDevices(@Nullable RegistryName parent)
    
    
    public final DeviceManagerClient.ListDevicesPagedResponse listDevices(@Nullable RegistryName parent)

List devices in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       RegistryName parent = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       for (Device element : deviceManagerClient.listDevices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.RegistryName`  
Required. The device registry path. Required. For example, `projects/my-project/locations/us-central1/registries/my-registry`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient.ListDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient.ListDevicesPagedResponse)` |   
  
### listDevices(ListDevicesRequest request)
    
    
    public final DeviceManagerClient.ListDevicesPagedResponse listDevices(ListDevicesRequest request)

List devices in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDevicesRequest request =
           ListDevicesRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .addAllDeviceNumIds(new ArrayList<Long>())
               .addAllDeviceIds(new ArrayList<String>())
               .setFieldMask(FieldMask.newBuilder().build())
               .setGatewayListOptions(GatewayListOptions.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Device element : deviceManagerClient.listDevices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDevicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDevicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient.ListDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient.ListDevicesPagedResponse)` |   
  
### listDevices(String parent)
    
    
    public final DeviceManagerClient.ListDevicesPagedResponse listDevices(String parent)

List devices in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String parent = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString();
       for (Device element : deviceManagerClient.listDevices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The device registry path. Required. For example, `projects/my-project/locations/us-central1/registries/my-registry`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceManagerClient.ListDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient.ListDevicesPagedResponse)` |   
  
### listDevicesCallable()
    
    
    public final UnaryCallable<ListDevicesRequest,ListDevicesResponse> listDevicesCallable()

List devices in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDevicesRequest request =
           ListDevicesRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .addAllDeviceNumIds(new ArrayList<Long>())
               .addAllDeviceIds(new ArrayList<String>())
               .setFieldMask(FieldMask.newBuilder().build())
               .setGatewayListOptions(GatewayListOptions.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDevicesResponse response = deviceManagerClient.listDevicesCallable().call(request);
         for (Device element : response.getDevicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDevicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDevicesRequest),[ListDevicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDevicesResponse)>` |   
  
### listDevicesPagedCallable()
    
    
    public final UnaryCallable<ListDevicesRequest,DeviceManagerClient.ListDevicesPagedResponse> listDevicesPagedCallable()

List devices in a device registry.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ListDevicesRequest request =
           ListDevicesRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .addAllDeviceNumIds(new ArrayList<Long>())
               .addAllDeviceIds(new ArrayList<String>())
               .setFieldMask(FieldMask.newBuilder().build())
               .setGatewayListOptions(GatewayListOptions.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Device> future = deviceManagerClient.listDevicesPagedCallable().futureCall(request);
       // Do something.
       for (Device element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDevicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ListDevicesRequest),[ListDevicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceManagerClient.ListDevicesPagedResponse)>` |   
  
### modifyCloudToDeviceConfig(@Nullable DeviceName name, ByteString binaryData)
    
    
    public final DeviceConfig modifyCloudToDeviceConfig(@Nullable DeviceName name, ByteString binaryData)

Modifies the configuration for the device, which is eventually sent from the Cloud IoT Core servers. Returns the modified configuration version and its metadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeviceName name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]");
       ByteString binaryData = ByteString.EMPTY;
       DeviceConfig response = deviceManagerClient.modifyCloudToDeviceConfig(name, binaryData);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.DeviceName`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
`binaryData` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
Required. The configuration data for the device.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceConfig)` |   
  
### modifyCloudToDeviceConfig(ModifyCloudToDeviceConfigRequest request)
    
    
    public final DeviceConfig modifyCloudToDeviceConfig(ModifyCloudToDeviceConfigRequest request)

Modifies the configuration for the device, which is eventually sent from the Cloud IoT Core servers. Returns the modified configuration version and its metadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ModifyCloudToDeviceConfigRequest request =
           ModifyCloudToDeviceConfigRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setVersionToUpdate(462348390)
               .setBinaryData(ByteString.EMPTY)
               .build();
       DeviceConfig response = deviceManagerClient.modifyCloudToDeviceConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ModifyCloudToDeviceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ModifyCloudToDeviceConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceConfig)` |   
  
### modifyCloudToDeviceConfig(String name, ByteString binaryData)
    
    
    public final DeviceConfig modifyCloudToDeviceConfig(String name, ByteString binaryData)

Modifies the configuration for the device, which is eventually sent from the Cloud IoT Core servers. Returns the modified configuration version and its metadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       ByteString binaryData = ByteString.EMPTY;
       DeviceConfig response = deviceManagerClient.modifyCloudToDeviceConfig(name, binaryData);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
`binaryData` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
Required. The configuration data for the device.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceConfig)` |   
  
### modifyCloudToDeviceConfigCallable()
    
    
    public final UnaryCallable<ModifyCloudToDeviceConfigRequest,DeviceConfig> modifyCloudToDeviceConfigCallable()

Modifies the configuration for the device, which is eventually sent from the Cloud IoT Core servers. Returns the modified configuration version and its metadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ModifyCloudToDeviceConfigRequest request =
           ModifyCloudToDeviceConfigRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setVersionToUpdate(462348390)
               .setBinaryData(ByteString.EMPTY)
               .build();
       ApiFuture<DeviceConfig> future =
           deviceManagerClient.modifyCloudToDeviceConfigCallable().futureCall(request);
       // Do something.
       DeviceConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ModifyCloudToDeviceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.ModifyCloudToDeviceConfigRequest),[DeviceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceConfig)>` |   
  
### sendCommandToDevice(@Nullable DeviceName name, ByteString binaryData)
    
    
    public final SendCommandToDeviceResponse sendCommandToDevice(@Nullable DeviceName name, ByteString binaryData)

Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeviceName name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]");
       ByteString binaryData = ByteString.EMPTY;
       SendCommandToDeviceResponse response =
           deviceManagerClient.sendCommandToDevice(name, binaryData);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.DeviceName`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
`binaryData` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
Required. The command data to send to the device.  
**Returns**  
---  
**Type** | **Description**  
`[SendCommandToDeviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.SendCommandToDeviceResponse)` |   
  
### sendCommandToDevice(@Nullable DeviceName name, ByteString binaryData, String subfolder)
    
    
    public final SendCommandToDeviceResponse sendCommandToDevice(@Nullable DeviceName name, ByteString binaryData, String subfolder)

Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeviceName name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]");
       ByteString binaryData = ByteString.EMPTY;
       String subfolder = "subfolder153561774";
       SendCommandToDeviceResponse response =
           deviceManagerClient.sendCommandToDevice(name, binaryData, subfolder);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.DeviceName`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
`binaryData` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
Required. The command data to send to the device.  
`subfolder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional subfolder for the command. If empty, the command will be delivered to the /devices/{device-id}/commands topic, otherwise it will be delivered to the /devices/{device-id}/commands/{subfolder} topic. Multi-level subfolders are allowed. This field must not have more than 256 characters, and must not contain any MQTT wildcards ("+" or "#") or null characters.  
**Returns**  
---  
**Type** | **Description**  
`[SendCommandToDeviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.SendCommandToDeviceResponse)` |   
  
### sendCommandToDevice(SendCommandToDeviceRequest request)
    
    
    public final SendCommandToDeviceResponse sendCommandToDevice(SendCommandToDeviceRequest request)

Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       SendCommandToDeviceRequest request =
           SendCommandToDeviceRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setBinaryData(ByteString.EMPTY)
               .setSubfolder("subfolder153561774")
               .build();
       SendCommandToDeviceResponse response = deviceManagerClient.sendCommandToDevice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SendCommandToDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.SendCommandToDeviceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SendCommandToDeviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.SendCommandToDeviceResponse)` |   
  
### sendCommandToDevice(String name, ByteString binaryData)
    
    
    public final SendCommandToDeviceResponse sendCommandToDevice(String name, ByteString binaryData)

Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       ByteString binaryData = ByteString.EMPTY;
       SendCommandToDeviceResponse response =
           deviceManagerClient.sendCommandToDevice(name, binaryData);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
`binaryData` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
Required. The command data to send to the device.  
**Returns**  
---  
**Type** | **Description**  
`[SendCommandToDeviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.SendCommandToDeviceResponse)` |   
  
### sendCommandToDevice(String name, ByteString binaryData, String subfolder)
    
    
    public final SendCommandToDeviceResponse sendCommandToDevice(String name, ByteString binaryData, String subfolder)

Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String name = DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       ByteString binaryData = ByteString.EMPTY;
       String subfolder = "subfolder153561774";
       SendCommandToDeviceResponse response =
           deviceManagerClient.sendCommandToDevice(name, binaryData, subfolder);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the device. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0` or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
`binaryData` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
Required. The command data to send to the device.  
`subfolder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional subfolder for the command. If empty, the command will be delivered to the /devices/{device-id}/commands topic, otherwise it will be delivered to the /devices/{device-id}/commands/{subfolder} topic. Multi-level subfolders are allowed. This field must not have more than 256 characters, and must not contain any MQTT wildcards ("+" or "#") or null characters.  
**Returns**  
---  
**Type** | **Description**  
`[SendCommandToDeviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.SendCommandToDeviceResponse)` |   
  
### sendCommandToDeviceCallable()
    
    
    public final UnaryCallable<SendCommandToDeviceRequest,SendCommandToDeviceResponse> sendCommandToDeviceCallable()

Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       SendCommandToDeviceRequest request =
           SendCommandToDeviceRequest.newBuilder()
               .setName(
                   DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString())
               .setBinaryData(ByteString.EMPTY)
               .setSubfolder("subfolder153561774")
               .build();
       ApiFuture<SendCommandToDeviceResponse> future =
           deviceManagerClient.sendCommandToDeviceCallable().futureCall(request);
       // Do something.
       SendCommandToDeviceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SendCommandToDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.SendCommandToDeviceRequest),[SendCommandToDeviceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.SendCommandToDeviceResponse)>` |   
  
### setIamPolicy(@Nullable ResourceName resource, Policy policy)
    
    
    public final Policy setIamPolicy(@Nullable ResourceName resource, Policy policy)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ResourceName resource = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       Policy policy = Policy.newBuilder().build();
       Policy response = deviceManagerClient.setIamPolicy(resource, policy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `com.google.iam.v1.Policy`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = deviceManagerClient.setIamPolicy(request);
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
  
### setIamPolicy(String resource, Policy policy)
    
    
    public final Policy setIamPolicy(String resource, Policy policy)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String resource =
           DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       Policy policy = Policy.newBuilder().build();
       Policy response = deviceManagerClient.setIamPolicy(resource, policy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.  
`policy` | `com.google.iam.v1.Policy`  
REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = deviceManagerClient.setIamPolicyCallable().futureCall(request);
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

### testIamPermissions(@Nullable ResourceName resource, List<String> permissions)
    
    
    public final TestIamPermissionsResponse testIamPermissions(@Nullable ResourceName resource, List<String> permissions)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       ResourceName resource = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       List<String> permissions = new ArrayList<>();
       TestIamPermissionsResponse response =
           deviceManagerClient.testIamPermissions(resource, permissions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '*' or 'storage.*') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = deviceManagerClient.testIamPermissions(request);
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
  
### testIamPermissions(String resource, List<String> permissions)
    
    
    public final TestIamPermissionsResponse testIamPermissions(String resource, List<String> permissions)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String resource =
           DeviceName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]", "[DEVICE]").toString();
       List<String> permissions = new ArrayList<>();
       TestIamPermissionsResponse response =
           deviceManagerClient.testIamPermissions(resource, permissions);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.  
`permissions` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The set of permissions to check for the `resource`. Permissions with wildcards (such as '*' or 'storage.*') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           deviceManagerClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### unbindDeviceFromGateway(@Nullable RegistryName parent, String gatewayId, String deviceId)
    
    
    public final UnbindDeviceFromGatewayResponse unbindDeviceFromGateway(@Nullable RegistryName parent, String gatewayId, String deviceId)

Deletes the association between the device and the gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       RegistryName parent = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]");
       String gatewayId = "gatewayId-1354641793";
       String deviceId = "deviceId1109191185";
       UnbindDeviceFromGatewayResponse response =
           deviceManagerClient.unbindDeviceFromGateway(parent, gatewayId, deviceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.iot.v1.RegistryName`  
Required. The name of the registry. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
`gatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value of `gateway_id` can be either the device numeric ID or the user-defined device identifier.  
`deviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The device to disassociate from the specified gateway. The value of `device_id` can be either the device numeric ID or the user-defined device identifier.  
**Returns**  
---  
**Type** | **Description**  
`[UnbindDeviceFromGatewayResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UnbindDeviceFromGatewayResponse)` |   
  
### unbindDeviceFromGateway(UnbindDeviceFromGatewayRequest request)
    
    
    public final UnbindDeviceFromGatewayResponse unbindDeviceFromGateway(UnbindDeviceFromGatewayRequest request)

Deletes the association between the device and the gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       UnbindDeviceFromGatewayRequest request =
           UnbindDeviceFromGatewayRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setGatewayId("gatewayId-1354641793")
               .setDeviceId("deviceId1109191185")
               .build();
       UnbindDeviceFromGatewayResponse response =
           deviceManagerClient.unbindDeviceFromGateway(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UnbindDeviceFromGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UnbindDeviceFromGatewayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnbindDeviceFromGatewayResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UnbindDeviceFromGatewayResponse)` |   
  
### unbindDeviceFromGateway(String parent, String gatewayId, String deviceId)
    
    
    public final UnbindDeviceFromGatewayResponse unbindDeviceFromGateway(String parent, String gatewayId, String deviceId)

Deletes the association between the device and the gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       String parent = RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString();
       String gatewayId = "gatewayId-1354641793";
       String deviceId = "deviceId1109191185";
       UnbindDeviceFromGatewayResponse response =
           deviceManagerClient.unbindDeviceFromGateway(parent, gatewayId, deviceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the registry. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
`gatewayId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The value of `gateway_id` can be either the device numeric ID or the user-defined device identifier.  
`deviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The device to disassociate from the specified gateway. The value of `device_id` can be either the device numeric ID or the user-defined device identifier.  
**Returns**  
---  
**Type** | **Description**  
`[UnbindDeviceFromGatewayResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UnbindDeviceFromGatewayResponse)` |   
  
### unbindDeviceFromGatewayCallable()
    
    
    public final UnaryCallable<UnbindDeviceFromGatewayRequest,UnbindDeviceFromGatewayResponse> unbindDeviceFromGatewayCallable()

Deletes the association between the device and the gateway.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       UnbindDeviceFromGatewayRequest request =
           UnbindDeviceFromGatewayRequest.newBuilder()
               .setParent(RegistryName.of("[PROJECT]", "[LOCATION]", "[REGISTRY]").toString())
               .setGatewayId("gatewayId-1354641793")
               .setDeviceId("deviceId1109191185")
               .build();
       ApiFuture<UnbindDeviceFromGatewayResponse> future =
           deviceManagerClient.unbindDeviceFromGatewayCallable().futureCall(request);
       // Do something.
       UnbindDeviceFromGatewayResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UnbindDeviceFromGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UnbindDeviceFromGatewayRequest),[UnbindDeviceFromGatewayResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UnbindDeviceFromGatewayResponse)>` |   
  
### updateDevice(Device device, FieldMask updateMask)
    
    
    public final Device updateDevice(Device device, FieldMask updateMask)

Updates a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       Device device = Device.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Device response = deviceManagerClient.updateDevice(device, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`device` | `[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)`  
Required. The new values for the device. The `id` and `num_id` fields must be empty, and the field `name` must specify the name path. For example, `projects/p0/locations/us-central1/registries/registry0/devices/device0`or `projects/p0/locations/us-central1/registries/registry0/devices/{num_id}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Only updates the `device` fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server. Mutable top-level fields: `credentials`, `blocked`, and `metadata`  
**Returns**  
---  
**Type** | **Description**  
`[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)` |   
  
### updateDevice(UpdateDeviceRequest request)
    
    
    public final Device updateDevice(UpdateDeviceRequest request)

Updates a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       UpdateDeviceRequest request =
           UpdateDeviceRequest.newBuilder()
               .setDevice(Device.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Device response = deviceManagerClient.updateDevice(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UpdateDeviceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)` |   
  
### updateDeviceCallable()
    
    
    public final UnaryCallable<UpdateDeviceRequest,Device> updateDeviceCallable()

Updates a device.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       UpdateDeviceRequest request =
           UpdateDeviceRequest.newBuilder()
               .setDevice(Device.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Device> future = deviceManagerClient.updateDeviceCallable().futureCall(request);
       // Do something.
       Device response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDeviceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UpdateDeviceRequest),[Device](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.Device)>` |   
  
### updateDeviceRegistry(DeviceRegistry deviceRegistry, FieldMask updateMask)
    
    
    public final DeviceRegistry updateDeviceRegistry(DeviceRegistry deviceRegistry, FieldMask updateMask)

Updates a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       DeviceRegistry deviceRegistry = DeviceRegistry.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DeviceRegistry response =
           deviceManagerClient.updateDeviceRegistry(deviceRegistry, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`deviceRegistry` | `[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)`  
Required. The new values for the device registry. The `id` field must be empty, and the `name` field must indicate the path of the resource. For example, `projects/example-project/locations/us-central1/registries/my-registry`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Only updates the `device_registry` fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server. Mutable top-level fields: `event_notification_config`, `http_config`, `mqtt_config`, and `state_notification_config`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)` |   
  
### updateDeviceRegistry(UpdateDeviceRegistryRequest request)
    
    
    public final DeviceRegistry updateDeviceRegistry(UpdateDeviceRegistryRequest request)

Updates a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       UpdateDeviceRegistryRequest request =
           UpdateDeviceRegistryRequest.newBuilder()
               .setDeviceRegistry(DeviceRegistry.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       DeviceRegistry response = deviceManagerClient.updateDeviceRegistry(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDeviceRegistryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UpdateDeviceRegistryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)` |   
  
### updateDeviceRegistryCallable()
    
    
    public final UnaryCallable<UpdateDeviceRegistryRequest,DeviceRegistry> updateDeviceRegistryCallable()

Updates a device registry configuration.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeviceManagerClient deviceManagerClient = DeviceManagerClient.create()) {
       UpdateDeviceRegistryRequest request =
           UpdateDeviceRegistryRequest.newBuilder()
               .setDeviceRegistry(DeviceRegistry.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<DeviceRegistry> future =
           deviceManagerClient.updateDeviceRegistryCallable().futureCall(request);
       // Do something.
       DeviceRegistry response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDeviceRegistryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.UpdateDeviceRegistryRequest),[DeviceRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloud-iot/latest/com.google.cloud.iot.v1.DeviceRegistry)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
