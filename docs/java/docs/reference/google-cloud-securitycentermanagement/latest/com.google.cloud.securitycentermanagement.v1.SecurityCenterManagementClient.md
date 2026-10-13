---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient
title: Class SecurityCenterManagementClient (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:20.117587+00:00
---

# Class SecurityCenterManagementClient (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityCenterManagementClient (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-securitycentermanagement/google-cloud-securitycentermanagement/src/main/java/com/google/cloud/securitycentermanagement/v1/SecurityCenterManagementClient.java)| [Product Reference](https://cloud.google.com/securitycentermanagement/docs/overview)  
---|---  
  
Service Description: Service describing handlers for resources

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       EffectiveSecurityHealthAnalyticsCustomModuleName name =
           EffectiveSecurityHealthAnalyticsCustomModuleName
               .ofProjectLocationEffectiveSecurityHealthAnalyticsCustomModuleName(
                   "[PROJECT]", "[LOCATION]", "[EFFECTIVE_SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]");
       EffectiveSecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.getEffectiveSecurityHealthAnalyticsCustomModule(name);
     }
     

Note: close() needs to be called on the SecurityCenterManagementClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListEffectiveSecurityHealthAnalyticsCustomModules |  Returns a list of all EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEffectiveSecurityHealthAnalyticsCustomModules(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEffectiveSecurityHealthAnalyticsCustomModules(FolderLocationName parent) 
  * listEffectiveSecurityHealthAnalyticsCustomModules(LocationName parent) 
  * listEffectiveSecurityHealthAnalyticsCustomModules(OrganizationLocationName parent) 
  * listEffectiveSecurityHealthAnalyticsCustomModules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEffectiveSecurityHealthAnalyticsCustomModulesPagedCallable() 
  * listEffectiveSecurityHealthAnalyticsCustomModulesCallable() 

  
GetEffectiveSecurityHealthAnalyticsCustomModule |  Gets details of a single EffectiveSecurityHealthAnalyticsCustomModule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEffectiveSecurityHealthAnalyticsCustomModule(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEffectiveSecurityHealthAnalyticsCustomModule(EffectiveSecurityHealthAnalyticsCustomModuleName name) 
  * getEffectiveSecurityHealthAnalyticsCustomModule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEffectiveSecurityHealthAnalyticsCustomModuleCallable() 

  
ListSecurityHealthAnalyticsCustomModules |  Returns a list of all SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSecurityHealthAnalyticsCustomModules(ListSecurityHealthAnalyticsCustomModulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSecurityHealthAnalyticsCustomModules(FolderLocationName parent) 
  * listSecurityHealthAnalyticsCustomModules(LocationName parent) 
  * listSecurityHealthAnalyticsCustomModules(OrganizationLocationName parent) 
  * listSecurityHealthAnalyticsCustomModules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSecurityHealthAnalyticsCustomModulesPagedCallable() 
  * listSecurityHealthAnalyticsCustomModulesCallable() 

  
ListDescendantSecurityHealthAnalyticsCustomModules |  Returns a list of all resident SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDescendantSecurityHealthAnalyticsCustomModules(ListDescendantSecurityHealthAnalyticsCustomModulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDescendantSecurityHealthAnalyticsCustomModules(FolderLocationName parent) 
  * listDescendantSecurityHealthAnalyticsCustomModules(LocationName parent) 
  * listDescendantSecurityHealthAnalyticsCustomModules(OrganizationLocationName parent) 
  * listDescendantSecurityHealthAnalyticsCustomModules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDescendantSecurityHealthAnalyticsCustomModulesPagedCallable() 
  * listDescendantSecurityHealthAnalyticsCustomModulesCallable() 

  
GetSecurityHealthAnalyticsCustomModule |  Retrieves a SecurityHealthAnalyticsCustomModule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSecurityHealthAnalyticsCustomModule(GetSecurityHealthAnalyticsCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSecurityHealthAnalyticsCustomModule(SecurityHealthAnalyticsCustomModuleName name) 
  * getSecurityHealthAnalyticsCustomModule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSecurityHealthAnalyticsCustomModuleCallable() 

  
CreateSecurityHealthAnalyticsCustomModule |  Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSecurityHealthAnalyticsCustomModule(CreateSecurityHealthAnalyticsCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSecurityHealthAnalyticsCustomModule(FolderLocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule) 
  * createSecurityHealthAnalyticsCustomModule(LocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule) 
  * createSecurityHealthAnalyticsCustomModule(OrganizationLocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule) 
  * createSecurityHealthAnalyticsCustomModule(String parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSecurityHealthAnalyticsCustomModuleCallable() 

  
UpdateSecurityHealthAnalyticsCustomModule |  Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSecurityHealthAnalyticsCustomModule(UpdateSecurityHealthAnalyticsCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSecurityHealthAnalyticsCustomModule(SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSecurityHealthAnalyticsCustomModuleCallable() 

  
DeleteSecurityHealthAnalyticsCustomModule |  Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSecurityHealthAnalyticsCustomModule(DeleteSecurityHealthAnalyticsCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSecurityHealthAnalyticsCustomModule(SecurityHealthAnalyticsCustomModuleName name) 
  * deleteSecurityHealthAnalyticsCustomModule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSecurityHealthAnalyticsCustomModuleCallable() 

  
SimulateSecurityHealthAnalyticsCustomModule |  Simulates the result of using a SecurityHealthAnalyticsCustomModule to check a resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * simulateSecurityHealthAnalyticsCustomModule(SimulateSecurityHealthAnalyticsCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * simulateSecurityHealthAnalyticsCustomModule(String parent, CustomConfig customConfig, SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * simulateSecurityHealthAnalyticsCustomModuleCallable() 

  
ListEffectiveEventThreatDetectionCustomModules |  Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEffectiveEventThreatDetectionCustomModules(ListEffectiveEventThreatDetectionCustomModulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEffectiveEventThreatDetectionCustomModules(FolderLocationName parent) 
  * listEffectiveEventThreatDetectionCustomModules(LocationName parent) 
  * listEffectiveEventThreatDetectionCustomModules(OrganizationLocationName parent) 
  * listEffectiveEventThreatDetectionCustomModules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEffectiveEventThreatDetectionCustomModulesPagedCallable() 
  * listEffectiveEventThreatDetectionCustomModulesCallable() 

  
GetEffectiveEventThreatDetectionCustomModule |  Gets the effective Event Threat Detection custom module at the given level.  The difference between an EffectiveEventThreatDetectionCustomModule and an EventThreatDetectionCustomModule is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEffectiveEventThreatDetectionCustomModule(GetEffectiveEventThreatDetectionCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEffectiveEventThreatDetectionCustomModule(EffectiveEventThreatDetectionCustomModuleName name) 
  * getEffectiveEventThreatDetectionCustomModule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEffectiveEventThreatDetectionCustomModuleCallable() 

  
ListEventThreatDetectionCustomModules |  Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEventThreatDetectionCustomModules(ListEventThreatDetectionCustomModulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEventThreatDetectionCustomModules(FolderLocationName parent) 
  * listEventThreatDetectionCustomModules(LocationName parent) 
  * listEventThreatDetectionCustomModules(OrganizationLocationName parent) 
  * listEventThreatDetectionCustomModules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEventThreatDetectionCustomModulesPagedCallable() 
  * listEventThreatDetectionCustomModulesCallable() 

  
ListDescendantEventThreatDetectionCustomModules |  Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDescendantEventThreatDetectionCustomModules(ListDescendantEventThreatDetectionCustomModulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDescendantEventThreatDetectionCustomModules(FolderLocationName parent) 
  * listDescendantEventThreatDetectionCustomModules(LocationName parent) 
  * listDescendantEventThreatDetectionCustomModules(OrganizationLocationName parent) 
  * listDescendantEventThreatDetectionCustomModules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDescendantEventThreatDetectionCustomModulesPagedCallable() 
  * listDescendantEventThreatDetectionCustomModulesCallable() 

  
GetEventThreatDetectionCustomModule |  Gets an Event Threat Detection custom module. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEventThreatDetectionCustomModule(GetEventThreatDetectionCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEventThreatDetectionCustomModule(EventThreatDetectionCustomModuleName name) 
  * getEventThreatDetectionCustomModule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEventThreatDetectionCustomModuleCallable() 

  
CreateEventThreatDetectionCustomModule |  Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEventThreatDetectionCustomModule(CreateEventThreatDetectionCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createEventThreatDetectionCustomModule(FolderLocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule) 
  * createEventThreatDetectionCustomModule(LocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule) 
  * createEventThreatDetectionCustomModule(OrganizationLocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule) 
  * createEventThreatDetectionCustomModule(String parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEventThreatDetectionCustomModuleCallable() 

  
UpdateEventThreatDetectionCustomModule |  Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEventThreatDetectionCustomModule(UpdateEventThreatDetectionCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEventThreatDetectionCustomModule(EventThreatDetectionCustomModule eventThreatDetectionCustomModule, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEventThreatDetectionCustomModuleCallable() 

  
DeleteEventThreatDetectionCustomModule |  Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEventThreatDetectionCustomModule(DeleteEventThreatDetectionCustomModuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteEventThreatDetectionCustomModule(EventThreatDetectionCustomModuleName name) 
  * deleteEventThreatDetectionCustomModule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEventThreatDetectionCustomModuleCallable() 

  
ValidateEventThreatDetectionCustomModule |  Validates the given Event Threat Detection custom module. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * validateEventThreatDetectionCustomModule(ValidateEventThreatDetectionCustomModuleRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * validateEventThreatDetectionCustomModuleCallable() 

  
GetSecurityCenterService |  Gets service settings for the specified Security Command Center service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSecurityCenterService(GetSecurityCenterServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSecurityCenterService(SecurityCenterServiceName name) 
  * getSecurityCenterService(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSecurityCenterServiceCallable() 

  
ListSecurityCenterServices |  Returns a list of all Security Command Center services for the given parent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSecurityCenterServices(ListSecurityCenterServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSecurityCenterServices(FolderLocationName parent) 
  * listSecurityCenterServices(LocationName parent) 
  * listSecurityCenterServices(OrganizationLocationName parent) 
  * listSecurityCenterServices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSecurityCenterServicesPagedCallable() 
  * listSecurityCenterServicesCallable() 

  
UpdateSecurityCenterService |  Updates a Security Command Center service using the given update mask. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSecurityCenterService(UpdateSecurityCenterServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSecurityCenterService(SecurityCenterService securityCenterService, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSecurityCenterServiceCallable() 

  
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

This class can be customized by passing in a custom instance of SecurityCenterManagementSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityCenterManagementSettings securityCenterManagementSettings =
         SecurityCenterManagementSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create(securityCenterManagementSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityCenterManagementSettings securityCenterManagementSettings =
         SecurityCenterManagementSettings.newBuilder().setEndpoint(myEndpoint).build();
     SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create(securityCenterManagementSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityCenterManagementSettings securityCenterManagementSettings =
         SecurityCenterManagementSettings.newHttpJsonBuilder().build();
     SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create(securityCenterManagementSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SecurityCenterManagementClient

## Static Methods 

### create()
    
    
    public static final SecurityCenterManagementClient create()

Constructs an instance of SecurityCenterManagementClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SecurityCenterManagementSettings settings)
    
    
    public static final SecurityCenterManagementClient create(SecurityCenterManagementSettings settings)

Constructs an instance of SecurityCenterManagementClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SecurityCenterManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SecurityCenterManagementStub stub)
    
    
    public static final SecurityCenterManagementClient create(SecurityCenterManagementStub stub)

Constructs an instance of SecurityCenterManagementClient, using the given stub for making calls. This is for advanced usage - prefer using create(SecurityCenterManagementSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecurityCenterManagementStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.stub.SecurityCenterManagementStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient)` |   
  
## Constructors 

### SecurityCenterManagementClient(SecurityCenterManagementSettings settings)
    
    
    protected SecurityCenterManagementClient(SecurityCenterManagementSettings settings)

Constructs an instance of SecurityCenterManagementClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SecurityCenterManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings)`  
  
  
### SecurityCenterManagementClient(SecurityCenterManagementStub stub)
    
    
    protected SecurityCenterManagementClient(SecurityCenterManagementStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecurityCenterManagementStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.stub.SecurityCenterManagementStub)`  
  
  
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

### createEventThreatDetectionCustomModule(@Nullable FolderLocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule)
    
    
    public final EventThreatDetectionCustomModule createEventThreatDetectionCustomModule(@Nullable FolderLocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       EventThreatDetectionCustomModule eventThreatDetectionCustomModule =
           EventThreatDetectionCustomModule.newBuilder().build();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.createEventThreatDetectionCustomModule(
               parent, eventThreatDetectionCustomModule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. Name of parent for the module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`eventThreatDetectionCustomModule` | `[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)`  
Required. The module to create. The EventThreatDetectionCustomModule.name field is ignored; Security Command Center generates the name.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### createEventThreatDetectionCustomModule(@Nullable LocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule)
    
    
    public final EventThreatDetectionCustomModule createEventThreatDetectionCustomModule(@Nullable LocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       EventThreatDetectionCustomModule eventThreatDetectionCustomModule =
           EventThreatDetectionCustomModule.newBuilder().build();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.createEventThreatDetectionCustomModule(
               parent, eventThreatDetectionCustomModule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. Name of parent for the module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`eventThreatDetectionCustomModule` | `[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)`  
Required. The module to create. The EventThreatDetectionCustomModule.name field is ignored; Security Command Center generates the name.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### createEventThreatDetectionCustomModule(@Nullable OrganizationLocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule)
    
    
    public final EventThreatDetectionCustomModule createEventThreatDetectionCustomModule(@Nullable OrganizationLocationName parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       EventThreatDetectionCustomModule eventThreatDetectionCustomModule =
           EventThreatDetectionCustomModule.newBuilder().build();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.createEventThreatDetectionCustomModule(
               parent, eventThreatDetectionCustomModule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. Name of parent for the module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`eventThreatDetectionCustomModule` | `[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)`  
Required. The module to create. The EventThreatDetectionCustomModule.name field is ignored; Security Command Center generates the name.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### createEventThreatDetectionCustomModule(CreateEventThreatDetectionCustomModuleRequest request)
    
    
    public final EventThreatDetectionCustomModule createEventThreatDetectionCustomModule(CreateEventThreatDetectionCustomModuleRequest request)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       CreateEventThreatDetectionCustomModuleRequest request =
           CreateEventThreatDetectionCustomModuleRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setEventThreatDetectionCustomModule(
                   EventThreatDetectionCustomModule.newBuilder().build())
               .setValidateOnly(true)
               .build();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.createEventThreatDetectionCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateEventThreatDetectionCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### createEventThreatDetectionCustomModule(String parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule)
    
    
    public final EventThreatDetectionCustomModule createEventThreatDetectionCustomModule(String parent, EventThreatDetectionCustomModule eventThreatDetectionCustomModule)

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       EventThreatDetectionCustomModule eventThreatDetectionCustomModule =
           EventThreatDetectionCustomModule.newBuilder().build();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.createEventThreatDetectionCustomModule(
               parent, eventThreatDetectionCustomModule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of parent for the module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`eventThreatDetectionCustomModule` | `[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)`  
Required. The module to create. The EventThreatDetectionCustomModule.name field is ignored; Security Command Center generates the name.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### createEventThreatDetectionCustomModuleCallable()
    
    
    public final UnaryCallable<CreateEventThreatDetectionCustomModuleRequest,EventThreatDetectionCustomModule> createEventThreatDetectionCustomModuleCallable()

Creates a resident Event Threat Detection custom module at the scope of the given organization, folder, or project, and creates inherited custom modules for all descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       CreateEventThreatDetectionCustomModuleRequest request =
           CreateEventThreatDetectionCustomModuleRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setEventThreatDetectionCustomModule(
                   EventThreatDetectionCustomModule.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<EventThreatDetectionCustomModule> future =
           securityCenterManagementClient
               .createEventThreatDetectionCustomModuleCallable()
               .futureCall(request);
       // Do something.
       EventThreatDetectionCustomModule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateEventThreatDetectionCustomModuleRequest),[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)>` |   
  
### createSecurityHealthAnalyticsCustomModule(@Nullable FolderLocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule)
    
    
    public final SecurityHealthAnalyticsCustomModule createSecurityHealthAnalyticsCustomModule(@Nullable FolderLocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule)

Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule =
           SecurityHealthAnalyticsCustomModule.newBuilder().build();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.createSecurityHealthAnalyticsCustomModule(
               parent, securityHealthAnalyticsCustomModule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. Name of the parent organization, folder, or project of the module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`securityHealthAnalyticsCustomModule` | `[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)`  
Required. The resource being created.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### createSecurityHealthAnalyticsCustomModule(@Nullable LocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule)
    
    
    public final SecurityHealthAnalyticsCustomModule createSecurityHealthAnalyticsCustomModule(@Nullable LocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule)

Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule =
           SecurityHealthAnalyticsCustomModule.newBuilder().build();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.createSecurityHealthAnalyticsCustomModule(
               parent, securityHealthAnalyticsCustomModule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. Name of the parent organization, folder, or project of the module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`securityHealthAnalyticsCustomModule` | `[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)`  
Required. The resource being created.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### createSecurityHealthAnalyticsCustomModule(@Nullable OrganizationLocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule)
    
    
    public final SecurityHealthAnalyticsCustomModule createSecurityHealthAnalyticsCustomModule(@Nullable OrganizationLocationName parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule)

Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule =
           SecurityHealthAnalyticsCustomModule.newBuilder().build();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.createSecurityHealthAnalyticsCustomModule(
               parent, securityHealthAnalyticsCustomModule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. Name of the parent organization, folder, or project of the module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`securityHealthAnalyticsCustomModule` | `[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)`  
Required. The resource being created.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### createSecurityHealthAnalyticsCustomModule(CreateSecurityHealthAnalyticsCustomModuleRequest request)
    
    
    public final SecurityHealthAnalyticsCustomModule createSecurityHealthAnalyticsCustomModule(CreateSecurityHealthAnalyticsCustomModuleRequest request)

Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       CreateSecurityHealthAnalyticsCustomModuleRequest request =
           CreateSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setSecurityHealthAnalyticsCustomModule(
                   SecurityHealthAnalyticsCustomModule.newBuilder().build())
               .setValidateOnly(true)
               .build();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.createSecurityHealthAnalyticsCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateSecurityHealthAnalyticsCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### createSecurityHealthAnalyticsCustomModule(String parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule)
    
    
    public final SecurityHealthAnalyticsCustomModule createSecurityHealthAnalyticsCustomModule(String parent, SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule)

Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule =
           SecurityHealthAnalyticsCustomModule.newBuilder().build();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.createSecurityHealthAnalyticsCustomModule(
               parent, securityHealthAnalyticsCustomModule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the parent organization, folder, or project of the module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
`securityHealthAnalyticsCustomModule` | `[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)`  
Required. The resource being created.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### createSecurityHealthAnalyticsCustomModuleCallable()
    
    
    public final UnaryCallable<CreateSecurityHealthAnalyticsCustomModuleRequest,SecurityHealthAnalyticsCustomModule> createSecurityHealthAnalyticsCustomModuleCallable()

Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given organization, folder, or project, and also creates inherited `SecurityHealthAnalyticsCustomModule` resources for all folders and projects that are descendants of the given parent. These modules are enabled by default.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       CreateSecurityHealthAnalyticsCustomModuleRequest request =
           CreateSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setSecurityHealthAnalyticsCustomModule(
                   SecurityHealthAnalyticsCustomModule.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<SecurityHealthAnalyticsCustomModule> future =
           securityCenterManagementClient
               .createSecurityHealthAnalyticsCustomModuleCallable()
               .futureCall(request);
       // Do something.
       SecurityHealthAnalyticsCustomModule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateSecurityHealthAnalyticsCustomModuleRequest),[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)>` |   
  
### deleteEventThreatDetectionCustomModule(@Nullable EventThreatDetectionCustomModuleName name)
    
    
    public final void deleteEventThreatDetectionCustomModule(@Nullable EventThreatDetectionCustomModuleName name)

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       EventThreatDetectionCustomModuleName name =
           EventThreatDetectionCustomModuleName
               .ofProjectLocationEventThreatDetectionCustomModuleName(
                   "[PROJECT]", "[LOCATION]", "[EVENT_THREAT_DETECTION_CUSTOM_MODULE]");
       securityCenterManagementClient.deleteEventThreatDetectionCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModuleName`  
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`

  
  
### deleteEventThreatDetectionCustomModule(DeleteEventThreatDetectionCustomModuleRequest request)
    
    
    public final void deleteEventThreatDetectionCustomModule(DeleteEventThreatDetectionCustomModuleRequest request)

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       DeleteEventThreatDetectionCustomModuleRequest request =
           DeleteEventThreatDetectionCustomModuleRequest.newBuilder()
               .setName(
                   EventThreatDetectionCustomModuleName
                       .ofProjectLocationEventThreatDetectionCustomModuleName(
                           "[PROJECT]", "[LOCATION]", "[EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
                       .toString())
               .setValidateOnly(true)
               .build();
       securityCenterManagementClient.deleteEventThreatDetectionCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteEventThreatDetectionCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteEventThreatDetectionCustomModule(String name)
    
    
    public final void deleteEventThreatDetectionCustomModule(String name)

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String name =
           EventThreatDetectionCustomModuleName
               .ofOrganizationLocationEventThreatDetectionCustomModuleName(
                   "[ORGANIZATION]", "[LOCATION]", "[EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
               .toString();
       securityCenterManagementClient.deleteEventThreatDetectionCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`

  
  
### deleteEventThreatDetectionCustomModuleCallable()
    
    
    public final UnaryCallable<DeleteEventThreatDetectionCustomModuleRequest,Empty> deleteEventThreatDetectionCustomModuleCallable()

Deletes the specified Event Threat Detection custom module and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       DeleteEventThreatDetectionCustomModuleRequest request =
           DeleteEventThreatDetectionCustomModuleRequest.newBuilder()
               .setName(
                   EventThreatDetectionCustomModuleName
                       .ofProjectLocationEventThreatDetectionCustomModuleName(
                           "[PROJECT]", "[LOCATION]", "[EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
                       .toString())
               .setValidateOnly(true)
               .build();
       ApiFuture<Empty> future =
           securityCenterManagementClient
               .deleteEventThreatDetectionCustomModuleCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteEventThreatDetectionCustomModuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSecurityHealthAnalyticsCustomModule(@Nullable SecurityHealthAnalyticsCustomModuleName name)
    
    
    public final void deleteSecurityHealthAnalyticsCustomModule(@Nullable SecurityHealthAnalyticsCustomModuleName name)

Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       SecurityHealthAnalyticsCustomModuleName name =
           SecurityHealthAnalyticsCustomModuleName
               .ofProjectLocationSecurityHealthAnalyticsCustomModuleName(
                   "[PROJECT]", "[LOCATION]", "[SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]");
       securityCenterManagementClient.deleteSecurityHealthAnalyticsCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModuleName`  
Required. The resource name of the SHA custom module, in one of the following formats: * `organizations/{organization}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}` * `folders/{folder}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}` * `projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`  
  
### deleteSecurityHealthAnalyticsCustomModule(DeleteSecurityHealthAnalyticsCustomModuleRequest request)
    
    
    public final void deleteSecurityHealthAnalyticsCustomModule(DeleteSecurityHealthAnalyticsCustomModuleRequest request)

Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       DeleteSecurityHealthAnalyticsCustomModuleRequest request =
           DeleteSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setName(
                   SecurityHealthAnalyticsCustomModuleName
                       .ofProjectLocationSecurityHealthAnalyticsCustomModuleName(
                           "[PROJECT]", "[LOCATION]", "[SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
                       .toString())
               .setValidateOnly(true)
               .build();
       securityCenterManagementClient.deleteSecurityHealthAnalyticsCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteSecurityHealthAnalyticsCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSecurityHealthAnalyticsCustomModule(String name)
    
    
    public final void deleteSecurityHealthAnalyticsCustomModule(String name)

Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String name =
           SecurityHealthAnalyticsCustomModuleName
               .ofOrganizationLocationSecurityHealthAnalyticsCustomModuleName(
                   "[ORGANIZATION]", "[LOCATION]", "[SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
               .toString();
       securityCenterManagementClient.deleteSecurityHealthAnalyticsCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the SHA custom module, in one of the following formats: * `organizations/{organization}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}` * `folders/{folder}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}` * `projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`  
  
### deleteSecurityHealthAnalyticsCustomModuleCallable()
    
    
    public final UnaryCallable<DeleteSecurityHealthAnalyticsCustomModuleRequest,Empty> deleteSecurityHealthAnalyticsCustomModuleCallable()

Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the resource hierarchy. This method is only supported for resident custom modules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       DeleteSecurityHealthAnalyticsCustomModuleRequest request =
           DeleteSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setName(
                   SecurityHealthAnalyticsCustomModuleName
                       .ofProjectLocationSecurityHealthAnalyticsCustomModuleName(
                           "[PROJECT]", "[LOCATION]", "[SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
                       .toString())
               .setValidateOnly(true)
               .build();
       ApiFuture<Empty> future =
           securityCenterManagementClient
               .deleteSecurityHealthAnalyticsCustomModuleCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteSecurityHealthAnalyticsCustomModuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getEffectiveEventThreatDetectionCustomModule(@Nullable EffectiveEventThreatDetectionCustomModuleName name)
    
    
    public final EffectiveEventThreatDetectionCustomModule getEffectiveEventThreatDetectionCustomModule(@Nullable EffectiveEventThreatDetectionCustomModuleName name)

Gets the effective Event Threat Detection custom module at the given level.

The difference between an EffectiveEventThreatDetectionCustomModule and an EventThreatDetectionCustomModule is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       EffectiveEventThreatDetectionCustomModuleName name =
           EffectiveEventThreatDetectionCustomModuleName
               .ofProjectLocationEffectiveEventThreatDetectionCustomModuleName(
                   "[PROJECT]", "[LOCATION]", "[EFFECTIVE_EVENT_THREAT_DETECTION_CUSTOM_MODULE]");
       EffectiveEventThreatDetectionCustomModule response =
           securityCenterManagementClient.getEffectiveEventThreatDetectionCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModuleName`  
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`
  * `folders/{folder}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`
  * `projects/{project}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`

  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule)` |   
  
### getEffectiveEventThreatDetectionCustomModule(GetEffectiveEventThreatDetectionCustomModuleRequest request)
    
    
    public final EffectiveEventThreatDetectionCustomModule getEffectiveEventThreatDetectionCustomModule(GetEffectiveEventThreatDetectionCustomModuleRequest request)

Gets the effective Event Threat Detection custom module at the given level.

The difference between an EffectiveEventThreatDetectionCustomModule and an EventThreatDetectionCustomModule is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetEffectiveEventThreatDetectionCustomModuleRequest request =
           GetEffectiveEventThreatDetectionCustomModuleRequest.newBuilder()
               .setName(
                   EffectiveEventThreatDetectionCustomModuleName
                       .ofProjectLocationEffectiveEventThreatDetectionCustomModuleName(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[EFFECTIVE_EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
                       .toString())
               .build();
       EffectiveEventThreatDetectionCustomModule response =
           securityCenterManagementClient.getEffectiveEventThreatDetectionCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEffectiveEventThreatDetectionCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule)` |   
  
### getEffectiveEventThreatDetectionCustomModule(String name)
    
    
    public final EffectiveEventThreatDetectionCustomModule getEffectiveEventThreatDetectionCustomModule(String name)

Gets the effective Event Threat Detection custom module at the given level.

The difference between an EffectiveEventThreatDetectionCustomModule and an EventThreatDetectionCustomModule is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String name =
           EffectiveEventThreatDetectionCustomModuleName
               .ofOrganizationLocationEffectiveEventThreatDetectionCustomModuleName(
                   "[ORGANIZATION]",
                   "[LOCATION]",
                   "[EFFECTIVE_EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
               .toString();
       EffectiveEventThreatDetectionCustomModule response =
           securityCenterManagementClient.getEffectiveEventThreatDetectionCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`
  * `folders/{folder}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`
  * `projects/{project}/locations/{location}/effectiveEventThreatDetectionCustomModules/{custom_module}`

  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule)` |   
  
### getEffectiveEventThreatDetectionCustomModuleCallable()
    
    
    public final UnaryCallable<GetEffectiveEventThreatDetectionCustomModuleRequest,EffectiveEventThreatDetectionCustomModule> getEffectiveEventThreatDetectionCustomModuleCallable()

Gets the effective Event Threat Detection custom module at the given level.

The difference between an EffectiveEventThreatDetectionCustomModule and an EventThreatDetectionCustomModule is that the fields for an `EffectiveEventThreatDetectionCustomModule` are computed from ancestors if needed. For example, the enablement state for an `EventThreatDetectionCustomModule` can be `ENABLED`, `DISABLED`, or `INHERITED`. In contrast, the enablement state for an `EffectiveEventThreatDetectionCustomModule` is always computed as `ENABLED` or `DISABLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetEffectiveEventThreatDetectionCustomModuleRequest request =
           GetEffectiveEventThreatDetectionCustomModuleRequest.newBuilder()
               .setName(
                   EffectiveEventThreatDetectionCustomModuleName
                       .ofProjectLocationEffectiveEventThreatDetectionCustomModuleName(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[EFFECTIVE_EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
                       .toString())
               .build();
       ApiFuture<EffectiveEventThreatDetectionCustomModule> future =
           securityCenterManagementClient
               .getEffectiveEventThreatDetectionCustomModuleCallable()
               .futureCall(request);
       // Do something.
       EffectiveEventThreatDetectionCustomModule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEffectiveEventThreatDetectionCustomModuleRequest),[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule)>` |   
  
### getEffectiveSecurityHealthAnalyticsCustomModule(@Nullable EffectiveSecurityHealthAnalyticsCustomModuleName name)
    
    
    public final EffectiveSecurityHealthAnalyticsCustomModule getEffectiveSecurityHealthAnalyticsCustomModule(@Nullable EffectiveSecurityHealthAnalyticsCustomModuleName name)

Gets details of a single EffectiveSecurityHealthAnalyticsCustomModule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       EffectiveSecurityHealthAnalyticsCustomModuleName name =
           EffectiveSecurityHealthAnalyticsCustomModuleName
               .ofProjectLocationEffectiveSecurityHealthAnalyticsCustomModuleName(
                   "[PROJECT]", "[LOCATION]", "[EFFECTIVE_SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]");
       EffectiveSecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.getEffectiveSecurityHealthAnalyticsCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModuleName`  
Required. The full resource name of the custom module, specified in one of the following formats: 

  * `organizations/organization/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`
  * `folders/folder/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`
  * `projects/project/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`

  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule)` |   
  
### getEffectiveSecurityHealthAnalyticsCustomModule(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request)
    
    
    public final EffectiveSecurityHealthAnalyticsCustomModule getEffectiveSecurityHealthAnalyticsCustomModule(GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request)

Gets details of a single EffectiveSecurityHealthAnalyticsCustomModule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request =
           GetEffectiveSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setName(
                   EffectiveSecurityHealthAnalyticsCustomModuleName
                       .ofProjectLocationEffectiveSecurityHealthAnalyticsCustomModuleName(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[EFFECTIVE_SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
                       .toString())
               .build();
       EffectiveSecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.getEffectiveSecurityHealthAnalyticsCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule)` |   
  
### getEffectiveSecurityHealthAnalyticsCustomModule(String name)
    
    
    public final EffectiveSecurityHealthAnalyticsCustomModule getEffectiveSecurityHealthAnalyticsCustomModule(String name)

Gets details of a single EffectiveSecurityHealthAnalyticsCustomModule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String name =
           EffectiveSecurityHealthAnalyticsCustomModuleName
               .ofOrganizationLocationEffectiveSecurityHealthAnalyticsCustomModuleName(
                   "[ORGANIZATION]",
                   "[LOCATION]",
                   "[EFFECTIVE_SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
               .toString();
       EffectiveSecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.getEffectiveSecurityHealthAnalyticsCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full resource name of the custom module, specified in one of the following formats: 

  * `organizations/organization/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`
  * `folders/folder/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`
  * `projects/project/{location}/effectiveSecurityHealthAnalyticsCustomModules/{custom_module}`

  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule)` |   
  
### getEffectiveSecurityHealthAnalyticsCustomModuleCallable()
    
    
    public final UnaryCallable<GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,EffectiveSecurityHealthAnalyticsCustomModule> getEffectiveSecurityHealthAnalyticsCustomModuleCallable()

Gets details of a single EffectiveSecurityHealthAnalyticsCustomModule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetEffectiveSecurityHealthAnalyticsCustomModuleRequest request =
           GetEffectiveSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setName(
                   EffectiveSecurityHealthAnalyticsCustomModuleName
                       .ofProjectLocationEffectiveSecurityHealthAnalyticsCustomModuleName(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[EFFECTIVE_SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
                       .toString())
               .build();
       ApiFuture<EffectiveSecurityHealthAnalyticsCustomModule> future =
           securityCenterManagementClient
               .getEffectiveSecurityHealthAnalyticsCustomModuleCallable()
               .futureCall(request);
       // Do something.
       EffectiveSecurityHealthAnalyticsCustomModule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest),[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule)>` |   
  
### getEventThreatDetectionCustomModule(@Nullable EventThreatDetectionCustomModuleName name)
    
    
    public final EventThreatDetectionCustomModule getEventThreatDetectionCustomModule(@Nullable EventThreatDetectionCustomModuleName name)

Gets an Event Threat Detection custom module.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       EventThreatDetectionCustomModuleName name =
           EventThreatDetectionCustomModuleName
               .ofProjectLocationEventThreatDetectionCustomModuleName(
                   "[PROJECT]", "[LOCATION]", "[EVENT_THREAT_DETECTION_CUSTOM_MODULE]");
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.getEventThreatDetectionCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModuleName`  
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`

  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### getEventThreatDetectionCustomModule(GetEventThreatDetectionCustomModuleRequest request)
    
    
    public final EventThreatDetectionCustomModule getEventThreatDetectionCustomModule(GetEventThreatDetectionCustomModuleRequest request)

Gets an Event Threat Detection custom module.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetEventThreatDetectionCustomModuleRequest request =
           GetEventThreatDetectionCustomModuleRequest.newBuilder()
               .setName(
                   EventThreatDetectionCustomModuleName
                       .ofProjectLocationEventThreatDetectionCustomModuleName(
                           "[PROJECT]", "[LOCATION]", "[EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
                       .toString())
               .build();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.getEventThreatDetectionCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEventThreatDetectionCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### getEventThreatDetectionCustomModule(String name)
    
    
    public final EventThreatDetectionCustomModule getEventThreatDetectionCustomModule(String name)

Gets an Event Threat Detection custom module.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String name =
           EventThreatDetectionCustomModuleName
               .ofOrganizationLocationEventThreatDetectionCustomModuleName(
                   "[ORGANIZATION]", "[LOCATION]", "[EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
               .toString();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.getEventThreatDetectionCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Event Threat Detection custom module, in one of the following formats: 

  * `organizations/{organization}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `folders/{folder}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`
  * `projects/{project}/locations/{location}/eventThreatDetectionCustomModules/{custom_module}`

  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### getEventThreatDetectionCustomModuleCallable()
    
    
    public final UnaryCallable<GetEventThreatDetectionCustomModuleRequest,EventThreatDetectionCustomModule> getEventThreatDetectionCustomModuleCallable()

Gets an Event Threat Detection custom module.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetEventThreatDetectionCustomModuleRequest request =
           GetEventThreatDetectionCustomModuleRequest.newBuilder()
               .setName(
                   EventThreatDetectionCustomModuleName
                       .ofProjectLocationEventThreatDetectionCustomModuleName(
                           "[PROJECT]", "[LOCATION]", "[EVENT_THREAT_DETECTION_CUSTOM_MODULE]")
                       .toString())
               .build();
       ApiFuture<EventThreatDetectionCustomModule> future =
           securityCenterManagementClient
               .getEventThreatDetectionCustomModuleCallable()
               .futureCall(request);
       // Do something.
       EventThreatDetectionCustomModule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEventThreatDetectionCustomModuleRequest),[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = securityCenterManagementClient.getLocation(request);
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
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           securityCenterManagementClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSecurityCenterService(@Nullable SecurityCenterServiceName name)
    
    
    public final SecurityCenterService getSecurityCenterService(@Nullable SecurityCenterServiceName name)

Gets service settings for the specified Security Command Center service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       SecurityCenterServiceName name =
           SecurityCenterServiceName.ofProjectLocationServiceName(
               "[PROJECT]", "[LOCATION]", "[SERVICE]");
       SecurityCenterService response =
           securityCenterManagementClient.getSecurityCenterService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.SecurityCenterServiceName`  
Required. The Security Command Center service to retrieve, in one of the following formats: 

  * organizations/{organization}/locations/{location}/securityCenterServices/{service} 
  * folders/{folder}/locations/{location}/securityCenterServices/{service} 
  * projects/{project}/locations/{location}/securityCenterServices/{service} 

The following values are valid for `{service}`: 

  * `container-threat-detection`
  * `event-threat-detection`
  * `security-health-analytics`
  * `vm-threat-detection`
  * `web-security-scanner`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)` |   
  
### getSecurityCenterService(GetSecurityCenterServiceRequest request)
    
    
    public final SecurityCenterService getSecurityCenterService(GetSecurityCenterServiceRequest request)

Gets service settings for the specified Security Command Center service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetSecurityCenterServiceRequest request =
           GetSecurityCenterServiceRequest.newBuilder()
               .setName(
                   SecurityCenterServiceName.ofProjectLocationServiceName(
                           "[PROJECT]", "[LOCATION]", "[SERVICE]")
                       .toString())
               .setShowEligibleModulesOnly(true)
               .build();
       SecurityCenterService response =
           securityCenterManagementClient.getSecurityCenterService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetSecurityCenterServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)` |   
  
### getSecurityCenterService(String name)
    
    
    public final SecurityCenterService getSecurityCenterService(String name)

Gets service settings for the specified Security Command Center service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String name =
           SecurityCenterServiceName.ofProjectLocationServiceName(
                   "[PROJECT]", "[LOCATION]", "[SERVICE]")
               .toString();
       SecurityCenterService response =
           securityCenterManagementClient.getSecurityCenterService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Security Command Center service to retrieve, in one of the following formats: 

  * organizations/{organization}/locations/{location}/securityCenterServices/{service} 
  * folders/{folder}/locations/{location}/securityCenterServices/{service} 
  * projects/{project}/locations/{location}/securityCenterServices/{service} 

The following values are valid for `{service}`: 

  * `container-threat-detection`
  * `event-threat-detection`
  * `security-health-analytics`
  * `vm-threat-detection`
  * `web-security-scanner`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)` |   
  
### getSecurityCenterServiceCallable()
    
    
    public final UnaryCallable<GetSecurityCenterServiceRequest,SecurityCenterService> getSecurityCenterServiceCallable()

Gets service settings for the specified Security Command Center service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetSecurityCenterServiceRequest request =
           GetSecurityCenterServiceRequest.newBuilder()
               .setName(
                   SecurityCenterServiceName.ofProjectLocationServiceName(
                           "[PROJECT]", "[LOCATION]", "[SERVICE]")
                       .toString())
               .setShowEligibleModulesOnly(true)
               .build();
       ApiFuture<SecurityCenterService> future =
           securityCenterManagementClient.getSecurityCenterServiceCallable().futureCall(request);
       // Do something.
       SecurityCenterService response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetSecurityCenterServiceRequest),[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)>` |   
  
### getSecurityHealthAnalyticsCustomModule(@Nullable SecurityHealthAnalyticsCustomModuleName name)
    
    
    public final SecurityHealthAnalyticsCustomModule getSecurityHealthAnalyticsCustomModule(@Nullable SecurityHealthAnalyticsCustomModuleName name)

Retrieves a SecurityHealthAnalyticsCustomModule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       SecurityHealthAnalyticsCustomModuleName name =
           SecurityHealthAnalyticsCustomModuleName
               .ofProjectLocationSecurityHealthAnalyticsCustomModuleName(
                   "[PROJECT]", "[LOCATION]", "[SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]");
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.getSecurityHealthAnalyticsCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModuleName`  
Required. Name of the resource, in the format `projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### getSecurityHealthAnalyticsCustomModule(GetSecurityHealthAnalyticsCustomModuleRequest request)
    
    
    public final SecurityHealthAnalyticsCustomModule getSecurityHealthAnalyticsCustomModule(GetSecurityHealthAnalyticsCustomModuleRequest request)

Retrieves a SecurityHealthAnalyticsCustomModule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetSecurityHealthAnalyticsCustomModuleRequest request =
           GetSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setName(
                   SecurityHealthAnalyticsCustomModuleName
                       .ofProjectLocationSecurityHealthAnalyticsCustomModuleName(
                           "[PROJECT]", "[LOCATION]", "[SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
                       .toString())
               .build();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.getSecurityHealthAnalyticsCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetSecurityHealthAnalyticsCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### getSecurityHealthAnalyticsCustomModule(String name)
    
    
    public final SecurityHealthAnalyticsCustomModule getSecurityHealthAnalyticsCustomModule(String name)

Retrieves a SecurityHealthAnalyticsCustomModule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String name =
           SecurityHealthAnalyticsCustomModuleName
               .ofOrganizationLocationSecurityHealthAnalyticsCustomModuleName(
                   "[ORGANIZATION]", "[LOCATION]", "[SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
               .toString();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.getSecurityHealthAnalyticsCustomModule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource, in the format `projects/{project}/locations/{location}/securityHealthAnalyticsCustomModules/{custom_module}`.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### getSecurityHealthAnalyticsCustomModuleCallable()
    
    
    public final UnaryCallable<GetSecurityHealthAnalyticsCustomModuleRequest,SecurityHealthAnalyticsCustomModule> getSecurityHealthAnalyticsCustomModuleCallable()

Retrieves a SecurityHealthAnalyticsCustomModule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       GetSecurityHealthAnalyticsCustomModuleRequest request =
           GetSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setName(
                   SecurityHealthAnalyticsCustomModuleName
                       .ofProjectLocationSecurityHealthAnalyticsCustomModuleName(
                           "[PROJECT]", "[LOCATION]", "[SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE]")
                       .toString())
               .build();
       ApiFuture<SecurityHealthAnalyticsCustomModule> future =
           securityCenterManagementClient
               .getSecurityHealthAnalyticsCustomModuleCallable()
               .futureCall(request);
       // Do something.
       SecurityHealthAnalyticsCustomModule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetSecurityHealthAnalyticsCustomModuleRequest),[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)>` |   
  
### getSettings()
    
    
    public final @Nullable SecurityCenterManagementSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings` |   
  
### getStub()
    
    
    public SecurityCenterManagementStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.stub.SecurityCenterManagementStub)` |   
  
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
  
### listDescendantEventThreatDetectionCustomModules(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse listDescendantEventThreatDetectionCustomModules(@Nullable FolderLocationName parent)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listDescendantEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. Name of parent to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listDescendantEventThreatDetectionCustomModules(@Nullable LocationName parent)
    
    
    public final SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse listDescendantEventThreatDetectionCustomModules(@Nullable LocationName parent)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listDescendantEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. Name of parent to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listDescendantEventThreatDetectionCustomModules(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse listDescendantEventThreatDetectionCustomModules(@Nullable OrganizationLocationName parent)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listDescendantEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. Name of parent to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listDescendantEventThreatDetectionCustomModules(ListDescendantEventThreatDetectionCustomModulesRequest request)
    
    
    public final SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse listDescendantEventThreatDetectionCustomModules(ListDescendantEventThreatDetectionCustomModulesRequest request)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListDescendantEventThreatDetectionCustomModulesRequest request =
           ListDescendantEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listDescendantEventThreatDetectionCustomModules(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantEventThreatDetectionCustomModulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listDescendantEventThreatDetectionCustomModules(String parent)
    
    
    public final SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse listDescendantEventThreatDetectionCustomModules(String parent)

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listDescendantEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of parent to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listDescendantEventThreatDetectionCustomModulesCallable()
    
    
    public final UnaryCallable<ListDescendantEventThreatDetectionCustomModulesRequest,ListDescendantEventThreatDetectionCustomModulesResponse> listDescendantEventThreatDetectionCustomModulesCallable()

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListDescendantEventThreatDetectionCustomModulesRequest request =
           ListDescendantEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDescendantEventThreatDetectionCustomModulesResponse response =
             securityCenterManagementClient
                 .listDescendantEventThreatDetectionCustomModulesCallable()
                 .call(request);
         for (EventThreatDetectionCustomModule element :
             response.getEventThreatDetectionCustomModulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantEventThreatDetectionCustomModulesRequest),[ListDescendantEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantEventThreatDetectionCustomModulesResponse)>` |   
  
### listDescendantEventThreatDetectionCustomModulesPagedCallable()
    
    
    public final UnaryCallable<ListDescendantEventThreatDetectionCustomModulesRequest,SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse> listDescendantEventThreatDetectionCustomModulesPagedCallable()

Lists all resident Event Threat Detection custom modules for the given organization, folder, or project and its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListDescendantEventThreatDetectionCustomModulesRequest request =
           ListDescendantEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<EventThreatDetectionCustomModule> future =
           securityCenterManagementClient
               .listDescendantEventThreatDetectionCustomModulesPagedCallable()
               .futureCall(request);
       // Do something.
       for (EventThreatDetectionCustomModule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantEventThreatDetectionCustomModulesRequest),[ListDescendantEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse)>` |   
  
### listDescendantSecurityHealthAnalyticsCustomModules(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse listDescendantSecurityHealthAnalyticsCustomModules(@Nullable FolderLocationName parent)

Returns a list of all resident SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listDescendantSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listDescendantSecurityHealthAnalyticsCustomModules(@Nullable LocationName parent)
    
    
    public final SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse listDescendantSecurityHealthAnalyticsCustomModules(@Nullable LocationName parent)

Returns a list of all resident SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listDescendantSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listDescendantSecurityHealthAnalyticsCustomModules(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse listDescendantSecurityHealthAnalyticsCustomModules(@Nullable OrganizationLocationName parent)

Returns a list of all resident SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listDescendantSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listDescendantSecurityHealthAnalyticsCustomModules(ListDescendantSecurityHealthAnalyticsCustomModulesRequest request)
    
    
    public final SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse listDescendantSecurityHealthAnalyticsCustomModules(ListDescendantSecurityHealthAnalyticsCustomModulesRequest request)

Returns a list of all resident SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListDescendantSecurityHealthAnalyticsCustomModulesRequest request =
           ListDescendantSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listDescendantSecurityHealthAnalyticsCustomModules(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listDescendantSecurityHealthAnalyticsCustomModules(String parent)
    
    
    public final SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse listDescendantSecurityHealthAnalyticsCustomModules(String parent)

Returns a list of all resident SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listDescendantSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listDescendantSecurityHealthAnalyticsCustomModulesCallable()
    
    
    public final UnaryCallable<ListDescendantSecurityHealthAnalyticsCustomModulesRequest,ListDescendantSecurityHealthAnalyticsCustomModulesResponse> listDescendantSecurityHealthAnalyticsCustomModulesCallable()

Returns a list of all resident SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListDescendantSecurityHealthAnalyticsCustomModulesRequest request =
           ListDescendantSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDescendantSecurityHealthAnalyticsCustomModulesResponse response =
             securityCenterManagementClient
                 .listDescendantSecurityHealthAnalyticsCustomModulesCallable()
                 .call(request);
         for (SecurityHealthAnalyticsCustomModule element :
             response.getSecurityHealthAnalyticsCustomModulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest),[ListDescendantSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantSecurityHealthAnalyticsCustomModulesResponse)>` |   
  
### listDescendantSecurityHealthAnalyticsCustomModulesPagedCallable()
    
    
    public final UnaryCallable<ListDescendantSecurityHealthAnalyticsCustomModulesRequest,SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse> listDescendantSecurityHealthAnalyticsCustomModulesPagedCallable()

Returns a list of all resident SecurityHealthAnalyticsCustomModule resources under the given organization, folder, or project and all of its descendants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListDescendantSecurityHealthAnalyticsCustomModulesRequest request =
           ListDescendantSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SecurityHealthAnalyticsCustomModule> future =
           securityCenterManagementClient
               .listDescendantSecurityHealthAnalyticsCustomModulesPagedCallable()
               .futureCall(request);
       // Do something.
       for (SecurityHealthAnalyticsCustomModule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest),[ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse)>` |   
  
### listEffectiveEventThreatDetectionCustomModules(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse listEffectiveEventThreatDetectionCustomModules(@Nullable FolderLocationName parent)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (EffectiveEventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEffectiveEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. Name of parent to list effective custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEffectiveEventThreatDetectionCustomModules(@Nullable LocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse listEffectiveEventThreatDetectionCustomModules(@Nullable LocationName parent)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (EffectiveEventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEffectiveEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. Name of parent to list effective custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEffectiveEventThreatDetectionCustomModules(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse listEffectiveEventThreatDetectionCustomModules(@Nullable OrganizationLocationName parent)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (EffectiveEventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEffectiveEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. Name of parent to list effective custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEffectiveEventThreatDetectionCustomModules(ListEffectiveEventThreatDetectionCustomModulesRequest request)
    
    
    public final SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse listEffectiveEventThreatDetectionCustomModules(ListEffectiveEventThreatDetectionCustomModulesRequest request)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEffectiveEventThreatDetectionCustomModulesRequest request =
           ListEffectiveEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (EffectiveEventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEffectiveEventThreatDetectionCustomModules(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveEventThreatDetectionCustomModulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEffectiveEventThreatDetectionCustomModules(String parent)
    
    
    public final SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse listEffectiveEventThreatDetectionCustomModules(String parent)

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (EffectiveEventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEffectiveEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of parent to list effective custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEffectiveEventThreatDetectionCustomModulesCallable()
    
    
    public final UnaryCallable<ListEffectiveEventThreatDetectionCustomModulesRequest,ListEffectiveEventThreatDetectionCustomModulesResponse> listEffectiveEventThreatDetectionCustomModulesCallable()

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEffectiveEventThreatDetectionCustomModulesRequest request =
           ListEffectiveEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListEffectiveEventThreatDetectionCustomModulesResponse response =
             securityCenterManagementClient
                 .listEffectiveEventThreatDetectionCustomModulesCallable()
                 .call(request);
         for (EffectiveEventThreatDetectionCustomModule element :
             response.getEffectiveEventThreatDetectionCustomModulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveEventThreatDetectionCustomModulesRequest),[ListEffectiveEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveEventThreatDetectionCustomModulesResponse)>` |   
  
### listEffectiveEventThreatDetectionCustomModulesPagedCallable()
    
    
    public final UnaryCallable<ListEffectiveEventThreatDetectionCustomModulesRequest,SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse> listEffectiveEventThreatDetectionCustomModulesPagedCallable()

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEffectiveEventThreatDetectionCustomModulesRequest request =
           ListEffectiveEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<EffectiveEventThreatDetectionCustomModule> future =
           securityCenterManagementClient
               .listEffectiveEventThreatDetectionCustomModulesPagedCallable()
               .futureCall(request);
       // Do something.
       for (EffectiveEventThreatDetectionCustomModule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveEventThreatDetectionCustomModulesRequest),[ListEffectiveEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse)>` |   
  
### listEffectiveSecurityHealthAnalyticsCustomModules(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse listEffectiveSecurityHealthAnalyticsCustomModules(@Nullable FolderLocationName parent)

Returns a list of all EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (EffectiveSecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listEffectiveSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. Name of parent to list effective custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listEffectiveSecurityHealthAnalyticsCustomModules(@Nullable LocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse listEffectiveSecurityHealthAnalyticsCustomModules(@Nullable LocationName parent)

Returns a list of all EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (EffectiveSecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listEffectiveSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. Name of parent to list effective custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listEffectiveSecurityHealthAnalyticsCustomModules(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse listEffectiveSecurityHealthAnalyticsCustomModules(@Nullable OrganizationLocationName parent)

Returns a list of all EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (EffectiveSecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listEffectiveSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. Name of parent to list effective custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listEffectiveSecurityHealthAnalyticsCustomModules(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request)
    
    
    public final SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse listEffectiveSecurityHealthAnalyticsCustomModules(ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request)

Returns a list of all EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request =
           ListEffectiveSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (EffectiveSecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listEffectiveSecurityHealthAnalyticsCustomModules(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listEffectiveSecurityHealthAnalyticsCustomModules(String parent)
    
    
    public final SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse listEffectiveSecurityHealthAnalyticsCustomModules(String parent)

Returns a list of all EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (EffectiveSecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listEffectiveSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of parent to list effective custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listEffectiveSecurityHealthAnalyticsCustomModulesCallable()
    
    
    public final UnaryCallable<ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,ListEffectiveSecurityHealthAnalyticsCustomModulesResponse> listEffectiveSecurityHealthAnalyticsCustomModulesCallable()

Returns a list of all EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request =
           ListEffectiveSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListEffectiveSecurityHealthAnalyticsCustomModulesResponse response =
             securityCenterManagementClient
                 .listEffectiveSecurityHealthAnalyticsCustomModulesCallable()
                 .call(request);
         for (EffectiveSecurityHealthAnalyticsCustomModule element :
             response.getEffectiveSecurityHealthAnalyticsCustomModulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest),[ListEffectiveSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse)>` |   
  
### listEffectiveSecurityHealthAnalyticsCustomModulesPagedCallable()
    
    
    public final UnaryCallable<ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse> listEffectiveSecurityHealthAnalyticsCustomModulesPagedCallable()

Returns a list of all EffectiveSecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEffectiveSecurityHealthAnalyticsCustomModulesRequest request =
           ListEffectiveSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<EffectiveSecurityHealthAnalyticsCustomModule> future =
           securityCenterManagementClient
               .listEffectiveSecurityHealthAnalyticsCustomModulesPagedCallable()
               .futureCall(request);
       // Do something.
       for (EffectiveSecurityHealthAnalyticsCustomModule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest),[ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse)>` |   
  
### listEventThreatDetectionCustomModules(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse listEventThreatDetectionCustomModules(@Nullable FolderLocationName parent)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. Name of parent to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEventThreatDetectionCustomModules(@Nullable LocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse listEventThreatDetectionCustomModules(@Nullable LocationName parent)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. Name of parent to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEventThreatDetectionCustomModules(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse listEventThreatDetectionCustomModules(@Nullable OrganizationLocationName parent)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. Name of parent to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEventThreatDetectionCustomModules(ListEventThreatDetectionCustomModulesRequest request)
    
    
    public final SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse listEventThreatDetectionCustomModules(ListEventThreatDetectionCustomModulesRequest request)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEventThreatDetectionCustomModulesRequest request =
           ListEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEventThreatDetectionCustomModules(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEventThreatDetectionCustomModules(String parent)
    
    
    public final SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse listEventThreatDetectionCustomModules(String parent)

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (EventThreatDetectionCustomModule element :
           securityCenterManagementClient
               .listEventThreatDetectionCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of parent to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse)` |   
  
### listEventThreatDetectionCustomModulesCallable()
    
    
    public final UnaryCallable<ListEventThreatDetectionCustomModulesRequest,ListEventThreatDetectionCustomModulesResponse> listEventThreatDetectionCustomModulesCallable()

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEventThreatDetectionCustomModulesRequest request =
           ListEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListEventThreatDetectionCustomModulesResponse response =
             securityCenterManagementClient
                 .listEventThreatDetectionCustomModulesCallable()
                 .call(request);
         for (EventThreatDetectionCustomModule element :
             response.getEventThreatDetectionCustomModulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesRequest),[ListEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesResponse)>` |   
  
### listEventThreatDetectionCustomModulesPagedCallable()
    
    
    public final UnaryCallable<ListEventThreatDetectionCustomModulesRequest,SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse> listEventThreatDetectionCustomModulesPagedCallable()

Lists all Event Threat Detection custom modules for the given organization, folder, or project. This includes resident modules defined at the scope of the parent along with modules inherited from ancestors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListEventThreatDetectionCustomModulesRequest request =
           ListEventThreatDetectionCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<EventThreatDetectionCustomModule> future =
           securityCenterManagementClient
               .listEventThreatDetectionCustomModulesPagedCallable()
               .futureCall(request);
       // Do something.
       for (EventThreatDetectionCustomModule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesRequest),[ListEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final SecurityCenterManagementClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : securityCenterManagementClient.listLocations(request).iterateAll()) {
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
`[SecurityCenterManagementClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             securityCenterManagementClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SecurityCenterManagementClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           securityCenterManagementClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListLocationsPagedResponse)>` |   
  
### listSecurityCenterServices(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse listSecurityCenterServices(@Nullable FolderLocationName parent)

Returns a list of all Security Command Center services for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (SecurityCenterService element :
           securityCenterManagementClient.listSecurityCenterServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. The name of the parent to list Security Command Center services, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse)` |   
  
### listSecurityCenterServices(@Nullable LocationName parent)
    
    
    public final SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse listSecurityCenterServices(@Nullable LocationName parent)

Returns a list of all Security Command Center services for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SecurityCenterService element :
           securityCenterManagementClient.listSecurityCenterServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. The name of the parent to list Security Command Center services, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse)` |   
  
### listSecurityCenterServices(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse listSecurityCenterServices(@Nullable OrganizationLocationName parent)

Returns a list of all Security Command Center services for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (SecurityCenterService element :
           securityCenterManagementClient.listSecurityCenterServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. The name of the parent to list Security Command Center services, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse)` |   
  
### listSecurityCenterServices(ListSecurityCenterServicesRequest request)
    
    
    public final SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse listSecurityCenterServices(ListSecurityCenterServicesRequest request)

Returns a list of all Security Command Center services for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListSecurityCenterServicesRequest request =
           ListSecurityCenterServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowEligibleModulesOnly(true)
               .build();
       for (SecurityCenterService element :
           securityCenterManagementClient.listSecurityCenterServices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityCenterServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse)` |   
  
### listSecurityCenterServices(String parent)
    
    
    public final SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse listSecurityCenterServices(String parent)

Returns a list of all Security Command Center services for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (SecurityCenterService element :
           securityCenterManagementClient.listSecurityCenterServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent to list Security Command Center services, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse)` |   
  
### listSecurityCenterServicesCallable()
    
    
    public final UnaryCallable<ListSecurityCenterServicesRequest,ListSecurityCenterServicesResponse> listSecurityCenterServicesCallable()

Returns a list of all Security Command Center services for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListSecurityCenterServicesRequest request =
           ListSecurityCenterServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowEligibleModulesOnly(true)
               .build();
       while (true) {
         ListSecurityCenterServicesResponse response =
             securityCenterManagementClient.listSecurityCenterServicesCallable().call(request);
         for (SecurityCenterService element : response.getSecurityCenterServicesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityCenterServicesRequest),[ListSecurityCenterServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityCenterServicesResponse)>` |   
  
### listSecurityCenterServicesPagedCallable()
    
    
    public final UnaryCallable<ListSecurityCenterServicesRequest,SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse> listSecurityCenterServicesPagedCallable()

Returns a list of all Security Command Center services for the given parent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListSecurityCenterServicesRequest request =
           ListSecurityCenterServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowEligibleModulesOnly(true)
               .build();
       ApiFuture<SecurityCenterService> future =
           securityCenterManagementClient
               .listSecurityCenterServicesPagedCallable()
               .futureCall(request);
       // Do something.
       for (SecurityCenterService element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityCenterServicesRequest),[ListSecurityCenterServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse)>` |   
  
### listSecurityHealthAnalyticsCustomModules(@Nullable FolderLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse listSecurityHealthAnalyticsCustomModules(@Nullable FolderLocationName parent)

Returns a list of all SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.FolderLocationName`  
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listSecurityHealthAnalyticsCustomModules(@Nullable LocationName parent)
    
    
    public final SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse listSecurityHealthAnalyticsCustomModules(@Nullable LocationName parent)

Returns a list of all SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.LocationName`  
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listSecurityHealthAnalyticsCustomModules(@Nullable OrganizationLocationName parent)
    
    
    public final SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse listSecurityHealthAnalyticsCustomModules(@Nullable OrganizationLocationName parent)

Returns a list of all SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.securitycentermanagement.v1.OrganizationLocationName`  
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listSecurityHealthAnalyticsCustomModules(ListSecurityHealthAnalyticsCustomModulesRequest request)
    
    
    public final SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse listSecurityHealthAnalyticsCustomModules(ListSecurityHealthAnalyticsCustomModulesRequest request)

Returns a list of all SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListSecurityHealthAnalyticsCustomModulesRequest request =
           ListSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listSecurityHealthAnalyticsCustomModules(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listSecurityHealthAnalyticsCustomModules(String parent)
    
    
    public final SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse listSecurityHealthAnalyticsCustomModules(String parent)

Returns a list of all SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (SecurityHealthAnalyticsCustomModule element :
           securityCenterManagementClient
               .listSecurityHealthAnalyticsCustomModules(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the parent organization, folder, or project in which to list custom modules, in one of the following formats: 

  * `organizations/{organization}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `projects/{project}/locations/{location}`

  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse)` |   
  
### listSecurityHealthAnalyticsCustomModulesCallable()
    
    
    public final UnaryCallable<ListSecurityHealthAnalyticsCustomModulesRequest,ListSecurityHealthAnalyticsCustomModulesResponse> listSecurityHealthAnalyticsCustomModulesCallable()

Returns a list of all SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListSecurityHealthAnalyticsCustomModulesRequest request =
           ListSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSecurityHealthAnalyticsCustomModulesResponse response =
             securityCenterManagementClient
                 .listSecurityHealthAnalyticsCustomModulesCallable()
                 .call(request);
         for (SecurityHealthAnalyticsCustomModule element :
             response.getSecurityHealthAnalyticsCustomModulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesRequest),[ListSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesResponse)>` |   
  
### listSecurityHealthAnalyticsCustomModulesPagedCallable()
    
    
    public final UnaryCallable<ListSecurityHealthAnalyticsCustomModulesRequest,SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse> listSecurityHealthAnalyticsCustomModulesPagedCallable()

Returns a list of all SecurityHealthAnalyticsCustomModule resources for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from ancestor organizations, folders, and projects (no descendants).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ListSecurityHealthAnalyticsCustomModulesRequest request =
           ListSecurityHealthAnalyticsCustomModulesRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SecurityHealthAnalyticsCustomModule> future =
           securityCenterManagementClient
               .listSecurityHealthAnalyticsCustomModulesPagedCallable()
               .futureCall(request);
       // Do something.
       for (SecurityHealthAnalyticsCustomModule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesRequest),[ListSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### simulateSecurityHealthAnalyticsCustomModule(SimulateSecurityHealthAnalyticsCustomModuleRequest request)
    
    
    public final SimulateSecurityHealthAnalyticsCustomModuleResponse simulateSecurityHealthAnalyticsCustomModule(SimulateSecurityHealthAnalyticsCustomModuleRequest request)

Simulates the result of using a SecurityHealthAnalyticsCustomModule to check a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       SimulateSecurityHealthAnalyticsCustomModuleRequest request =
           SimulateSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setParent("parent-995424086")
               .setCustomConfig(CustomConfig.newBuilder().build())
               .setResource(
                   SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource.newBuilder()
                       .build())
               .build();
       SimulateSecurityHealthAnalyticsCustomModuleResponse response =
           securityCenterManagementClient.simulateSecurityHealthAnalyticsCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SimulateSecurityHealthAnalyticsCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SimulateSecurityHealthAnalyticsCustomModuleResponse)` |   
  
### simulateSecurityHealthAnalyticsCustomModule(String parent, CustomConfig customConfig, SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource resource)
    
    
    public final SimulateSecurityHealthAnalyticsCustomModuleResponse simulateSecurityHealthAnalyticsCustomModule(String parent, CustomConfig customConfig, SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource resource)

Simulates the result of using a SecurityHealthAnalyticsCustomModule to check a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       String parent = "parent-995424086";
       CustomConfig customConfig = CustomConfig.newBuilder().build();
       SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource resource =
           SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource.newBuilder().build();
       SimulateSecurityHealthAnalyticsCustomModuleResponse response =
           securityCenterManagementClient.simulateSecurityHealthAnalyticsCustomModule(
               parent, customConfig, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The relative resource name of the organization, project, or folder. For more information about relative resource names, see [AIP-122: Resource names](https://google.aip.dev/122). Example: `organizations/{organization_id}`.  
`customConfig` | `[CustomConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig)`  
Required. The custom configuration that you need to test.  
`resource` | `[SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource)`  
Required. Resource data to simulate custom module against.  
**Returns**  
---  
**Type** | **Description**  
`[SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SimulateSecurityHealthAnalyticsCustomModuleResponse)` |   
  
### simulateSecurityHealthAnalyticsCustomModuleCallable()
    
    
    public final UnaryCallable<SimulateSecurityHealthAnalyticsCustomModuleRequest,SimulateSecurityHealthAnalyticsCustomModuleResponse> simulateSecurityHealthAnalyticsCustomModuleCallable()

Simulates the result of using a SecurityHealthAnalyticsCustomModule to check a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       SimulateSecurityHealthAnalyticsCustomModuleRequest request =
           SimulateSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setParent("parent-995424086")
               .setCustomConfig(CustomConfig.newBuilder().build())
               .setResource(
                   SimulateSecurityHealthAnalyticsCustomModuleRequest.SimulatedResource.newBuilder()
                       .build())
               .build();
       ApiFuture<SimulateSecurityHealthAnalyticsCustomModuleResponse> future =
           securityCenterManagementClient
               .simulateSecurityHealthAnalyticsCustomModuleCallable()
               .futureCall(request);
       // Do something.
       SimulateSecurityHealthAnalyticsCustomModuleResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SimulateSecurityHealthAnalyticsCustomModuleRequest),[SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SimulateSecurityHealthAnalyticsCustomModuleResponse)>` |   
  
### updateEventThreatDetectionCustomModule(EventThreatDetectionCustomModule eventThreatDetectionCustomModule, FieldMask updateMask)
    
    
    public final EventThreatDetectionCustomModule updateEventThreatDetectionCustomModule(EventThreatDetectionCustomModule eventThreatDetectionCustomModule, FieldMask updateMask)

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       EventThreatDetectionCustomModule eventThreatDetectionCustomModule =
           EventThreatDetectionCustomModule.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.updateEventThreatDetectionCustomModule(
               eventThreatDetectionCustomModule, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`eventThreatDetectionCustomModule` | `[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)`  
Required. The module being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The fields to update. If omitted, then all fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### updateEventThreatDetectionCustomModule(UpdateEventThreatDetectionCustomModuleRequest request)
    
    
    public final EventThreatDetectionCustomModule updateEventThreatDetectionCustomModule(UpdateEventThreatDetectionCustomModuleRequest request)

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       UpdateEventThreatDetectionCustomModuleRequest request =
           UpdateEventThreatDetectionCustomModuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setEventThreatDetectionCustomModule(
                   EventThreatDetectionCustomModule.newBuilder().build())
               .setValidateOnly(true)
               .build();
       EventThreatDetectionCustomModule response =
           securityCenterManagementClient.updateEventThreatDetectionCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateEventThreatDetectionCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)` |   
  
### updateEventThreatDetectionCustomModuleCallable()
    
    
    public final UnaryCallable<UpdateEventThreatDetectionCustomModuleRequest,EventThreatDetectionCustomModule> updateEventThreatDetectionCustomModuleCallable()

Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       UpdateEventThreatDetectionCustomModuleRequest request =
           UpdateEventThreatDetectionCustomModuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setEventThreatDetectionCustomModule(
                   EventThreatDetectionCustomModule.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<EventThreatDetectionCustomModule> future =
           securityCenterManagementClient
               .updateEventThreatDetectionCustomModuleCallable()
               .futureCall(request);
       // Do something.
       EventThreatDetectionCustomModule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateEventThreatDetectionCustomModuleRequest),[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)>` |   
  
### updateSecurityCenterService(SecurityCenterService securityCenterService, FieldMask updateMask)
    
    
    public final SecurityCenterService updateSecurityCenterService(SecurityCenterService securityCenterService, FieldMask updateMask)

Updates a Security Command Center service using the given update mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       SecurityCenterService securityCenterService = SecurityCenterService.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SecurityCenterService response =
           securityCenterManagementClient.updateSecurityCenterService(
               securityCenterService, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securityCenterService` | `[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)`  
Required. The updated service.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The fields to update. Accepts the following values: 

  * `intended_enablement_state`
  * `modules`

If omitted, then all eligible fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)` |   
  
### updateSecurityCenterService(UpdateSecurityCenterServiceRequest request)
    
    
    public final SecurityCenterService updateSecurityCenterService(UpdateSecurityCenterServiceRequest request)

Updates a Security Command Center service using the given update mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       UpdateSecurityCenterServiceRequest request =
           UpdateSecurityCenterServiceRequest.newBuilder()
               .setSecurityCenterService(SecurityCenterService.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       SecurityCenterService response =
           securityCenterManagementClient.updateSecurityCenterService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateSecurityCenterServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)` |   
  
### updateSecurityCenterServiceCallable()
    
    
    public final UnaryCallable<UpdateSecurityCenterServiceRequest,SecurityCenterService> updateSecurityCenterServiceCallable()

Updates a Security Command Center service using the given update mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       UpdateSecurityCenterServiceRequest request =
           UpdateSecurityCenterServiceRequest.newBuilder()
               .setSecurityCenterService(SecurityCenterService.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<SecurityCenterService> future =
           securityCenterManagementClient.updateSecurityCenterServiceCallable().futureCall(request);
       // Do something.
       SecurityCenterService response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateSecurityCenterServiceRequest),[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)>` |   
  
### updateSecurityHealthAnalyticsCustomModule(SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule, FieldMask updateMask)
    
    
    public final SecurityHealthAnalyticsCustomModule updateSecurityHealthAnalyticsCustomModule(SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule, FieldMask updateMask)

Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       SecurityHealthAnalyticsCustomModule securityHealthAnalyticsCustomModule =
           SecurityHealthAnalyticsCustomModule.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.updateSecurityHealthAnalyticsCustomModule(
               securityHealthAnalyticsCustomModule, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securityHealthAnalyticsCustomModule` | `[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The fields to update. The following values are valid: 

  * `custom_config`
  * `enablement_state`

If you omit this field or set it to the wildcard value `*`, then all eligible fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### updateSecurityHealthAnalyticsCustomModule(UpdateSecurityHealthAnalyticsCustomModuleRequest request)
    
    
    public final SecurityHealthAnalyticsCustomModule updateSecurityHealthAnalyticsCustomModule(UpdateSecurityHealthAnalyticsCustomModuleRequest request)

Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       UpdateSecurityHealthAnalyticsCustomModuleRequest request =
           UpdateSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSecurityHealthAnalyticsCustomModule(
                   SecurityHealthAnalyticsCustomModule.newBuilder().build())
               .setValidateOnly(true)
               .build();
       SecurityHealthAnalyticsCustomModule response =
           securityCenterManagementClient.updateSecurityHealthAnalyticsCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateSecurityHealthAnalyticsCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)` |   
  
### updateSecurityHealthAnalyticsCustomModuleCallable()
    
    
    public final UnaryCallable<UpdateSecurityHealthAnalyticsCustomModuleRequest,SecurityHealthAnalyticsCustomModule> updateSecurityHealthAnalyticsCustomModuleCallable()

Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom configuration of a module is supported on resident modules only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       UpdateSecurityHealthAnalyticsCustomModuleRequest request =
           UpdateSecurityHealthAnalyticsCustomModuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setSecurityHealthAnalyticsCustomModule(
                   SecurityHealthAnalyticsCustomModule.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<SecurityHealthAnalyticsCustomModule> future =
           securityCenterManagementClient
               .updateSecurityHealthAnalyticsCustomModuleCallable()
               .futureCall(request);
       // Do something.
       SecurityHealthAnalyticsCustomModule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateSecurityHealthAnalyticsCustomModuleRequest),[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)>` |   
  
### validateEventThreatDetectionCustomModule(ValidateEventThreatDetectionCustomModuleRequest request)
    
    
    public final ValidateEventThreatDetectionCustomModuleResponse validateEventThreatDetectionCustomModule(ValidateEventThreatDetectionCustomModuleRequest request)

Validates the given Event Threat Detection custom module.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ValidateEventThreatDetectionCustomModuleRequest request =
           ValidateEventThreatDetectionCustomModuleRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setRawText("rawText985734517")
               .setType("type3575610")
               .build();
       ValidateEventThreatDetectionCustomModuleResponse response =
           securityCenterManagementClient.validateEventThreatDetectionCustomModule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ValidateEventThreatDetectionCustomModuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ValidateEventThreatDetectionCustomModuleResponse)` |   
  
### validateEventThreatDetectionCustomModuleCallable()
    
    
    public final UnaryCallable<ValidateEventThreatDetectionCustomModuleRequest,ValidateEventThreatDetectionCustomModuleResponse> validateEventThreatDetectionCustomModuleCallable()

Validates the given Event Threat Detection custom module.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SecurityCenterManagementClient securityCenterManagementClient =
         SecurityCenterManagementClient.create()) {
       ValidateEventThreatDetectionCustomModuleRequest request =
           ValidateEventThreatDetectionCustomModuleRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setRawText("rawText985734517")
               .setType("type3575610")
               .build();
       ApiFuture<ValidateEventThreatDetectionCustomModuleResponse> future =
           securityCenterManagementClient
               .validateEventThreatDetectionCustomModuleCallable()
               .futureCall(request);
       // Do something.
       ValidateEventThreatDetectionCustomModuleResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ValidateEventThreatDetectionCustomModuleRequest),[ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ValidateEventThreatDetectionCustomModuleResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
