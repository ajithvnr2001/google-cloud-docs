---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient
title: Class OrganizationVpcFlowLogsServiceClient (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:32.474576+00:00
---

# Class OrganizationVpcFlowLogsServiceClient (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrganizationVpcFlowLogsServiceClient (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.1.10 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-network-management/google-cloud-network-management/src/main/java/com/google/cloud/networkmanagement/v1/OrganizationVpcFlowLogsServiceClient.java)| [Product Reference](https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/)  
---|---  
  
Service Description: The VPC Flow Logs organization service in the Google Cloud Network Management API provides organization level configurations that generate Flow Logs. The service and the configuration resources created using this service are global.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       VpcFlowLogsConfigName name =
           VpcFlowLogsConfigName.ofOrganizationLocationVpcFlowLogsConfigName(
               "[ORGANIZATION]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]");
       VpcFlowLogsConfig response = organizationVpcFlowLogsServiceClient.getVpcFlowLogsConfig(name);
     }
     

Note: close() needs to be called on the OrganizationVpcFlowLogsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListVpcFlowLogsConfigs |  Lists all `VpcFlowLogsConfigs` in a given organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listVpcFlowLogsConfigs(ListVpcFlowLogsConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listVpcFlowLogsConfigs(LocationName parent) 
  * listVpcFlowLogsConfigs(OrganizationLocationName parent) 
  * listVpcFlowLogsConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listVpcFlowLogsConfigsPagedCallable() 
  * listVpcFlowLogsConfigsCallable() 

  
GetVpcFlowLogsConfig |  Gets the details of a specific `VpcFlowLogsConfig`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVpcFlowLogsConfig(GetVpcFlowLogsConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getVpcFlowLogsConfig(VpcFlowLogsConfigName name) 
  * getVpcFlowLogsConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVpcFlowLogsConfigCallable() 

  
CreateVpcFlowLogsConfig |  Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:  1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createVpcFlowLogsConfigAsync(CreateVpcFlowLogsConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createVpcFlowLogsConfigAsync(LocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, VpcFlowLogsConfigName vpcFlowLogsConfigId) 
  * createVpcFlowLogsConfigAsync(LocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId) 
  * createVpcFlowLogsConfigAsync(OrganizationLocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, VpcFlowLogsConfigName vpcFlowLogsConfigId) 
  * createVpcFlowLogsConfigAsync(OrganizationLocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId) 
  * createVpcFlowLogsConfigAsync(String parent, VpcFlowLogsConfig vpcFlowLogsConfig, VpcFlowLogsConfigName vpcFlowLogsConfigId) 
  * createVpcFlowLogsConfigAsync(String parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createVpcFlowLogsConfigOperationCallable() 
  * createVpcFlowLogsConfigCallable() 

  
UpdateVpcFlowLogsConfig |  Updates an existing `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:  1\. Updating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - updating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateVpcFlowLogsConfigAsync(UpdateVpcFlowLogsConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateVpcFlowLogsConfigAsync(VpcFlowLogsConfig vpcFlowLogsConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateVpcFlowLogsConfigOperationCallable() 
  * updateVpcFlowLogsConfigCallable() 

  
DeleteVpcFlowLogsConfig |  Deletes a specific `VpcFlowLogsConfig`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteVpcFlowLogsConfigAsync(DeleteVpcFlowLogsConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteVpcFlowLogsConfigAsync(VpcFlowLogsConfigName name) 
  * deleteVpcFlowLogsConfigAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteVpcFlowLogsConfigOperationCallable() 
  * deleteVpcFlowLogsConfigCallable() 

  
ListLocations |  Lists information about the supported locations for this service.This method can be called in two ways:  * **List all public locations:** Use the path `GET /v1/locations`.* **List project-visible locations:** Use the path`GET /v1/projects/{project_id}/locations`. This may include publiclocations as well as private or other locations specifically visibleto the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of OrganizationVpcFlowLogsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrganizationVpcFlowLogsServiceSettings organizationVpcFlowLogsServiceSettings =
         OrganizationVpcFlowLogsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create(organizationVpcFlowLogsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrganizationVpcFlowLogsServiceSettings organizationVpcFlowLogsServiceSettings =
         OrganizationVpcFlowLogsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create(organizationVpcFlowLogsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrganizationVpcFlowLogsServiceSettings organizationVpcFlowLogsServiceSettings =
         OrganizationVpcFlowLogsServiceSettings.newHttpJsonBuilder().build();
     OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create(organizationVpcFlowLogsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OrganizationVpcFlowLogsServiceClient

## Static Methods 

### create()
    
    
    public static final OrganizationVpcFlowLogsServiceClient create()

Constructs an instance of OrganizationVpcFlowLogsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[OrganizationVpcFlowLogsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OrganizationVpcFlowLogsServiceSettings settings)
    
    
    public static final OrganizationVpcFlowLogsServiceClient create(OrganizationVpcFlowLogsServiceSettings settings)

Constructs an instance of OrganizationVpcFlowLogsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OrganizationVpcFlowLogsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationVpcFlowLogsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OrganizationVpcFlowLogsServiceStub stub)
    
    
    public static final OrganizationVpcFlowLogsServiceClient create(OrganizationVpcFlowLogsServiceStub stub)

Constructs an instance of OrganizationVpcFlowLogsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(OrganizationVpcFlowLogsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OrganizationVpcFlowLogsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.stub.OrganizationVpcFlowLogsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationVpcFlowLogsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient)` |   
  
## Constructors 

### OrganizationVpcFlowLogsServiceClient(OrganizationVpcFlowLogsServiceSettings settings)
    
    
    protected OrganizationVpcFlowLogsServiceClient(OrganizationVpcFlowLogsServiceSettings settings)

Constructs an instance of OrganizationVpcFlowLogsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OrganizationVpcFlowLogsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceSettings)`  
  
  
### OrganizationVpcFlowLogsServiceClient(OrganizationVpcFlowLogsServiceStub stub)
    
    
    protected OrganizationVpcFlowLogsServiceClient(OrganizationVpcFlowLogsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OrganizationVpcFlowLogsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.stub.OrganizationVpcFlowLogsServiceStub)`  
  
  
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

### createVpcFlowLogsConfigAsync(@Nullable LocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, @Nullable VpcFlowLogsConfigName vpcFlowLogsConfigId)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigAsync(@Nullable LocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, @Nullable VpcFlowLogsConfigName vpcFlowLogsConfigId)

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       VpcFlowLogsConfig vpcFlowLogsConfig = VpcFlowLogsConfig.newBuilder().build();
       VpcFlowLogsConfigName vpcFlowLogsConfigId =
           VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
               "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]");
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient
               .createVpcFlowLogsConfigAsync(parent, vpcFlowLogsConfig, vpcFlowLogsConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.LocationName`  
Required. The parent resource of the VpcFlowLogsConfig to create, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
`vpcFlowLogsConfig` | `[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)`  
Required. A `VpcFlowLogsConfig` resource  
`vpcFlowLogsConfigId` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.VpcFlowLogsConfigName`  
Required. ID of the `VpcFlowLogsConfig`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### createVpcFlowLogsConfigAsync(@Nullable LocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigAsync(@Nullable LocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId)

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       VpcFlowLogsConfig vpcFlowLogsConfig = VpcFlowLogsConfig.newBuilder().build();
       String vpcFlowLogsConfigId =
           VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
                   "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
               .toString();
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient
               .createVpcFlowLogsConfigAsync(parent, vpcFlowLogsConfig, vpcFlowLogsConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.LocationName`  
Required. The parent resource of the VpcFlowLogsConfig to create, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
`vpcFlowLogsConfig` | `[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)`  
Required. A `VpcFlowLogsConfig` resource  
`vpcFlowLogsConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the `VpcFlowLogsConfig`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### createVpcFlowLogsConfigAsync(@Nullable OrganizationLocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, @Nullable VpcFlowLogsConfigName vpcFlowLogsConfigId)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigAsync(@Nullable OrganizationLocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, @Nullable VpcFlowLogsConfigName vpcFlowLogsConfigId)

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       VpcFlowLogsConfig vpcFlowLogsConfig = VpcFlowLogsConfig.newBuilder().build();
       VpcFlowLogsConfigName vpcFlowLogsConfigId =
           VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
               "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]");
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient
               .createVpcFlowLogsConfigAsync(parent, vpcFlowLogsConfig, vpcFlowLogsConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.OrganizationLocationName`  
Required. The parent resource of the VpcFlowLogsConfig to create, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
`vpcFlowLogsConfig` | `[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)`  
Required. A `VpcFlowLogsConfig` resource  
`vpcFlowLogsConfigId` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.VpcFlowLogsConfigName`  
Required. ID of the `VpcFlowLogsConfig`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### createVpcFlowLogsConfigAsync(@Nullable OrganizationLocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigAsync(@Nullable OrganizationLocationName parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId)

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       VpcFlowLogsConfig vpcFlowLogsConfig = VpcFlowLogsConfig.newBuilder().build();
       String vpcFlowLogsConfigId =
           VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
                   "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
               .toString();
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient
               .createVpcFlowLogsConfigAsync(parent, vpcFlowLogsConfig, vpcFlowLogsConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.OrganizationLocationName`  
Required. The parent resource of the VpcFlowLogsConfig to create, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
`vpcFlowLogsConfig` | `[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)`  
Required. A `VpcFlowLogsConfig` resource  
`vpcFlowLogsConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the `VpcFlowLogsConfig`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### createVpcFlowLogsConfigAsync(CreateVpcFlowLogsConfigRequest request)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigAsync(CreateVpcFlowLogsConfigRequest request)

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       CreateVpcFlowLogsConfigRequest request =
           CreateVpcFlowLogsConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVpcFlowLogsConfigId(
                   VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
                           "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
                       .toString())
               .setVpcFlowLogsConfig(VpcFlowLogsConfig.newBuilder().build())
               .build();
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient.createVpcFlowLogsConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.CreateVpcFlowLogsConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### createVpcFlowLogsConfigAsync(String parent, VpcFlowLogsConfig vpcFlowLogsConfig, @Nullable VpcFlowLogsConfigName vpcFlowLogsConfigId)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigAsync(String parent, VpcFlowLogsConfig vpcFlowLogsConfig, @Nullable VpcFlowLogsConfigName vpcFlowLogsConfigId)

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       VpcFlowLogsConfig vpcFlowLogsConfig = VpcFlowLogsConfig.newBuilder().build();
       VpcFlowLogsConfigName vpcFlowLogsConfigId =
           VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
               "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]");
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient
               .createVpcFlowLogsConfigAsync(parent, vpcFlowLogsConfig, vpcFlowLogsConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the VpcFlowLogsConfig to create, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
`vpcFlowLogsConfig` | `[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)`  
Required. A `VpcFlowLogsConfig` resource  
`vpcFlowLogsConfigId` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.VpcFlowLogsConfigName`  
Required. ID of the `VpcFlowLogsConfig`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### createVpcFlowLogsConfigAsync(String parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigAsync(String parent, VpcFlowLogsConfig vpcFlowLogsConfig, String vpcFlowLogsConfigId)

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       VpcFlowLogsConfig vpcFlowLogsConfig = VpcFlowLogsConfig.newBuilder().build();
       String vpcFlowLogsConfigId =
           VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
                   "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
               .toString();
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient
               .createVpcFlowLogsConfigAsync(parent, vpcFlowLogsConfig, vpcFlowLogsConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the VpcFlowLogsConfig to create, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
`vpcFlowLogsConfig` | `[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)`  
Required. A `VpcFlowLogsConfig` resource  
`vpcFlowLogsConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the `VpcFlowLogsConfig`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### createVpcFlowLogsConfigCallable()
    
    
    public final UnaryCallable<CreateVpcFlowLogsConfigRequest,Operation> createVpcFlowLogsConfigCallable()

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       CreateVpcFlowLogsConfigRequest request =
           CreateVpcFlowLogsConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVpcFlowLogsConfigId(
                   VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
                           "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
                       .toString())
               .setVpcFlowLogsConfig(VpcFlowLogsConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           organizationVpcFlowLogsServiceClient
               .createVpcFlowLogsConfigCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.CreateVpcFlowLogsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createVpcFlowLogsConfigOperationCallable()
    
    
    public final OperationCallable<CreateVpcFlowLogsConfigRequest,VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigOperationCallable()

Creates a new `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Creating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - creating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       CreateVpcFlowLogsConfigRequest request =
           CreateVpcFlowLogsConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVpcFlowLogsConfigId(
                   VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
                           "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
                       .toString())
               .setVpcFlowLogsConfig(VpcFlowLogsConfig.newBuilder().build())
               .build();
       OperationFuture<VpcFlowLogsConfig, OperationMetadata> future =
           organizationVpcFlowLogsServiceClient
               .createVpcFlowLogsConfigOperationCallable()
               .futureCall(request);
       // Do something.
       VpcFlowLogsConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.CreateVpcFlowLogsConfigRequest),[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### deleteVpcFlowLogsConfigAsync(@Nullable VpcFlowLogsConfigName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVpcFlowLogsConfigAsync(@Nullable VpcFlowLogsConfigName name)

Deletes a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       VpcFlowLogsConfigName name =
           VpcFlowLogsConfigName.ofOrganizationLocationVpcFlowLogsConfigName(
               "[ORGANIZATION]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]");
       organizationVpcFlowLogsServiceClient.deleteVpcFlowLogsConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.VpcFlowLogsConfigName`  
Required. The resource name of the VpcFlowLogsConfig, in one of the following formats: \- For a project-level resource: `projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}` \- For an organization-level resource: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### deleteVpcFlowLogsConfigAsync(DeleteVpcFlowLogsConfigRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVpcFlowLogsConfigAsync(DeleteVpcFlowLogsConfigRequest request)

Deletes a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       DeleteVpcFlowLogsConfigRequest request =
           DeleteVpcFlowLogsConfigRequest.newBuilder()
               .setName(
                   VpcFlowLogsConfigName.ofOrganizationLocationVpcFlowLogsConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
                       .toString())
               .build();
       organizationVpcFlowLogsServiceClient.deleteVpcFlowLogsConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.DeleteVpcFlowLogsConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### deleteVpcFlowLogsConfigAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVpcFlowLogsConfigAsync(String name)

Deletes a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       String name =
           VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
                   "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
               .toString();
       organizationVpcFlowLogsServiceClient.deleteVpcFlowLogsConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the VpcFlowLogsConfig, in one of the following formats: \- For a project-level resource: `projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}` \- For an organization-level resource: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### deleteVpcFlowLogsConfigCallable()
    
    
    public final UnaryCallable<DeleteVpcFlowLogsConfigRequest,Operation> deleteVpcFlowLogsConfigCallable()

Deletes a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       DeleteVpcFlowLogsConfigRequest request =
           DeleteVpcFlowLogsConfigRequest.newBuilder()
               .setName(
                   VpcFlowLogsConfigName.ofOrganizationLocationVpcFlowLogsConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           organizationVpcFlowLogsServiceClient
               .deleteVpcFlowLogsConfigCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.DeleteVpcFlowLogsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteVpcFlowLogsConfigOperationCallable()
    
    
    public final OperationCallable<DeleteVpcFlowLogsConfigRequest,Empty,OperationMetadata> deleteVpcFlowLogsConfigOperationCallable()

Deletes a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       DeleteVpcFlowLogsConfigRequest request =
           DeleteVpcFlowLogsConfigRequest.newBuilder()
               .setName(
                   VpcFlowLogsConfigName.ofOrganizationLocationVpcFlowLogsConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           organizationVpcFlowLogsServiceClient
               .deleteVpcFlowLogsConfigOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.DeleteVpcFlowLogsConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(ConnectivityTestName.of("[PROJECT]", "[TEST]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = organizationVpcFlowLogsServiceClient.getIamPolicy(request);
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
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(ConnectivityTestName.of("[PROJECT]", "[TEST]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           organizationVpcFlowLogsServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = organizationVpcFlowLogsServiceClient.getLocation(request);
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
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           organizationVpcFlowLogsServiceClient.getLocationCallable().futureCall(request);
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
  
### getSettings()
    
    
    public final @Nullable OrganizationVpcFlowLogsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceSettings` |   
  
### getStub()
    
    
    public OrganizationVpcFlowLogsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[OrganizationVpcFlowLogsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.stub.OrganizationVpcFlowLogsServiceStub)` |   
  
### getVpcFlowLogsConfig(@Nullable VpcFlowLogsConfigName name)
    
    
    public final VpcFlowLogsConfig getVpcFlowLogsConfig(@Nullable VpcFlowLogsConfigName name)

Gets the details of a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       VpcFlowLogsConfigName name =
           VpcFlowLogsConfigName.ofOrganizationLocationVpcFlowLogsConfigName(
               "[ORGANIZATION]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]");
       VpcFlowLogsConfig response = organizationVpcFlowLogsServiceClient.getVpcFlowLogsConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.VpcFlowLogsConfigName`  
Required. The resource name of the VpcFlowLogsConfig, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}` \- For organization-level resources: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)` |   
  
### getVpcFlowLogsConfig(GetVpcFlowLogsConfigRequest request)
    
    
    public final VpcFlowLogsConfig getVpcFlowLogsConfig(GetVpcFlowLogsConfigRequest request)

Gets the details of a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       GetVpcFlowLogsConfigRequest request =
           GetVpcFlowLogsConfigRequest.newBuilder()
               .setName(
                   VpcFlowLogsConfigName.ofOrganizationLocationVpcFlowLogsConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
                       .toString())
               .build();
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient.getVpcFlowLogsConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.GetVpcFlowLogsConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)` |   
  
### getVpcFlowLogsConfig(String name)
    
    
    public final VpcFlowLogsConfig getVpcFlowLogsConfig(String name)

Gets the details of a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       String name =
           VpcFlowLogsConfigName.ofProjectLocationVpcFlowLogsConfigName(
                   "[PROJECT]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
               .toString();
       VpcFlowLogsConfig response = organizationVpcFlowLogsServiceClient.getVpcFlowLogsConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the VpcFlowLogsConfig, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}` \- For organization-level resources: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}`  
**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)` |   
  
### getVpcFlowLogsConfigCallable()
    
    
    public final UnaryCallable<GetVpcFlowLogsConfigRequest,VpcFlowLogsConfig> getVpcFlowLogsConfigCallable()

Gets the details of a specific `VpcFlowLogsConfig`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       GetVpcFlowLogsConfigRequest request =
           GetVpcFlowLogsConfigRequest.newBuilder()
               .setName(
                   VpcFlowLogsConfigName.ofOrganizationLocationVpcFlowLogsConfigName(
                           "[ORGANIZATION]", "[LOCATION]", "[VPC_FLOW_LOGS_CONFIG]")
                       .toString())
               .build();
       ApiFuture<VpcFlowLogsConfig> future =
           organizationVpcFlowLogsServiceClient.getVpcFlowLogsConfigCallable().futureCall(request);
       // Do something.
       VpcFlowLogsConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.GetVpcFlowLogsConfigRequest),[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)>` |   
  
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
    
    
    public final OrganizationVpcFlowLogsServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.This method can be called in two ways:

* **List all public locations:** Use the path `GET /v1/locations`.* **List project-visible locations:** Use the path`GET /v1/projects/{project_id}/locations`. This may include publiclocations as well as private or other locations specifically visibleto the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element :
           organizationVpcFlowLogsServiceClient.listLocations(request).iterateAll()) {
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
`[OrganizationVpcFlowLogsServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.This method can be called in two ways:

* **List all public locations:** Use the path `GET /v1/locations`.* **List project-visible locations:** Use the path`GET /v1/projects/{project_id}/locations`. This may include publiclocations as well as private or other locations specifically visibleto the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             organizationVpcFlowLogsServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,OrganizationVpcFlowLogsServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.This method can be called in two ways:

* **List all public locations:** Use the path `GET /v1/locations`.* **List project-visible locations:** Use the path`GET /v1/projects/{project_id}/locations`. This may include publiclocations as well as private or other locations specifically visibleto the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           organizationVpcFlowLogsServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient.ListLocationsPagedResponse)>` |   
  
### listVpcFlowLogsConfigs(@Nullable LocationName parent)
    
    
    public final OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse listVpcFlowLogsConfigs(@Nullable LocationName parent)

Lists all `VpcFlowLogsConfigs` in a given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (VpcFlowLogsConfig element :
           organizationVpcFlowLogsServiceClient.listVpcFlowLogsConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.LocationName`  
Required. The parent resource of the VpcFlowLogsConfig, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse)` |   
  
### listVpcFlowLogsConfigs(@Nullable OrganizationLocationName parent)
    
    
    public final OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse listVpcFlowLogsConfigs(@Nullable OrganizationLocationName parent)

Lists all `VpcFlowLogsConfigs` in a given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (VpcFlowLogsConfig element :
           organizationVpcFlowLogsServiceClient.listVpcFlowLogsConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkmanagement.v1.OrganizationLocationName`  
Required. The parent resource of the VpcFlowLogsConfig, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse)` |   
  
### listVpcFlowLogsConfigs(ListVpcFlowLogsConfigsRequest request)
    
    
    public final OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse listVpcFlowLogsConfigs(ListVpcFlowLogsConfigsRequest request)

Lists all `VpcFlowLogsConfigs` in a given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       ListVpcFlowLogsConfigsRequest request =
           ListVpcFlowLogsConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (VpcFlowLogsConfig element :
           organizationVpcFlowLogsServiceClient.listVpcFlowLogsConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVpcFlowLogsConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse)` |   
  
### listVpcFlowLogsConfigs(String parent)
    
    
    public final OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse listVpcFlowLogsConfigs(String parent)

Lists all `VpcFlowLogsConfigs` in a given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (VpcFlowLogsConfig element :
           organizationVpcFlowLogsServiceClient.listVpcFlowLogsConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the VpcFlowLogsConfig, in one of the following formats: \- For project-level resources: `projects/{project_id}/locations/global` \- For organization-level resources: `organizations/{organization_id}/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse)` |   
  
### listVpcFlowLogsConfigsCallable()
    
    
    public final UnaryCallable<ListVpcFlowLogsConfigsRequest,ListVpcFlowLogsConfigsResponse> listVpcFlowLogsConfigsCallable()

Lists all `VpcFlowLogsConfigs` in a given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       ListVpcFlowLogsConfigsRequest request =
           ListVpcFlowLogsConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListVpcFlowLogsConfigsResponse response =
             organizationVpcFlowLogsServiceClient.listVpcFlowLogsConfigsCallable().call(request);
         for (VpcFlowLogsConfig element : response.getVpcFlowLogsConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVpcFlowLogsConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsRequest),[ListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse)>` |   
  
### listVpcFlowLogsConfigsPagedCallable()
    
    
    public final UnaryCallable<ListVpcFlowLogsConfigsRequest,OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse> listVpcFlowLogsConfigsPagedCallable()

Lists all `VpcFlowLogsConfigs` in a given organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       ListVpcFlowLogsConfigsRequest request =
           ListVpcFlowLogsConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<VpcFlowLogsConfig> future =
           organizationVpcFlowLogsServiceClient
               .listVpcFlowLogsConfigsPagedCallable()
               .futureCall(request);
       // Do something.
       for (VpcFlowLogsConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVpcFlowLogsConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsRequest),[ListVpcFlowLogsConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OrganizationVpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse)>` |   
  
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
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(ConnectivityTestName.of("[PROJECT]", "[TEST]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = organizationVpcFlowLogsServiceClient.setIamPolicy(request);
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
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(ConnectivityTestName.of("[PROJECT]", "[TEST]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           organizationVpcFlowLogsServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(ConnectivityTestName.of("[PROJECT]", "[TEST]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           organizationVpcFlowLogsServiceClient.testIamPermissions(request);
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
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(ConnectivityTestName.of("[PROJECT]", "[TEST]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           organizationVpcFlowLogsServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateVpcFlowLogsConfigAsync(UpdateVpcFlowLogsConfigRequest request)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> updateVpcFlowLogsConfigAsync(UpdateVpcFlowLogsConfigRequest request)

Updates an existing `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Updating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - updating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       UpdateVpcFlowLogsConfigRequest request =
           UpdateVpcFlowLogsConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setVpcFlowLogsConfig(VpcFlowLogsConfig.newBuilder().build())
               .build();
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient.updateVpcFlowLogsConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.UpdateVpcFlowLogsConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### updateVpcFlowLogsConfigAsync(VpcFlowLogsConfig vpcFlowLogsConfig, FieldMask updateMask)
    
    
    public final OperationFuture<VpcFlowLogsConfig,OperationMetadata> updateVpcFlowLogsConfigAsync(VpcFlowLogsConfig vpcFlowLogsConfig, FieldMask updateMask)

Updates an existing `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Updating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - updating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       VpcFlowLogsConfig vpcFlowLogsConfig = VpcFlowLogsConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       VpcFlowLogsConfig response =
           organizationVpcFlowLogsServiceClient
               .updateVpcFlowLogsConfigAsync(vpcFlowLogsConfig, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`vpcFlowLogsConfig` | `[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig)`  
Required. Only fields specified in update_mask are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update. At least one path must be supplied in this field. For example, to change the state of the configuration to ENABLED, specify `update_mask` = `"state"`, and the `vpc_flow_logs_config` would be: `vpc_flow_logs_config = { name = "projects/my-project/locations/global/vpcFlowLogsConfigs/my-config" state = "ENABLED" }`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
### updateVpcFlowLogsConfigCallable()
    
    
    public final UnaryCallable<UpdateVpcFlowLogsConfigRequest,Operation> updateVpcFlowLogsConfigCallable()

Updates an existing `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Updating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - updating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       UpdateVpcFlowLogsConfigRequest request =
           UpdateVpcFlowLogsConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setVpcFlowLogsConfig(VpcFlowLogsConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           organizationVpcFlowLogsServiceClient
               .updateVpcFlowLogsConfigCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.UpdateVpcFlowLogsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateVpcFlowLogsConfigOperationCallable()
    
    
    public final OperationCallable<UpdateVpcFlowLogsConfigRequest,VpcFlowLogsConfig,OperationMetadata> updateVpcFlowLogsConfigOperationCallable()

Updates an existing `VpcFlowLogsConfig`. If a configuration with the exact same settings already exists (even if the ID is different), the creation fails. Notes:

1\. Updating a configuration with `state=DISABLED` will fail 2. The following fields are not considered as settings for the purpose of the check mentioned above, therefore - updating another configuration with the same fields but different values for the following fields will fail as well: * name * create_time * update_time * labels * description

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationVpcFlowLogsServiceClient organizationVpcFlowLogsServiceClient =
         OrganizationVpcFlowLogsServiceClient.create()) {
       UpdateVpcFlowLogsConfigRequest request =
           UpdateVpcFlowLogsConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setVpcFlowLogsConfig(VpcFlowLogsConfig.newBuilder().build())
               .build();
       OperationFuture<VpcFlowLogsConfig, OperationMetadata> future =
           organizationVpcFlowLogsServiceClient
               .updateVpcFlowLogsConfigOperationCallable()
               .futureCall(request);
       // Do something.
       VpcFlowLogsConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.UpdateVpcFlowLogsConfigRequest),[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
