---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceClient
title: Class CmEnrollmentServiceClient (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:49:49.423690+00:00
---

# Class CmEnrollmentServiceClient (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CmEnrollmentServiceClient (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudsecuritycompliance/google-cloud-cloudsecuritycompliance/src/main/java/com/google/cloud/cloudsecuritycompliance/v1/CmEnrollmentServiceClient.java)| [Product Reference](https://cloud.google.com/security-command-center/docs/compliance-manager-overview)  
---|---  
  
Service Description: Service describing CmEnrollment related RPCs for complianceManager.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       CmEnrollment cmEnrollment = CmEnrollment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CmEnrollment response =
           cmEnrollmentServiceClient.updateCmEnrollment(cmEnrollment, updateMask);
     }
     

Note: close() needs to be called on the CmEnrollmentServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
UpdateCmEnrollment |  Updates the Compliance Manager enrollment for a resource to facilitate an audit. Use this method to enroll a resource in Compliance Manager or to create or update feature-specific configurations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCmEnrollment(UpdateCmEnrollmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCmEnrollment(CmEnrollment cmEnrollment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCmEnrollmentCallable() 

  
CalculateEffectiveCmEnrollment |  Calculates the effective Compliance Manager enrollment for a resource. An effective enrollment is either a direct enrollment of a resource (if it exists), or an enrollment of the closest parent of a resource that's enrolled in Compliance Manager. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * calculateEffectiveCmEnrollment(CalculateEffectiveCmEnrollmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * calculateEffectiveCmEnrollment(CmEnrollmentName name) 
  * calculateEffectiveCmEnrollment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * calculateEffectiveCmEnrollmentCallable() 

  
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

This class can be customized by passing in a custom instance of CmEnrollmentServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmEnrollmentServiceSettings cmEnrollmentServiceSettings =
         CmEnrollmentServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CmEnrollmentServiceClient cmEnrollmentServiceClient =
         CmEnrollmentServiceClient.create(cmEnrollmentServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmEnrollmentServiceSettings cmEnrollmentServiceSettings =
         CmEnrollmentServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CmEnrollmentServiceClient cmEnrollmentServiceClient =
         CmEnrollmentServiceClient.create(cmEnrollmentServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmEnrollmentServiceSettings cmEnrollmentServiceSettings =
         CmEnrollmentServiceSettings.newHttpJsonBuilder().build();
     CmEnrollmentServiceClient cmEnrollmentServiceClient =
         CmEnrollmentServiceClient.create(cmEnrollmentServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CmEnrollmentServiceClient

## Static Methods 

### create()
    
    
    public static final CmEnrollmentServiceClient create()

Constructs an instance of CmEnrollmentServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CmEnrollmentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmEnrollmentServiceSettings settings)
    
    
    public static final CmEnrollmentServiceClient create(CmEnrollmentServiceSettings settings)

Constructs an instance of CmEnrollmentServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmEnrollmentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmEnrollmentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmEnrollmentServiceStub stub)
    
    
    public static final CmEnrollmentServiceClient create(CmEnrollmentServiceStub stub)

Constructs an instance of CmEnrollmentServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CmEnrollmentServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmEnrollmentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.CmEnrollmentServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmEnrollmentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceClient)` |   
  
## Constructors 

### CmEnrollmentServiceClient(CmEnrollmentServiceSettings settings)
    
    
    protected CmEnrollmentServiceClient(CmEnrollmentServiceSettings settings)

Constructs an instance of CmEnrollmentServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmEnrollmentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceSettings)`  
  
  
### CmEnrollmentServiceClient(CmEnrollmentServiceStub stub)
    
    
    protected CmEnrollmentServiceClient(CmEnrollmentServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmEnrollmentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.CmEnrollmentServiceStub)`  
  
  
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
  
### calculateEffectiveCmEnrollment(@Nullable CmEnrollmentName name)
    
    
    public final CalculateEffectiveCmEnrollmentResponse calculateEffectiveCmEnrollment(@Nullable CmEnrollmentName name)

Calculates the effective Compliance Manager enrollment for a resource. An effective enrollment is either a direct enrollment of a resource (if it exists), or an enrollment of the closest parent of a resource that's enrolled in Compliance Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       CmEnrollmentName name =
           CmEnrollmentName.ofOrganizationLocationName("[ORGANIZATION]", "[LOCATION]");
       CalculateEffectiveCmEnrollmentResponse response =
           cmEnrollmentServiceClient.calculateEffectiveCmEnrollment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentName`  
Required. The name of the Compliance Manager enrollment to calculate. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}/cmEnrollment`
  * `folders/{folder_id}/locations/{location}/cmEnrollment`
  * `projects/{project_id}/locations/{location}/cmEnrollment`

  
**Returns**  
---  
**Type** | **Description**  
`[CalculateEffectiveCmEnrollmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CalculateEffectiveCmEnrollmentResponse)` |   
  
### calculateEffectiveCmEnrollment(CalculateEffectiveCmEnrollmentRequest request)
    
    
    public final CalculateEffectiveCmEnrollmentResponse calculateEffectiveCmEnrollment(CalculateEffectiveCmEnrollmentRequest request)

Calculates the effective Compliance Manager enrollment for a resource. An effective enrollment is either a direct enrollment of a resource (if it exists), or an enrollment of the closest parent of a resource that's enrolled in Compliance Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       CalculateEffectiveCmEnrollmentRequest request =
           CalculateEffectiveCmEnrollmentRequest.newBuilder()
               .setName(
                   CmEnrollmentName.ofOrganizationLocationName("[ORGANIZATION]", "[LOCATION]")
                       .toString())
               .build();
       CalculateEffectiveCmEnrollmentResponse response =
           cmEnrollmentServiceClient.calculateEffectiveCmEnrollment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CalculateEffectiveCmEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CalculateEffectiveCmEnrollmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CalculateEffectiveCmEnrollmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CalculateEffectiveCmEnrollmentResponse)` |   
  
### calculateEffectiveCmEnrollment(String name)
    
    
    public final CalculateEffectiveCmEnrollmentResponse calculateEffectiveCmEnrollment(String name)

Calculates the effective Compliance Manager enrollment for a resource. An effective enrollment is either a direct enrollment of a resource (if it exists), or an enrollment of the closest parent of a resource that's enrolled in Compliance Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       String name =
           CmEnrollmentName.ofOrganizationLocationName("[ORGANIZATION]", "[LOCATION]").toString();
       CalculateEffectiveCmEnrollmentResponse response =
           cmEnrollmentServiceClient.calculateEffectiveCmEnrollment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Compliance Manager enrollment to calculate. Supported formats are the following: 

  * `organizations/{organization_id}/locations/{location}/cmEnrollment`
  * `folders/{folder_id}/locations/{location}/cmEnrollment`
  * `projects/{project_id}/locations/{location}/cmEnrollment`

  
**Returns**  
---  
**Type** | **Description**  
`[CalculateEffectiveCmEnrollmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CalculateEffectiveCmEnrollmentResponse)` |   
  
### calculateEffectiveCmEnrollmentCallable()
    
    
    public final UnaryCallable<CalculateEffectiveCmEnrollmentRequest,CalculateEffectiveCmEnrollmentResponse> calculateEffectiveCmEnrollmentCallable()

Calculates the effective Compliance Manager enrollment for a resource. An effective enrollment is either a direct enrollment of a resource (if it exists), or an enrollment of the closest parent of a resource that's enrolled in Compliance Manager.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       CalculateEffectiveCmEnrollmentRequest request =
           CalculateEffectiveCmEnrollmentRequest.newBuilder()
               .setName(
                   CmEnrollmentName.ofOrganizationLocationName("[ORGANIZATION]", "[LOCATION]")
                       .toString())
               .build();
       ApiFuture<CalculateEffectiveCmEnrollmentResponse> future =
           cmEnrollmentServiceClient.calculateEffectiveCmEnrollmentCallable().futureCall(request);
       // Do something.
       CalculateEffectiveCmEnrollmentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CalculateEffectiveCmEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CalculateEffectiveCmEnrollmentRequest),[CalculateEffectiveCmEnrollmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CalculateEffectiveCmEnrollmentResponse)>` |   
  
### close()
    
    
    public final void close()

### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = cmEnrollmentServiceClient.getLocation(request);
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
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           cmEnrollmentServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable CmEnrollmentServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceSettings` |   
  
