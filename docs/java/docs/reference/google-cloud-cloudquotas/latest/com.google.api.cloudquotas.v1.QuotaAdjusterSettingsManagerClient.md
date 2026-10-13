---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsManagerClient
title: Class QuotaAdjusterSettingsManagerClient (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:58.324465+00:00
---

# Class QuotaAdjusterSettingsManagerClient (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsManagerClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class QuotaAdjusterSettingsManagerClient (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudquotas/google-cloud-cloudquotas/src/main/java/com/google/api/cloudquotas/v1/QuotaAdjusterSettingsManagerClient.java)| [Product Reference](https://cloud.google.com/cloudquotas/docs/)  
---|---  
  
Service Description: The Quotas Adjuster Settings API is an infrastructure service for Google Cloud that lets service consumers view and update their quota adjuster settings.

\- Update quota adjuster settings. - Get the name of the configurations.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create()) {
       QuotaAdjusterSettings quotaAdjusterSettings = QuotaAdjusterSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       QuotaAdjusterSettings response =
           quotaAdjusterSettingsManagerClient.updateQuotaAdjusterSettings(
               quotaAdjusterSettings, updateMask);
     }
     

Note: close() needs to be called on the QuotaAdjusterSettingsManagerClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
UpdateQuotaAdjusterSettings |  Updates the QuotaAdjusterSettings for the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateQuotaAdjusterSettings(QuotaAdjusterSettings quotaAdjusterSettings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateQuotaAdjusterSettingsCallable() 

  
GetQuotaAdjusterSettings |  Gets the QuotaAdjusterSettings for the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getQuotaAdjusterSettings(QuotaAdjusterSettingsName name) 
  * getQuotaAdjusterSettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getQuotaAdjusterSettingsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of QuotaAdjusterSettingsManagerSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     QuotaAdjusterSettingsManagerSettings quotaAdjusterSettingsManagerSettings =
         QuotaAdjusterSettingsManagerSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create(quotaAdjusterSettingsManagerSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     QuotaAdjusterSettingsManagerSettings quotaAdjusterSettingsManagerSettings =
         QuotaAdjusterSettingsManagerSettings.newBuilder().setEndpoint(myEndpoint).build();
     QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create(quotaAdjusterSettingsManagerSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     QuotaAdjusterSettingsManagerSettings quotaAdjusterSettingsManagerSettings =
         QuotaAdjusterSettingsManagerSettings.newHttpJsonBuilder().build();
     QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create(quotaAdjusterSettingsManagerSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > QuotaAdjusterSettingsManagerClient

## Static Methods 

### create()
    
    
    public static final QuotaAdjusterSettingsManagerClient create()

Constructs an instance of QuotaAdjusterSettingsManagerClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsManagerClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(QuotaAdjusterSettingsManagerSettings settings)
    
    
    public static final QuotaAdjusterSettingsManagerClient create(QuotaAdjusterSettingsManagerSettings settings)

Constructs an instance of QuotaAdjusterSettingsManagerClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[QuotaAdjusterSettingsManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsManagerSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsManagerClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(QuotaAdjusterSettingsManagerStub stub)
    
    
    public static final QuotaAdjusterSettingsManagerClient create(QuotaAdjusterSettingsManagerStub stub)

Constructs an instance of QuotaAdjusterSettingsManagerClient, using the given stub for making calls. This is for advanced usage - prefer using create(QuotaAdjusterSettingsManagerSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[QuotaAdjusterSettingsManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.stub.QuotaAdjusterSettingsManagerStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsManagerClient)` |   
  
## Constructors 

### QuotaAdjusterSettingsManagerClient(QuotaAdjusterSettingsManagerSettings settings)
    
    
    protected QuotaAdjusterSettingsManagerClient(QuotaAdjusterSettingsManagerSettings settings)

Constructs an instance of QuotaAdjusterSettingsManagerClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[QuotaAdjusterSettingsManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsManagerSettings)`  
  
  
### QuotaAdjusterSettingsManagerClient(QuotaAdjusterSettingsManagerStub stub)
    
    
    protected QuotaAdjusterSettingsManagerClient(QuotaAdjusterSettingsManagerStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[QuotaAdjusterSettingsManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.stub.QuotaAdjusterSettingsManagerStub)`  
  
  
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

### getQuotaAdjusterSettings(@Nullable QuotaAdjusterSettingsName name)
    
    
    public final QuotaAdjusterSettings getQuotaAdjusterSettings(@Nullable QuotaAdjusterSettingsName name)

Gets the QuotaAdjusterSettings for the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create()) {
       QuotaAdjusterSettingsName name =
           QuotaAdjusterSettingsName.ofProjectLocationName("[PROJECT]", "[LOCATION]");
       QuotaAdjusterSettings response =
           quotaAdjusterSettingsManagerClient.getQuotaAdjusterSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1.QuotaAdjusterSettingsName`  
Required. Identifier. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings)` |   
  
### getQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest request)
    
    
    public final QuotaAdjusterSettings getQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest request)

Gets the QuotaAdjusterSettings for the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create()) {
       GetQuotaAdjusterSettingsRequest request =
           GetQuotaAdjusterSettingsRequest.newBuilder()
               .setName(
                   QuotaAdjusterSettingsName.ofProjectLocationName("[PROJECT]", "[LOCATION]")
                       .toString())
               .build();
       QuotaAdjusterSettings response =
           quotaAdjusterSettingsManagerClient.getQuotaAdjusterSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaAdjusterSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings)` |   
  
### getQuotaAdjusterSettings(String name)
    
    
    public final QuotaAdjusterSettings getQuotaAdjusterSettings(String name)

Gets the QuotaAdjusterSettings for the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create()) {
       String name =
           QuotaAdjusterSettingsName.ofProjectLocationName("[PROJECT]", "[LOCATION]").toString();
       QuotaAdjusterSettings response =
           quotaAdjusterSettingsManagerClient.getQuotaAdjusterSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Identifier. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings)` |   
  
### getQuotaAdjusterSettingsCallable()
    
    
    public final UnaryCallable<GetQuotaAdjusterSettingsRequest,QuotaAdjusterSettings> getQuotaAdjusterSettingsCallable()

Gets the QuotaAdjusterSettings for the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create()) {
       GetQuotaAdjusterSettingsRequest request =
           GetQuotaAdjusterSettingsRequest.newBuilder()
               .setName(
                   QuotaAdjusterSettingsName.ofProjectLocationName("[PROJECT]", "[LOCATION]")
                       .toString())
               .build();
       ApiFuture<QuotaAdjusterSettings> future =
           quotaAdjusterSettingsManagerClient.getQuotaAdjusterSettingsCallable().futureCall(request);
       // Do something.
       QuotaAdjusterSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaAdjusterSettingsRequest),[QuotaAdjusterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings)>` |   
  
### getSettings()
    
    
    public final @Nullable QuotaAdjusterSettingsManagerSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.cloudquotas.v1.QuotaAdjusterSettingsManagerSettings` |   
  
### getStub()
    
    
    public QuotaAdjusterSettingsManagerStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.stub.QuotaAdjusterSettingsManagerStub)` |   
  
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

### updateQuotaAdjusterSettings(QuotaAdjusterSettings quotaAdjusterSettings, FieldMask updateMask)
    
    
    public final QuotaAdjusterSettings updateQuotaAdjusterSettings(QuotaAdjusterSettings quotaAdjusterSettings, FieldMask updateMask)

Updates the QuotaAdjusterSettings for the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create()) {
       QuotaAdjusterSettings quotaAdjusterSettings = QuotaAdjusterSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       QuotaAdjusterSettings response =
           quotaAdjusterSettingsManagerClient.updateQuotaAdjusterSettings(
               quotaAdjusterSettings, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`quotaAdjusterSettings` | `[QuotaAdjusterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings)`  
Required. The QuotaAdjusterSettings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings)` |   
  
### updateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest request)
    
    
    public final QuotaAdjusterSettings updateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest request)

Updates the QuotaAdjusterSettings for the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create()) {
       UpdateQuotaAdjusterSettingsRequest request =
           UpdateQuotaAdjusterSettingsRequest.newBuilder()
               .setQuotaAdjusterSettings(QuotaAdjusterSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       QuotaAdjusterSettings response =
           quotaAdjusterSettingsManagerClient.updateQuotaAdjusterSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.UpdateQuotaAdjusterSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings)` |   
  
### updateQuotaAdjusterSettingsCallable()
    
    
    public final UnaryCallable<UpdateQuotaAdjusterSettingsRequest,QuotaAdjusterSettings> updateQuotaAdjusterSettingsCallable()

Updates the QuotaAdjusterSettings for the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient =
         QuotaAdjusterSettingsManagerClient.create()) {
       UpdateQuotaAdjusterSettingsRequest request =
           UpdateQuotaAdjusterSettingsRequest.newBuilder()
               .setQuotaAdjusterSettings(QuotaAdjusterSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<QuotaAdjusterSettings> future =
           quotaAdjusterSettingsManagerClient
               .updateQuotaAdjusterSettingsCallable()
               .futureCall(request);
       // Do something.
       QuotaAdjusterSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.UpdateQuotaAdjusterSettingsRequest),[QuotaAdjusterSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
