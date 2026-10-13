---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesClient
title: Class LicensesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:57.122078+00:00
---

# Class LicensesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LicensesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/LicensesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Licenses API.

This client uses Licenses version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       String license = "license166757441";
       License response = licensesClient.get(project, license);
     }
     

Note: close() needs to be called on the LicensesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified license. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteLicenseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String license) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified License resource. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetLicenseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String license) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyLicenseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Create a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertLicenseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, License licenseResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of licenses available in the specified project. This method does not get any licenses that belong to other projects, including licenses attached to publicly-available images, like Debian 9. If you want to get a list of publicly-available licenses, use this method to make a request to the respective image project, such as debian-cloud orwindows-cloud. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListLicensesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyLicenseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsLicenseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Updates a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateLicenseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String license, License licenseResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LicensesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LicensesSettings licensesSettings =
         LicensesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LicensesClient licensesClient = LicensesClient.create(licensesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LicensesSettings licensesSettings =
         LicensesSettings.newBuilder().setEndpoint(myEndpoint).build();
     LicensesClient licensesClient = LicensesClient.create(licensesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LicensesClient

## Static Methods 

### create()
    
    
    public static final LicensesClient create()

Constructs an instance of LicensesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LicensesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LicensesSettings settings)
    
    
    public static final LicensesClient create(LicensesSettings settings)

Constructs an instance of LicensesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LicensesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LicensesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LicensesStub stub)
    
    
    public static final LicensesClient create(LicensesStub stub)

Constructs an instance of LicensesClient, using the given stub for making calls. This is for advanced usage - prefer using create(LicensesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LicensesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.LicensesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LicensesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesClient)` |   
  
## Constructors 

### LicensesClient(LicensesSettings settings)
    
    
    protected LicensesClient(LicensesSettings settings)

Constructs an instance of LicensesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LicensesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesSettings)`  
  
  
### LicensesClient(LicensesStub stub)
    
    
    protected LicensesClient(LicensesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LicensesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.LicensesStub)`  
  
  
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

### deleteAsync(DeleteLicenseRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteLicenseRequest request)

Deletes the specified license. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       DeleteLicenseRequest request =
           DeleteLicenseRequest.newBuilder()
               .setLicense("license166757441")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = licensesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteLicenseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String license)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String license)

Deletes the specified license. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       String license = "license166757441";
       Operation response = licensesClient.deleteAsync(project, license).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`license` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the license resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteLicenseRequest,Operation> deleteCallable()

Deletes the specified license. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       DeleteLicenseRequest request =
           DeleteLicenseRequest.newBuilder()
               .setLicense("license166757441")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = licensesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteLicenseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteLicenseRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified license. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       DeleteLicenseRequest request =
           DeleteLicenseRequest.newBuilder()
               .setLicense("license166757441")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           licensesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteLicenseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetLicenseRequest request)
    
    
    public final License get(GetLicenseRequest request)

Returns the specified License resource. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       GetLicenseRequest request =
           GetLicenseRequest.newBuilder()
               .setLicense("license166757441")
               .setProject("project-309310695")
               .build();
       License response = licensesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetLicenseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[License](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.License)` |   
  
### get(String project, String license)
    
    
    public final License get(String project, String license)

Returns the specified License resource. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       String license = "license166757441";
       License response = licensesClient.get(project, license);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`license` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the License resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[License](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.License)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetLicenseRequest,License> getCallable()

Returns the specified License resource. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       GetLicenseRequest request =
           GetLicenseRequest.newBuilder()
               .setLicense("license166757441")
               .setProject("project-309310695")
               .build();
       ApiFuture<License> future = licensesClient.getCallable().futureCall(request);
       // Do something.
       License response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetLicenseRequest),[License](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.License)>` |   
  
### getIamPolicy(GetIamPolicyLicenseRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyLicenseRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       GetIamPolicyLicenseRequest request =
           GetIamPolicyLicenseRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = licensesClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyLicenseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String resource)
    
    
    public final Policy getIamPolicy(String project, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       Policy response = licensesClient.getIamPolicy(project, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyLicenseRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       GetIamPolicyLicenseRequest request =
           GetIamPolicyLicenseRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = licensesClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyLicenseRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable LicensesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.LicensesSettings` |   
  
### getStub()
    
    
    public LicensesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LicensesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.LicensesStub)` |   
  
### insertAsync(InsertLicenseRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertLicenseRequest request)

Create a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       InsertLicenseRequest request =
           InsertLicenseRequest.newBuilder()
               .setLicenseResource(License.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = licensesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertLicenseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, License licenseResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, License licenseResource)

Create a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       License licenseResource = License.newBuilder().build();
       Operation response = licensesClient.insertAsync(project, licenseResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`licenseResource` | `[License](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.License)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertLicenseRequest,Operation> insertCallable()

