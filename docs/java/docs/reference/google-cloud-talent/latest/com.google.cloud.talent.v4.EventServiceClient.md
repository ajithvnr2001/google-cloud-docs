---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EventServiceClient
title: Class EventServiceClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:41:54.778471+00:00
---

# Class EventServiceClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EventServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EventServiceClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.6  2.2.9 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-talent/google-cloud-talent/src/main/java/com/google/cloud/talent/v4/EventServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/talent-solution/)  
---|---  
  
Service Description: A service handles client event report.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EventServiceClient eventServiceClient = EventServiceClient.create()) {
       TenantName parent = TenantName.of("[PROJECT]", "[TENANT]");
       ClientEvent clientEvent = ClientEvent.newBuilder().build();
       ClientEvent response = eventServiceClient.createClientEvent(parent, clientEvent);
     }
     

Note: close() needs to be called on the EventServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateClientEvent |  Report events issued when end user interacts with customer's application that uses Cloud Talent Solution. You may inspect the created events in [self service tools](https://console.cloud.google.com/talent-solution/overview). [Learn more](https://cloud.google.com/talent-solution/docs/management-tools) about self service tools. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createClientEvent(CreateClientEventRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createClientEvent(TenantName parent, ClientEvent clientEvent) 
  * createClientEvent(String parent, ClientEvent clientEvent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createClientEventCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of EventServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EventServiceSettings eventServiceSettings =
         EventServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     EventServiceClient eventServiceClient = EventServiceClient.create(eventServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EventServiceSettings eventServiceSettings =
         EventServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     EventServiceClient eventServiceClient = EventServiceClient.create(eventServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EventServiceSettings eventServiceSettings = EventServiceSettings.newHttpJsonBuilder().build();
     EventServiceClient eventServiceClient = EventServiceClient.create(eventServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EventServiceClient

## Static Methods 

### create()
    
    
    public static final EventServiceClient create()

Constructs an instance of EventServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[EventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EventServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EventServiceSettings settings)
    
    
    public static final EventServiceClient create(EventServiceSettings settings)

Constructs an instance of EventServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EventServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EventServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EventServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EventServiceStub stub)
    
    
    public static final EventServiceClient create(EventServiceStub stub)

Constructs an instance of EventServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(EventServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.EventServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EventServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EventServiceClient)` |   
  
## Constructors 

### EventServiceClient(EventServiceSettings settings)
    
    
    protected EventServiceClient(EventServiceSettings settings)

Constructs an instance of EventServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EventServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.EventServiceSettings)`  
  
  
### EventServiceClient(EventServiceStub stub)
    
    
    protected EventServiceClient(EventServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.EventServiceStub)`  
  
  
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

### createClientEvent(@Nullable TenantName parent, ClientEvent clientEvent)
    
    
    public final ClientEvent createClientEvent(@Nullable TenantName parent, ClientEvent clientEvent)

Report events issued when end user interacts with customer's application that uses Cloud Talent Solution. You may inspect the created events in [self service tools](https://console.cloud.google.com/talent-solution/overview). [Learn more](https://cloud.google.com/talent-solution/docs/management-tools) about self service tools.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EventServiceClient eventServiceClient = EventServiceClient.create()) {
       TenantName parent = TenantName.of("[PROJECT]", "[TENANT]");
       ClientEvent clientEvent = ClientEvent.newBuilder().build();
       ClientEvent response = eventServiceClient.createClientEvent(parent, clientEvent);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.talent.v4.TenantName`  
Required. Resource name of the tenant under which the event is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`clientEvent` | `[ClientEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ClientEvent)`  
Required. Events issued when end user interacts with customer's application that uses Cloud Talent Solution.  
**Returns**  
---  
**Type** | **Description**  
`[ClientEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ClientEvent)` |   
  
### createClientEvent(CreateClientEventRequest request)
    
    
    public final ClientEvent createClientEvent(CreateClientEventRequest request)

Report events issued when end user interacts with customer's application that uses Cloud Talent Solution. You may inspect the created events in [self service tools](https://console.cloud.google.com/talent-solution/overview). [Learn more](https://cloud.google.com/talent-solution/docs/management-tools) about self service tools.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EventServiceClient eventServiceClient = EventServiceClient.create()) {
       CreateClientEventRequest request =
           CreateClientEventRequest.newBuilder()
               .setParent(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setClientEvent(ClientEvent.newBuilder().build())
               .build();
       ClientEvent response = eventServiceClient.createClientEvent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClientEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateClientEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ClientEvent)` |   
  
### createClientEvent(String parent, ClientEvent clientEvent)
    
    
    public final ClientEvent createClientEvent(String parent, ClientEvent clientEvent)

Report events issued when end user interacts with customer's application that uses Cloud Talent Solution. You may inspect the created events in [self service tools](https://console.cloud.google.com/talent-solution/overview). [Learn more](https://cloud.google.com/talent-solution/docs/management-tools) about self service tools.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EventServiceClient eventServiceClient = EventServiceClient.create()) {
       String parent = TenantName.of("[PROJECT]", "[TENANT]").toString();
       ClientEvent clientEvent = ClientEvent.newBuilder().build();
       ClientEvent response = eventServiceClient.createClientEvent(parent, clientEvent);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the tenant under which the event is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`clientEvent` | `[ClientEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ClientEvent)`  
Required. Events issued when end user interacts with customer's application that uses Cloud Talent Solution.  
**Returns**  
---  
**Type** | **Description**  
`[ClientEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ClientEvent)` |   
  
### createClientEventCallable()
    
    
    public final UnaryCallable<CreateClientEventRequest,ClientEvent> createClientEventCallable()

Report events issued when end user interacts with customer's application that uses Cloud Talent Solution. You may inspect the created events in [self service tools](https://console.cloud.google.com/talent-solution/overview). [Learn more](https://cloud.google.com/talent-solution/docs/management-tools) about self service tools.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EventServiceClient eventServiceClient = EventServiceClient.create()) {
       CreateClientEventRequest request =
           CreateClientEventRequest.newBuilder()
               .setParent(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setClientEvent(ClientEvent.newBuilder().build())
               .build();
       ApiFuture<ClientEvent> future =
           eventServiceClient.createClientEventCallable().futureCall(request);
       // Do something.
       ClientEvent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateClientEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateClientEventRequest),[ClientEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ClientEvent)>` |   
  
### getSettings()
    
    
    public final @Nullable EventServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.talent.v4.EventServiceSettings` |   
  
### getStub()
    
    
    public EventServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EventServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.EventServiceStub)` |   
  
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
