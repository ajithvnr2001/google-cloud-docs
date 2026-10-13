---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient
title: Class ApiHubPluginClient (0.52.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:24.888360+00:00
---

# Class ApiHubPluginClient (0.52.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ApiHubPluginClient (0.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.52.0 (latest)  0.48.0  0.47.0  0.46.0  0.44.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-apihub/google-cloud-apihub/src/main/java/com/google/cloud/apihub/v1/ApiHubPluginClient.java)| [Product Reference](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub)  
---|---  
  
Service Description: This service is used for managing plugins inside the API Hub.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginName name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]");
       Plugin response = apiHubPluginClient.getPlugin(name);
     }
     

Note: close() needs to be called on the ApiHubPluginClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetPlugin |  Get an API Hub plugin. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPlugin(GetPluginRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPlugin(PluginName name) 
  * getPlugin(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPluginCallable() 

  
EnablePlugin |  Enables a plugin. The `state` of the plugin after enabling is `ENABLED` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enablePlugin(EnablePluginRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * enablePlugin(PluginName name) 
  * enablePlugin(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enablePluginCallable() 

  
DisablePlugin |  Disables a plugin. The `state` of the plugin after disabling is `DISABLED` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * disablePlugin(DisablePluginRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * disablePlugin(PluginName name) 
  * disablePlugin(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * disablePluginCallable() 

  
CreatePlugin |  Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPlugin(CreatePluginRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createPlugin(LocationName parent, Plugin plugin, String pluginId) 
  * createPlugin(String parent, Plugin plugin, String pluginId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPluginCallable() 

  
ListPlugins |  List all the plugins in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPlugins(ListPluginsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPlugins(LocationName parent) 
  * listPlugins(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPluginsPagedCallable() 
  * listPluginsCallable() 

  
DeletePlugin |  Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePluginAsync(DeletePluginRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePluginAsync(PluginName name) 
  * deletePluginAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePluginOperationCallable() 
  * deletePluginCallable() 

  
CreatePluginInstance |  Creates a Plugin instance in the API hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPluginInstanceAsync(CreatePluginInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPluginInstanceAsync(PluginName parent, PluginInstance pluginInstance, String pluginInstanceId) 
  * createPluginInstanceAsync(String parent, PluginInstance pluginInstance, String pluginInstanceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPluginInstanceOperationCallable() 
  * createPluginInstanceCallable() 

  
ExecutePluginInstanceAction |  Executes a plugin instance in the API hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * executePluginInstanceActionAsync(ExecutePluginInstanceActionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * executePluginInstanceActionAsync(PluginInstanceName name, ActionExecutionDetail actionExecutionDetail) 
  * executePluginInstanceActionAsync(String name, ActionExecutionDetail actionExecutionDetail) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * executePluginInstanceActionOperationCallable() 
  * executePluginInstanceActionCallable() 

  
GetPluginInstance |  Get an API Hub plugin instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPluginInstance(GetPluginInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPluginInstance(PluginInstanceName name) 
  * getPluginInstance(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPluginInstanceCallable() 

  
ListPluginInstances |  List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id} |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPluginInstances(ListPluginInstancesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPluginInstances(PluginName parent) 
  * listPluginInstances(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPluginInstancesPagedCallable() 
  * listPluginInstancesCallable() 

  
EnablePluginInstanceAction |  Enables a plugin instance in the API hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enablePluginInstanceActionAsync(EnablePluginInstanceActionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * enablePluginInstanceActionAsync(PluginInstanceName name, String actionId) 
  * enablePluginInstanceActionAsync(String name, String actionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enablePluginInstanceActionOperationCallable() 
  * enablePluginInstanceActionCallable() 

  
DisablePluginInstanceAction |  Disables a plugin instance in the API hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * disablePluginInstanceActionAsync(DisablePluginInstanceActionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * disablePluginInstanceActionAsync(PluginInstanceName name, String actionId) 
  * disablePluginInstanceActionAsync(String name, String actionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * disablePluginInstanceActionOperationCallable() 
  * disablePluginInstanceActionCallable() 

  
UpdatePluginInstance |  Updates a plugin instance in the API hub. The following fields in the plugin_instance can be updated currently: 

  * display_name
  * schedule_cron_expression

The update_mask should be used to specify the fields being updated.  To update the auth_config and additional_config of the plugin instance, use the ApplyPluginInstanceConfig method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePluginInstance(UpdatePluginInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePluginInstance(PluginInstance pluginInstance, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePluginInstanceCallable() 

  
DeletePluginInstance |  Deletes a plugin instance in the API hub. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePluginInstanceAsync(DeletePluginInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePluginInstanceAsync(PluginInstanceName name) 
  * deletePluginInstanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePluginInstanceOperationCallable() 
  * deletePluginInstanceCallable() 

  
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

This class can be customized by passing in a custom instance of ApiHubPluginSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ApiHubPluginSettings apiHubPluginSettings =
         ApiHubPluginSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create(apiHubPluginSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ApiHubPluginSettings apiHubPluginSettings =
         ApiHubPluginSettings.newBuilder().setEndpoint(myEndpoint).build();
     ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create(apiHubPluginSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ApiHubPluginClient

## Static Methods 

### create()
    
    
    public static final ApiHubPluginClient create()

Constructs an instance of ApiHubPluginClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ApiHubPluginSettings settings)
    
    
    public static final ApiHubPluginClient create(ApiHubPluginSettings settings)

Constructs an instance of ApiHubPluginClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ApiHubPluginSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ApiHubPluginStub stub)
    
    
    public static final ApiHubPluginClient create(ApiHubPluginStub stub)

Constructs an instance of ApiHubPluginClient, using the given stub for making calls. This is for advanced usage - prefer using create(ApiHubPluginSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ApiHubPluginStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.stub.ApiHubPluginStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient)` |   
  
## Constructors 

### ApiHubPluginClient(ApiHubPluginSettings settings)
    
    
    protected ApiHubPluginClient(ApiHubPluginSettings settings)

Constructs an instance of ApiHubPluginClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ApiHubPluginSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginSettings)`  
  
  
### ApiHubPluginClient(ApiHubPluginStub stub)
    
    
    protected ApiHubPluginClient(ApiHubPluginStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ApiHubPluginStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.stub.ApiHubPluginStub)`  
  
  
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

### createPlugin(@Nullable LocationName parent, Plugin plugin, String pluginId)
    
    
    public final Plugin createPlugin(@Nullable LocationName parent, Plugin plugin, String pluginId)

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Plugin plugin = Plugin.newBuilder().build();
       String pluginId = "pluginId-1859618898";
       Plugin response = apiHubPluginClient.createPlugin(parent, plugin, pluginId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.LocationName`  
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}`.  
`plugin` | `[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)`  
Required. The plugin to create.  
`pluginId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the Plugin resource, which will become the final component of the Plugin's resource name. This field is optional. 

  * If provided, the same will be used. The service will throw an error if the specified id is already used by another Plugin resource in the API hub instance. 
  * If not provided, a system generated id will be used. 

This value should be 4-63 characters, overall resource name which will be of format `projects/{project}/locations/{location}/plugins/{plugin}`, its length is limited to 1000 characters and valid characters are /a-z[0-9]-_/.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### createPlugin(CreatePluginRequest request)
    
    
    public final Plugin createPlugin(CreatePluginRequest request)

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       CreatePluginRequest request =
           CreatePluginRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPluginId("pluginId-1859618898")
               .setPlugin(Plugin.newBuilder().build())
               .build();
       Plugin response = apiHubPluginClient.createPlugin(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.CreatePluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### createPlugin(String parent, Plugin plugin, String pluginId)
    
    
    public final Plugin createPlugin(String parent, Plugin plugin, String pluginId)

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Plugin plugin = Plugin.newBuilder().build();
       String pluginId = "pluginId-1859618898";
       Plugin response = apiHubPluginClient.createPlugin(parent, plugin, pluginId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}`.  
`plugin` | `[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)`  
Required. The plugin to create.  
`pluginId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the Plugin resource, which will become the final component of the Plugin's resource name. This field is optional. 

  * If provided, the same will be used. The service will throw an error if the specified id is already used by another Plugin resource in the API hub instance. 
  * If not provided, a system generated id will be used. 

This value should be 4-63 characters, overall resource name which will be of format `projects/{project}/locations/{location}/plugins/{plugin}`, its length is limited to 1000 characters and valid characters are /a-z[0-9]-_/.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### createPluginCallable()
    
    
    public final UnaryCallable<CreatePluginRequest,Plugin> createPluginCallable()

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       CreatePluginRequest request =
           CreatePluginRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPluginId("pluginId-1859618898")
               .setPlugin(Plugin.newBuilder().build())
               .build();
       ApiFuture<Plugin> future = apiHubPluginClient.createPluginCallable().futureCall(request);
       // Do something.
       Plugin response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.CreatePluginRequest),[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)>` |   
  
### createPluginInstanceAsync(@Nullable PluginName parent, PluginInstance pluginInstance, String pluginInstanceId)
    
    
    public final OperationFuture<PluginInstance,OperationMetadata> createPluginInstanceAsync(@Nullable PluginName parent, PluginInstance pluginInstance, String pluginInstanceId)

Creates a Plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginName parent = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]");
       PluginInstance pluginInstance = PluginInstance.newBuilder().build();
       String pluginInstanceId = "pluginInstanceId-1741818845";
       PluginInstance response =
           apiHubPluginClient
               .createPluginInstanceAsync(parent, pluginInstance, pluginInstanceId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginName`  
Required. The parent of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}`  
`pluginInstance` | `[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)`  
Required. The plugin instance to create.  
`pluginInstanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the plugin instance, which will become the final component of the plugin instance's resource name. This field is optional. 

  * If provided, the same will be used. The service will throw an error if the specified id is already used by another plugin instance in the plugin resource. 
  * If not provided, a system generated id will be used. 

This value should be 4-63 characters, and valid characters are /a-z[0-9]-_/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### createPluginInstanceAsync(CreatePluginInstanceRequest request)
    
    
    public final OperationFuture<PluginInstance,OperationMetadata> createPluginInstanceAsync(CreatePluginInstanceRequest request)

Creates a Plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       CreatePluginInstanceRequest request =
           CreatePluginInstanceRequest.newBuilder()
               .setParent(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .setPluginInstanceId("pluginInstanceId-1741818845")
               .setPluginInstance(PluginInstance.newBuilder().build())
               .build();
       PluginInstance response = apiHubPluginClient.createPluginInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.CreatePluginInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### createPluginInstanceAsync(String parent, PluginInstance pluginInstance, String pluginInstanceId)
    
    
    public final OperationFuture<PluginInstance,OperationMetadata> createPluginInstanceAsync(String parent, PluginInstance pluginInstance, String pluginInstanceId)

Creates a Plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String parent = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString();
       PluginInstance pluginInstance = PluginInstance.newBuilder().build();
       String pluginInstanceId = "pluginInstanceId-1741818845";
       PluginInstance response =
           apiHubPluginClient
               .createPluginInstanceAsync(parent, pluginInstance, pluginInstanceId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}`  
`pluginInstance` | `[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)`  
Required. The plugin instance to create.  
`pluginInstanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The ID to use for the plugin instance, which will become the final component of the plugin instance's resource name. This field is optional. 

  * If provided, the same will be used. The service will throw an error if the specified id is already used by another plugin instance in the plugin resource. 
  * If not provided, a system generated id will be used. 

This value should be 4-63 characters, and valid characters are /a-z[0-9]-_/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### createPluginInstanceCallable()
    
    
    public final UnaryCallable<CreatePluginInstanceRequest,Operation> createPluginInstanceCallable()

Creates a Plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       CreatePluginInstanceRequest request =
           CreatePluginInstanceRequest.newBuilder()
               .setParent(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .setPluginInstanceId("pluginInstanceId-1741818845")
               .setPluginInstance(PluginInstance.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           apiHubPluginClient.createPluginInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.CreatePluginInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPluginInstanceOperationCallable()
    
    
    public final OperationCallable<CreatePluginInstanceRequest,PluginInstance,OperationMetadata> createPluginInstanceOperationCallable()

Creates a Plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       CreatePluginInstanceRequest request =
           CreatePluginInstanceRequest.newBuilder()
               .setParent(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .setPluginInstanceId("pluginInstanceId-1741818845")
               .setPluginInstance(PluginInstance.newBuilder().build())
               .build();
       OperationFuture<PluginInstance, OperationMetadata> future =
           apiHubPluginClient.createPluginInstanceOperationCallable().futureCall(request);
       // Do something.
       PluginInstance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.CreatePluginInstanceRequest),[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### deletePluginAsync(@Nullable PluginName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePluginAsync(@Nullable PluginName name)

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginName name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]");
       apiHubPluginClient.deletePluginAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginName`  
Required. The name of the Plugin resource to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### deletePluginAsync(DeletePluginRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePluginAsync(DeletePluginRequest request)

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DeletePluginRequest request =
           DeletePluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       apiHubPluginClient.deletePluginAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DeletePluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### deletePluginAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePluginAsync(String name)

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString();
       apiHubPluginClient.deletePluginAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Plugin resource to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### deletePluginCallable()
    
    
    public final UnaryCallable<DeletePluginRequest,Operation> deletePluginCallable()

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DeletePluginRequest request =
           DeletePluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       ApiFuture<Operation> future = apiHubPluginClient.deletePluginCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DeletePluginRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePluginInstanceAsync(@Nullable PluginInstanceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePluginInstanceAsync(@Nullable PluginInstanceName name)

Deletes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginInstanceName name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]");
       apiHubPluginClient.deletePluginInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginInstanceName`  
Required. The name of the plugin instance to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### deletePluginInstanceAsync(DeletePluginInstanceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePluginInstanceAsync(DeletePluginInstanceRequest request)

Deletes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DeletePluginInstanceRequest request =
           DeletePluginInstanceRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .build();
       apiHubPluginClient.deletePluginInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DeletePluginInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### deletePluginInstanceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePluginInstanceAsync(String name)

Deletes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]").toString();
       apiHubPluginClient.deletePluginInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the plugin instance to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### deletePluginInstanceCallable()
    
    
    public final UnaryCallable<DeletePluginInstanceRequest,Operation> deletePluginInstanceCallable()

Deletes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DeletePluginInstanceRequest request =
           DeletePluginInstanceRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           apiHubPluginClient.deletePluginInstanceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DeletePluginInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePluginInstanceOperationCallable()
    
    
    public final OperationCallable<DeletePluginInstanceRequest,Empty,OperationMetadata> deletePluginInstanceOperationCallable()

Deletes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DeletePluginInstanceRequest request =
           DeletePluginInstanceRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           apiHubPluginClient.deletePluginInstanceOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DeletePluginInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### deletePluginOperationCallable()
    
    
    public final OperationCallable<DeletePluginRequest,Empty,OperationMetadata> deletePluginOperationCallable()

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DeletePluginRequest request =
           DeletePluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           apiHubPluginClient.deletePluginOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DeletePluginRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### disablePlugin(@Nullable PluginName name)
    
    
    public final Plugin disablePlugin(@Nullable PluginName name)

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginName name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]");
       Plugin response = apiHubPluginClient.disablePlugin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginName`  
Required. The name of the plugin to disable. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### disablePlugin(DisablePluginRequest request)
    
    
    public final Plugin disablePlugin(DisablePluginRequest request)

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DisablePluginRequest request =
           DisablePluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       Plugin response = apiHubPluginClient.disablePlugin(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisablePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### disablePlugin(String name)
    
    
    public final Plugin disablePlugin(String name)

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString();
       Plugin response = apiHubPluginClient.disablePlugin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the plugin to disable. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### disablePluginCallable()
    
    
    public final UnaryCallable<DisablePluginRequest,Plugin> disablePluginCallable()

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DisablePluginRequest request =
           DisablePluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       ApiFuture<Plugin> future = apiHubPluginClient.disablePluginCallable().futureCall(request);
       // Do something.
       Plugin response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisablePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginRequest),[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)>` |   
  
### disablePluginInstanceActionAsync(@Nullable PluginInstanceName name, String actionId)
    
    
    public final OperationFuture<DisablePluginInstanceActionResponse,OperationMetadata> disablePluginInstanceActionAsync(@Nullable PluginInstanceName name, String actionId)

Disables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginInstanceName name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]");
       String actionId = "actionId-1656172047";
       DisablePluginInstanceActionResponse response =
           apiHubPluginClient.disablePluginInstanceActionAsync(name, actionId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginInstanceName`  
Required. The name of the plugin instance to disable. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
`actionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The action id to disable.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DisablePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### disablePluginInstanceActionAsync(DisablePluginInstanceActionRequest request)
    
    
    public final OperationFuture<DisablePluginInstanceActionResponse,OperationMetadata> disablePluginInstanceActionAsync(DisablePluginInstanceActionRequest request)

Disables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DisablePluginInstanceActionRequest request =
           DisablePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionId("actionId-1656172047")
               .build();
       DisablePluginInstanceActionResponse response =
           apiHubPluginClient.disablePluginInstanceActionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisablePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginInstanceActionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DisablePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### disablePluginInstanceActionAsync(String name, String actionId)
    
    
    public final OperationFuture<DisablePluginInstanceActionResponse,OperationMetadata> disablePluginInstanceActionAsync(String name, String actionId)

Disables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]").toString();
       String actionId = "actionId-1656172047";
       DisablePluginInstanceActionResponse response =
           apiHubPluginClient.disablePluginInstanceActionAsync(name, actionId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the plugin instance to disable. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
`actionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The action id to disable.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DisablePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### disablePluginInstanceActionCallable()
    
    
    public final UnaryCallable<DisablePluginInstanceActionRequest,Operation> disablePluginInstanceActionCallable()

Disables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DisablePluginInstanceActionRequest request =
           DisablePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionId("actionId-1656172047")
               .build();
       ApiFuture<Operation> future =
           apiHubPluginClient.disablePluginInstanceActionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisablePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginInstanceActionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### disablePluginInstanceActionOperationCallable()
    
    
    public final OperationCallable<DisablePluginInstanceActionRequest,DisablePluginInstanceActionResponse,OperationMetadata> disablePluginInstanceActionOperationCallable()

Disables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       DisablePluginInstanceActionRequest request =
           DisablePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionId("actionId-1656172047")
               .build();
       OperationFuture<DisablePluginInstanceActionResponse, OperationMetadata> future =
           apiHubPluginClient.disablePluginInstanceActionOperationCallable().futureCall(request);
       // Do something.
       DisablePluginInstanceActionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DisablePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginInstanceActionRequest),[DisablePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.DisablePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### enablePlugin(@Nullable PluginName name)
    
    
    public final Plugin enablePlugin(@Nullable PluginName name)

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginName name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]");
       Plugin response = apiHubPluginClient.enablePlugin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginName`  
Required. The name of the plugin to enable. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### enablePlugin(EnablePluginRequest request)
    
    
    public final Plugin enablePlugin(EnablePluginRequest request)

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       EnablePluginRequest request =
           EnablePluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       Plugin response = apiHubPluginClient.enablePlugin(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnablePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### enablePlugin(String name)
    
    
    public final Plugin enablePlugin(String name)

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString();
       Plugin response = apiHubPluginClient.enablePlugin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the plugin to enable. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### enablePluginCallable()
    
    
    public final UnaryCallable<EnablePluginRequest,Plugin> enablePluginCallable()

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       EnablePluginRequest request =
           EnablePluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       ApiFuture<Plugin> future = apiHubPluginClient.enablePluginCallable().futureCall(request);
       // Do something.
       Plugin response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnablePluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginRequest),[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)>` |   
  
### enablePluginInstanceActionAsync(@Nullable PluginInstanceName name, String actionId)
    
    
    public final OperationFuture<EnablePluginInstanceActionResponse,OperationMetadata> enablePluginInstanceActionAsync(@Nullable PluginInstanceName name, String actionId)

Enables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginInstanceName name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]");
       String actionId = "actionId-1656172047";
       EnablePluginInstanceActionResponse response =
           apiHubPluginClient.enablePluginInstanceActionAsync(name, actionId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginInstanceName`  
Required. The name of the plugin instance to enable. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
`actionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The action id to enable.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EnablePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### enablePluginInstanceActionAsync(EnablePluginInstanceActionRequest request)
    
    
    public final OperationFuture<EnablePluginInstanceActionResponse,OperationMetadata> enablePluginInstanceActionAsync(EnablePluginInstanceActionRequest request)

Enables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       EnablePluginInstanceActionRequest request =
           EnablePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionId("actionId-1656172047")
               .build();
       EnablePluginInstanceActionResponse response =
           apiHubPluginClient.enablePluginInstanceActionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnablePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginInstanceActionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EnablePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### enablePluginInstanceActionAsync(String name, String actionId)
    
    
    public final OperationFuture<EnablePluginInstanceActionResponse,OperationMetadata> enablePluginInstanceActionAsync(String name, String actionId)

Enables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]").toString();
       String actionId = "actionId-1656172047";
       EnablePluginInstanceActionResponse response =
           apiHubPluginClient.enablePluginInstanceActionAsync(name, actionId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the plugin instance to enable. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
`actionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The action id to enable.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EnablePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### enablePluginInstanceActionCallable()
    
    
    public final UnaryCallable<EnablePluginInstanceActionRequest,Operation> enablePluginInstanceActionCallable()

Enables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       EnablePluginInstanceActionRequest request =
           EnablePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionId("actionId-1656172047")
               .build();
       ApiFuture<Operation> future =
           apiHubPluginClient.enablePluginInstanceActionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnablePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginInstanceActionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### enablePluginInstanceActionOperationCallable()
    
    
    public final OperationCallable<EnablePluginInstanceActionRequest,EnablePluginInstanceActionResponse,OperationMetadata> enablePluginInstanceActionOperationCallable()

Enables a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       EnablePluginInstanceActionRequest request =
           EnablePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionId("actionId-1656172047")
               .build();
       OperationFuture<EnablePluginInstanceActionResponse, OperationMetadata> future =
           apiHubPluginClient.enablePluginInstanceActionOperationCallable().futureCall(request);
       // Do something.
       EnablePluginInstanceActionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[EnablePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginInstanceActionRequest),[EnablePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.EnablePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### executePluginInstanceActionAsync(@Nullable PluginInstanceName name, ActionExecutionDetail actionExecutionDetail)
    
    
    public final OperationFuture<ExecutePluginInstanceActionResponse,OperationMetadata> executePluginInstanceActionAsync(@Nullable PluginInstanceName name, ActionExecutionDetail actionExecutionDetail)

Executes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginInstanceName name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]");
       ActionExecutionDetail actionExecutionDetail = ActionExecutionDetail.newBuilder().build();
       ExecutePluginInstanceActionResponse response =
           apiHubPluginClient.executePluginInstanceActionAsync(name, actionExecutionDetail).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginInstanceName`  
Required. The name of the plugin instance to execute. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
`actionExecutionDetail` | `[ActionExecutionDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ActionExecutionDetail)`  
Required. The execution details for the action to execute.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExecutePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ExecutePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### executePluginInstanceActionAsync(ExecutePluginInstanceActionRequest request)
    
    
    public final OperationFuture<ExecutePluginInstanceActionResponse,OperationMetadata> executePluginInstanceActionAsync(ExecutePluginInstanceActionRequest request)

Executes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ExecutePluginInstanceActionRequest request =
           ExecutePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionExecutionDetail(ActionExecutionDetail.newBuilder().build())
               .build();
       ExecutePluginInstanceActionResponse response =
           apiHubPluginClient.executePluginInstanceActionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ExecutePluginInstanceActionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExecutePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ExecutePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### executePluginInstanceActionAsync(String name, ActionExecutionDetail actionExecutionDetail)
    
    
    public final OperationFuture<ExecutePluginInstanceActionResponse,OperationMetadata> executePluginInstanceActionAsync(String name, ActionExecutionDetail actionExecutionDetail)

Executes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]").toString();
       ActionExecutionDetail actionExecutionDetail = ActionExecutionDetail.newBuilder().build();
       ExecutePluginInstanceActionResponse response =
           apiHubPluginClient.executePluginInstanceActionAsync(name, actionExecutionDetail).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the plugin instance to execute. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
`actionExecutionDetail` | `[ActionExecutionDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ActionExecutionDetail)`  
Required. The execution details for the action to execute.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExecutePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ExecutePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### executePluginInstanceActionCallable()
    
    
    public final UnaryCallable<ExecutePluginInstanceActionRequest,Operation> executePluginInstanceActionCallable()

Executes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ExecutePluginInstanceActionRequest request =
           ExecutePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionExecutionDetail(ActionExecutionDetail.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           apiHubPluginClient.executePluginInstanceActionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ExecutePluginInstanceActionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### executePluginInstanceActionOperationCallable()
    
    
    public final OperationCallable<ExecutePluginInstanceActionRequest,ExecutePluginInstanceActionResponse,OperationMetadata> executePluginInstanceActionOperationCallable()

Executes a plugin instance in the API hub.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ExecutePluginInstanceActionRequest request =
           ExecutePluginInstanceActionRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .setActionExecutionDetail(ActionExecutionDetail.newBuilder().build())
               .build();
       OperationFuture<ExecutePluginInstanceActionResponse, OperationMetadata> future =
           apiHubPluginClient.executePluginInstanceActionOperationCallable().futureCall(request);
       // Do something.
       ExecutePluginInstanceActionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ExecutePluginInstanceActionRequest),[ExecutePluginInstanceActionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ExecutePluginInstanceActionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

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
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = apiHubPluginClient.getLocation(request);
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
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = apiHubPluginClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getPlugin(@Nullable PluginName name)
    
    
    public final Plugin getPlugin(@Nullable PluginName name)

Get an API Hub plugin.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginName name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]");
       Plugin response = apiHubPluginClient.getPlugin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginName`  
Required. The name of the plugin to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### getPlugin(GetPluginRequest request)
    
    
    public final Plugin getPlugin(GetPluginRequest request)

Get an API Hub plugin.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       GetPluginRequest request =
           GetPluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       Plugin response = apiHubPluginClient.getPlugin(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.GetPluginRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### getPlugin(String name)
    
    
    public final Plugin getPlugin(String name)

Get an API Hub plugin.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString();
       Plugin response = apiHubPluginClient.getPlugin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the plugin to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}`.  
**Returns**  
---  
**Type** | **Description**  
`[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)` |   
  
### getPluginCallable()
    
    
    public final UnaryCallable<GetPluginRequest,Plugin> getPluginCallable()

Get an API Hub plugin.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       GetPluginRequest request =
           GetPluginRequest.newBuilder()
               .setName(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .build();
       ApiFuture<Plugin> future = apiHubPluginClient.getPluginCallable().futureCall(request);
       // Do something.
       Plugin response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.GetPluginRequest),[Plugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Plugin)>` |   
  
### getPluginInstance(@Nullable PluginInstanceName name)
    
    
    public final PluginInstance getPluginInstance(@Nullable PluginInstanceName name)

Get an API Hub plugin instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginInstanceName name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]");
       PluginInstance response = apiHubPluginClient.getPluginInstance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginInstanceName`  
Required. The name of the plugin instance to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)` |   
  
### getPluginInstance(GetPluginInstanceRequest request)
    
    
    public final PluginInstance getPluginInstance(GetPluginInstanceRequest request)

Get an API Hub plugin instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       GetPluginInstanceRequest request =
           GetPluginInstanceRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .build();
       PluginInstance response = apiHubPluginClient.getPluginInstance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.GetPluginInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)` |   
  
### getPluginInstance(String name)
    
    
    public final PluginInstance getPluginInstance(String name)

Get an API Hub plugin instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String name =
           PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]").toString();
       PluginInstance response = apiHubPluginClient.getPluginInstance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the plugin instance to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)` |   
  
### getPluginInstanceCallable()
    
    
    public final UnaryCallable<GetPluginInstanceRequest,PluginInstance> getPluginInstanceCallable()

Get an API Hub plugin instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       GetPluginInstanceRequest request =
           GetPluginInstanceRequest.newBuilder()
               .setName(
                   PluginInstanceName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]", "[INSTANCE]")
                       .toString())
               .build();
       ApiFuture<PluginInstance> future =
           apiHubPluginClient.getPluginInstanceCallable().futureCall(request);
       // Do something.
       PluginInstance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.GetPluginInstanceRequest),[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)>` |   
  
### getSettings()
    
    
    public final @Nullable ApiHubPluginSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.ApiHubPluginSettings` |   
  
### getStub()
    
    
    public ApiHubPluginStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.stub.ApiHubPluginStub)` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final ApiHubPluginClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : apiHubPluginClient.listLocations(request).iterateAll()) {
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
`[ApiHubPluginClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = apiHubPluginClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ApiHubPluginClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           apiHubPluginClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListLocationsPagedResponse)>` |   
  
### listPluginInstances(@Nullable PluginName parent)
    
    
    public final ApiHubPluginClient.ListPluginInstancesPagedResponse listPluginInstances(@Nullable PluginName parent)

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginName parent = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]");
       for (PluginInstance element : apiHubPluginClient.listPluginInstances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.PluginName`  
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}/plugins/{plugin}`. To list plugin instances for multiple plugins, use the - character instead of the plugin ID.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient.ListPluginInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListPluginInstancesPagedResponse)` |   
  
### listPluginInstances(ListPluginInstancesRequest request)
    
    
    public final ApiHubPluginClient.ListPluginInstancesPagedResponse listPluginInstances(ListPluginInstancesRequest request)

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListPluginInstancesRequest request =
           ListPluginInstancesRequest.newBuilder()
               .setParent(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (PluginInstance element : apiHubPluginClient.listPluginInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPluginInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ListPluginInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient.ListPluginInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListPluginInstancesPagedResponse)` |   
  
### listPluginInstances(String parent)
    
    
    public final ApiHubPluginClient.ListPluginInstancesPagedResponse listPluginInstances(String parent)

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String parent = PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString();
       for (PluginInstance element : apiHubPluginClient.listPluginInstances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}/plugins/{plugin}`. To list plugin instances for multiple plugins, use the - character instead of the plugin ID.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient.ListPluginInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListPluginInstancesPagedResponse)` |   
  
### listPluginInstancesCallable()
    
    
    public final UnaryCallable<ListPluginInstancesRequest,ListPluginInstancesResponse> listPluginInstancesCallable()

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListPluginInstancesRequest request =
           ListPluginInstancesRequest.newBuilder()
               .setParent(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPluginInstancesResponse response =
             apiHubPluginClient.listPluginInstancesCallable().call(request);
         for (PluginInstance element : response.getPluginInstancesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPluginInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ListPluginInstancesRequest),[ListPluginInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ListPluginInstancesResponse)>` |   
  
### listPluginInstancesPagedCallable()
    
    
    public final UnaryCallable<ListPluginInstancesRequest,ApiHubPluginClient.ListPluginInstancesPagedResponse> listPluginInstancesPagedCallable()

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListPluginInstancesRequest request =
           ListPluginInstancesRequest.newBuilder()
               .setParent(PluginName.of("[PROJECT]", "[LOCATION]", "[PLUGIN]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<PluginInstance> future =
           apiHubPluginClient.listPluginInstancesPagedCallable().futureCall(request);
       // Do something.
       for (PluginInstance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPluginInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ListPluginInstancesRequest),[ListPluginInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListPluginInstancesPagedResponse)>` |   
  
### listPlugins(@Nullable LocationName parent)
    
    
    public final ApiHubPluginClient.ListPluginsPagedResponse listPlugins(@Nullable LocationName parent)

List all the plugins in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Plugin element : apiHubPluginClient.listPlugins(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.apihub.v1.LocationName`  
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient.ListPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListPluginsPagedResponse)` |   
  
### listPlugins(ListPluginsRequest request)
    
    
    public final ApiHubPluginClient.ListPluginsPagedResponse listPlugins(ListPluginsRequest request)

List all the plugins in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListPluginsRequest request =
           ListPluginsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Plugin element : apiHubPluginClient.listPlugins(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ListPluginsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient.ListPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListPluginsPagedResponse)` |   
  
### listPlugins(String parent)
    
    
    public final ApiHubPluginClient.ListPluginsPagedResponse listPlugins(String parent)

List all the plugins in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Plugin element : apiHubPluginClient.listPlugins(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[ApiHubPluginClient.ListPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListPluginsPagedResponse)` |   
  
### listPluginsCallable()
    
    
    public final UnaryCallable<ListPluginsRequest,ListPluginsResponse> listPluginsCallable()

List all the plugins in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListPluginsRequest request =
           ListPluginsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPluginsResponse response = apiHubPluginClient.listPluginsCallable().call(request);
         for (Plugin element : response.getPluginsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ListPluginsRequest),[ListPluginsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ListPluginsResponse)>` |   
  
### listPluginsPagedCallable()
    
    
    public final UnaryCallable<ListPluginsRequest,ApiHubPluginClient.ListPluginsPagedResponse> listPluginsPagedCallable()

List all the plugins in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       ListPluginsRequest request =
           ListPluginsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Plugin> future = apiHubPluginClient.listPluginsPagedCallable().futureCall(request);
       // Do something.
       for (Plugin element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ListPluginsRequest),[ListPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiHubPluginClient.ListPluginsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePluginInstance(PluginInstance pluginInstance, FieldMask updateMask)
    
    
    public final PluginInstance updatePluginInstance(PluginInstance pluginInstance, FieldMask updateMask)

Updates a plugin instance in the API hub. The following fields in the plugin_instance can be updated currently:

  * display_name
  * schedule_cron_expression



The update_mask should be used to specify the fields being updated.

To update the auth_config and additional_config of the plugin instance, use the ApplyPluginInstanceConfig method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       PluginInstance pluginInstance = PluginInstance.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PluginInstance response = apiHubPluginClient.updatePluginInstance(pluginInstance, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`pluginInstance` | `[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)`  
Required. The plugin instance to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)` |   
  
### updatePluginInstance(UpdatePluginInstanceRequest request)
    
    
    public final PluginInstance updatePluginInstance(UpdatePluginInstanceRequest request)

Updates a plugin instance in the API hub. The following fields in the plugin_instance can be updated currently:

  * display_name
  * schedule_cron_expression



The update_mask should be used to specify the fields being updated.

To update the auth_config and additional_config of the plugin instance, use the ApplyPluginInstanceConfig method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       UpdatePluginInstanceRequest request =
           UpdatePluginInstanceRequest.newBuilder()
               .setPluginInstance(PluginInstance.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       PluginInstance response = apiHubPluginClient.updatePluginInstance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.UpdatePluginInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)` |   
  
### updatePluginInstanceCallable()
    
    
    public final UnaryCallable<UpdatePluginInstanceRequest,PluginInstance> updatePluginInstanceCallable()

Updates a plugin instance in the API hub. The following fields in the plugin_instance can be updated currently:

  * display_name
  * schedule_cron_expression



The update_mask should be used to specify the fields being updated.

To update the auth_config and additional_config of the plugin instance, use the ApplyPluginInstanceConfig method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ApiHubPluginClient apiHubPluginClient = ApiHubPluginClient.create()) {
       UpdatePluginInstanceRequest request =
           UpdatePluginInstanceRequest.newBuilder()
               .setPluginInstance(PluginInstance.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<PluginInstance> future =
           apiHubPluginClient.updatePluginInstanceCallable().futureCall(request);
       // Do something.
       PluginInstance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePluginInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.UpdatePluginInstanceRequest),[PluginInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.PluginInstance)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
