---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient
title: Class RuleExecutionErrorServiceClient (0.37.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:49.755477+00:00
---

# Class RuleExecutionErrorServiceClient (0.37.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RuleExecutionErrorServiceClient (0.37.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.0 (latest)  0.33.0  0.32.0  0.31.0  0.29.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-chronicle/google-cloud-chronicle/src/main/java/com/google/cloud/chronicle/v1/RuleExecutionErrorServiceClient.java)| [Product Reference](https://cloud.google.com/chronicle/docs/secops/secops-overview)  
---|---  
  
Service Description: RuleExecutionErrorService contains endpoints related to rule execution errors.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       for (RuleExecutionError element :
           ruleExecutionErrorServiceClient.listRuleExecutionErrors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

Note: close() needs to be called on the RuleExecutionErrorServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListRuleExecutionErrors |  Lists rule execution errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRuleExecutionErrors(ListRuleExecutionErrorsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRuleExecutionErrors(InstanceName parent) 
  * listRuleExecutionErrors(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRuleExecutionErrorsPagedCallable() 
  * listRuleExecutionErrorsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RuleExecutionErrorServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleExecutionErrorServiceSettings ruleExecutionErrorServiceSettings =
         RuleExecutionErrorServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create(ruleExecutionErrorServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleExecutionErrorServiceSettings ruleExecutionErrorServiceSettings =
         RuleExecutionErrorServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create(ruleExecutionErrorServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleExecutionErrorServiceSettings ruleExecutionErrorServiceSettings =
         RuleExecutionErrorServiceSettings.newHttpJsonBuilder().build();
     RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create(ruleExecutionErrorServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RuleExecutionErrorServiceClient

## Static Methods 

### create()
    
    
    public static final RuleExecutionErrorServiceClient create()

Constructs an instance of RuleExecutionErrorServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RuleExecutionErrorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RuleExecutionErrorServiceSettings settings)
    
    
    public static final RuleExecutionErrorServiceClient create(RuleExecutionErrorServiceSettings settings)

Constructs an instance of RuleExecutionErrorServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RuleExecutionErrorServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuleExecutionErrorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RuleExecutionErrorServiceStub stub)
    
    
    public static final RuleExecutionErrorServiceClient create(RuleExecutionErrorServiceStub stub)

Constructs an instance of RuleExecutionErrorServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(RuleExecutionErrorServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RuleExecutionErrorServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.stub.RuleExecutionErrorServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuleExecutionErrorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient)` |   
  
## Constructors 

### RuleExecutionErrorServiceClient(RuleExecutionErrorServiceSettings settings)
    
    
    protected RuleExecutionErrorServiceClient(RuleExecutionErrorServiceSettings settings)

Constructs an instance of RuleExecutionErrorServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RuleExecutionErrorServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceSettings)`  
  
  
### RuleExecutionErrorServiceClient(RuleExecutionErrorServiceStub stub)
    
    
    protected RuleExecutionErrorServiceClient(RuleExecutionErrorServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RuleExecutionErrorServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.stub.RuleExecutionErrorServiceStub)`  
  
  
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
    
    
    public final @Nullable RuleExecutionErrorServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleExecutionErrorServiceSettings` |   
  
### getStub()
    
    
    public RuleExecutionErrorServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RuleExecutionErrorServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.stub.RuleExecutionErrorServiceStub)` |   
  
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
  
### listRuleExecutionErrors(@Nullable InstanceName parent)
    
    
    public final RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse listRuleExecutionErrors(@Nullable InstanceName parent)

Lists rule execution errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       for (RuleExecutionError element :
           ruleExecutionErrorServiceClient.listRuleExecutionErrors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.InstanceName`  
Required. The instance to list rule execution errors from. Format: projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse)` |   
  
### listRuleExecutionErrors(ListRuleExecutionErrorsRequest request)
    
    
    public final RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse listRuleExecutionErrors(ListRuleExecutionErrorsRequest request)

Lists rule execution errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create()) {
       ListRuleExecutionErrorsRequest request =
           ListRuleExecutionErrorsRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (RuleExecutionError element :
           ruleExecutionErrorServiceClient.listRuleExecutionErrors(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRuleExecutionErrorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleExecutionErrorsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse)` |   
  
### listRuleExecutionErrors(String parent)
    
    
    public final RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse listRuleExecutionErrors(String parent)

Lists rule execution errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create()) {
       String parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       for (RuleExecutionError element :
           ruleExecutionErrorServiceClient.listRuleExecutionErrors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The instance to list rule execution errors from. Format: projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse)` |   
  
### listRuleExecutionErrorsCallable()
    
    
    public final UnaryCallable<ListRuleExecutionErrorsRequest,ListRuleExecutionErrorsResponse> listRuleExecutionErrorsCallable()

Lists rule execution errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create()) {
       ListRuleExecutionErrorsRequest request =
           ListRuleExecutionErrorsRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListRuleExecutionErrorsResponse response =
             ruleExecutionErrorServiceClient.listRuleExecutionErrorsCallable().call(request);
         for (RuleExecutionError element : response.getRuleExecutionErrorsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRuleExecutionErrorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleExecutionErrorsRequest),[ListRuleExecutionErrorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleExecutionErrorsResponse)>` |   
  
### listRuleExecutionErrorsPagedCallable()
    
    
    public final UnaryCallable<ListRuleExecutionErrorsRequest,RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse> listRuleExecutionErrorsPagedCallable()

Lists rule execution errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleExecutionErrorServiceClient ruleExecutionErrorServiceClient =
         RuleExecutionErrorServiceClient.create()) {
       ListRuleExecutionErrorsRequest request =
           ListRuleExecutionErrorsRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<RuleExecutionError> future =
           ruleExecutionErrorServiceClient
               .listRuleExecutionErrorsPagedCallable()
               .futureCall(request);
       // Do something.
       for (RuleExecutionError element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRuleExecutionErrorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleExecutionErrorsRequest),[ListRuleExecutionErrorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorServiceClient.ListRuleExecutionErrorsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
