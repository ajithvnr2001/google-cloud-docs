---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient
title: Class LicenseManagementServiceClient (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:28.428443+00:00
---

# Class LicenseManagementServiceClient (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LicenseManagementServiceClient (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudcommerceconsumerprocurement/google-cloud-cloudcommerceconsumerprocurement/src/main/java/com/google/cloud/commerce/consumer/procurement/v1/LicenseManagementServiceClient.java)| [Product Reference](https://cloud.google.com/marketplace/)  
---|---  
  
Service Description: Service for managing licenses.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       String name = "name3373707";
       LicensePool response = licenseManagementServiceClient.getLicensePool(name);
     }
     

Note: close() needs to be called on the LicenseManagementServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetLicensePool |  Gets the license pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLicensePool(GetLicensePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLicensePool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLicensePoolCallable() 

  
UpdateLicensePool |  Updates the license pool if one exists for this Order. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLicensePool(UpdateLicensePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateLicensePool(LicensePool licensePool, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLicensePoolCallable() 

  
Assign |  Assigns a license to a user. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * assign(AssignRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * assign(String parent, List<String> usernames) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * assignCallable() 

  
Unassign |  Unassigns a license from a user. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * unassign(UnassignRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * unassign(String parent, List<String> usernames) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * unassignCallable() 

  
EnumerateLicensedUsers |  Enumerates all users assigned a license. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enumerateLicensedUsers(EnumerateLicensedUsersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * enumerateLicensedUsers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enumerateLicensedUsersPagedCallable() 
  * enumerateLicensedUsersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LicenseManagementServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LicenseManagementServiceSettings licenseManagementServiceSettings =
         LicenseManagementServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create(licenseManagementServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LicenseManagementServiceSettings licenseManagementServiceSettings =
         LicenseManagementServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create(licenseManagementServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LicenseManagementServiceSettings licenseManagementServiceSettings =
         LicenseManagementServiceSettings.newHttpJsonBuilder().build();
     LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create(licenseManagementServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LicenseManagementServiceClient

## Static Methods 

### create()
    
    
    public static final LicenseManagementServiceClient create()

Constructs an instance of LicenseManagementServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LicenseManagementServiceSettings settings)
    
    
    public static final LicenseManagementServiceClient create(LicenseManagementServiceSettings settings)

Constructs an instance of LicenseManagementServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LicenseManagementServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LicenseManagementServiceStub stub)
    
    
    public static final LicenseManagementServiceClient create(LicenseManagementServiceStub stub)

Constructs an instance of LicenseManagementServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(LicenseManagementServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LicenseManagementServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.stub.LicenseManagementServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient)` |   
  
## Constructors 

### LicenseManagementServiceClient(LicenseManagementServiceSettings settings)
    
    
    protected LicenseManagementServiceClient(LicenseManagementServiceSettings settings)

Constructs an instance of LicenseManagementServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LicenseManagementServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings)`  
  
  
### LicenseManagementServiceClient(LicenseManagementServiceStub stub)
    
    
    protected LicenseManagementServiceClient(LicenseManagementServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LicenseManagementServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.stub.LicenseManagementServiceStub)`  
  
  
## Methods 

### assign(AssignRequest request)
    
    
    public final AssignResponse assign(AssignRequest request)

Assigns a license to a user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       AssignRequest request =
           AssignRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllUsernames(new ArrayList<String>())
               .build();
       AssignResponse response = licenseManagementServiceClient.assign(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AssignRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.AssignRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AssignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.AssignResponse)` |   
  
### assign(String parent, List<String> usernames)
    
    
    public final AssignResponse assign(String parent, List<String> usernames)

Assigns a license to a user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       String parent = "parent-995424086";
       List<String> usernames = new ArrayList<>();
       AssignResponse response = licenseManagementServiceClient.assign(parent, usernames);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. License pool name.  
`usernames` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Username. Format: `name@domain.com`.  
**Returns**  
---  
**Type** | **Description**  
`[AssignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.AssignResponse)` |   
  
### assignCallable()
    
    
    public final UnaryCallable<AssignRequest,AssignResponse> assignCallable()

Assigns a license to a user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       AssignRequest request =
           AssignRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllUsernames(new ArrayList<String>())
               .build();
       ApiFuture<AssignResponse> future =
           licenseManagementServiceClient.assignCallable().futureCall(request);
       // Do something.
       AssignResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AssignRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.AssignRequest),[AssignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.AssignResponse)>` |   
  
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

### enumerateLicensedUsers(EnumerateLicensedUsersRequest request)
    
    
    public final LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse enumerateLicensedUsers(EnumerateLicensedUsersRequest request)

Enumerates all users assigned a license.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       EnumerateLicensedUsersRequest request =
           EnumerateLicensedUsersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (LicensedUser element :
           licenseManagementServiceClient.enumerateLicensedUsers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnumerateLicensedUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.EnumerateLicensedUsersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse)` |   
  
### enumerateLicensedUsers(String parent)
    
    
    public final LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse enumerateLicensedUsers(String parent)

Enumerates all users assigned a license.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       String parent = "parent-995424086";
       for (LicensedUser element :
           licenseManagementServiceClient.enumerateLicensedUsers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. License pool name.  
**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse)` |   
  
### enumerateLicensedUsersCallable()
    
    
    public final UnaryCallable<EnumerateLicensedUsersRequest,EnumerateLicensedUsersResponse> enumerateLicensedUsersCallable()

Enumerates all users assigned a license.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       EnumerateLicensedUsersRequest request =
           EnumerateLicensedUsersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         EnumerateLicensedUsersResponse response =
             licenseManagementServiceClient.enumerateLicensedUsersCallable().call(request);
         for (LicensedUser element : response.getLicensedUsersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnumerateLicensedUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.EnumerateLicensedUsersRequest),[EnumerateLicensedUsersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.EnumerateLicensedUsersResponse)>` |   
  
### enumerateLicensedUsersPagedCallable()
    
    
    public final UnaryCallable<EnumerateLicensedUsersRequest,LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse> enumerateLicensedUsersPagedCallable()

Enumerates all users assigned a license.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       EnumerateLicensedUsersRequest request =
           EnumerateLicensedUsersRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<LicensedUser> future =
           licenseManagementServiceClient.enumerateLicensedUsersPagedCallable().futureCall(request);
       // Do something.
       for (LicensedUser element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnumerateLicensedUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.EnumerateLicensedUsersRequest),[EnumerateLicensedUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse)>` |   
  
### getLicensePool(GetLicensePoolRequest request)
    
    
    public final LicensePool getLicensePool(GetLicensePoolRequest request)

Gets the license pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       GetLicensePoolRequest request =
           GetLicensePoolRequest.newBuilder().setName("name3373707").build();
       LicensePool response = licenseManagementServiceClient.getLicensePool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLicensePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.GetLicensePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)` |   
  
### getLicensePool(String name)
    
    
    public final LicensePool getLicensePool(String name)

Gets the license pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       String name = "name3373707";
       LicensePool response = licenseManagementServiceClient.getLicensePool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the license pool to get. Format: `billingAccounts/{billing_account}/orders/{order}/licensePool`  
**Returns**  
---  
**Type** | **Description**  
`[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)` |   
  
### getLicensePoolCallable()
    
    
    public final UnaryCallable<GetLicensePoolRequest,LicensePool> getLicensePoolCallable()

Gets the license pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       GetLicensePoolRequest request =
           GetLicensePoolRequest.newBuilder().setName("name3373707").build();
       ApiFuture<LicensePool> future =
           licenseManagementServiceClient.getLicensePoolCallable().futureCall(request);
       // Do something.
       LicensePool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLicensePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.GetLicensePoolRequest),[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)>` |   
  
### getSettings()
    
    
    public final @Nullable LicenseManagementServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings` |   
  
### getStub()
    
    
    public LicenseManagementServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.stub.LicenseManagementServiceStub)` |   
  
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
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### unassign(UnassignRequest request)
    
    
    public final UnassignResponse unassign(UnassignRequest request)

Unassigns a license from a user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       UnassignRequest request =
           UnassignRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllUsernames(new ArrayList<String>())
               .build();
       UnassignResponse response = licenseManagementServiceClient.unassign(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UnassignRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UnassignRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UnassignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UnassignResponse)` |   
  
### unassign(String parent, List<String> usernames)
    
    
    public final UnassignResponse unassign(String parent, List<String> usernames)

Unassigns a license from a user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       String parent = "parent-995424086";
       List<String> usernames = new ArrayList<>();
       UnassignResponse response = licenseManagementServiceClient.unassign(parent, usernames);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. License pool name.  
`usernames` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Username. Format: `name@domain.com`.  
**Returns**  
---  
**Type** | **Description**  
`[UnassignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UnassignResponse)` |   
  
### unassignCallable()
    
    
    public final UnaryCallable<UnassignRequest,UnassignResponse> unassignCallable()

Unassigns a license from a user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       UnassignRequest request =
           UnassignRequest.newBuilder()
               .setParent("parent-995424086")
               .addAllUsernames(new ArrayList<String>())
               .build();
       ApiFuture<UnassignResponse> future =
           licenseManagementServiceClient.unassignCallable().futureCall(request);
       // Do something.
       UnassignResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UnassignRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UnassignRequest),[UnassignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UnassignResponse)>` |   
  
### updateLicensePool(LicensePool licensePool, FieldMask updateMask)
    
    
    public final LicensePool updateLicensePool(LicensePool licensePool, FieldMask updateMask)

Updates the license pool if one exists for this Order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       LicensePool licensePool = LicensePool.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LicensePool response =
           licenseManagementServiceClient.updateLicensePool(licensePool, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`licensePool` | `[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)`  
Required. The license pool to update. The license pool's name field is used to identify the license pool to update. Format: `billingAccounts/{billing_account}/orders/{order}/licensePool`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)` |   
  
### updateLicensePool(UpdateLicensePoolRequest request)
    
    
    public final LicensePool updateLicensePool(UpdateLicensePoolRequest request)

Updates the license pool if one exists for this Order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       UpdateLicensePoolRequest request =
           UpdateLicensePoolRequest.newBuilder()
               .setLicensePool(LicensePool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       LicensePool response = licenseManagementServiceClient.updateLicensePool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLicensePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UpdateLicensePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)` |   
  
### updateLicensePoolCallable()
    
    
    public final UnaryCallable<UpdateLicensePoolRequest,LicensePool> updateLicensePoolCallable()

Updates the license pool if one exists for this Order.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LicenseManagementServiceClient licenseManagementServiceClient =
         LicenseManagementServiceClient.create()) {
       UpdateLicensePoolRequest request =
           UpdateLicensePoolRequest.newBuilder()
               .setLicensePool(LicensePool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<LicensePool> future =
           licenseManagementServiceClient.updateLicensePoolCallable().futureCall(request);
       // Do something.
       LicensePool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLicensePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UpdateLicensePoolRequest),[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