Create a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       InsertLicenseRequest request =
           InsertLicenseRequest.newBuilder()
               .setLicenseResource(License.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = licensesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertLicenseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertLicenseRequest,Operation,Operation> insertOperationCallable()

Create a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       InsertLicenseRequest request =
           InsertLicenseRequest.newBuilder()
               .setLicenseResource(License.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           licensesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertLicenseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListLicensesRequest request)
    
    
    public final LicensesClient.ListPagedResponse list(ListLicensesRequest request)

Retrieves the list of licenses available in the specified project. This method does not get any licenses that belong to other projects, including licenses attached to publicly-available images, like Debian 9. If you want to get a list of publicly-available licenses, use this method to make a request to the respective image project, such as debian-cloud orwindows-cloud. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       ListLicensesRequest request =
           ListLicensesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (License element : licensesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListLicensesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LicensesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final LicensesClient.ListPagedResponse list(String project)

Retrieves the list of licenses available in the specified project. This method does not get any licenses that belong to other projects, including licenses attached to publicly-available images, like Debian 9. If you want to get a list of publicly-available licenses, use this method to make a request to the respective image project, such as debian-cloud orwindows-cloud. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       for (License element : licensesClient.list(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[LicensesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListLicensesRequest,LicensesListResponse> listCallable()

Retrieves the list of licenses available in the specified project. This method does not get any licenses that belong to other projects, including licenses attached to publicly-available images, like Debian 9. If you want to get a list of publicly-available licenses, use this method to make a request to the respective image project, such as debian-cloud orwindows-cloud. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       ListLicensesRequest request =
           ListLicensesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         LicensesListResponse response = licensesClient.listCallable().call(request);
         for (License element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListLicensesRequest),[LicensesListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListLicensesRequest,LicensesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of licenses available in the specified project. This method does not get any licenses that belong to other projects, including licenses attached to publicly-available images, like Debian 9. If you want to get a list of publicly-available licenses, use this method to make a request to the respective image project, such as debian-cloud orwindows-cloud. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       ListLicensesRequest request =
           ListLicensesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<License> future = licensesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (License element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLicensesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListLicensesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.LicensesClient.ListPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyLicenseRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyLicenseRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       SetIamPolicyLicenseRequest request =
           SetIamPolicyLicenseRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = licensesClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyLicenseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetPolicyRequest globalSetPolicyRequestResource =
           GlobalSetPolicyRequest.newBuilder().build();
       Policy response =
           licensesClient.setIamPolicy(project, resource, globalSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetPolicyRequestResource` | `[GlobalSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyLicenseRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       SetIamPolicyLicenseRequest request =
           SetIamPolicyLicenseRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = licensesClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyLicenseRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsLicenseRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsLicenseRequest request)

Returns permissions that a caller has on the specified resource. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       TestIamPermissionsLicenseRequest request =
           TestIamPermissionsLicenseRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = licensesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsLicenseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           licensesClient.testIamPermissions(project, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsLicenseRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       TestIamPermissionsLicenseRequest request =
           TestIamPermissionsLicenseRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           licensesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsLicenseRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateLicenseRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateLicenseRequest request)

Updates a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       UpdateLicenseRequest request =
           UpdateLicenseRequest.newBuilder()
               .setLicense("license166757441")
               .setLicenseResource(License.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       Operation response = licensesClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateLicenseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String license, License licenseResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String license, License licenseResource)

Updates a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       String project = "project-309310695";
       String license = "license166757441";
       License licenseResource = License.newBuilder().build();
       Operation response = licensesClient.updateAsync(project, license, licenseResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`license` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The license name for this request.  
`licenseResource` | `[License](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.License)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateLicenseRequest,Operation> updateCallable()

Updates a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       UpdateLicenseRequest request =
           UpdateLicenseRequest.newBuilder()
               .setLicense("license166757441")
               .setLicenseResource(License.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       ApiFuture<Operation> future = licensesClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateLicenseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateLicenseRequest,Operation,Operation> updateOperationCallable()

Updates a License resource in the specified project. *Caution* This resource is intended for use only by third-party partners who are creatingCloud Marketplace images.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicensesClient licensesClient = LicensesClient.create()) {
       UpdateLicenseRequest request =
           UpdateLicenseRequest.newBuilder()
               .setLicense("license166757441")
               .setLicenseResource(License.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       OperationFuture<Operation, Operation> future =
           licensesClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLicenseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateLicenseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
