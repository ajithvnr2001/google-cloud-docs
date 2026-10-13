---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient
title: Class CloudQuotasClient (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:25.505542+00:00
---

# Class CloudQuotasClient (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudQuotasClient (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudquotas/google-cloud-cloudquotas/src/main/java/com/google/api/cloudquotas/v1beta/CloudQuotasClient.java)| [Product Reference](https://cloud.google.com/cloudquotas/docs/)  
---|---  
  
Service Description: The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.

\- List/Get the metadata and current status of the quotas for a service. - Create/Update quota preferencess that declare the preferred quota values. - Check the status of a quota preference request. - List/Get pending and historical quota preference.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       QuotaInfoName name =
           QuotaInfoName.ofProjectLocationServiceQuotaInfoName(
               "[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]");
       QuotaInfo response = cloudQuotasClient.getQuotaInfo(name);
     }
     

Note: close() needs to be called on the CloudQuotasClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListQuotaInfos |  Lists QuotaInfos of all quotas for a given project, folder or organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listQuotaInfos(ListQuotaInfosRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listQuotaInfos(ServiceName parent) 
  * listQuotaInfos(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listQuotaInfosPagedCallable() 
  * listQuotaInfosCallable() 

  
GetQuotaInfo |  Retrieve the QuotaInfo of a quota for a project, folder or organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getQuotaInfo(GetQuotaInfoRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getQuotaInfo(QuotaInfoName name) 
  * getQuotaInfo(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getQuotaInfoCallable() 

  
ListQuotaPreferences |  Lists QuotaPreferences in a given project, folder or organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listQuotaPreferences(ListQuotaPreferencesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listQuotaPreferences(LocationName parent) 
  * listQuotaPreferences(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listQuotaPreferencesPagedCallable() 
  * listQuotaPreferencesCallable() 

  
GetQuotaPreference |  Gets details of a single QuotaPreference. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getQuotaPreference(GetQuotaPreferenceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getQuotaPreference(QuotaPreferenceName name) 
  * getQuotaPreference(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getQuotaPreferenceCallable() 

  
CreateQuotaPreference |  Creates a new QuotaPreference that declares the desired value for a quota. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createQuotaPreference(CreateQuotaPreferenceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createQuotaPreference(LocationName parent, QuotaPreference quotaPreference) 
  * createQuotaPreference(String parent, QuotaPreference quotaPreference) 
  * createQuotaPreference(LocationName parent, QuotaPreference quotaPreference, String quotaPreferenceId) 
  * createQuotaPreference(String parent, QuotaPreference quotaPreference, String quotaPreferenceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createQuotaPreferenceCallable() 

  
UpdateQuotaPreference |  Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateQuotaPreference(UpdateQuotaPreferenceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateQuotaPreference(QuotaPreference quotaPreference, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateQuotaPreferenceCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CloudQuotasSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudQuotasSettings cloudQuotasSettings =
         CloudQuotasSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create(cloudQuotasSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudQuotasSettings cloudQuotasSettings =
         CloudQuotasSettings.newBuilder().setEndpoint(myEndpoint).build();
     CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create(cloudQuotasSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudQuotasSettings cloudQuotasSettings = CloudQuotasSettings.newHttpJsonBuilder().build();
     CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create(cloudQuotasSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudQuotasClient

## Static Methods 

### create()
    
    
    public static final CloudQuotasClient create()

Constructs an instance of CloudQuotasClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudQuotasSettings settings)
    
    
    public static final CloudQuotasClient create(CloudQuotasSettings settings)

Constructs an instance of CloudQuotasClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudQuotasSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudQuotasStub stub)
    
    
    public static final CloudQuotasClient create(CloudQuotasStub stub)

Constructs an instance of CloudQuotasClient, using the given stub for making calls. This is for advanced usage - prefer using create(CloudQuotasSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudQuotasStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.stub.CloudQuotasStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient)` |   
  
## Constructors 

### CloudQuotasClient(CloudQuotasSettings settings)
    
    
    protected CloudQuotasClient(CloudQuotasSettings settings)

Constructs an instance of CloudQuotasClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudQuotasSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasSettings)`  
  
  
### CloudQuotasClient(CloudQuotasStub stub)
    
    
    protected CloudQuotasClient(CloudQuotasStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudQuotasStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.stub.CloudQuotasStub)`  
  
  
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

### createQuotaPreference(@Nullable LocationName parent, QuotaPreference quotaPreference)
    
    
    public final QuotaPreference createQuotaPreference(@Nullable LocationName parent, QuotaPreference quotaPreference)

Creates a new QuotaPreference that declares the desired value for a quota.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       LocationName parent = LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]");
       QuotaPreference quotaPreference = QuotaPreference.newBuilder().build();
       QuotaPreference response = cloudQuotasClient.createQuotaPreference(parent, quotaPreference);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1beta.LocationName`  
Required. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)`  
Required. The resource being created  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### createQuotaPreference(@Nullable LocationName parent, QuotaPreference quotaPreference, String quotaPreferenceId)
    
    
    public final QuotaPreference createQuotaPreference(@Nullable LocationName parent, QuotaPreference quotaPreference, String quotaPreferenceId)

Creates a new QuotaPreference that declares the desired value for a quota.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       LocationName parent = LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]");
       QuotaPreference quotaPreference = QuotaPreference.newBuilder().build();
       String quotaPreferenceId = "quotaPreferenceId-948332050";
       QuotaPreference response =
           cloudQuotasClient.createQuotaPreference(parent, quotaPreference, quotaPreferenceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1beta.LocationName`  
Required. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)`  
Required. The resource being created  
`quotaPreferenceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### createQuotaPreference(CreateQuotaPreferenceRequest request)
    
    
    public final QuotaPreference createQuotaPreference(CreateQuotaPreferenceRequest request)

Creates a new QuotaPreference that declares the desired value for a quota.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       CreateQuotaPreferenceRequest request =
           CreateQuotaPreferenceRequest.newBuilder()
               .setParent(LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString())
               .setQuotaPreferenceId("quotaPreferenceId-948332050")
               .setQuotaPreference(QuotaPreference.newBuilder().build())
               .addAllIgnoreSafetyChecks(new ArrayList<QuotaSafetyCheck>())
               .build();
       QuotaPreference response = cloudQuotasClient.createQuotaPreference(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CreateQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### createQuotaPreference(String parent, QuotaPreference quotaPreference)
    
    
    public final QuotaPreference createQuotaPreference(String parent, QuotaPreference quotaPreference)

Creates a new QuotaPreference that declares the desired value for a quota.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       String parent = LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString();
       QuotaPreference quotaPreference = QuotaPreference.newBuilder().build();
       QuotaPreference response = cloudQuotasClient.createQuotaPreference(parent, quotaPreference);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)`  
Required. The resource being created  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### createQuotaPreference(String parent, QuotaPreference quotaPreference, String quotaPreferenceId)
    
    
    public final QuotaPreference createQuotaPreference(String parent, QuotaPreference quotaPreference, String quotaPreferenceId)

Creates a new QuotaPreference that declares the desired value for a quota.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       String parent = LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString();
       QuotaPreference quotaPreference = QuotaPreference.newBuilder().build();
       String quotaPreferenceId = "quotaPreferenceId-948332050";
       QuotaPreference response =
           cloudQuotasClient.createQuotaPreference(parent, quotaPreference, quotaPreferenceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent. Example: `projects/123/locations/global`  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)`  
Required. The resource being created  
`quotaPreferenceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### createQuotaPreferenceCallable()
    
    
    public final UnaryCallable<CreateQuotaPreferenceRequest,QuotaPreference> createQuotaPreferenceCallable()

Creates a new QuotaPreference that declares the desired value for a quota.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       CreateQuotaPreferenceRequest request =
           CreateQuotaPreferenceRequest.newBuilder()
               .setParent(LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString())
               .setQuotaPreferenceId("quotaPreferenceId-948332050")
               .setQuotaPreference(QuotaPreference.newBuilder().build())
               .addAllIgnoreSafetyChecks(new ArrayList<QuotaSafetyCheck>())
               .build();
       ApiFuture<QuotaPreference> future =
           cloudQuotasClient.createQuotaPreferenceCallable().futureCall(request);
       // Do something.
       QuotaPreference response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CreateQuotaPreferenceRequest),[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)>` |   
  
### getQuotaInfo(@Nullable QuotaInfoName name)
    
    
    public final QuotaInfo getQuotaInfo(@Nullable QuotaInfoName name)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       QuotaInfoName name =
           QuotaInfoName.ofProjectLocationServiceQuotaInfoName(
               "[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]");
       QuotaInfo response = cloudQuotasClient.getQuotaInfo(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1beta.QuotaInfoName`  
Required. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaInfo)` |   
  
### getQuotaInfo(GetQuotaInfoRequest request)
    
    
    public final QuotaInfo getQuotaInfo(GetQuotaInfoRequest request)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       GetQuotaInfoRequest request =
           GetQuotaInfoRequest.newBuilder()
               .setName(
                   QuotaInfoName.ofProjectLocationServiceQuotaInfoName(
                           "[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]")
                       .toString())
               .build();
       QuotaInfo response = cloudQuotasClient.getQuotaInfo(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.GetQuotaInfoRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaInfo)` |   
  
### getQuotaInfo(String name)
    
    
    public final QuotaInfo getQuotaInfo(String name)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       String name =
           QuotaInfoName.ofProjectLocationServiceQuotaInfoName(
                   "[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]")
               .toString();
       QuotaInfo response = cloudQuotasClient.getQuotaInfo(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the quota info. An example name: `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaInfo)` |   
  
### getQuotaInfoCallable()
    
    
    public final UnaryCallable<GetQuotaInfoRequest,QuotaInfo> getQuotaInfoCallable()

Retrieve the QuotaInfo of a quota for a project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       GetQuotaInfoRequest request =
           GetQuotaInfoRequest.newBuilder()
               .setName(
                   QuotaInfoName.ofProjectLocationServiceQuotaInfoName(
                           "[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]")
                       .toString())
               .build();
       ApiFuture<QuotaInfo> future = cloudQuotasClient.getQuotaInfoCallable().futureCall(request);
       // Do something.
       QuotaInfo response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetQuotaInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.GetQuotaInfoRequest),[QuotaInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaInfo)>` |   
  
### getQuotaPreference(@Nullable QuotaPreferenceName name)
    
    
    public final QuotaPreference getQuotaPreference(@Nullable QuotaPreferenceName name)

Gets details of a single QuotaPreference.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       QuotaPreferenceName name =
           QuotaPreferenceName.ofProjectLocationQuotaPreferenceName(
               "[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]");
       QuotaPreference response = cloudQuotasClient.getQuotaPreference(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1beta.QuotaPreferenceName`  
Required. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### getQuotaPreference(GetQuotaPreferenceRequest request)
    
    
    public final QuotaPreference getQuotaPreference(GetQuotaPreferenceRequest request)

Gets details of a single QuotaPreference.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       GetQuotaPreferenceRequest request =
           GetQuotaPreferenceRequest.newBuilder()
               .setName(
                   QuotaPreferenceName.ofProjectLocationQuotaPreferenceName(
                           "[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]")
                       .toString())
               .build();
       QuotaPreference response = cloudQuotasClient.getQuotaPreference(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.GetQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### getQuotaPreference(String name)
    
    
    public final QuotaPreference getQuotaPreference(String name)

Gets details of a single QuotaPreference.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       String name =
           QuotaPreferenceName.ofProjectLocationQuotaPreferenceName(
                   "[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]")
               .toString();
       QuotaPreference response = cloudQuotasClient.getQuotaPreference(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource Example name: `projects/123/locations/global/quota_preferences/my-config-for-us-east1`  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### getQuotaPreferenceCallable()
    
    
    public final UnaryCallable<GetQuotaPreferenceRequest,QuotaPreference> getQuotaPreferenceCallable()

Gets details of a single QuotaPreference.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       GetQuotaPreferenceRequest request =
           GetQuotaPreferenceRequest.newBuilder()
               .setName(
                   QuotaPreferenceName.ofProjectLocationQuotaPreferenceName(
                           "[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]")
                       .toString())
               .build();
       ApiFuture<QuotaPreference> future =
           cloudQuotasClient.getQuotaPreferenceCallable().futureCall(request);
       // Do something.
       QuotaPreference response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.GetQuotaPreferenceRequest),[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)>` |   
  
### getSettings()
    
    
    public final @Nullable CloudQuotasSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1beta.CloudQuotasSettings` |   
  
### getStub()
    
    
    public CloudQuotasStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.stub.CloudQuotasStub)` |   
  
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
  
### listQuotaInfos(@Nullable ServiceName parent)
    
    
    public final CloudQuotasClient.ListQuotaInfosPagedResponse listQuotaInfos(@Nullable ServiceName parent)

Lists QuotaInfos of all quotas for a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       ServiceName parent =
           ServiceName.ofProjectLocationServiceName("[PROJECT]", "[LOCATION]", "[SERVICE]");
       for (QuotaInfo element : cloudQuotasClient.listQuotaInfos(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1beta.ServiceName`  
Required. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed. Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient.ListQuotaInfosPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient.ListQuotaInfosPagedResponse)` |   
  
### listQuotaInfos(ListQuotaInfosRequest request)
    
    
    public final CloudQuotasClient.ListQuotaInfosPagedResponse listQuotaInfos(ListQuotaInfosRequest request)

Lists QuotaInfos of all quotas for a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       ListQuotaInfosRequest request =
           ListQuotaInfosRequest.newBuilder()
               .setParent(
                   ServiceName.ofProjectLocationServiceName("[PROJECT]", "[LOCATION]", "[SERVICE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (QuotaInfo element : cloudQuotasClient.listQuotaInfos(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.ListQuotaInfosRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient.ListQuotaInfosPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient.ListQuotaInfosPagedResponse)` |   
  
### listQuotaInfos(String parent)
    
    
    public final CloudQuotasClient.ListQuotaInfosPagedResponse listQuotaInfos(String parent)

Lists QuotaInfos of all quotas for a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       String parent =
           ServiceName.ofProjectLocationServiceName("[PROJECT]", "[LOCATION]", "[SERVICE]")
               .toString();
       for (QuotaInfo element : cloudQuotasClient.listQuotaInfos(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed. Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient.ListQuotaInfosPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient.ListQuotaInfosPagedResponse)` |   
  
### listQuotaInfosCallable()
    
    
    public final UnaryCallable<ListQuotaInfosRequest,ListQuotaInfosResponse> listQuotaInfosCallable()

Lists QuotaInfos of all quotas for a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       ListQuotaInfosRequest request =
           ListQuotaInfosRequest.newBuilder()
               .setParent(
                   ServiceName.ofProjectLocationServiceName("[PROJECT]", "[LOCATION]", "[SERVICE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListQuotaInfosResponse response = cloudQuotasClient.listQuotaInfosCallable().call(request);
         for (QuotaInfo element : response.getQuotaInfosList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListQuotaInfosRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.ListQuotaInfosRequest),[ListQuotaInfosResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.ListQuotaInfosResponse)>` |   
  
### listQuotaInfosPagedCallable()
    
    
    public final UnaryCallable<ListQuotaInfosRequest,CloudQuotasClient.ListQuotaInfosPagedResponse> listQuotaInfosPagedCallable()

Lists QuotaInfos of all quotas for a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       ListQuotaInfosRequest request =
           ListQuotaInfosRequest.newBuilder()
               .setParent(
                   ServiceName.ofProjectLocationServiceName("[PROJECT]", "[LOCATION]", "[SERVICE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<QuotaInfo> future =
           cloudQuotasClient.listQuotaInfosPagedCallable().futureCall(request);
       // Do something.
       for (QuotaInfo element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListQuotaInfosRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.ListQuotaInfosRequest),[ListQuotaInfosPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient.ListQuotaInfosPagedResponse)>` |   
  
### listQuotaPreferences(@Nullable LocationName parent)
    
    
    public final CloudQuotasClient.ListQuotaPreferencesPagedResponse listQuotaPreferences(@Nullable LocationName parent)

Lists QuotaPreferences in a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       LocationName parent = LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]");
       for (QuotaPreference element : cloudQuotasClient.listQuotaPreferences(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1beta.LocationName`  
Required. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient.ListQuotaPreferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient.ListQuotaPreferencesPagedResponse)` |   
  
### listQuotaPreferences(ListQuotaPreferencesRequest request)
    
    
    public final CloudQuotasClient.ListQuotaPreferencesPagedResponse listQuotaPreferences(ListQuotaPreferencesRequest request)

Lists QuotaPreferences in a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       ListQuotaPreferencesRequest request =
           ListQuotaPreferencesRequest.newBuilder()
               .setParent(LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (QuotaPreference element : cloudQuotasClient.listQuotaPreferences(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.ListQuotaPreferencesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient.ListQuotaPreferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient.ListQuotaPreferencesPagedResponse)` |   
  
### listQuotaPreferences(String parent)
    
    
    public final CloudQuotasClient.ListQuotaPreferencesPagedResponse listQuotaPreferences(String parent)

Lists QuotaPreferences in a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       String parent = LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString();
       for (QuotaPreference element : cloudQuotasClient.listQuotaPreferences(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasClient.ListQuotaPreferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient.ListQuotaPreferencesPagedResponse)` |   
  
### listQuotaPreferencesCallable()
    
    
    public final UnaryCallable<ListQuotaPreferencesRequest,ListQuotaPreferencesResponse> listQuotaPreferencesCallable()

Lists QuotaPreferences in a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       ListQuotaPreferencesRequest request =
           ListQuotaPreferencesRequest.newBuilder()
               .setParent(LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListQuotaPreferencesResponse response =
             cloudQuotasClient.listQuotaPreferencesCallable().call(request);
         for (QuotaPreference element : response.getQuotaPreferencesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListQuotaPreferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.ListQuotaPreferencesRequest),[ListQuotaPreferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.ListQuotaPreferencesResponse)>` |   
  
### listQuotaPreferencesPagedCallable()
    
    
    public final UnaryCallable<ListQuotaPreferencesRequest,CloudQuotasClient.ListQuotaPreferencesPagedResponse> listQuotaPreferencesPagedCallable()

Lists QuotaPreferences in a given project, folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       ListQuotaPreferencesRequest request =
           ListQuotaPreferencesRequest.newBuilder()
               .setParent(LocationName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<QuotaPreference> future =
           cloudQuotasClient.listQuotaPreferencesPagedCallable().futureCall(request);
       // Do something.
       for (QuotaPreference element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListQuotaPreferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.ListQuotaPreferencesRequest),[ListQuotaPreferencesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.CloudQuotasClient.ListQuotaPreferencesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateQuotaPreference(QuotaPreference quotaPreference, FieldMask updateMask)
    
    
    public final QuotaPreference updateQuotaPreference(QuotaPreference quotaPreference, FieldMask updateMask)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       QuotaPreference quotaPreference = QuotaPreference.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       QuotaPreference response =
           cloudQuotasClient.updateQuotaPreference(quotaPreference, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`quotaPreference` | `[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the QuotaPreference resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### updateQuotaPreference(UpdateQuotaPreferenceRequest request)
    
    
    public final QuotaPreference updateQuotaPreference(UpdateQuotaPreferenceRequest request)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       UpdateQuotaPreferenceRequest request =
           UpdateQuotaPreferenceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setQuotaPreference(QuotaPreference.newBuilder().build())
               .setAllowMissing(true)
               .setValidateOnly(true)
               .addAllIgnoreSafetyChecks(new ArrayList<QuotaSafetyCheck>())
               .build();
       QuotaPreference response = cloudQuotasClient.updateQuotaPreference(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.UpdateQuotaPreferenceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)` |   
  
### updateQuotaPreferenceCallable()
    
    
    public final UnaryCallable<UpdateQuotaPreferenceRequest,QuotaPreference> updateQuotaPreferenceCallable()

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudQuotasClient cloudQuotasClient = CloudQuotasClient.create()) {
       UpdateQuotaPreferenceRequest request =
           UpdateQuotaPreferenceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setQuotaPreference(QuotaPreference.newBuilder().build())
               .setAllowMissing(true)
               .setValidateOnly(true)
               .addAllIgnoreSafetyChecks(new ArrayList<QuotaSafetyCheck>())
               .build();
       ApiFuture<QuotaPreference> future =
           cloudQuotasClient.updateQuotaPreferenceCallable().futureCall(request);
       // Do something.
       QuotaPreference response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.UpdateQuotaPreferenceRequest),[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1beta.QuotaPreference)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