### getStub()
    
    
    public CmEnrollmentServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CmEnrollmentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.stub.CmEnrollmentServiceStub)` |   
  
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
    
    
    public final CmEnrollmentServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : cmEnrollmentServiceClient.listLocations(request).iterateAll()) {
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
`[CmEnrollmentServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             cmEnrollmentServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,CmEnrollmentServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           cmEnrollmentServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentServiceClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCmEnrollment(CmEnrollment cmEnrollment, FieldMask updateMask)
    
    
    public final CmEnrollment updateCmEnrollment(CmEnrollment cmEnrollment, FieldMask updateMask)

Updates the Compliance Manager enrollment for a resource to facilitate an audit. Use this method to enroll a resource in Compliance Manager or to create or update feature-specific configurations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       CmEnrollment cmEnrollment = CmEnrollment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CmEnrollment response =
           cmEnrollmentServiceClient.updateCmEnrollment(cmEnrollment, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`cmEnrollment` | `[CmEnrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollment)`  
Required. The Compliance Manager enrollment to update. The `name` field is used to identify the settings that you want to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields that you want to update.  
**Returns**  
---  
**Type** | **Description**  
`[CmEnrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollment)` |   
  
### updateCmEnrollment(UpdateCmEnrollmentRequest request)
    
    
    public final CmEnrollment updateCmEnrollment(UpdateCmEnrollmentRequest request)

Updates the Compliance Manager enrollment for a resource to facilitate an audit. Use this method to enroll a resource in Compliance Manager or to create or update feature-specific configurations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       UpdateCmEnrollmentRequest request =
           UpdateCmEnrollmentRequest.newBuilder()
               .setCmEnrollment(CmEnrollment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CmEnrollment response = cmEnrollmentServiceClient.updateCmEnrollment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCmEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.UpdateCmEnrollmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmEnrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollment)` |   
  
### updateCmEnrollmentCallable()
    
    
    public final UnaryCallable<UpdateCmEnrollmentRequest,CmEnrollment> updateCmEnrollmentCallable()

Updates the Compliance Manager enrollment for a resource to facilitate an audit. Use this method to enroll a resource in Compliance Manager or to create or update feature-specific configurations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmEnrollmentServiceClient cmEnrollmentServiceClient = CmEnrollmentServiceClient.create()) {
       UpdateCmEnrollmentRequest request =
           UpdateCmEnrollmentRequest.newBuilder()
               .setCmEnrollment(CmEnrollment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CmEnrollment> future =
           cmEnrollmentServiceClient.updateCmEnrollmentCallable().futureCall(request);
       // Do something.
       CmEnrollment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCmEnrollmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.UpdateCmEnrollmentRequest),[CmEnrollment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollment)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
