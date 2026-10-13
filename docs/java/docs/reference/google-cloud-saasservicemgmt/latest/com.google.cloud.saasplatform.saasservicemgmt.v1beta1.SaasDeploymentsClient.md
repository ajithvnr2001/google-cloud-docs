---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient
title: Class SaasDeploymentsClient (0.29.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:52.347320+00:00
---

# Class SaasDeploymentsClient (0.29.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SaasDeploymentsClient (0.29.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.0 (latest)  0.25.0  0.24.0  0.23.0  0.21.0  0.18.0  0.17.0  0.15.0  0.13.0  0.12.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-saasservicemgmt/google-cloud-saasservicemgmt/src/main/java/com/google/cloud/saasplatform/saasservicemgmt/v1beta1/SaasDeploymentsClient.java)| [Product Reference](https://cloud.google.com/saas-runtime/docs/overview)| [RPC Documentation](https://cloud.google.com/saas-runtime/docs/apis)  
---|---|---  
  
Service Description: Manages the deployment of SaaS services.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       SaasName name = SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]");
       Saas response = saasDeploymentsClient.getSaas(name);
     }
     

Note: close() needs to be called on the SaasDeploymentsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListSaas |  Retrieve a collection of saas. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSaas(ListSaasRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSaas(LocationName parent) 
  * listSaas(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSaasPagedCallable() 
  * listSaasCallable() 

  
GetSaas |  Retrieve a single saas. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSaas(GetSaasRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSaas(SaasName name) 
  * getSaas(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSaasCallable() 

  
CreateSaas |  Create a new saas. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSaas(CreateSaasRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSaas(LocationName parent, Saas saas, String saasId) 
  * createSaas(String parent, Saas saas, String saasId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSaasCallable() 

  
UpdateSaas |  Update a single saas. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSaas(UpdateSaasRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSaas(Saas saas, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSaasCallable() 

  
DeleteSaas |  Delete a single saas. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSaas(DeleteSaasRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSaas(SaasName name) 
  * deleteSaas(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSaasCallable() 

  
ListTenants |  Retrieve a collection of tenants. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTenants(ListTenantsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTenants(LocationName parent) 
  * listTenants(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTenantsPagedCallable() 
  * listTenantsCallable() 

  
GetTenant |  Retrieve a single tenant. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTenant(GetTenantRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTenant(TenantName name) 
  * getTenant(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTenantCallable() 

  
CreateTenant |  Create a new tenant. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTenant(CreateTenantRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTenant(LocationName parent, Tenant tenant, String tenantId) 
  * createTenant(String parent, Tenant tenant, String tenantId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTenantCallable() 

  
UpdateTenant |  Update a single tenant. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTenant(UpdateTenantRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTenant(Tenant tenant, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTenantCallable() 

  
DeleteTenant |  Delete a single tenant. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTenant(DeleteTenantRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteTenant(TenantName name) 
  * deleteTenant(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTenantCallable() 

  
ListUnitKinds |  Retrieve a collection of unit kinds. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUnitKinds(ListUnitKindsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUnitKinds(LocationName parent) 
  * listUnitKinds(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUnitKindsPagedCallable() 
  * listUnitKindsCallable() 

  
GetUnitKind |  Retrieve a single unit kind. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUnitKind(GetUnitKindRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUnitKind(UnitKindName name) 
  * getUnitKind(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUnitKindCallable() 

  
CreateUnitKind |  Create a new unit kind. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUnitKind(CreateUnitKindRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUnitKind(LocationName parent, UnitKind unitKind, String unitKindId) 
  * createUnitKind(String parent, UnitKind unitKind, String unitKindId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUnitKindCallable() 

  
UpdateUnitKind |  Update a single unit kind. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUnitKind(UpdateUnitKindRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUnitKind(UnitKind unitKind, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUnitKindCallable() 

  
DeleteUnitKind |  Delete a single unit kind. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUnitKind(DeleteUnitKindRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUnitKind(UnitKindName name) 
  * deleteUnitKind(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUnitKindCallable() 

  
ListUnits |  Retrieve a collection of units. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUnits(ListUnitsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUnits(LocationName parent) 
  * listUnits(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUnitsPagedCallable() 
  * listUnitsCallable() 

  
GetUnit |  Retrieve a single unit. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUnit(GetUnitRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUnit(UnitName name) 
  * getUnit(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUnitCallable() 

  
CreateUnit |  Create a new unit. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUnit(CreateUnitRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUnit(LocationName parent, Unit unit, String unitId) 
  * createUnit(String parent, Unit unit, String unitId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUnitCallable() 

  
UpdateUnit |  Update a single unit. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUnit(UpdateUnitRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUnit(Unit unit, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUnitCallable() 

  
DeleteUnit |  Delete a single unit. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUnit(DeleteUnitRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUnit(UnitName name) 
  * deleteUnit(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUnitCallable() 

  
ListUnitOperations |  Retrieve a collection of unit operations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUnitOperations(ListUnitOperationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUnitOperations(LocationName parent) 
  * listUnitOperations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUnitOperationsPagedCallable() 
  * listUnitOperationsCallable() 

  
GetUnitOperation |  Retrieve a single unit operation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUnitOperation(GetUnitOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUnitOperation(UnitOperationName name) 
  * getUnitOperation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUnitOperationCallable() 

  
CreateUnitOperation |  Create a new unit operation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUnitOperation(CreateUnitOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUnitOperation(LocationName parent, UnitOperation unitOperation, String unitOperationId) 
  * createUnitOperation(String parent, UnitOperation unitOperation, String unitOperationId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUnitOperationCallable() 

  
UpdateUnitOperation |  Update a single unit operation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUnitOperation(UpdateUnitOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUnitOperation(UnitOperation unitOperation, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUnitOperationCallable() 

  
DeleteUnitOperation |  Delete a single unit operation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUnitOperation(DeleteUnitOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUnitOperation(UnitOperationName name) 
  * deleteUnitOperation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUnitOperationCallable() 

  
ListReleases |  Retrieve a collection of releases. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReleases(ListReleasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReleases(LocationName parent) 
  * listReleases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReleasesPagedCallable() 
  * listReleasesCallable() 

  
GetRelease |  Retrieve a single release. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRelease(GetReleaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRelease(ReleaseName name) 
  * getRelease(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getReleaseCallable() 

  
CreateRelease |  Create a new release. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRelease(CreateReleaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createRelease(LocationName parent, Release release, String releaseId) 
  * createRelease(String parent, Release release, String releaseId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createReleaseCallable() 

  
UpdateRelease |  Update a single release. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRelease(UpdateReleaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRelease(Release release, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateReleaseCallable() 

  
DeleteRelease |  Delete a single release. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRelease(DeleteReleaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteRelease(ReleaseName name) 
  * deleteRelease(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteReleaseCallable() 

  
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

This class can be customized by passing in a custom instance of SaasDeploymentsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SaasDeploymentsSettings saasDeploymentsSettings =
         SaasDeploymentsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SaasDeploymentsClient saasDeploymentsClient =
         SaasDeploymentsClient.create(saasDeploymentsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SaasDeploymentsSettings saasDeploymentsSettings =
         SaasDeploymentsSettings.newBuilder().setEndpoint(myEndpoint).build();
     SaasDeploymentsClient saasDeploymentsClient =
         SaasDeploymentsClient.create(saasDeploymentsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SaasDeploymentsSettings saasDeploymentsSettings =
         SaasDeploymentsSettings.newHttpJsonBuilder().build();
     SaasDeploymentsClient saasDeploymentsClient =
         SaasDeploymentsClient.create(saasDeploymentsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SaasDeploymentsClient

## Static Methods 

### create()
    
    
    public static final SaasDeploymentsClient create()

Constructs an instance of SaasDeploymentsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SaasDeploymentsSettings settings)
    
    
    public static final SaasDeploymentsClient create(SaasDeploymentsSettings settings)

Constructs an instance of SaasDeploymentsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SaasDeploymentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SaasDeploymentsStub stub)
    
    
    public static final SaasDeploymentsClient create(SaasDeploymentsStub stub)

Constructs an instance of SaasDeploymentsClient, using the given stub for making calls. This is for advanced usage - prefer using create(SaasDeploymentsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SaasDeploymentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.stub.SaasDeploymentsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient)` |   
  
## Constructors 

### SaasDeploymentsClient(SaasDeploymentsSettings settings)
    
    
    protected SaasDeploymentsClient(SaasDeploymentsSettings settings)

Constructs an instance of SaasDeploymentsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SaasDeploymentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsSettings)`  
  
  
### SaasDeploymentsClient(SaasDeploymentsStub stub)
    
    
    protected SaasDeploymentsClient(SaasDeploymentsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SaasDeploymentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.stub.SaasDeploymentsStub)`  
  
  
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

### createRelease(@Nullable LocationName parent, Release release, String releaseId)
    
    
    public final Release createRelease(@Nullable LocationName parent, Release release, String releaseId)

Create a new release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Release release = Release.newBuilder().build();
       String releaseId = "releaseId89607042";
       Release response = saasDeploymentsClient.createRelease(parent, release, releaseId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the release.  
`release` | `[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)`  
Required. The desired state for the release.  
`releaseId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new release.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)` |   
  
### createRelease(CreateReleaseRequest request)
    
    
    public final Release createRelease(CreateReleaseRequest request)

Create a new release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateReleaseRequest request =
           CreateReleaseRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setReleaseId("releaseId89607042")
               .setRelease(Release.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       Release response = saasDeploymentsClient.createRelease(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateReleaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)` |   
  
### createRelease(String parent, Release release, String releaseId)
    
    
    public final Release createRelease(String parent, Release release, String releaseId)

Create a new release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Release release = Release.newBuilder().build();
       String releaseId = "releaseId89607042";
       Release response = saasDeploymentsClient.createRelease(parent, release, releaseId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the release.  
`release` | `[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)`  
Required. The desired state for the release.  
`releaseId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new release.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)` |   
  
### createReleaseCallable()
    
    
    public final UnaryCallable<CreateReleaseRequest,Release> createReleaseCallable()

Create a new release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateReleaseRequest request =
           CreateReleaseRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setReleaseId("releaseId89607042")
               .setRelease(Release.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Release> future = saasDeploymentsClient.createReleaseCallable().futureCall(request);
       // Do something.
       Release response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateReleaseRequest),[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)>` |   
  
### createSaas(@Nullable LocationName parent, Saas saas, String saasId)
    
    
    public final Saas createSaas(@Nullable LocationName parent, Saas saas, String saasId)

Create a new saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Saas saas = Saas.newBuilder().build();
       String saasId = "saasId-910030789";
       Saas response = saasDeploymentsClient.createSaas(parent, saas, saasId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the saas.  
`saas` | `[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)`  
Required. The desired state for the saas.  
`saasId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new saas.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)` |   
  
### createSaas(CreateSaasRequest request)
    
    
    public final Saas createSaas(CreateSaasRequest request)

Create a new saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateSaasRequest request =
           CreateSaasRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSaasId("saasId-910030789")
               .setSaas(Saas.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       Saas response = saasDeploymentsClient.createSaas(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateSaasRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)` |   
  
### createSaas(String parent, Saas saas, String saasId)
    
    
    public final Saas createSaas(String parent, Saas saas, String saasId)

Create a new saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Saas saas = Saas.newBuilder().build();
       String saasId = "saasId-910030789";
       Saas response = saasDeploymentsClient.createSaas(parent, saas, saasId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the saas.  
`saas` | `[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)`  
Required. The desired state for the saas.  
`saasId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new saas.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)` |   
  
### createSaasCallable()
    
    
    public final UnaryCallable<CreateSaasRequest,Saas> createSaasCallable()

Create a new saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateSaasRequest request =
           CreateSaasRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSaasId("saasId-910030789")
               .setSaas(Saas.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Saas> future = saasDeploymentsClient.createSaasCallable().futureCall(request);
       // Do something.
       Saas response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateSaasRequest),[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)>` |   
  
### createTenant(@Nullable LocationName parent, Tenant tenant, String tenantId)
    
    
    public final Tenant createTenant(@Nullable LocationName parent, Tenant tenant, String tenantId)

Create a new tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Tenant tenant = Tenant.newBuilder().build();
       String tenantId = "tenantId-1306693787";
       Tenant response = saasDeploymentsClient.createTenant(parent, tenant, tenantId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the tenant.  
`tenant` | `[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)`  
Required. The desired state for the tenant.  
`tenantId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new tenant.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)` |   
  
### createTenant(CreateTenantRequest request)
    
    
    public final Tenant createTenant(CreateTenantRequest request)

Create a new tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateTenantRequest request =
           CreateTenantRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTenantId("tenantId-1306693787")
               .setTenant(Tenant.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       Tenant response = saasDeploymentsClient.createTenant(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateTenantRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)` |   
  
### createTenant(String parent, Tenant tenant, String tenantId)
    
    
    public final Tenant createTenant(String parent, Tenant tenant, String tenantId)

Create a new tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Tenant tenant = Tenant.newBuilder().build();
       String tenantId = "tenantId-1306693787";
       Tenant response = saasDeploymentsClient.createTenant(parent, tenant, tenantId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the tenant.  
`tenant` | `[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)`  
Required. The desired state for the tenant.  
`tenantId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new tenant.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)` |   
  
### createTenantCallable()
    
    
    public final UnaryCallable<CreateTenantRequest,Tenant> createTenantCallable()

Create a new tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateTenantRequest request =
           CreateTenantRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTenantId("tenantId-1306693787")
               .setTenant(Tenant.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Tenant> future = saasDeploymentsClient.createTenantCallable().futureCall(request);
       // Do something.
       Tenant response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateTenantRequest),[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)>` |   
  
### createUnit(@Nullable LocationName parent, Unit unit, String unitId)
    
    
    public final Unit createUnit(@Nullable LocationName parent, Unit unit, String unitId)

Create a new unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Unit unit = Unit.newBuilder().build();
       String unitId = "unitId-840527425";
       Unit response = saasDeploymentsClient.createUnit(parent, unit, unitId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the unit.  
`unit` | `[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)`  
Required. The desired state for the unit.  
`unitId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new unit.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)` |   
  
### createUnit(CreateUnitRequest request)
    
    
    public final Unit createUnit(CreateUnitRequest request)

Create a new unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateUnitRequest request =
           CreateUnitRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUnitId("unitId-840527425")
               .setUnit(Unit.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       Unit response = saasDeploymentsClient.createUnit(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)` |   
  
### createUnit(String parent, Unit unit, String unitId)
    
    
    public final Unit createUnit(String parent, Unit unit, String unitId)

Create a new unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Unit unit = Unit.newBuilder().build();
       String unitId = "unitId-840527425";
       Unit response = saasDeploymentsClient.createUnit(parent, unit, unitId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the unit.  
`unit` | `[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)`  
Required. The desired state for the unit.  
`unitId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new unit.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)` |   
  
### createUnitCallable()
    
    
    public final UnaryCallable<CreateUnitRequest,Unit> createUnitCallable()

Create a new unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateUnitRequest request =
           CreateUnitRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUnitId("unitId-840527425")
               .setUnit(Unit.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Unit> future = saasDeploymentsClient.createUnitCallable().futureCall(request);
       // Do something.
       Unit response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitRequest),[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)>` |   
  
### createUnitKind(@Nullable LocationName parent, UnitKind unitKind, String unitKindId)
    
    
    public final UnitKind createUnitKind(@Nullable LocationName parent, UnitKind unitKind, String unitKindId)

Create a new unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       UnitKind unitKind = UnitKind.newBuilder().build();
       String unitKindId = "unitKindId1956463219";
       UnitKind response = saasDeploymentsClient.createUnitKind(parent, unitKind, unitKindId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the unit kind.  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`unitKindId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new unit kind.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` |   
  
### createUnitKind(CreateUnitKindRequest request)
    
    
    public final UnitKind createUnitKind(CreateUnitKindRequest request)

Create a new unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateUnitKindRequest request =
           CreateUnitKindRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUnitKindId("unitKindId1956463219")
               .setUnitKind(UnitKind.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       UnitKind response = saasDeploymentsClient.createUnitKind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` |   
  
### createUnitKind(String parent, UnitKind unitKind, String unitKindId)
    
    
    public final UnitKind createUnitKind(String parent, UnitKind unitKind, String unitKindId)

Create a new unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       UnitKind unitKind = UnitKind.newBuilder().build();
       String unitKindId = "unitKindId1956463219";
       UnitKind response = saasDeploymentsClient.createUnitKind(parent, unitKind, unitKindId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the unit kind.  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`unitKindId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new unit kind.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` |   
  
### createUnitKindCallable()
    
    
    public final UnaryCallable<CreateUnitKindRequest,UnitKind> createUnitKindCallable()

Create a new unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateUnitKindRequest request =
           CreateUnitKindRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUnitKindId("unitKindId1956463219")
               .setUnitKind(UnitKind.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<UnitKind> future =
           saasDeploymentsClient.createUnitKindCallable().futureCall(request);
       // Do something.
       UnitKind response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitKindRequest),[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)>` |   
  
### createUnitOperation(@Nullable LocationName parent, UnitOperation unitOperation, String unitOperationId)
    
    
    public final UnitOperation createUnitOperation(@Nullable LocationName parent, UnitOperation unitOperation, String unitOperationId)

Create a new unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       UnitOperation unitOperation = UnitOperation.newBuilder().build();
       String unitOperationId = "unitOperationId-638217026";
       UnitOperation response =
           saasDeploymentsClient.createUnitOperation(parent, unitOperation, unitOperationId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the unit operation.  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`unitOperationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new unit operation.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)` |   
  
### createUnitOperation(CreateUnitOperationRequest request)
    
    
    public final UnitOperation createUnitOperation(CreateUnitOperationRequest request)

Create a new unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateUnitOperationRequest request =
           CreateUnitOperationRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUnitOperationId("unitOperationId-638217026")
               .setUnitOperation(UnitOperation.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       UnitOperation response = saasDeploymentsClient.createUnitOperation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)` |   
  
### createUnitOperation(String parent, UnitOperation unitOperation, String unitOperationId)
    
    
    public final UnitOperation createUnitOperation(String parent, UnitOperation unitOperation, String unitOperationId)

Create a new unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       UnitOperation unitOperation = UnitOperation.newBuilder().build();
       String unitOperationId = "unitOperationId-638217026";
       UnitOperation response =
           saasDeploymentsClient.createUnitOperation(parent, unitOperation, unitOperationId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the unit operation.  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`unitOperationId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID value for the new unit operation.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)` |   
  
### createUnitOperationCallable()
    
    
    public final UnaryCallable<CreateUnitOperationRequest,UnitOperation> createUnitOperationCallable()

Create a new unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       CreateUnitOperationRequest request =
           CreateUnitOperationRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUnitOperationId("unitOperationId-638217026")
               .setUnitOperation(UnitOperation.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<UnitOperation> future =
           saasDeploymentsClient.createUnitOperationCallable().futureCall(request);
       // Do something.
       UnitOperation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateUnitOperationRequest),[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)>` |   
  
### deleteRelease(@Nullable ReleaseName name)
    
    
    public final void deleteRelease(@Nullable ReleaseName name)

Delete a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ReleaseName name = ReleaseName.of("[PROJECT]", "[LOCATION]", "[RELEASE]");
       saasDeploymentsClient.deleteRelease(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ReleaseName`  
Required. The resource name of the resource within a service.  
  
### deleteRelease(DeleteReleaseRequest request)
    
    
    public final void deleteRelease(DeleteReleaseRequest request)

Delete a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteReleaseRequest request =
           DeleteReleaseRequest.newBuilder()
               .setName(ReleaseName.of("[PROJECT]", "[LOCATION]", "[RELEASE]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       saasDeploymentsClient.deleteRelease(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteReleaseRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteRelease(String name)
    
    
    public final void deleteRelease(String name)

Delete a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = ReleaseName.of("[PROJECT]", "[LOCATION]", "[RELEASE]").toString();
       saasDeploymentsClient.deleteRelease(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
  
### deleteReleaseCallable()
    
    
    public final UnaryCallable<DeleteReleaseRequest,Empty> deleteReleaseCallable()

Delete a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteReleaseRequest request =
           DeleteReleaseRequest.newBuilder()
               .setName(ReleaseName.of("[PROJECT]", "[LOCATION]", "[RELEASE]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future = saasDeploymentsClient.deleteReleaseCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteReleaseRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSaas(@Nullable SaasName name)
    
    
    public final void deleteSaas(@Nullable SaasName name)

Delete a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       SaasName name = SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]");
       saasDeploymentsClient.deleteSaas(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasName`  
Required. The resource name of the resource within a service.  
  
### deleteSaas(DeleteSaasRequest request)
    
    
    public final void deleteSaas(DeleteSaasRequest request)

Delete a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteSaasRequest request =
           DeleteSaasRequest.newBuilder()
               .setName(SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       saasDeploymentsClient.deleteSaas(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteSaasRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSaas(String name)
    
    
    public final void deleteSaas(String name)

Delete a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]").toString();
       saasDeploymentsClient.deleteSaas(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
  
### deleteSaasCallable()
    
    
    public final UnaryCallable<DeleteSaasRequest,Empty> deleteSaasCallable()

Delete a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteSaasRequest request =
           DeleteSaasRequest.newBuilder()
               .setName(SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future = saasDeploymentsClient.deleteSaasCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteSaasRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTenant(@Nullable TenantName name)
    
    
    public final void deleteTenant(@Nullable TenantName name)

Delete a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       TenantName name = TenantName.of("[PROJECT]", "[LOCATION]", "[TENANT]");
       saasDeploymentsClient.deleteTenant(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.TenantName`  
Required. The resource name of the resource within a service.  
  
### deleteTenant(DeleteTenantRequest request)
    
    
    public final void deleteTenant(DeleteTenantRequest request)

Delete a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteTenantRequest request =
           DeleteTenantRequest.newBuilder()
               .setName(TenantName.of("[PROJECT]", "[LOCATION]", "[TENANT]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       saasDeploymentsClient.deleteTenant(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteTenantRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteTenant(String name)
    
    
    public final void deleteTenant(String name)

Delete a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = TenantName.of("[PROJECT]", "[LOCATION]", "[TENANT]").toString();
       saasDeploymentsClient.deleteTenant(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
  
### deleteTenantCallable()
    
    
    public final UnaryCallable<DeleteTenantRequest,Empty> deleteTenantCallable()

Delete a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteTenantRequest request =
           DeleteTenantRequest.newBuilder()
               .setName(TenantName.of("[PROJECT]", "[LOCATION]", "[TENANT]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future = saasDeploymentsClient.deleteTenantCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteTenantRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUnit(@Nullable UnitName name)
    
    
    public final void deleteUnit(@Nullable UnitName name)

Delete a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UnitName name = UnitName.of("[PROJECT]", "[LOCATION]", "[UNIT]");
       saasDeploymentsClient.deleteUnit(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitName`  
Required. The resource name of the resource within a service.  
  
### deleteUnit(DeleteUnitRequest request)
    
    
    public final void deleteUnit(DeleteUnitRequest request)

Delete a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteUnitRequest request =
           DeleteUnitRequest.newBuilder()
               .setName(UnitName.of("[PROJECT]", "[LOCATION]", "[UNIT]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       saasDeploymentsClient.deleteUnit(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUnit(String name)
    
    
    public final void deleteUnit(String name)

Delete a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = UnitName.of("[PROJECT]", "[LOCATION]", "[UNIT]").toString();
       saasDeploymentsClient.deleteUnit(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
  
### deleteUnitCallable()
    
    
    public final UnaryCallable<DeleteUnitRequest,Empty> deleteUnitCallable()

Delete a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteUnitRequest request =
           DeleteUnitRequest.newBuilder()
               .setName(UnitName.of("[PROJECT]", "[LOCATION]", "[UNIT]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future = saasDeploymentsClient.deleteUnitCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUnitKind(@Nullable UnitKindName name)
    
    
    public final void deleteUnitKind(@Nullable UnitKindName name)

Delete a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UnitKindName name = UnitKindName.of("[PROJECT]", "[LOCATION]", "[UNITKIND]");
       saasDeploymentsClient.deleteUnitKind(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKindName`  
Required. The resource name of the resource within a service.  
  
### deleteUnitKind(DeleteUnitKindRequest request)
    
    
    public final void deleteUnitKind(DeleteUnitKindRequest request)

Delete a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteUnitKindRequest request =
           DeleteUnitKindRequest.newBuilder()
               .setName(UnitKindName.of("[PROJECT]", "[LOCATION]", "[UNITKIND]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       saasDeploymentsClient.deleteUnitKind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUnitKind(String name)
    
    
    public final void deleteUnitKind(String name)

Delete a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = UnitKindName.of("[PROJECT]", "[LOCATION]", "[UNITKIND]").toString();
       saasDeploymentsClient.deleteUnitKind(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
  
### deleteUnitKindCallable()
    
    
    public final UnaryCallable<DeleteUnitKindRequest,Empty> deleteUnitKindCallable()

Delete a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteUnitKindRequest request =
           DeleteUnitKindRequest.newBuilder()
               .setName(UnitKindName.of("[PROJECT]", "[LOCATION]", "[UNITKIND]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future = saasDeploymentsClient.deleteUnitKindCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitKindRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUnitOperation(@Nullable UnitOperationName name)
    
    
    public final void deleteUnitOperation(@Nullable UnitOperationName name)

Delete a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UnitOperationName name = UnitOperationName.of("[PROJECT]", "[LOCATION]", "[UNITOPERATION]");
       saasDeploymentsClient.deleteUnitOperation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperationName`  
Required. The resource name of the resource within a service.  
  
### deleteUnitOperation(DeleteUnitOperationRequest request)
    
    
    public final void deleteUnitOperation(DeleteUnitOperationRequest request)

Delete a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteUnitOperationRequest request =
           DeleteUnitOperationRequest.newBuilder()
               .setName(
                   UnitOperationName.of("[PROJECT]", "[LOCATION]", "[UNITOPERATION]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       saasDeploymentsClient.deleteUnitOperation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUnitOperation(String name)
    
    
    public final void deleteUnitOperation(String name)

Delete a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = UnitOperationName.of("[PROJECT]", "[LOCATION]", "[UNITOPERATION]").toString();
       saasDeploymentsClient.deleteUnitOperation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
  
### deleteUnitOperationCallable()
    
    
    public final UnaryCallable<DeleteUnitOperationRequest,Empty> deleteUnitOperationCallable()

Delete a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       DeleteUnitOperationRequest request =
           DeleteUnitOperationRequest.newBuilder()
               .setName(
                   UnitOperationName.of("[PROJECT]", "[LOCATION]", "[UNITOPERATION]").toString())
               .setEtag("etag3123477")
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future =
           saasDeploymentsClient.deleteUnitOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteUnitOperationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = saasDeploymentsClient.getLocation(request);
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
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = saasDeploymentsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getRelease(@Nullable ReleaseName name)
    
    
    public final Release getRelease(@Nullable ReleaseName name)

Retrieve a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ReleaseName name = ReleaseName.of("[PROJECT]", "[LOCATION]", "[RELEASE]");
       Release response = saasDeploymentsClient.getRelease(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ReleaseName`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)` |   
  
### getRelease(GetReleaseRequest request)
    
    
    public final Release getRelease(GetReleaseRequest request)

Retrieve a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetReleaseRequest request =
           GetReleaseRequest.newBuilder()
               .setName(ReleaseName.of("[PROJECT]", "[LOCATION]", "[RELEASE]").toString())
               .build();
       Release response = saasDeploymentsClient.getRelease(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetReleaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)` |   
  
### getRelease(String name)
    
    
    public final Release getRelease(String name)

Retrieve a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = ReleaseName.of("[PROJECT]", "[LOCATION]", "[RELEASE]").toString();
       Release response = saasDeploymentsClient.getRelease(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)` |   
  
### getReleaseCallable()
    
    
    public final UnaryCallable<GetReleaseRequest,Release> getReleaseCallable()

Retrieve a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetReleaseRequest request =
           GetReleaseRequest.newBuilder()
               .setName(ReleaseName.of("[PROJECT]", "[LOCATION]", "[RELEASE]").toString())
               .build();
       ApiFuture<Release> future = saasDeploymentsClient.getReleaseCallable().futureCall(request);
       // Do something.
       Release response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetReleaseRequest),[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)>` |   
  
### getSaas(@Nullable SaasName name)
    
    
    public final Saas getSaas(@Nullable SaasName name)

Retrieve a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       SaasName name = SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]");
       Saas response = saasDeploymentsClient.getSaas(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasName`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)` |   
  
### getSaas(GetSaasRequest request)
    
    
    public final Saas getSaas(GetSaasRequest request)

Retrieve a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetSaasRequest request =
           GetSaasRequest.newBuilder()
               .setName(SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]").toString())
               .build();
       Saas response = saasDeploymentsClient.getSaas(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetSaasRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)` |   
  
### getSaas(String name)
    
    
    public final Saas getSaas(String name)

Retrieve a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]").toString();
       Saas response = saasDeploymentsClient.getSaas(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)` |   
  
### getSaasCallable()
    
    
    public final UnaryCallable<GetSaasRequest,Saas> getSaasCallable()

Retrieve a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetSaasRequest request =
           GetSaasRequest.newBuilder()
               .setName(SaasName.of("[PROJECT]", "[LOCATION]", "[SAAS]").toString())
               .build();
       ApiFuture<Saas> future = saasDeploymentsClient.getSaasCallable().futureCall(request);
       // Do something.
       Saas response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetSaasRequest),[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)>` |   
  
### getSettings()
    
    
    public final @Nullable SaasDeploymentsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsSettings` |   
  
### getStub()
    
    
    public SaasDeploymentsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.stub.SaasDeploymentsStub)` |   
  
### getTenant(@Nullable TenantName name)
    
    
    public final Tenant getTenant(@Nullable TenantName name)

Retrieve a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       TenantName name = TenantName.of("[PROJECT]", "[LOCATION]", "[TENANT]");
       Tenant response = saasDeploymentsClient.getTenant(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.TenantName`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)` |   
  
### getTenant(GetTenantRequest request)
    
    
    public final Tenant getTenant(GetTenantRequest request)

Retrieve a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetTenantRequest request =
           GetTenantRequest.newBuilder()
               .setName(TenantName.of("[PROJECT]", "[LOCATION]", "[TENANT]").toString())
               .build();
       Tenant response = saasDeploymentsClient.getTenant(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetTenantRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)` |   
  
### getTenant(String name)
    
    
    public final Tenant getTenant(String name)

Retrieve a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = TenantName.of("[PROJECT]", "[LOCATION]", "[TENANT]").toString();
       Tenant response = saasDeploymentsClient.getTenant(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)` |   
  
### getTenantCallable()
    
    
    public final UnaryCallable<GetTenantRequest,Tenant> getTenantCallable()

Retrieve a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetTenantRequest request =
           GetTenantRequest.newBuilder()
               .setName(TenantName.of("[PROJECT]", "[LOCATION]", "[TENANT]").toString())
               .build();
       ApiFuture<Tenant> future = saasDeploymentsClient.getTenantCallable().futureCall(request);
       // Do something.
       Tenant response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetTenantRequest),[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)>` |   
  
### getUnit(@Nullable UnitName name)
    
    
    public final Unit getUnit(@Nullable UnitName name)

Retrieve a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UnitName name = UnitName.of("[PROJECT]", "[LOCATION]", "[UNIT]");
       Unit response = saasDeploymentsClient.getUnit(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitName`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)` |   
  
### getUnit(GetUnitRequest request)
    
    
    public final Unit getUnit(GetUnitRequest request)

Retrieve a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetUnitRequest request =
           GetUnitRequest.newBuilder()
               .setName(UnitName.of("[PROJECT]", "[LOCATION]", "[UNIT]").toString())
               .build();
       Unit response = saasDeploymentsClient.getUnit(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)` |   
  
### getUnit(String name)
    
    
    public final Unit getUnit(String name)

Retrieve a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = UnitName.of("[PROJECT]", "[LOCATION]", "[UNIT]").toString();
       Unit response = saasDeploymentsClient.getUnit(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)` |   
  
### getUnitCallable()
    
    
    public final UnaryCallable<GetUnitRequest,Unit> getUnitCallable()

Retrieve a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetUnitRequest request =
           GetUnitRequest.newBuilder()
               .setName(UnitName.of("[PROJECT]", "[LOCATION]", "[UNIT]").toString())
               .build();
       ApiFuture<Unit> future = saasDeploymentsClient.getUnitCallable().futureCall(request);
       // Do something.
       Unit response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitRequest),[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)>` |   
  
### getUnitKind(@Nullable UnitKindName name)
    
    
    public final UnitKind getUnitKind(@Nullable UnitKindName name)

Retrieve a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UnitKindName name = UnitKindName.of("[PROJECT]", "[LOCATION]", "[UNITKIND]");
       UnitKind response = saasDeploymentsClient.getUnitKind(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKindName`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` |   
  
### getUnitKind(GetUnitKindRequest request)
    
    
    public final UnitKind getUnitKind(GetUnitKindRequest request)

Retrieve a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetUnitKindRequest request =
           GetUnitKindRequest.newBuilder()
               .setName(UnitKindName.of("[PROJECT]", "[LOCATION]", "[UNITKIND]").toString())
               .build();
       UnitKind response = saasDeploymentsClient.getUnitKind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` |   
  
### getUnitKind(String name)
    
    
    public final UnitKind getUnitKind(String name)

Retrieve a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = UnitKindName.of("[PROJECT]", "[LOCATION]", "[UNITKIND]").toString();
       UnitKind response = saasDeploymentsClient.getUnitKind(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` |   
  
### getUnitKindCallable()
    
    
    public final UnaryCallable<GetUnitKindRequest,UnitKind> getUnitKindCallable()

Retrieve a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetUnitKindRequest request =
           GetUnitKindRequest.newBuilder()
               .setName(UnitKindName.of("[PROJECT]", "[LOCATION]", "[UNITKIND]").toString())
               .build();
       ApiFuture<UnitKind> future = saasDeploymentsClient.getUnitKindCallable().futureCall(request);
       // Do something.
       UnitKind response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitKindRequest),[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)>` |   
  
### getUnitOperation(@Nullable UnitOperationName name)
    
    
    public final UnitOperation getUnitOperation(@Nullable UnitOperationName name)

Retrieve a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UnitOperationName name = UnitOperationName.of("[PROJECT]", "[LOCATION]", "[UNITOPERATION]");
       UnitOperation response = saasDeploymentsClient.getUnitOperation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperationName`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)` |   
  
### getUnitOperation(GetUnitOperationRequest request)
    
    
    public final UnitOperation getUnitOperation(GetUnitOperationRequest request)

Retrieve a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetUnitOperationRequest request =
           GetUnitOperationRequest.newBuilder()
               .setName(
                   UnitOperationName.of("[PROJECT]", "[LOCATION]", "[UNITOPERATION]").toString())
               .build();
       UnitOperation response = saasDeploymentsClient.getUnitOperation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)` |   
  
### getUnitOperation(String name)
    
    
    public final UnitOperation getUnitOperation(String name)

Retrieve a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String name = UnitOperationName.of("[PROJECT]", "[LOCATION]", "[UNITOPERATION]").toString();
       UnitOperation response = saasDeploymentsClient.getUnitOperation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the resource within a service.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)` |   
  
### getUnitOperationCallable()
    
    
    public final UnaryCallable<GetUnitOperationRequest,UnitOperation> getUnitOperationCallable()

Retrieve a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       GetUnitOperationRequest request =
           GetUnitOperationRequest.newBuilder()
               .setName(
                   UnitOperationName.of("[PROJECT]", "[LOCATION]", "[UNITOPERATION]").toString())
               .build();
       ApiFuture<UnitOperation> future =
           saasDeploymentsClient.getUnitOperationCallable().futureCall(request);
       // Do something.
       UnitOperation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetUnitOperationRequest),[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)>` |   
  
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
    
    
    public final SaasDeploymentsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : saasDeploymentsClient.listLocations(request).iterateAll()) {
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
`[SaasDeploymentsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListLocationsPagedResponse)` |   
  
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
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             saasDeploymentsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SaasDeploymentsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           saasDeploymentsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListLocationsPagedResponse)>` |   
  
### listReleases(@Nullable LocationName parent)
    
    
    public final SaasDeploymentsClient.ListReleasesPagedResponse listReleases(@Nullable LocationName parent)

Retrieve a collection of releases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Release element : saasDeploymentsClient.listReleases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the release.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListReleasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListReleasesPagedResponse)` |   
  
### listReleases(ListReleasesRequest request)
    
    
    public final SaasDeploymentsClient.ListReleasesPagedResponse listReleases(ListReleasesRequest request)

Retrieve a collection of releases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListReleasesRequest request =
           ListReleasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Release element : saasDeploymentsClient.listReleases(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReleasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListReleasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListReleasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListReleasesPagedResponse)` |   
  
### listReleases(String parent)
    
    
    public final SaasDeploymentsClient.ListReleasesPagedResponse listReleases(String parent)

Retrieve a collection of releases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Release element : saasDeploymentsClient.listReleases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the release.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListReleasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListReleasesPagedResponse)` |   
  
### listReleasesCallable()
    
    
    public final UnaryCallable<ListReleasesRequest,ListReleasesResponse> listReleasesCallable()

Retrieve a collection of releases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListReleasesRequest request =
           ListReleasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListReleasesResponse response = saasDeploymentsClient.listReleasesCallable().call(request);
         for (Release element : response.getReleasesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReleasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListReleasesRequest),[ListReleasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListReleasesResponse)>` |   
  
### listReleasesPagedCallable()
    
    
    public final UnaryCallable<ListReleasesRequest,SaasDeploymentsClient.ListReleasesPagedResponse> listReleasesPagedCallable()

Retrieve a collection of releases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListReleasesRequest request =
           ListReleasesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Release> future =
           saasDeploymentsClient.listReleasesPagedCallable().futureCall(request);
       // Do something.
       for (Release element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReleasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListReleasesRequest),[ListReleasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListReleasesPagedResponse)>` |   
  
### listSaas(@Nullable LocationName parent)
    
    
    public final SaasDeploymentsClient.ListSaasPagedResponse listSaas(@Nullable LocationName parent)

Retrieve a collection of saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Saas element : saasDeploymentsClient.listSaas(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the saas.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListSaasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListSaasPagedResponse)` |   
  
### listSaas(ListSaasRequest request)
    
    
    public final SaasDeploymentsClient.ListSaasPagedResponse listSaas(ListSaasRequest request)

Retrieve a collection of saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListSaasRequest request =
           ListSaasRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Saas element : saasDeploymentsClient.listSaas(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListSaasRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListSaasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListSaasPagedResponse)` |   
  
### listSaas(String parent)
    
    
    public final SaasDeploymentsClient.ListSaasPagedResponse listSaas(String parent)

Retrieve a collection of saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Saas element : saasDeploymentsClient.listSaas(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the saas.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListSaasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListSaasPagedResponse)` |   
  
### listSaasCallable()
    
    
    public final UnaryCallable<ListSaasRequest,ListSaasResponse> listSaasCallable()

Retrieve a collection of saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListSaasRequest request =
           ListSaasRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSaasResponse response = saasDeploymentsClient.listSaasCallable().call(request);
         for (Saas element : response.getSaasList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListSaasRequest),[ListSaasResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListSaasResponse)>` |   
  
### listSaasPagedCallable()
    
    
    public final UnaryCallable<ListSaasRequest,SaasDeploymentsClient.ListSaasPagedResponse> listSaasPagedCallable()

Retrieve a collection of saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListSaasRequest request =
           ListSaasRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Saas> future = saasDeploymentsClient.listSaasPagedCallable().futureCall(request);
       // Do something.
       for (Saas element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListSaasRequest),[ListSaasPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListSaasPagedResponse)>` |   
  
### listTenants(@Nullable LocationName parent)
    
    
    public final SaasDeploymentsClient.ListTenantsPagedResponse listTenants(@Nullable LocationName parent)

Retrieve a collection of tenants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Tenant element : saasDeploymentsClient.listTenants(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the tenant.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListTenantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListTenantsPagedResponse)` |   
  
### listTenants(ListTenantsRequest request)
    
    
    public final SaasDeploymentsClient.ListTenantsPagedResponse listTenants(ListTenantsRequest request)

Retrieve a collection of tenants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListTenantsRequest request =
           ListTenantsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Tenant element : saasDeploymentsClient.listTenants(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTenantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListTenantsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListTenantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListTenantsPagedResponse)` |   
  
### listTenants(String parent)
    
    
    public final SaasDeploymentsClient.ListTenantsPagedResponse listTenants(String parent)

Retrieve a collection of tenants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Tenant element : saasDeploymentsClient.listTenants(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the tenant.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListTenantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListTenantsPagedResponse)` |   
  
### listTenantsCallable()
    
    
    public final UnaryCallable<ListTenantsRequest,ListTenantsResponse> listTenantsCallable()

Retrieve a collection of tenants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListTenantsRequest request =
           ListTenantsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListTenantsResponse response = saasDeploymentsClient.listTenantsCallable().call(request);
         for (Tenant element : response.getTenantsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTenantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListTenantsRequest),[ListTenantsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListTenantsResponse)>` |   
  
### listTenantsPagedCallable()
    
    
    public final UnaryCallable<ListTenantsRequest,SaasDeploymentsClient.ListTenantsPagedResponse> listTenantsPagedCallable()

Retrieve a collection of tenants.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListTenantsRequest request =
           ListTenantsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Tenant> future =
           saasDeploymentsClient.listTenantsPagedCallable().futureCall(request);
       // Do something.
       for (Tenant element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTenantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListTenantsRequest),[ListTenantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListTenantsPagedResponse)>` |   
  
### listUnitKinds(@Nullable LocationName parent)
    
    
    public final SaasDeploymentsClient.ListUnitKindsPagedResponse listUnitKinds(@Nullable LocationName parent)

Retrieve a collection of unit kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (UnitKind element : saasDeploymentsClient.listUnitKinds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the unit kind.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitKindsPagedResponse)` |   
  
### listUnitKinds(ListUnitKindsRequest request)
    
    
    public final SaasDeploymentsClient.ListUnitKindsPagedResponse listUnitKinds(ListUnitKindsRequest request)

Retrieve a collection of unit kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitKindsRequest request =
           ListUnitKindsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (UnitKind element : saasDeploymentsClient.listUnitKinds(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUnitKindsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitKindsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitKindsPagedResponse)` |   
  
### listUnitKinds(String parent)
    
    
    public final SaasDeploymentsClient.ListUnitKindsPagedResponse listUnitKinds(String parent)

Retrieve a collection of unit kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (UnitKind element : saasDeploymentsClient.listUnitKinds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the unit kind.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitKindsPagedResponse)` |   
  
### listUnitKindsCallable()
    
    
    public final UnaryCallable<ListUnitKindsRequest,ListUnitKindsResponse> listUnitKindsCallable()

Retrieve a collection of unit kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitKindsRequest request =
           ListUnitKindsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListUnitKindsResponse response =
             saasDeploymentsClient.listUnitKindsCallable().call(request);
         for (UnitKind element : response.getUnitKindsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitKindsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitKindsRequest),[ListUnitKindsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitKindsResponse)>` |   
  
### listUnitKindsPagedCallable()
    
    
    public final UnaryCallable<ListUnitKindsRequest,SaasDeploymentsClient.ListUnitKindsPagedResponse> listUnitKindsPagedCallable()

Retrieve a collection of unit kinds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitKindsRequest request =
           ListUnitKindsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<UnitKind> future =
           saasDeploymentsClient.listUnitKindsPagedCallable().futureCall(request);
       // Do something.
       for (UnitKind element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitKindsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitKindsRequest),[ListUnitKindsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitKindsPagedResponse)>` |   
  
### listUnitOperations(@Nullable LocationName parent)
    
    
    public final SaasDeploymentsClient.ListUnitOperationsPagedResponse listUnitOperations(@Nullable LocationName parent)

Retrieve a collection of unit operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (UnitOperation element : saasDeploymentsClient.listUnitOperations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the unit operation.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitOperationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitOperationsPagedResponse)` |   
  
### listUnitOperations(ListUnitOperationsRequest request)
    
    
    public final SaasDeploymentsClient.ListUnitOperationsPagedResponse listUnitOperations(ListUnitOperationsRequest request)

Retrieve a collection of unit operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitOperationsRequest request =
           ListUnitOperationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (UnitOperation element : saasDeploymentsClient.listUnitOperations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUnitOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitOperationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitOperationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitOperationsPagedResponse)` |   
  
### listUnitOperations(String parent)
    
    
    public final SaasDeploymentsClient.ListUnitOperationsPagedResponse listUnitOperations(String parent)

Retrieve a collection of unit operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (UnitOperation element : saasDeploymentsClient.listUnitOperations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the unit operation.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitOperationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitOperationsPagedResponse)` |   
  
### listUnitOperationsCallable()
    
    
    public final UnaryCallable<ListUnitOperationsRequest,ListUnitOperationsResponse> listUnitOperationsCallable()

Retrieve a collection of unit operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitOperationsRequest request =
           ListUnitOperationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListUnitOperationsResponse response =
             saasDeploymentsClient.listUnitOperationsCallable().call(request);
         for (UnitOperation element : response.getUnitOperationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitOperationsRequest),[ListUnitOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitOperationsResponse)>` |   
  
### listUnitOperationsPagedCallable()
    
    
    public final UnaryCallable<ListUnitOperationsRequest,SaasDeploymentsClient.ListUnitOperationsPagedResponse> listUnitOperationsPagedCallable()

Retrieve a collection of unit operations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitOperationsRequest request =
           ListUnitOperationsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<UnitOperation> future =
           saasDeploymentsClient.listUnitOperationsPagedCallable().futureCall(request);
       // Do something.
       for (UnitOperation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitOperationsRequest),[ListUnitOperationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitOperationsPagedResponse)>` |   
  
### listUnits(@Nullable LocationName parent)
    
    
    public final SaasDeploymentsClient.ListUnitsPagedResponse listUnits(@Nullable LocationName parent)

Retrieve a collection of units.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Unit element : saasDeploymentsClient.listUnits(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.saasplatform.saasservicemgmt.v1beta1.LocationName`  
Required. The parent of the unit.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitsPagedResponse)` |   
  
### listUnits(ListUnitsRequest request)
    
    
    public final SaasDeploymentsClient.ListUnitsPagedResponse listUnits(ListUnitsRequest request)

Retrieve a collection of units.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitsRequest request =
           ListUnitsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Unit element : saasDeploymentsClient.listUnits(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUnitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitsPagedResponse)` |   
  
### listUnits(String parent)
    
    
    public final SaasDeploymentsClient.ListUnitsPagedResponse listUnits(String parent)

Retrieve a collection of units.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Unit element : saasDeploymentsClient.listUnits(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the unit.  
**Returns**  
---  
**Type** | **Description**  
`[SaasDeploymentsClient.ListUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitsPagedResponse)` |   
  
### listUnitsCallable()
    
    
    public final UnaryCallable<ListUnitsRequest,ListUnitsResponse> listUnitsCallable()

Retrieve a collection of units.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitsRequest request =
           ListUnitsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListUnitsResponse response = saasDeploymentsClient.listUnitsCallable().call(request);
         for (Unit element : response.getUnitsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitsRequest),[ListUnitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitsResponse)>` |   
  
### listUnitsPagedCallable()
    
    
    public final UnaryCallable<ListUnitsRequest,SaasDeploymentsClient.ListUnitsPagedResponse> listUnitsPagedCallable()

Retrieve a collection of units.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       ListUnitsRequest request =
           ListUnitsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Unit> future = saasDeploymentsClient.listUnitsPagedCallable().futureCall(request);
       // Do something.
       for (Unit element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUnitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListUnitsRequest),[ListUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeploymentsClient.ListUnitsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateRelease(Release release, FieldMask updateMask)
    
    
    public final Release updateRelease(Release release, FieldMask updateMask)

Update a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       Release release = Release.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Release response = saasDeploymentsClient.updateRelease(release, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`release` | `[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)`  
Required. The desired state for the release.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Release resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Release will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)` |   
  
### updateRelease(UpdateReleaseRequest request)
    
    
    public final Release updateRelease(UpdateReleaseRequest request)

Update a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateReleaseRequest request =
           UpdateReleaseRequest.newBuilder()
               .setRelease(Release.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Release response = saasDeploymentsClient.updateRelease(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateReleaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)` |   
  
### updateReleaseCallable()
    
    
    public final UnaryCallable<UpdateReleaseRequest,Release> updateReleaseCallable()

Update a single release.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateReleaseRequest request =
           UpdateReleaseRequest.newBuilder()
               .setRelease(Release.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Release> future = saasDeploymentsClient.updateReleaseCallable().futureCall(request);
       // Do something.
       Release response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateReleaseRequest),[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Release)>` |   
  
### updateSaas(Saas saas, FieldMask updateMask)
    
    
    public final Saas updateSaas(Saas saas, FieldMask updateMask)

Update a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       Saas saas = Saas.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Saas response = saasDeploymentsClient.updateSaas(saas, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`saas` | `[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)`  
Required. The desired state for the saas.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Saas resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Saas will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)` |   
  
### updateSaas(UpdateSaasRequest request)
    
    
    public final Saas updateSaas(UpdateSaasRequest request)

Update a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateSaasRequest request =
           UpdateSaasRequest.newBuilder()
               .setSaas(Saas.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Saas response = saasDeploymentsClient.updateSaas(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateSaasRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)` |   
  
### updateSaasCallable()
    
    
    public final UnaryCallable<UpdateSaasRequest,Saas> updateSaasCallable()

Update a single saas.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateSaasRequest request =
           UpdateSaasRequest.newBuilder()
               .setSaas(Saas.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Saas> future = saasDeploymentsClient.updateSaasCallable().futureCall(request);
       // Do something.
       Saas response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSaasRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateSaasRequest),[Saas](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Saas)>` |   
  
### updateTenant(Tenant tenant, FieldMask updateMask)
    
    
    public final Tenant updateTenant(Tenant tenant, FieldMask updateMask)

Update a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       Tenant tenant = Tenant.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Tenant response = saasDeploymentsClient.updateTenant(tenant, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tenant` | `[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)`  
Required. The desired state for the tenant.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Tenant resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Tenant will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)` |   
  
### updateTenant(UpdateTenantRequest request)
    
    
    public final Tenant updateTenant(UpdateTenantRequest request)

Update a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateTenantRequest request =
           UpdateTenantRequest.newBuilder()
               .setTenant(Tenant.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Tenant response = saasDeploymentsClient.updateTenant(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateTenantRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)` |   
  
### updateTenantCallable()
    
    
    public final UnaryCallable<UpdateTenantRequest,Tenant> updateTenantCallable()

Update a single tenant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateTenantRequest request =
           UpdateTenantRequest.newBuilder()
               .setTenant(Tenant.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Tenant> future = saasDeploymentsClient.updateTenantCallable().futureCall(request);
       // Do something.
       Tenant response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTenantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateTenantRequest),[Tenant](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Tenant)>` |   
  
### updateUnit(Unit unit, FieldMask updateMask)
    
    
    public final Unit updateUnit(Unit unit, FieldMask updateMask)

Update a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       Unit unit = Unit.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Unit response = saasDeploymentsClient.updateUnit(unit, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`unit` | `[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)`  
Required. The desired state for the unit.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Unit resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Unit will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)` |   
  
### updateUnit(UpdateUnitRequest request)
    
    
    public final Unit updateUnit(UpdateUnitRequest request)

Update a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateUnitRequest request =
           UpdateUnitRequest.newBuilder()
               .setUnit(Unit.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Unit response = saasDeploymentsClient.updateUnit(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)` |   
  
### updateUnitCallable()
    
    
    public final UnaryCallable<UpdateUnitRequest,Unit> updateUnitCallable()

Update a single unit.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateUnitRequest request =
           UpdateUnitRequest.newBuilder()
               .setUnit(Unit.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Unit> future = saasDeploymentsClient.updateUnitCallable().futureCall(request);
       // Do something.
       Unit response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUnitRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitRequest),[Unit](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.Unit)>` |   
  
### updateUnitKind(UnitKind unitKind, FieldMask updateMask)
    
    
    public final UnitKind updateUnitKind(UnitKind unitKind, FieldMask updateMask)

Update a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UnitKind unitKind = UnitKind.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       UnitKind response = saasDeploymentsClient.updateUnitKind(unitKind, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`unitKind` | `[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)`  
Required. The desired state for the unit kind.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the UnitKind resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the UnitKind will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` |   
  
### updateUnitKind(UpdateUnitKindRequest request)
    
    
    public final UnitKind updateUnitKind(UpdateUnitKindRequest request)

Update a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateUnitKindRequest request =
           UpdateUnitKindRequest.newBuilder()
               .setUnitKind(UnitKind.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       UnitKind response = saasDeploymentsClient.updateUnitKind(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitKindRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)` |   
  
### updateUnitKindCallable()
    
    
    public final UnaryCallable<UpdateUnitKindRequest,UnitKind> updateUnitKindCallable()

Update a single unit kind.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateUnitKindRequest request =
           UpdateUnitKindRequest.newBuilder()
               .setUnitKind(UnitKind.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<UnitKind> future =
           saasDeploymentsClient.updateUnitKindCallable().futureCall(request);
       // Do something.
       UnitKind response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUnitKindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitKindRequest),[UnitKind](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitKind)>` |   
  
### updateUnitOperation(UnitOperation unitOperation, FieldMask updateMask)
    
    
    public final UnitOperation updateUnitOperation(UnitOperation unitOperation, FieldMask updateMask)

Update a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UnitOperation unitOperation = UnitOperation.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       UnitOperation response = saasDeploymentsClient.updateUnitOperation(unitOperation, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`unitOperation` | `[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)`  
Required. The desired state for the unit operation.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the UnitOperation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the UnitOperation will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)` |   
  
### updateUnitOperation(UpdateUnitOperationRequest request)
    
    
    public final UnitOperation updateUnitOperation(UpdateUnitOperationRequest request)

Update a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateUnitOperationRequest request =
           UpdateUnitOperationRequest.newBuilder()
               .setUnitOperation(UnitOperation.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       UnitOperation response = saasDeploymentsClient.updateUnitOperation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)` |   
  
### updateUnitOperationCallable()
    
    
    public final UnaryCallable<UpdateUnitOperationRequest,UnitOperation> updateUnitOperationCallable()

Update a single unit operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SaasDeploymentsClient saasDeploymentsClient = SaasDeploymentsClient.create()) {
       UpdateUnitOperationRequest request =
           UpdateUnitOperationRequest.newBuilder()
               .setUnitOperation(UnitOperation.newBuilder().build())
               .setValidateOnly(true)
               .setRequestId("requestId693933066")
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<UnitOperation> future =
           saasDeploymentsClient.updateUnitOperationCallable().futureCall(request);
       // Do something.
       UnitOperation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUnitOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateUnitOperationRequest),[UnitOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-saasservicemgmt/latest/com.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
