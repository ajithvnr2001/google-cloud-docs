---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionClient
title: Class CompletionClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:41:54.601559+00:00
---

# Class CompletionClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CompletionClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.6  2.2.9 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-talent/google-cloud-talent/src/main/java/com/google/cloud/talent/v4/CompletionClient.java)| [Product Reference](https://cloud.google.com/solutions/talent-solution/)  
---|---  
  
Service Description: A service handles auto completion.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionClient completionClient = CompletionClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setTenant(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setQuery("query107944136")
               .addAllLanguageCodes(new ArrayList<String>())
               .setPageSize(883849137)
               .setCompany(CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString())
               .build();
       CompleteQueryResponse response = completionClient.completeQuery(request);
     }
     

Note: close() needs to be called on the CompletionClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CompleteQuery |  Completes the specified prefix with keyword suggestions. Intended for use by a job search auto-complete search box. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeQuery(CompleteQueryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeQueryCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CompletionSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompletionSettings completionSettings =
         CompletionSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CompletionClient completionClient = CompletionClient.create(completionSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompletionSettings completionSettings =
         CompletionSettings.newBuilder().setEndpoint(myEndpoint).build();
     CompletionClient completionClient = CompletionClient.create(completionSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompletionSettings completionSettings = CompletionSettings.newHttpJsonBuilder().build();
     CompletionClient completionClient = CompletionClient.create(completionSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CompletionClient

## Static Methods 

### create()
    
    
    public static final CompletionClient create()

Constructs an instance of CompletionClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CompletionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CompletionSettings settings)
    
    
    public static final CompletionClient create(CompletionSettings settings)

Constructs an instance of CompletionClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompletionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompletionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CompletionStub stub)
    
    
    public static final CompletionClient create(CompletionStub stub)

Constructs an instance of CompletionClient, using the given stub for making calls. This is for advanced usage - prefer using create(CompletionSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompletionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.CompletionStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompletionClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionClient)` |   
  
## Constructors 

### CompletionClient(CompletionSettings settings)
    
    
    protected CompletionClient(CompletionSettings settings)

Constructs an instance of CompletionClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompletionSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompletionSettings)`  
  
  
### CompletionClient(CompletionStub stub)
    
    
    protected CompletionClient(CompletionStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompletionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.CompletionStub)`  
  
  
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

### completeQuery(CompleteQueryRequest request)
    
    
    public final CompleteQueryResponse completeQuery(CompleteQueryRequest request)

Completes the specified prefix with keyword suggestions. Intended for use by a job search auto-complete search box.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionClient completionClient = CompletionClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setTenant(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setQuery("query107944136")
               .addAllLanguageCodes(new ArrayList<String>())
               .setPageSize(883849137)
               .setCompany(CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString())
               .build();
       CompleteQueryResponse response = completionClient.completeQuery(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryResponse)` |   
  
### completeQueryCallable()
    
    
    public final UnaryCallable<CompleteQueryRequest,CompleteQueryResponse> completeQueryCallable()

Completes the specified prefix with keyword suggestions. Intended for use by a job search auto-complete search box.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompletionClient completionClient = CompletionClient.create()) {
       CompleteQueryRequest request =
           CompleteQueryRequest.newBuilder()
               .setTenant(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setQuery("query107944136")
               .addAllLanguageCodes(new ArrayList<String>())
               .setPageSize(883849137)
               .setCompany(CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString())
               .build();
       ApiFuture<CompleteQueryResponse> future =
           completionClient.completeQueryCallable().futureCall(request);
       // Do something.
       CompleteQueryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryRequest),[CompleteQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompleteQueryResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable CompletionSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.talent.v4.CompletionSettings` |   
  
### getStub()
    
    
    public CompletionStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CompletionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.CompletionStub)` |   
  
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
