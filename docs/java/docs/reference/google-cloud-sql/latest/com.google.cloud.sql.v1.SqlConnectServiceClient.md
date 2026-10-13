---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceClient
title: Class SqlConnectServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:16.706005+00:00
---

# Class SqlConnectServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlConnectServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-sql/google-cloud-sql/src/main/java/com/google/cloud/sql/v1/SqlConnectServiceClient.java)| [Product Reference](https://cloud.google.com/sql/)  
---|---  
  
Service Description: Cloud SQL connect service.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlConnectServiceClient sqlConnectServiceClient = SqlConnectServiceClient.create()) {
       GetConnectSettingsRequest request =
           GetConnectSettingsRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setReadTime(Timestamp.newBuilder().build())
               .build();
       ConnectSettings response = sqlConnectServiceClient.getConnectSettings(request);
     }
     

Note: close() needs to be called on the SqlConnectServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetConnectSettings |  Retrieves connect settings about a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConnectSettings(GetConnectSettingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConnectSettingsCallable() 

  
ResolveConnectSettings |  Retrieves connect settings about a Cloud SQL instance using the instance DNS name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resolveConnectSettings(ResolveConnectSettingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resolveConnectSettingsCallable() 

  
GenerateEphemeralCert |  Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateEphemeralCert(GenerateEphemeralCertRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateEphemeralCertCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SqlConnectServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlConnectServiceSettings sqlConnectServiceSettings =
         SqlConnectServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SqlConnectServiceClient sqlConnectServiceClient =
         SqlConnectServiceClient.create(sqlConnectServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlConnectServiceSettings sqlConnectServiceSettings =
         SqlConnectServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SqlConnectServiceClient sqlConnectServiceClient =
         SqlConnectServiceClient.create(sqlConnectServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlConnectServiceSettings sqlConnectServiceSettings =
         SqlConnectServiceSettings.newHttpJsonBuilder().build();
     SqlConnectServiceClient sqlConnectServiceClient =
         SqlConnectServiceClient.create(sqlConnectServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SqlConnectServiceClient

## Static Methods 

### create()
    
    
    public static final SqlConnectServiceClient create()

Constructs an instance of SqlConnectServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SqlConnectServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlConnectServiceSettings settings)
    
    
    public static final SqlConnectServiceClient create(SqlConnectServiceSettings settings)

Constructs an instance of SqlConnectServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlConnectServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlConnectServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlConnectServiceStub stub)
    
    
    public static final SqlConnectServiceClient create(SqlConnectServiceStub stub)

Constructs an instance of SqlConnectServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SqlConnectServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlConnectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlConnectServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlConnectServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceClient)` |   
  
## Constructors 

### SqlConnectServiceClient(SqlConnectServiceSettings settings)
    
    
    protected SqlConnectServiceClient(SqlConnectServiceSettings settings)

Constructs an instance of SqlConnectServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlConnectServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceSettings)`  
  
  
### SqlConnectServiceClient(SqlConnectServiceStub stub)
    
    
    protected SqlConnectServiceClient(SqlConnectServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlConnectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlConnectServiceStub)`  
  
  
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

### generateEphemeralCert(GenerateEphemeralCertRequest request)
    
    
    public final GenerateEphemeralCertResponse generateEphemeralCert(GenerateEphemeralCertRequest request)

Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlConnectServiceClient sqlConnectServiceClient = SqlConnectServiceClient.create()) {
       GenerateEphemeralCertRequest request =
           GenerateEphemeralCertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setPublicKey("publicKey1446899510")
               .setAccessToken("accessToken-1042689291")
               .setReadTime(Timestamp.newBuilder().build())
               .setValidDuration(Duration.newBuilder().build())
               .build();
       GenerateEphemeralCertResponse response =
           sqlConnectServiceClient.generateEphemeralCert(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateEphemeralCertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GenerateEphemeralCertRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateEphemeralCertResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GenerateEphemeralCertResponse)` |   
  
### generateEphemeralCertCallable()
    
    
    public final UnaryCallable<GenerateEphemeralCertRequest,GenerateEphemeralCertResponse> generateEphemeralCertCallable()

Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlConnectServiceClient sqlConnectServiceClient = SqlConnectServiceClient.create()) {
       GenerateEphemeralCertRequest request =
           GenerateEphemeralCertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setPublicKey("publicKey1446899510")
               .setAccessToken("accessToken-1042689291")
               .setReadTime(Timestamp.newBuilder().build())
               .setValidDuration(Duration.newBuilder().build())
               .build();
       ApiFuture<GenerateEphemeralCertResponse> future =
           sqlConnectServiceClient.generateEphemeralCertCallable().futureCall(request);
       // Do something.
       GenerateEphemeralCertResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateEphemeralCertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GenerateEphemeralCertRequest),[GenerateEphemeralCertResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GenerateEphemeralCertResponse)>` |   
  
### getConnectSettings(GetConnectSettingsRequest request)
    
    
    public final ConnectSettings getConnectSettings(GetConnectSettingsRequest request)

Retrieves connect settings about a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlConnectServiceClient sqlConnectServiceClient = SqlConnectServiceClient.create()) {
       GetConnectSettingsRequest request =
           GetConnectSettingsRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setReadTime(Timestamp.newBuilder().build())
               .build();
       ConnectSettings response = sqlConnectServiceClient.getConnectSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConnectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GetConnectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ConnectSettings)` |   
  
### getConnectSettingsCallable()
    
    
    public final UnaryCallable<GetConnectSettingsRequest,ConnectSettings> getConnectSettingsCallable()

Retrieves connect settings about a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlConnectServiceClient sqlConnectServiceClient = SqlConnectServiceClient.create()) {
       GetConnectSettingsRequest request =
           GetConnectSettingsRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setReadTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<ConnectSettings> future =
           sqlConnectServiceClient.getConnectSettingsCallable().futureCall(request);
       // Do something.
       ConnectSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConnectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GetConnectSettingsRequest),[ConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ConnectSettings)>` |   
  
### getSettings()
    
    
    public final @Nullable SqlConnectServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.SqlConnectServiceSettings` |   
  
### getStub()
    
    
    public SqlConnectServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SqlConnectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlConnectServiceStub)` |   
  
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
  
### resolveConnectSettings(ResolveConnectSettingsRequest request)
    
    
    public final ConnectSettings resolveConnectSettings(ResolveConnectSettingsRequest request)

Retrieves connect settings about a Cloud SQL instance using the instance DNS name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlConnectServiceClient sqlConnectServiceClient = SqlConnectServiceClient.create()) {
       ResolveConnectSettingsRequest request =
           ResolveConnectSettingsRequest.newBuilder()
               .setDnsName("dnsName1813886804")
               .setLocation("location1901043637")
               .build();
       ConnectSettings response = sqlConnectServiceClient.resolveConnectSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResolveConnectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ResolveConnectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ConnectSettings)` |   
  
### resolveConnectSettingsCallable()
    
    
    public final UnaryCallable<ResolveConnectSettingsRequest,ConnectSettings> resolveConnectSettingsCallable()

Retrieves connect settings about a Cloud SQL instance using the instance DNS name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlConnectServiceClient sqlConnectServiceClient = SqlConnectServiceClient.create()) {
       ResolveConnectSettingsRequest request =
           ResolveConnectSettingsRequest.newBuilder()
               .setDnsName("dnsName1813886804")
               .setLocation("location1901043637")
               .build();
       ApiFuture<ConnectSettings> future =
           sqlConnectServiceClient.resolveConnectSettingsCallable().futureCall(request);
       // Do something.
       ConnectSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResolveConnectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ResolveConnectSettingsRequest),[ConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ConnectSettings)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
