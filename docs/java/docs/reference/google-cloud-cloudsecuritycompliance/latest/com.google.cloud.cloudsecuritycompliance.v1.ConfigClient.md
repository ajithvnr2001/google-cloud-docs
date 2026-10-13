---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient
title: Class ConfigClient (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:52.015563+00:00
---

# Class ConfigClient (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConfigClient (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudsecuritycompliance/google-cloud-cloudsecuritycompliance/src/main/java/com/google/cloud/cloudsecuritycompliance/v1/ConfigClient.java)| [Product Reference](https://cloud.google.com/security-command-center/docs/compliance-manager-overview)  
---|---  
  
Service Description: Config Service manages compliance frameworks, cloud controls, and their configurations.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       FrameworkName name =
           FrameworkName.ofOrganizationLocationFrameworkName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]");
       Framework response = configClient.getFramework(name);
     }
     

Note: close() needs to be called on the ConfigClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListFrameworks |  Lists the frameworks (both built-in and custom) that are available within the parent resource. The latest major version of each framework is returned. This method supports pagination. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFrameworks(ListFrameworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFrameworks(LocationName parent) 
  * listFrameworks(OrganizationLocationName parent) 
  * listFrameworks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFrameworksPagedCallable() 
  * listFrameworksCallable() 

  
GetFramework |  Gets details about a framework. This method retrieves the latest major version of the framework.  To retrieve a specific major version, include `major_revision_id` in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getFramework(GetFrameworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getFramework(FrameworkName name) 
  * getFramework(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFrameworkCallable() 

  
CreateFramework |  Creates a custom framework in a given parent resource. You can't create built-in frameworks because those are managed by Google. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createFramework(CreateFrameworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createFramework(LocationName parent, Framework framework, String frameworkId) 
  * createFramework(OrganizationLocationName parent, Framework framework, String frameworkId) 
  * createFramework(String parent, Framework framework, String frameworkId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createFrameworkCallable() 

  
UpdateFramework |  Updates a custom framework. This method allows for partial updates of a framework. Use the `update_mask` to specify which fields to update. Consider the following:  \- If you provide an `update_mask`, only the fields that are specified in the mask are updated. - If you don't provide an `update_mask`, all the fields that are present in the request's `framework` body are used to overwrite the existing resource.  You can only update frameworks with the `CUSTOM` type. A successful update creates a new version of the framework. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFramework(UpdateFrameworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateFramework(Framework framework, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFrameworkCallable() 

  
DeleteFramework |  Deletes a custom framework, including all its major and minor revisions. Consider the following:  \- You can't delete built-in frameworks. You can only delete frameworks with type `CUSTOM`. - You can't delete frameworks that are deployed to a resource. - You can't restore a deleted framework. This action is permanent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteFramework(DeleteFrameworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteFramework(FrameworkName name) 
  * deleteFramework(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteFrameworkCallable() 

  
ListCloudControls |  Lists the cloud controls (both built-in and custom) that are available in a given parent resource. The latest major version of each cloud control is returned. This method supports pagination. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCloudControls(ListCloudControlsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCloudControls(LocationName parent) 
  * listCloudControls(OrganizationLocationName parent) 
  * listCloudControls(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCloudControlsPagedCallable() 
  * listCloudControlsCallable() 

  
GetCloudControl |  Gets details about a cloud control. This method retrieves the latest major version of a cloud control that you identify by name.  By default, the latest major version of the cloud control is returned. To retrieve a specific major version, include `major_revision_id` in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCloudControl(GetCloudControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCloudControl(CloudControlName name) 
  * getCloudControl(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCloudControlCallable() 

  
CreateCloudControl |  Creates a custom cloud control in a given parent resource. You can't create built-in cloud controls because those are managed by Google. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCloudControl(CreateCloudControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCloudControl(LocationName parent, CloudControl cloudControl, String cloudControlId) 
  * createCloudControl(OrganizationLocationName parent, CloudControl cloudControl, String cloudControlId) 
  * createCloudControl(String parent, CloudControl cloudControl, String cloudControlId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCloudControlCallable() 

  
UpdateCloudControl |  Updates a custom cloud control. This method allows for partial updates of a cloud control. Use the `update_mask` to specify which fields to update. Consider the following:  \- If you provide an `update_mask`, only the fields that are specified in the mask are updated. - If you don't provide an `update_mask`, all the fields that are present in the request's `cloud_control` body are used to overwrite the existing resource.  You can only update cloud controls with the `CUSTOM` type. A successful update creates a new version of the cloud control. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCloudControl(UpdateCloudControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCloudControl(CloudControl cloudControl, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCloudControlCallable() 

  
DeleteCloudControl |  Deletes a custom cloud control, including all its major and minor revisions. Consider the following:  \- You can't delete built-in cloud controls. You can only delete cloud controls with type `CUSTOM`. - You can't delete cloud controls if any of the versions are referenced by a framework. - You can't restore a deleted cloud control. This action is permanent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCloudControl(DeleteCloudControlRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteCloudControl(CloudControlName name) 
  * deleteCloudControl(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCloudControlCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of ConfigSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConfigSettings configSettings =
         ConfigSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConfigClient configClient = ConfigClient.create(configSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConfigSettings configSettings = ConfigSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConfigClient configClient = ConfigClient.create(configSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConfigSettings configSettings = ConfigSettings.newHttpJsonBuilder().build();
     ConfigClient configClient = ConfigClient.create(configSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConfigClient

## Static Methods 

### create()
    
    
    public static final ConfigClient create()

Constructs an instance of ConfigClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConfigClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConfigSettings settings)
    
    
    public static final ConfigClient create(ConfigSettings settings)

Constructs an instance of ConfigClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConfigSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConfigStub stub)
    
    
    public static final ConfigClient create(ConfigStub stub)

Constructs an instance of ConfigClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConfigSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConfigStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.ConfigStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient)` |   
  
## Constructors 

### ConfigClient(ConfigSettings settings)
    
    
    protected ConfigClient(ConfigSettings settings)

Constructs an instance of ConfigClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConfigSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigSettings)`  
  
  
### ConfigClient(ConfigStub stub)
    
    
    protected ConfigClient(ConfigStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConfigStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.ConfigStub)`  
  
  
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

### createCloudControl(@Nullable LocationName parent, CloudControl cloudControl, String cloudControlId)
    
    
    public final CloudControl createCloudControl(@Nullable LocationName parent, CloudControl cloudControl, String cloudControlId)

Creates a custom cloud control in a given parent resource. You can't create built-in cloud controls because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CloudControl cloudControl = CloudControl.newBuilder().build();
       String cloudControlId = "cloudControlId657324195";
       CloudControl response = configClient.createCloudControl(parent, cloudControl, cloudControlId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}`. - `projects/{project}/locations/{location}`. The only supported location is `global`.  
`cloudControl` | `[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)`  
Required. The cloud control that's being created.  
`cloudControlId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The identifier for the cloud control, which is the last segment of the cloud control name. The format is `^a-zA-Z{0,61}[a-zA-Z0-9]$`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### createCloudControl(@Nullable OrganizationLocationName parent, CloudControl cloudControl, String cloudControlId)
    
    
    public final CloudControl createCloudControl(@Nullable OrganizationLocationName parent, CloudControl cloudControl, String cloudControlId)

Creates a custom cloud control in a given parent resource. You can't create built-in cloud controls because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       CloudControl cloudControl = CloudControl.newBuilder().build();
       String cloudControlId = "cloudControlId657324195";
       CloudControl response = configClient.createCloudControl(parent, cloudControl, cloudControlId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}`. - `projects/{project}/locations/{location}`. The only supported location is `global`.  
`cloudControl` | `[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)`  
Required. The cloud control that's being created.  
`cloudControlId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The identifier for the cloud control, which is the last segment of the cloud control name. The format is `^a-zA-Z{0,61}[a-zA-Z0-9]$`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### createCloudControl(CreateCloudControlRequest request)
    
    
    public final CloudControl createCloudControl(CreateCloudControlRequest request)

Creates a custom cloud control in a given parent resource. You can't create built-in cloud controls because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateCloudControlRequest request =
           CreateCloudControlRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setCloudControlId("cloudControlId657324195")
               .setCloudControl(CloudControl.newBuilder().build())
               .build();
       CloudControl response = configClient.createCloudControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateCloudControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### createCloudControl(String parent, CloudControl cloudControl, String cloudControlId)
    
    
    public final CloudControl createCloudControl(String parent, CloudControl cloudControl, String cloudControlId)

Creates a custom cloud control in a given parent resource. You can't create built-in cloud controls because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       CloudControl cloudControl = CloudControl.newBuilder().build();
       String cloudControlId = "cloudControlId657324195";
       CloudControl response = configClient.createCloudControl(parent, cloudControl, cloudControlId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}`. - `projects/{project}/locations/{location}`. The only supported location is `global`.  
`cloudControl` | `[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)`  
Required. The cloud control that's being created.  
`cloudControlId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The identifier for the cloud control, which is the last segment of the cloud control name. The format is `^a-zA-Z{0,61}[a-zA-Z0-9]$`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### createCloudControlCallable()
    
    
    public final UnaryCallable<CreateCloudControlRequest,CloudControl> createCloudControlCallable()

Creates a custom cloud control in a given parent resource. You can't create built-in cloud controls because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateCloudControlRequest request =
           CreateCloudControlRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setCloudControlId("cloudControlId657324195")
               .setCloudControl(CloudControl.newBuilder().build())
               .build();
       ApiFuture<CloudControl> future =
           configClient.createCloudControlCallable().futureCall(request);
       // Do something.
       CloudControl response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateCloudControlRequest),[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)>` |   
  
### createFramework(@Nullable LocationName parent, Framework framework, String frameworkId)
    
    
    public final Framework createFramework(@Nullable LocationName parent, Framework framework, String frameworkId)

Creates a custom framework in a given parent resource. You can't create built-in frameworks because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Framework framework = Framework.newBuilder().build();
       String frameworkId = "frameworkId886666169";
       Framework response = configClient.createFramework(parent, framework, frameworkId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
`framework` | `[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)`  
Required. The resource being created.  
`frameworkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The identifier (ID) of the framework. The ID is not the full name of the framework; it's the last part of the full name of the framework.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### createFramework(@Nullable OrganizationLocationName parent, Framework framework, String frameworkId)
    
    
    public final Framework createFramework(@Nullable OrganizationLocationName parent, Framework framework, String frameworkId)

Creates a custom framework in a given parent resource. You can't create built-in frameworks because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       Framework framework = Framework.newBuilder().build();
       String frameworkId = "frameworkId886666169";
       Framework response = configClient.createFramework(parent, framework, frameworkId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
`framework` | `[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)`  
Required. The resource being created.  
`frameworkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The identifier (ID) of the framework. The ID is not the full name of the framework; it's the last part of the full name of the framework.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### createFramework(CreateFrameworkRequest request)
    
    
    public final Framework createFramework(CreateFrameworkRequest request)

Creates a custom framework in a given parent resource. You can't create built-in frameworks because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateFrameworkRequest request =
           CreateFrameworkRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setFrameworkId("frameworkId886666169")
               .setFramework(Framework.newBuilder().build())
               .build();
       Framework response = configClient.createFramework(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### createFramework(String parent, Framework framework, String frameworkId)
    
    
    public final Framework createFramework(String parent, Framework framework, String frameworkId)

Creates a custom framework in a given parent resource. You can't create built-in frameworks because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       Framework framework = Framework.newBuilder().build();
       String frameworkId = "frameworkId886666169";
       Framework response = configClient.createFramework(parent, framework, frameworkId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
`framework` | `[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)`  
Required. The resource being created.  
`frameworkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The identifier (ID) of the framework. The ID is not the full name of the framework; it's the last part of the full name of the framework.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### createFrameworkCallable()
    
    
    public final UnaryCallable<CreateFrameworkRequest,Framework> createFrameworkCallable()

Creates a custom framework in a given parent resource. You can't create built-in frameworks because those are managed by Google.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateFrameworkRequest request =
           CreateFrameworkRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setFrameworkId("frameworkId886666169")
               .setFramework(Framework.newBuilder().build())
               .build();
       ApiFuture<Framework> future = configClient.createFrameworkCallable().futureCall(request);
       // Do something.
       Framework response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkRequest),[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)>` |   
  
### deleteCloudControl(@Nullable CloudControlName name)
    
    
    public final void deleteCloudControl(@Nullable CloudControlName name)

Deletes a custom cloud control, including all its major and minor revisions. Consider the following:

\- You can't delete built-in cloud controls. You can only delete cloud controls with type `CUSTOM`. - You can't delete cloud controls if any of the versions are referenced by a framework. - You can't restore a deleted cloud control. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CloudControlName name =
           CloudControlName.ofOrganizationLocationCloudControlName(
               "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL]");
       configClient.deleteCloudControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.CloudControlName`  
Required. The name of the cloud control to delete, in one of the following formats: `organizations/{organization}/locations/{location}/CloudControls/{CloudControl}` or `projects/{project}/locations/{location}/CloudControls/{CloudControl}`. The only supported location is `global`.  
  
### deleteCloudControl(DeleteCloudControlRequest request)
    
    
    public final void deleteCloudControl(DeleteCloudControlRequest request)

Deletes a custom cloud control, including all its major and minor revisions. Consider the following:

\- You can't delete built-in cloud controls. You can only delete cloud controls with type `CUSTOM`. - You can't delete cloud controls if any of the versions are referenced by a framework. - You can't restore a deleted cloud control. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteCloudControlRequest request =
           DeleteCloudControlRequest.newBuilder()
               .setName(
                   CloudControlName.ofOrganizationLocationCloudControlName(
                           "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL]")
                       .toString())
               .build();
       configClient.deleteCloudControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteCloudControlRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteCloudControl(String name)
    
    
    public final void deleteCloudControl(String name)

Deletes a custom cloud control, including all its major and minor revisions. Consider the following:

\- You can't delete built-in cloud controls. You can only delete cloud controls with type `CUSTOM`. - You can't delete cloud controls if any of the versions are referenced by a framework. - You can't restore a deleted cloud control. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name =
           CloudControlName.ofOrganizationLocationCloudControlName(
                   "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL]")
               .toString();
       configClient.deleteCloudControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the cloud control to delete, in one of the following formats: `organizations/{organization}/locations/{location}/CloudControls/{CloudControl}` or `projects/{project}/locations/{location}/CloudControls/{CloudControl}`. The only supported location is `global`.  
  
### deleteCloudControlCallable()
    
    
    public final UnaryCallable<DeleteCloudControlRequest,Empty> deleteCloudControlCallable()

Deletes a custom cloud control, including all its major and minor revisions. Consider the following:

\- You can't delete built-in cloud controls. You can only delete cloud controls with type `CUSTOM`. - You can't delete cloud controls if any of the versions are referenced by a framework. - You can't restore a deleted cloud control. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteCloudControlRequest request =
           DeleteCloudControlRequest.newBuilder()
               .setName(
                   CloudControlName.ofOrganizationLocationCloudControlName(
                           "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL]")
                       .toString())
               .build();
       ApiFuture<Empty> future = configClient.deleteCloudControlCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteCloudControlRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteFramework(@Nullable FrameworkName name)
    
    
    public final void deleteFramework(@Nullable FrameworkName name)

Deletes a custom framework, including all its major and minor revisions. Consider the following:

\- You can't delete built-in frameworks. You can only delete frameworks with type `CUSTOM`. - You can't delete frameworks that are deployed to a resource. - You can't restore a deleted framework. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       FrameworkName name =
           FrameworkName.ofOrganizationLocationFrameworkName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]");
       configClient.deleteFramework(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FrameworkName`  
Required. The name of the resource, in one of the following formats: `organizations/{organization}/locations/{location}/frameworks/{framework}` or `projects/{project}/locations/{location}/frameworks/{framework}`. The only supported location is `global`.  
  
### deleteFramework(DeleteFrameworkRequest request)
    
    
    public final void deleteFramework(DeleteFrameworkRequest request)

Deletes a custom framework, including all its major and minor revisions. Consider the following:

\- You can't delete built-in frameworks. You can only delete frameworks with type `CUSTOM`. - You can't delete frameworks that are deployed to a resource. - You can't restore a deleted framework. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteFrameworkRequest request =
           DeleteFrameworkRequest.newBuilder()
               .setName(
                   FrameworkName.ofOrganizationLocationFrameworkName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]")
                       .toString())
               .build();
       configClient.deleteFramework(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteFrameworkRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteFramework(String name)
    
    
    public final void deleteFramework(String name)

Deletes a custom framework, including all its major and minor revisions. Consider the following:

\- You can't delete built-in frameworks. You can only delete frameworks with type `CUSTOM`. - You can't delete frameworks that are deployed to a resource. - You can't restore a deleted framework. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name =
           FrameworkName.ofOrganizationLocationFrameworkName(
                   "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]")
               .toString();
       configClient.deleteFramework(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the resource, in one of the following formats: `organizations/{organization}/locations/{location}/frameworks/{framework}` or `projects/{project}/locations/{location}/frameworks/{framework}`. The only supported location is `global`.  
  
### deleteFrameworkCallable()
    
    
    public final UnaryCallable<DeleteFrameworkRequest,Empty> deleteFrameworkCallable()

Deletes a custom framework, including all its major and minor revisions. Consider the following:

\- You can't delete built-in frameworks. You can only delete frameworks with type `CUSTOM`. - You can't delete frameworks that are deployed to a resource. - You can't restore a deleted framework. This action is permanent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteFrameworkRequest request =
           DeleteFrameworkRequest.newBuilder()
               .setName(
                   FrameworkName.ofOrganizationLocationFrameworkName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]")
                       .toString())
               .build();
       ApiFuture<Empty> future = configClient.deleteFrameworkCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteFrameworkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCloudControl(@Nullable CloudControlName name)
    
    
    public final CloudControl getCloudControl(@Nullable CloudControlName name)

Gets details about a cloud control. This method retrieves the latest major version of a cloud control that you identify by name.

By default, the latest major version of the cloud control is returned. To retrieve a specific major version, include `major_revision_id` in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CloudControlName name =
           CloudControlName.ofOrganizationLocationCloudControlName(
               "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL]");
       CloudControl response = configClient.getCloudControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.CloudControlName`  
Required. The name of the cloud control to retrieve, in one of the following formats: `organizations/{organization}/locations/{location}/cloudControls/{cloud_control}` or `projects/{project}/locations/{location}/cloudControls/{cloud_control}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### getCloudControl(GetCloudControlRequest request)
    
    
    public final CloudControl getCloudControl(GetCloudControlRequest request)

Gets details about a cloud control. This method retrieves the latest major version of a cloud control that you identify by name.

By default, the latest major version of the cloud control is returned. To retrieve a specific major version, include `major_revision_id` in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetCloudControlRequest request =
           GetCloudControlRequest.newBuilder()
               .setName(
                   CloudControlName.ofOrganizationLocationCloudControlName(
                           "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL]")
                       .toString())
               .setMajorRevisionId(612576889)
               .build();
       CloudControl response = configClient.getCloudControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetCloudControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### getCloudControl(String name)
    
    
    public final CloudControl getCloudControl(String name)

Gets details about a cloud control. This method retrieves the latest major version of a cloud control that you identify by name.

By default, the latest major version of the cloud control is returned. To retrieve a specific major version, include `major_revision_id` in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name =
           CloudControlName.ofOrganizationLocationCloudControlName(
                   "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL]")
               .toString();
       CloudControl response = configClient.getCloudControl(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the cloud control to retrieve, in one of the following formats: `organizations/{organization}/locations/{location}/cloudControls/{cloud_control}` or `projects/{project}/locations/{location}/cloudControls/{cloud_control}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### getCloudControlCallable()
    
    
    public final UnaryCallable<GetCloudControlRequest,CloudControl> getCloudControlCallable()

Gets details about a cloud control. This method retrieves the latest major version of a cloud control that you identify by name.

By default, the latest major version of the cloud control is returned. To retrieve a specific major version, include `major_revision_id` in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetCloudControlRequest request =
           GetCloudControlRequest.newBuilder()
               .setName(
                   CloudControlName.ofOrganizationLocationCloudControlName(
                           "[ORGANIZATION]", "[LOCATION]", "[CLOUD_CONTROL]")
                       .toString())
               .setMajorRevisionId(612576889)
               .build();
       ApiFuture<CloudControl> future = configClient.getCloudControlCallable().futureCall(request);
       // Do something.
       CloudControl response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetCloudControlRequest),[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)>` |   
  
### getFramework(@Nullable FrameworkName name)
    
    
    public final Framework getFramework(@Nullable FrameworkName name)

Gets details about a framework. This method retrieves the latest major version of the framework.

To retrieve a specific major version, include `major_revision_id` in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       FrameworkName name =
           FrameworkName.ofOrganizationLocationFrameworkName(
               "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]");
       Framework response = configClient.getFramework(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.FrameworkName`  
Required. The name of the framework to retrieve, in one of the following formats: `organizations/{organization}/locations/{location}/frameworks/{framework}` or `projects/{project}/locations/{location}/frameworks/{framework}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### getFramework(GetFrameworkRequest request)
    
    
    public final Framework getFramework(GetFrameworkRequest request)

Gets details about a framework. This method retrieves the latest major version of the framework.

To retrieve a specific major version, include `major_revision_id` in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetFrameworkRequest request =
           GetFrameworkRequest.newBuilder()
               .setName(
                   FrameworkName.ofOrganizationLocationFrameworkName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]")
                       .toString())
               .setMajorRevisionId(612576889)
               .build();
       Framework response = configClient.getFramework(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetFrameworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### getFramework(String name)
    
    
    public final Framework getFramework(String name)

Gets details about a framework. This method retrieves the latest major version of the framework.

To retrieve a specific major version, include `major_revision_id` in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name =
           FrameworkName.ofOrganizationLocationFrameworkName(
                   "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]")
               .toString();
       Framework response = configClient.getFramework(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the framework to retrieve, in one of the following formats: `organizations/{organization}/locations/{location}/frameworks/{framework}` or `projects/{project}/locations/{location}/frameworks/{framework}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### getFrameworkCallable()
    
    
    public final UnaryCallable<GetFrameworkRequest,Framework> getFrameworkCallable()

Gets details about a framework. This method retrieves the latest major version of the framework.

To retrieve a specific major version, include `major_revision_id` in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetFrameworkRequest request =
           GetFrameworkRequest.newBuilder()
               .setName(
                   FrameworkName.ofOrganizationLocationFrameworkName(
                           "[ORGANIZATION]", "[LOCATION]", "[FRAMEWORK]")
                       .toString())
               .setMajorRevisionId(612576889)
               .build();
       ApiFuture<Framework> future = configClient.getFrameworkCallable().futureCall(request);
       // Do something.
       Framework response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetFrameworkRequest),[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = configClient.getLocation(request);
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
     try (ConfigClient configClient = ConfigClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = configClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable ConfigSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.ConfigSettings` |   
  
### getStub()
    
    
    public ConfigStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConfigStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.ConfigStub)` |   
  
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
  
### listCloudControls(@Nullable LocationName parent)
    
    
    public final ConfigClient.ListCloudControlsPagedResponse listCloudControls(@Nullable LocationName parent)

Lists the cloud controls (both built-in and custom) that are available in a given parent resource. The latest major version of each cloud control is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (CloudControl element : configClient.listCloudControls(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListCloudControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListCloudControlsPagedResponse)` |   
  
### listCloudControls(@Nullable OrganizationLocationName parent)
    
    
    public final ConfigClient.ListCloudControlsPagedResponse listCloudControls(@Nullable OrganizationLocationName parent)

Lists the cloud controls (both built-in and custom) that are available in a given parent resource. The latest major version of each cloud control is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (CloudControl element : configClient.listCloudControls(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListCloudControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListCloudControlsPagedResponse)` |   
  
### listCloudControls(ListCloudControlsRequest request)
    
    
    public final ConfigClient.ListCloudControlsPagedResponse listCloudControls(ListCloudControlsRequest request)

Lists the cloud controls (both built-in and custom) that are available in a given parent resource. The latest major version of each cloud control is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListCloudControlsRequest request =
           ListCloudControlsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (CloudControl element : configClient.listCloudControls(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCloudControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListCloudControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListCloudControlsPagedResponse)` |   
  
### listCloudControls(String parent)
    
    
    public final ConfigClient.ListCloudControlsPagedResponse listCloudControls(String parent)

Lists the cloud controls (both built-in and custom) that are available in a given parent resource. The latest major version of each cloud control is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (CloudControl element : configClient.listCloudControls(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListCloudControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListCloudControlsPagedResponse)` |   
  
### listCloudControlsCallable()
    
    
    public final UnaryCallable<ListCloudControlsRequest,ListCloudControlsResponse> listCloudControlsCallable()

Lists the cloud controls (both built-in and custom) that are available in a given parent resource. The latest major version of each cloud control is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListCloudControlsRequest request =
           ListCloudControlsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListCloudControlsResponse response = configClient.listCloudControlsCallable().call(request);
         for (CloudControl element : response.getCloudControlsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlsRequest),[ListCloudControlsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlsResponse)>` |   
  
### listCloudControlsPagedCallable()
    
    
    public final UnaryCallable<ListCloudControlsRequest,ConfigClient.ListCloudControlsPagedResponse> listCloudControlsPagedCallable()

Lists the cloud controls (both built-in and custom) that are available in a given parent resource. The latest major version of each cloud control is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListCloudControlsRequest request =
           ListCloudControlsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<CloudControl> future =
           configClient.listCloudControlsPagedCallable().futureCall(request);
       // Do something.
       for (CloudControl element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCloudControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlsRequest),[ListCloudControlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListCloudControlsPagedResponse)>` |   
  
### listFrameworks(@Nullable LocationName parent)
    
    
    public final ConfigClient.ListFrameworksPagedResponse listFrameworks(@Nullable LocationName parent)

Lists the frameworks (both built-in and custom) that are available within the parent resource. The latest major version of each framework is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Framework element : configClient.listFrameworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.LocationName`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListFrameworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListFrameworksPagedResponse)` |   
  
### listFrameworks(@Nullable OrganizationLocationName parent)
    
    
    public final ConfigClient.ListFrameworksPagedResponse listFrameworks(@Nullable OrganizationLocationName parent)

Lists the frameworks (both built-in and custom) that are available within the parent resource. The latest major version of each framework is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (Framework element : configClient.listFrameworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.OrganizationLocationName`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListFrameworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListFrameworksPagedResponse)` |   
  
### listFrameworks(ListFrameworksRequest request)
    
    
    public final ConfigClient.ListFrameworksPagedResponse listFrameworks(ListFrameworksRequest request)

Lists the frameworks (both built-in and custom) that are available within the parent resource. The latest major version of each framework is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListFrameworksRequest request =
           ListFrameworksRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Framework element : configClient.listFrameworks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFrameworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListFrameworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListFrameworksPagedResponse)` |   
  
### listFrameworks(String parent)
    
    
    public final ConfigClient.ListFrameworksPagedResponse listFrameworks(String parent)

Lists the frameworks (both built-in and custom) that are available within the parent resource. The latest major version of each framework is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (Framework element : configClient.listFrameworks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name, in one of the following formats: - `organizations/{organization}/locations/{location}` \- `projects/{project}/locations/{location}`. The only supported location is `global`.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListFrameworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListFrameworksPagedResponse)` |   
  
### listFrameworksCallable()
    
    
    public final UnaryCallable<ListFrameworksRequest,ListFrameworksResponse> listFrameworksCallable()

Lists the frameworks (both built-in and custom) that are available within the parent resource. The latest major version of each framework is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListFrameworksRequest request =
           ListFrameworksRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListFrameworksResponse response = configClient.listFrameworksCallable().call(request);
         for (Framework element : response.getFrameworksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFrameworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworksRequest),[ListFrameworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworksResponse)>` |   
  
### listFrameworksPagedCallable()
    
    
    public final UnaryCallable<ListFrameworksRequest,ConfigClient.ListFrameworksPagedResponse> listFrameworksPagedCallable()

Lists the frameworks (both built-in and custom) that are available within the parent resource. The latest major version of each framework is returned. This method supports pagination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListFrameworksRequest request =
           ListFrameworksRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Framework> future = configClient.listFrameworksPagedCallable().futureCall(request);
       // Do something.
       for (Framework element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFrameworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworksRequest),[ListFrameworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListFrameworksPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final ConfigClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : configClient.listLocations(request).iterateAll()) {
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
`[ConfigClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListLocationsPagedResponse)` |   
  
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
     try (ConfigClient configClient = ConfigClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = configClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ConfigClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = configClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCloudControl(CloudControl cloudControl, FieldMask updateMask)
    
    
    public final CloudControl updateCloudControl(CloudControl cloudControl, FieldMask updateMask)

Updates a custom cloud control. This method allows for partial updates of a cloud control. Use the `update_mask` to specify which fields to update. Consider the following:

\- If you provide an `update_mask`, only the fields that are specified in the mask are updated. - If you don't provide an `update_mask`, all the fields that are present in the request's `cloud_control` body are used to overwrite the existing resource.

You can only update cloud controls with the `CUSTOM` type. A successful update creates a new version of the cloud control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CloudControl cloudControl = CloudControl.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CloudControl response = configClient.updateCloudControl(cloudControl, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`cloudControl` | `[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)`  
Required. The cloud control that you're updating.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Use a field mask to specify the fields to be overwritten in the cloud control during the update. The fields that you specify in the `update_mask` are relative to the cloud control, not the full request. A field is overwritten if it is in the mask. If you don't provide a mask, all fields in the request are updated. You can update the following fields: \- Display name - Description - Parameters - Rules - Parameter specification  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### updateCloudControl(UpdateCloudControlRequest request)
    
    
    public final CloudControl updateCloudControl(UpdateCloudControlRequest request)

Updates a custom cloud control. This method allows for partial updates of a cloud control. Use the `update_mask` to specify which fields to update. Consider the following:

\- If you provide an `update_mask`, only the fields that are specified in the mask are updated. - If you don't provide an `update_mask`, all the fields that are present in the request's `cloud_control` body are used to overwrite the existing resource.

You can only update cloud controls with the `CUSTOM` type. A successful update creates a new version of the cloud control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateCloudControlRequest request =
           UpdateCloudControlRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCloudControl(CloudControl.newBuilder().build())
               .build();
       CloudControl response = configClient.updateCloudControl(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.UpdateCloudControlRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
  
### updateCloudControlCallable()
    
    
    public final UnaryCallable<UpdateCloudControlRequest,CloudControl> updateCloudControlCallable()

Updates a custom cloud control. This method allows for partial updates of a cloud control. Use the `update_mask` to specify which fields to update. Consider the following:

\- If you provide an `update_mask`, only the fields that are specified in the mask are updated. - If you don't provide an `update_mask`, all the fields that are present in the request's `cloud_control` body are used to overwrite the existing resource.

You can only update cloud controls with the `CUSTOM` type. A successful update creates a new version of the cloud control.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateCloudControlRequest request =
           UpdateCloudControlRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCloudControl(CloudControl.newBuilder().build())
               .build();
       ApiFuture<CloudControl> future =
           configClient.updateCloudControlCallable().futureCall(request);
       // Do something.
       CloudControl response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.UpdateCloudControlRequest),[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)>` |   
  
### updateFramework(Framework framework, FieldMask updateMask)
    
    
    public final Framework updateFramework(Framework framework, FieldMask updateMask)

Updates a custom framework. This method allows for partial updates of a framework. Use the `update_mask` to specify which fields to update. Consider the following:

\- If you provide an `update_mask`, only the fields that are specified in the mask are updated. - If you don't provide an `update_mask`, all the fields that are present in the request's `framework` body are used to overwrite the existing resource.

You can only update frameworks with the `CUSTOM` type. A successful update creates a new version of the framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       Framework framework = Framework.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Framework response = configClient.updateFramework(framework, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`framework` | `[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)`  
Required. The resource that is being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. A field mask is used to specify the fields to be overwritten in the framework resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If you don't provide a mask then all fields present in the request will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### updateFramework(UpdateFrameworkRequest request)
    
    
    public final Framework updateFramework(UpdateFrameworkRequest request)

Updates a custom framework. This method allows for partial updates of a framework. Use the `update_mask` to specify which fields to update. Consider the following:

\- If you provide an `update_mask`, only the fields that are specified in the mask are updated. - If you don't provide an `update_mask`, all the fields that are present in the request's `framework` body are used to overwrite the existing resource.

You can only update frameworks with the `CUSTOM` type. A successful update creates a new version of the framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateFrameworkRequest request =
           UpdateFrameworkRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setFramework(Framework.newBuilder().build())
               .setMajorRevisionId(612576889)
               .build();
       Framework response = configClient.updateFramework(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.UpdateFrameworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
  
### updateFrameworkCallable()
    
    
    public final UnaryCallable<UpdateFrameworkRequest,Framework> updateFrameworkCallable()

Updates a custom framework. This method allows for partial updates of a framework. Use the `update_mask` to specify which fields to update. Consider the following:

\- If you provide an `update_mask`, only the fields that are specified in the mask are updated. - If you don't provide an `update_mask`, all the fields that are present in the request's `framework` body are used to overwrite the existing resource.

You can only update frameworks with the `CUSTOM` type. A successful update creates a new version of the framework.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateFrameworkRequest request =
           UpdateFrameworkRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setFramework(Framework.newBuilder().build())
               .setMajorRevisionId(612576889)
               .build();
       ApiFuture<Framework> future = configClient.updateFrameworkCallable().futureCall(request);
       // Do something.
       Framework response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.UpdateFrameworkRequest),[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
