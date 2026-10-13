---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestionServiceClient
title: Class IngestionServiceClient (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:48.821500+00:00
---

# Class IngestionServiceClient (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class IngestionServiceClient (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-datamanager/data-manager/src/main/java/com/google/ads/datamanager/v1/IngestionServiceClient.java)| [Product Reference](https://developers.google.com/data-manager)| [RPC Documentation](https://developers.google.com/data-manager/api/reference/rpc)  
---|---|---  
  
Service Description: Service for sending audience data to supported destinations.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestAudienceMembersRequest request =
           IngestAudienceMembersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllAudienceMembers(new ArrayList<AudienceMember>())
               .setConsent(Consent.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setTermsOfService(TermsOfService.newBuilder().build())
               .build();
       IngestAudienceMembersResponse response =
           ingestionServiceClient.ingestAudienceMembers(request);
     }
     

Note: close() needs to be called on the IngestionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
IngestAudienceMembers |  Uploads a list of AudienceMember resources to the provided Destination. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * ingestAudienceMembers(IngestAudienceMembersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * ingestAudienceMembersCallable() 

  
RemoveAudienceMembers |  Removes a list of AudienceMember resources from the provided Destination. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeAudienceMembers(RemoveAudienceMembersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeAudienceMembersCallable() 

  
RemoveAllAudienceMembers |  Removes all audience members from the provided destinations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeAllAudienceMembers(RemoveAllAudienceMembersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeAllAudienceMembersCallable() 

  
IngestEvents |  Uploads a list of Event resources from the provided Destination. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * ingestEvents(IngestEventsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * ingestEventsCallable() 

  
IngestUsers |  Uploads a list of users to the provided destinations. Unlike IngestAudienceMembers (which adds users to specific advertiser audience lists for targeting), `IngestUsers` ingests account level identity linkage data (for example, user identifiers linked to mobile IDs) independent of specific audience segments.  This feature is only available to accounts on an allowlist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * ingestUsers(IngestUsersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * ingestUsersCallable() 

  
RemoveUsers |  Removes a list of users from the provided destinations.  This feature is only available to accounts on an allowlist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeUsers(RemoveUsersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeUsersCallable() 

  
IngestAdEvents |  Uploads a list of AdEvent resources to Google Analytics.  This feature is only available to accounts on an allowlist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * ingestAdEvents(IngestAdEventsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * ingestAdEventsCallable() 

  
RetrieveRequestStatus |  Gets the status of a request given request id. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * retrieveRequestStatus(RetrieveRequestStatusRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * retrieveRequestStatusCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of IngestionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IngestionServiceSettings ingestionServiceSettings =
         IngestionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     IngestionServiceClient ingestionServiceClient =
         IngestionServiceClient.create(ingestionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IngestionServiceSettings ingestionServiceSettings =
         IngestionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     IngestionServiceClient ingestionServiceClient =
         IngestionServiceClient.create(ingestionServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IngestionServiceSettings ingestionServiceSettings =
         IngestionServiceSettings.newHttpJsonBuilder().build();
     IngestionServiceClient ingestionServiceClient =
         IngestionServiceClient.create(ingestionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > IngestionServiceClient

## Static Methods 

### create()
    
    
    public static final IngestionServiceClient create()

Constructs an instance of IngestionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[IngestionServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IngestionServiceSettings settings)
    
    
    public static final IngestionServiceClient create(IngestionServiceSettings settings)

Constructs an instance of IngestionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IngestionServiceSettings](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IngestionServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IngestionServiceStub stub)
    
    
    public static final IngestionServiceClient create(IngestionServiceStub stub)

Constructs an instance of IngestionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(IngestionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IngestionServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.IngestionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IngestionServiceClient](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestionServiceClient)` |   
  
## Constructors 

### IngestionServiceClient(IngestionServiceSettings settings)
    
    
    protected IngestionServiceClient(IngestionServiceSettings settings)

Constructs an instance of IngestionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IngestionServiceSettings](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestionServiceSettings)`  
  
  
### IngestionServiceClient(IngestionServiceStub stub)
    
    
    protected IngestionServiceClient(IngestionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IngestionServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.IngestionServiceStub)`  
  
  
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

### getSettings()
    
    
    public final @Nullable IngestionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.datamanager.v1.IngestionServiceSettings` |   
  
### getStub()
    
    
    public IngestionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[IngestionServiceStub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.stub.IngestionServiceStub)` |   
  
### ingestAdEvents(IngestAdEventsRequest request)
    
    
    public final IngestAdEventsResponse ingestAdEvents(IngestAdEventsRequest request)

Uploads a list of AdEvent resources to Google Analytics.

This feature is only available to accounts on an allowlist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestAdEventsRequest request =
           IngestAdEventsRequest.newBuilder()
               .addAllAdEvents(new ArrayList<AdEvent>())
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setValidateOnly(true)
               .build();
       IngestAdEventsResponse response = ingestionServiceClient.ingestAdEvents(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[IngestAdEventsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestAdEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IngestAdEventsResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestAdEventsResponse)` |   
  
### ingestAdEventsCallable()
    
    
    public final UnaryCallable<IngestAdEventsRequest,IngestAdEventsResponse> ingestAdEventsCallable()

Uploads a list of AdEvent resources to Google Analytics.

This feature is only available to accounts on an allowlist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestAdEventsRequest request =
           IngestAdEventsRequest.newBuilder()
               .addAllAdEvents(new ArrayList<AdEvent>())
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<IngestAdEventsResponse> future =
           ingestionServiceClient.ingestAdEventsCallable().futureCall(request);
       // Do something.
       IngestAdEventsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[IngestAdEventsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestAdEventsRequest),[IngestAdEventsResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestAdEventsResponse)>` |   
  
### ingestAudienceMembers(IngestAudienceMembersRequest request)
    
    
    public final IngestAudienceMembersResponse ingestAudienceMembers(IngestAudienceMembersRequest request)

Uploads a list of AudienceMember resources to the provided Destination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestAudienceMembersRequest request =
           IngestAudienceMembersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllAudienceMembers(new ArrayList<AudienceMember>())
               .setConsent(Consent.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setTermsOfService(TermsOfService.newBuilder().build())
               .build();
       IngestAudienceMembersResponse response =
           ingestionServiceClient.ingestAudienceMembers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[IngestAudienceMembersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestAudienceMembersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IngestAudienceMembersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestAudienceMembersResponse)` |   
  
### ingestAudienceMembersCallable()
    
    
    public final UnaryCallable<IngestAudienceMembersRequest,IngestAudienceMembersResponse> ingestAudienceMembersCallable()

Uploads a list of AudienceMember resources to the provided Destination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestAudienceMembersRequest request =
           IngestAudienceMembersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllAudienceMembers(new ArrayList<AudienceMember>())
               .setConsent(Consent.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setTermsOfService(TermsOfService.newBuilder().build())
               .build();
       ApiFuture<IngestAudienceMembersResponse> future =
           ingestionServiceClient.ingestAudienceMembersCallable().futureCall(request);
       // Do something.
       IngestAudienceMembersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[IngestAudienceMembersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestAudienceMembersRequest),[IngestAudienceMembersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestAudienceMembersResponse)>` |   
  
### ingestEvents(IngestEventsRequest request)
    
    
    public final IngestEventsResponse ingestEvents(IngestEventsRequest request)

Uploads a list of Event resources from the provided Destination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestEventsRequest request =
           IngestEventsRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllEvents(new ArrayList<Event>())
               .setConsent(Consent.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .build();
       IngestEventsResponse response = ingestionServiceClient.ingestEvents(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[IngestEventsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IngestEventsResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestEventsResponse)` |   
  
### ingestEventsCallable()
    
    
    public final UnaryCallable<IngestEventsRequest,IngestEventsResponse> ingestEventsCallable()

Uploads a list of Event resources from the provided Destination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestEventsRequest request =
           IngestEventsRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllEvents(new ArrayList<Event>())
               .setConsent(Consent.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .build();
       ApiFuture<IngestEventsResponse> future =
           ingestionServiceClient.ingestEventsCallable().futureCall(request);
       // Do something.
       IngestEventsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[IngestEventsRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestEventsRequest),[IngestEventsResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestEventsResponse)>` |   
  
### ingestUsers(IngestUsersRequest request)
    
    
    public final IngestUsersResponse ingestUsers(IngestUsersRequest request)

Uploads a list of users to the provided destinations. Unlike IngestAudienceMembers (which adds users to specific advertiser audience lists for targeting), `IngestUsers` ingests account level identity linkage data (for example, user identifiers linked to mobile IDs) independent of specific audience segments.

This feature is only available to accounts on an allowlist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestUsersRequest request =
           IngestUsersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllUsers(new ArrayList<User>())
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .build();
       IngestUsersResponse response = ingestionServiceClient.ingestUsers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[IngestUsersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestUsersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IngestUsersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestUsersResponse)` |   
  
### ingestUsersCallable()
    
    
    public final UnaryCallable<IngestUsersRequest,IngestUsersResponse> ingestUsersCallable()

Uploads a list of users to the provided destinations. Unlike IngestAudienceMembers (which adds users to specific advertiser audience lists for targeting), `IngestUsers` ingests account level identity linkage data (for example, user identifiers linked to mobile IDs) independent of specific audience segments.

This feature is only available to accounts on an allowlist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       IngestUsersRequest request =
           IngestUsersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllUsers(new ArrayList<User>())
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .build();
       ApiFuture<IngestUsersResponse> future =
           ingestionServiceClient.ingestUsersCallable().futureCall(request);
       // Do something.
       IngestUsersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[IngestUsersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestUsersRequest),[IngestUsersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.IngestUsersResponse)>` |   
  
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
  
### removeAllAudienceMembers(RemoveAllAudienceMembersRequest request)
    
    
    public final RemoveAllAudienceMembersResponse removeAllAudienceMembers(RemoveAllAudienceMembersRequest request)

Removes all audience members from the provided destinations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       RemoveAllAudienceMembersRequest request =
           RemoveAllAudienceMembersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .setRemoveAsOfTime(Timestamp.newBuilder().build())
               .setValidateOnly(true)
               .build();
       RemoveAllAudienceMembersResponse response =
           ingestionServiceClient.removeAllAudienceMembers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveAllAudienceMembersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveAllAudienceMembersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveAllAudienceMembersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveAllAudienceMembersResponse)` |   
  
### removeAllAudienceMembersCallable()
    
    
    public final UnaryCallable<RemoveAllAudienceMembersRequest,RemoveAllAudienceMembersResponse> removeAllAudienceMembersCallable()

Removes all audience members from the provided destinations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       RemoveAllAudienceMembersRequest request =
           RemoveAllAudienceMembersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .setRemoveAsOfTime(Timestamp.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<RemoveAllAudienceMembersResponse> future =
           ingestionServiceClient.removeAllAudienceMembersCallable().futureCall(request);
       // Do something.
       RemoveAllAudienceMembersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveAllAudienceMembersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveAllAudienceMembersRequest),[RemoveAllAudienceMembersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveAllAudienceMembersResponse)>` |   
  
### removeAudienceMembers(RemoveAudienceMembersRequest request)
    
    
    public final RemoveAudienceMembersResponse removeAudienceMembers(RemoveAudienceMembersRequest request)

Removes a list of AudienceMember resources from the provided Destination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       RemoveAudienceMembersRequest request =
           RemoveAudienceMembersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllAudienceMembers(new ArrayList<AudienceMember>())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .build();
       RemoveAudienceMembersResponse response =
           ingestionServiceClient.removeAudienceMembers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveAudienceMembersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveAudienceMembersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveAudienceMembersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveAudienceMembersResponse)` |   
  
### removeAudienceMembersCallable()
    
    
    public final UnaryCallable<RemoveAudienceMembersRequest,RemoveAudienceMembersResponse> removeAudienceMembersCallable()

Removes a list of AudienceMember resources from the provided Destination.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       RemoveAudienceMembersRequest request =
           RemoveAudienceMembersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllAudienceMembers(new ArrayList<AudienceMember>())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .build();
       ApiFuture<RemoveAudienceMembersResponse> future =
           ingestionServiceClient.removeAudienceMembersCallable().futureCall(request);
       // Do something.
       RemoveAudienceMembersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveAudienceMembersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveAudienceMembersRequest),[RemoveAudienceMembersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveAudienceMembersResponse)>` |   
  
### removeUsers(RemoveUsersRequest request)
    
    
    public final RemoveUsersResponse removeUsers(RemoveUsersRequest request)

Removes a list of users from the provided destinations.

This feature is only available to accounts on an allowlist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       RemoveUsersRequest request =
           RemoveUsersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllUserData(new ArrayList<UserData>())
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .build();
       RemoveUsersResponse response = ingestionServiceClient.removeUsers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveUsersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveUsersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveUsersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveUsersResponse)` |   
  
### removeUsersCallable()
    
    
    public final UnaryCallable<RemoveUsersRequest,RemoveUsersResponse> removeUsersCallable()

Removes a list of users from the provided destinations.

This feature is only available to accounts on an allowlist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       RemoveUsersRequest request =
           RemoveUsersRequest.newBuilder()
               .addAllDestinations(new ArrayList<Destination>())
               .addAllUserData(new ArrayList<UserData>())
               .setEncryptionInfo(EncryptionInfo.newBuilder().build())
               .setValidateOnly(true)
               .setEncoding(Encoding.forNumber(0))
               .build();
       ApiFuture<RemoveUsersResponse> future =
           ingestionServiceClient.removeUsersCallable().futureCall(request);
       // Do something.
       RemoveUsersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveUsersRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveUsersRequest),[RemoveUsersResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RemoveUsersResponse)>` |   
  
### retrieveRequestStatus(RetrieveRequestStatusRequest request)
    
    
    public final RetrieveRequestStatusResponse retrieveRequestStatus(RetrieveRequestStatusRequest request)

Gets the status of a request given request id.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       RetrieveRequestStatusRequest request =
           RetrieveRequestStatusRequest.newBuilder().setRequestId("requestId693933066").build();
       RetrieveRequestStatusResponse response =
           ingestionServiceClient.retrieveRequestStatus(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveRequestStatusRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RetrieveRequestStatusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RetrieveRequestStatusResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RetrieveRequestStatusResponse)` |   
  
### retrieveRequestStatusCallable()
    
    
    public final UnaryCallable<RetrieveRequestStatusRequest,RetrieveRequestStatusResponse> retrieveRequestStatusCallable()

Gets the status of a request given request id.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IngestionServiceClient ingestionServiceClient = IngestionServiceClient.create()) {
       RetrieveRequestStatusRequest request =
           RetrieveRequestStatusRequest.newBuilder().setRequestId("requestId693933066").build();
       ApiFuture<RetrieveRequestStatusResponse> future =
           ingestionServiceClient.retrieveRequestStatusCallable().futureCall(request);
       // Do something.
       RetrieveRequestStatusResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RetrieveRequestStatusRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RetrieveRequestStatusRequest),[RetrieveRequestStatusResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.RetrieveRequestStatusResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
