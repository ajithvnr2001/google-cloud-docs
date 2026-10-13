---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.QuotaControllerClient
title: Class QuotaControllerClient (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:16.757930+00:00
---

# Class QuotaControllerClient (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.QuotaControllerClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class QuotaControllerClient (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.1.10 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-service-control/google-cloud-service-control/src/main/java/com/google/api/servicecontrol/v1/QuotaControllerClient.java)| [Product Reference](https://cloud.google.com/service-infrastructure/docs/overview/)  
---|---  
  
Service Description: [Google Quota Control API](https://cloud.google.com/service-control/overview)

Allows clients to allocate and release quota against a [managed service](https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService).

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaControllerClient quotaControllerClient = QuotaControllerClient.create()) {
       AllocateQuotaRequest request =
           AllocateQuotaRequest.newBuilder()
               .setServiceName("serviceName-1928572192")
               .setAllocateOperation(QuotaOperation.newBuilder().build())
               .setServiceConfigId("serviceConfigId650537426")
               .build();
       AllocateQuotaResponse response = quotaControllerClient.allocateQuota(request);
     }
     

Note: close() needs to be called on the QuotaControllerClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AllocateQuota |  Attempts to allocate quota for the specified consumer. It should be called before the operation is executed.  This method requires the `servicemanagement.services.quota` permission on the specified service. For more information, see [Cloud IAM](https://cloud.google.com/iam).  **NOTE:** The client **must** fail-open on server errors `INTERNAL`, `UNKNOWN`, `DEADLINE_EXCEEDED`, and `UNAVAILABLE`. To ensure system reliability, the server may inject these errors to prohibit any hard dependency on the quota functionality. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * allocateQuota(AllocateQuotaRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * allocateQuotaCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of QuotaControllerSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     QuotaControllerSettings quotaControllerSettings =
         QuotaControllerSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     QuotaControllerClient quotaControllerClient =
         QuotaControllerClient.create(quotaControllerSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     QuotaControllerSettings quotaControllerSettings =
         QuotaControllerSettings.newBuilder().setEndpoint(myEndpoint).build();
     QuotaControllerClient quotaControllerClient =
         QuotaControllerClient.create(quotaControllerSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     QuotaControllerSettings quotaControllerSettings =
         QuotaControllerSettings.newHttpJsonBuilder().build();
     QuotaControllerClient quotaControllerClient =
         QuotaControllerClient.create(quotaControllerSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > QuotaControllerClient

## Static Methods 

### create()
    
    
    public static final QuotaControllerClient create()

Constructs an instance of QuotaControllerClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[QuotaControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.QuotaControllerClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(QuotaControllerSettings settings)
    
    
    public static final QuotaControllerClient create(QuotaControllerSettings settings)

Constructs an instance of QuotaControllerClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[QuotaControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.QuotaControllerSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.QuotaControllerClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(QuotaControllerStub stub)
    
    
    public static final QuotaControllerClient create(QuotaControllerStub stub)

Constructs an instance of QuotaControllerClient, using the given stub for making calls. This is for advanced usage - prefer using create(QuotaControllerSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[QuotaControllerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.stub.QuotaControllerStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaControllerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.QuotaControllerClient)` |   
  
## Constructors 

### QuotaControllerClient(QuotaControllerSettings settings)
    
    
    protected QuotaControllerClient(QuotaControllerSettings settings)

Constructs an instance of QuotaControllerClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[QuotaControllerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.QuotaControllerSettings)`  
  
  
### QuotaControllerClient(QuotaControllerStub stub)
    
    
    protected QuotaControllerClient(QuotaControllerStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[QuotaControllerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.stub.QuotaControllerStub)`  
  
  
## Methods 

### allocateQuota(AllocateQuotaRequest request)
    
    
    public final AllocateQuotaResponse allocateQuota(AllocateQuotaRequest request)

Attempts to allocate quota for the specified consumer. It should be called before the operation is executed.

This method requires the `servicemanagement.services.quota` permission on the specified service. For more information, see [Cloud IAM](https://cloud.google.com/iam).

**NOTE:** The client **must** fail-open on server errors `INTERNAL`, `UNKNOWN`, `DEADLINE_EXCEEDED`, and `UNAVAILABLE`. To ensure system reliability, the server may inject these errors to prohibit any hard dependency on the quota functionality.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaControllerClient quotaControllerClient = QuotaControllerClient.create()) {
       AllocateQuotaRequest request =
           AllocateQuotaRequest.newBuilder()
               .setServiceName("serviceName-1928572192")
               .setAllocateOperation(QuotaOperation.newBuilder().build())
               .setServiceConfigId("serviceConfigId650537426")
               .build();
       AllocateQuotaResponse response = quotaControllerClient.allocateQuota(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AllocateQuotaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.AllocateQuotaRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AllocateQuotaResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.AllocateQuotaResponse)` |   
  
### allocateQuotaCallable()
    
    
    public final UnaryCallable<AllocateQuotaRequest,AllocateQuotaResponse> allocateQuotaCallable()

Attempts to allocate quota for the specified consumer. It should be called before the operation is executed.

This method requires the `servicemanagement.services.quota` permission on the specified service. For more information, see [Cloud IAM](https://cloud.google.com/iam).

**NOTE:** The client **must** fail-open on server errors `INTERNAL`, `UNKNOWN`, `DEADLINE_EXCEEDED`, and `UNAVAILABLE`. To ensure system reliability, the server may inject these errors to prohibit any hard dependency on the quota functionality.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (QuotaControllerClient quotaControllerClient = QuotaControllerClient.create()) {
       AllocateQuotaRequest request =
           AllocateQuotaRequest.newBuilder()
               .setServiceName("serviceName-1928572192")
               .setAllocateOperation(QuotaOperation.newBuilder().build())
               .setServiceConfigId("serviceConfigId650537426")
               .build();
       ApiFuture<AllocateQuotaResponse> future =
           quotaControllerClient.allocateQuotaCallable().futureCall(request);
       // Do something.
       AllocateQuotaResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AllocateQuotaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.AllocateQuotaRequest),[AllocateQuotaResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.AllocateQuotaResponse)>` |   
  
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
    
    
    public final @Nullable QuotaControllerSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.servicecontrol.v1.QuotaControllerSettings` |   
  
### getStub()
    
    
    public QuotaControllerStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[QuotaControllerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.stub.QuotaControllerStub)` |   
  
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
