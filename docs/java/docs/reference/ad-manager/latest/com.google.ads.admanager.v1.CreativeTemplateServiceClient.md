---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient
title: Class CreativeTemplateServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:36.924662+00:00
---

# Class CreativeTemplateServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CreativeTemplateServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CreativeTemplateServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CreativeTemplate` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       CreativeTemplateName name = CreativeTemplateName.of("[NETWORK_CODE]", "[CREATIVE_TEMPLATE]");
       CreativeTemplate response = creativeTemplateServiceClient.getCreativeTemplate(name);
     }
     

Note: close() needs to be called on the CreativeTemplateServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCreativeTemplate |  Retrieves a `CreativeTemplate` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCreativeTemplate(GetCreativeTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCreativeTemplate(CreativeTemplateName name) 
  * getCreativeTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCreativeTemplateCallable() 

  
ListCreativeTemplates |  Lists `CreativeTemplate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCreativeTemplates(ListCreativeTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCreativeTemplates(NetworkName parent) 
  * listCreativeTemplates(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCreativeTemplatesPagedCallable() 
  * listCreativeTemplatesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CreativeTemplateServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CreativeTemplateServiceSettings creativeTemplateServiceSettings =
         CreativeTemplateServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create(creativeTemplateServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CreativeTemplateServiceSettings creativeTemplateServiceSettings =
         CreativeTemplateServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create(creativeTemplateServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CreativeTemplateServiceClient

## Static Methods 

### create()
    
    
    public static final CreativeTemplateServiceClient create()

Constructs an instance of CreativeTemplateServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CreativeTemplateServiceSettings settings)
    
    
    public static final CreativeTemplateServiceClient create(CreativeTemplateServiceSettings settings)

Constructs an instance of CreativeTemplateServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CreativeTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CreativeTemplateServiceStub stub)
    
    
    public static final CreativeTemplateServiceClient create(CreativeTemplateServiceStub stub)

Constructs an instance of CreativeTemplateServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CreativeTemplateServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CreativeTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeTemplateServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient)` |   
  
## Constructors 

### CreativeTemplateServiceClient(CreativeTemplateServiceSettings settings)
    
    
    protected CreativeTemplateServiceClient(CreativeTemplateServiceSettings settings)

Constructs an instance of CreativeTemplateServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CreativeTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceSettings)`  
  
  
### CreativeTemplateServiceClient(CreativeTemplateServiceStub stub)
    
    
    protected CreativeTemplateServiceClient(CreativeTemplateServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CreativeTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeTemplateServiceStub)`  
  
  
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

### getCreativeTemplate(@Nullable CreativeTemplateName name)
    
    
    public final CreativeTemplate getCreativeTemplate(@Nullable CreativeTemplateName name)

Retrieves a `CreativeTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       CreativeTemplateName name = CreativeTemplateName.of("[NETWORK_CODE]", "[CREATIVE_TEMPLATE]");
       CreativeTemplate response = creativeTemplateServiceClient.getCreativeTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CreativeTemplateName`  
Required. The resource name of the CreativeTemplate. Format: `networks/{network_code}/creativeTemplates/{creative_template_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplate)` |   
  
### getCreativeTemplate(GetCreativeTemplateRequest request)
    
    
    public final CreativeTemplate getCreativeTemplate(GetCreativeTemplateRequest request)

Retrieves a `CreativeTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       GetCreativeTemplateRequest request =
           GetCreativeTemplateRequest.newBuilder()
               .setName(CreativeTemplateName.of("[NETWORK_CODE]", "[CREATIVE_TEMPLATE]").toString())
               .build();
       CreativeTemplate response = creativeTemplateServiceClient.getCreativeTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCreativeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCreativeTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplate)` |   
  
### getCreativeTemplate(String name)
    
    
    public final CreativeTemplate getCreativeTemplate(String name)

Retrieves a `CreativeTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       String name = CreativeTemplateName.of("[NETWORK_CODE]", "[CREATIVE_TEMPLATE]").toString();
       CreativeTemplate response = creativeTemplateServiceClient.getCreativeTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CreativeTemplate. Format: `networks/{network_code}/creativeTemplates/{creative_template_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplate)` |   
  
### getCreativeTemplateCallable()
    
    
    public final UnaryCallable<GetCreativeTemplateRequest,CreativeTemplate> getCreativeTemplateCallable()

Retrieves a `CreativeTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       GetCreativeTemplateRequest request =
           GetCreativeTemplateRequest.newBuilder()
               .setName(CreativeTemplateName.of("[NETWORK_CODE]", "[CREATIVE_TEMPLATE]").toString())
               .build();
       ApiFuture<CreativeTemplate> future =
           creativeTemplateServiceClient.getCreativeTemplateCallable().futureCall(request);
       // Do something.
       CreativeTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCreativeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCreativeTemplateRequest),[CreativeTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplate)>` |   
  
### getSettings()
    
    
    public final @Nullable CreativeTemplateServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CreativeTemplateServiceSettings` |   
  
### getStub()
    
    
    public CreativeTemplateServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CreativeTemplateServiceStub)` |   
  
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
  
### listCreativeTemplates(@Nullable NetworkName parent)
    
    
    public final CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse listCreativeTemplates(@Nullable NetworkName parent)

Lists `CreativeTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CreativeTemplate element :
           creativeTemplateServiceClient.listCreativeTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CreativeTemplates. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse)` |   
  
### listCreativeTemplates(ListCreativeTemplatesRequest request)
    
    
    public final CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse listCreativeTemplates(ListCreativeTemplatesRequest request)

Lists `CreativeTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       ListCreativeTemplatesRequest request =
           ListCreativeTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CreativeTemplate element :
           creativeTemplateServiceClient.listCreativeTemplates(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCreativeTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse)` |   
  
### listCreativeTemplates(String parent)
    
    
    public final CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse listCreativeTemplates(String parent)

Lists `CreativeTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CreativeTemplate element :
           creativeTemplateServiceClient.listCreativeTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CreativeTemplates. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse)` |   
  
### listCreativeTemplatesCallable()
    
    
    public final UnaryCallable<ListCreativeTemplatesRequest,ListCreativeTemplatesResponse> listCreativeTemplatesCallable()

Lists `CreativeTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       ListCreativeTemplatesRequest request =
           ListCreativeTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCreativeTemplatesResponse response =
             creativeTemplateServiceClient.listCreativeTemplatesCallable().call(request);
         for (CreativeTemplate element : response.getCreativeTemplatesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCreativeTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeTemplatesRequest),[ListCreativeTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeTemplatesResponse)>` |   
  
### listCreativeTemplatesPagedCallable()
    
    
    public final UnaryCallable<ListCreativeTemplatesRequest,CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse> listCreativeTemplatesPagedCallable()

Lists `CreativeTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CreativeTemplateServiceClient creativeTemplateServiceClient =
         CreativeTemplateServiceClient.create()) {
       ListCreativeTemplatesRequest request =
           ListCreativeTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CreativeTemplate> future =
           creativeTemplateServiceClient.listCreativeTemplatesPagedCallable().futureCall(request);
       // Do something.
       for (CreativeTemplate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCreativeTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCreativeTemplatesRequest),[ListCreativeTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreativeTemplateServiceClient.ListCreativeTemplatesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
