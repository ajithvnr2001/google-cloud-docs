---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesClient
title: Class RegionInstanceTemplatesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:44.035130+00:00
---

# Class RegionInstanceTemplatesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionInstanceTemplatesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionInstanceTemplatesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionInstanceTemplates API.

This client uses RegionInstanceTemplates version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceTemplate = "instanceTemplate1009541167";
       InstanceTemplate response =
           regionInstanceTemplatesClient.get(project, region, instanceTemplate);
     }
     

Note: close() needs to be called on the RegionInstanceTemplatesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionInstanceTemplateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String instanceTemplate) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified instance template. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionInstanceTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String instanceTemplate) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates an instance template in the specified project and region using the global instance template whose URL is included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionInstanceTemplateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, InstanceTemplate instanceTemplateResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of instance templates that are contained within the specified project and region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionInstanceTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionInstanceTemplatesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstanceTemplatesSettings regionInstanceTemplatesSettings =
         RegionInstanceTemplatesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create(regionInstanceTemplatesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstanceTemplatesSettings regionInstanceTemplatesSettings =
         RegionInstanceTemplatesSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create(regionInstanceTemplatesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionInstanceTemplatesClient

## Static Methods 

### create()
    
    
    public static final RegionInstanceTemplatesClient create()

Constructs an instance of RegionInstanceTemplatesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstanceTemplatesSettings settings)
    
    
    public static final RegionInstanceTemplatesClient create(RegionInstanceTemplatesSettings settings)

Constructs an instance of RegionInstanceTemplatesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstanceTemplatesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstanceTemplatesStub stub)
    
    
    public static final RegionInstanceTemplatesClient create(RegionInstanceTemplatesStub stub)

Constructs an instance of RegionInstanceTemplatesClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionInstanceTemplatesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstanceTemplatesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceTemplatesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesClient)` |   
  
## Constructors 

### RegionInstanceTemplatesClient(RegionInstanceTemplatesSettings settings)
    
    
    protected RegionInstanceTemplatesClient(RegionInstanceTemplatesSettings settings)

Constructs an instance of RegionInstanceTemplatesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstanceTemplatesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesSettings)`  
  
  
### RegionInstanceTemplatesClient(RegionInstanceTemplatesStub stub)
    
    
    protected RegionInstanceTemplatesClient(RegionInstanceTemplatesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstanceTemplatesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceTemplatesStub)`  
  
  
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

### deleteAsync(DeleteRegionInstanceTemplateRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionInstanceTemplateRequest request)

Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       DeleteRegionInstanceTemplateRequest request =
           DeleteRegionInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceTemplatesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String instanceTemplate)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String instanceTemplate)

Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceTemplate = "instanceTemplate1009541167";
       Operation response =
           regionInstanceTemplatesClient.deleteAsync(project, region, instanceTemplate).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`instanceTemplate` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance template to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionInstanceTemplateRequest,Operation> deleteCallable()

Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       DeleteRegionInstanceTemplateRequest request =
           DeleteRegionInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceTemplatesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionInstanceTemplateRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       DeleteRegionInstanceTemplateRequest request =
           DeleteRegionInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceTemplatesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionInstanceTemplateRequest request)
    
    
    public final InstanceTemplate get(GetRegionInstanceTemplateRequest request)

Returns the specified instance template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       GetRegionInstanceTemplateRequest request =
           GetRegionInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       InstanceTemplate response = regionInstanceTemplatesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstanceTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate)` |   
  
### get(String project, String region, String instanceTemplate)
    
    
    public final InstanceTemplate get(String project, String region, String instanceTemplate)

Returns the specified instance template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceTemplate = "instanceTemplate1009541167";
       InstanceTemplate response =
           regionInstanceTemplatesClient.get(project, region, instanceTemplate);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`instanceTemplate` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance template.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionInstanceTemplateRequest,InstanceTemplate> getCallable()

Returns the specified instance template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       GetRegionInstanceTemplateRequest request =
           GetRegionInstanceTemplateRequest.newBuilder()
               .setInstanceTemplate("instanceTemplate1009541167")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstanceTemplate> future =
           regionInstanceTemplatesClient.getCallable().futureCall(request);
       // Do something.
       InstanceTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstanceTemplateRequest),[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionInstanceTemplatesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionInstanceTemplatesSettings` |   
  
### getStub()
    
    
    public RegionInstanceTemplatesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceTemplatesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceTemplatesStub)` |   
  
### insertAsync(InsertRegionInstanceTemplateRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionInstanceTemplateRequest request)

Creates an instance template in the specified project and region using the global instance template whose URL is included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       InsertRegionInstanceTemplateRequest request =
           InsertRegionInstanceTemplateRequest.newBuilder()
               .setInstanceTemplateResource(InstanceTemplate.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceTemplatesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, InstanceTemplate instanceTemplateResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, InstanceTemplate instanceTemplateResource)

Creates an instance template in the specified project and region using the global instance template whose URL is included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       InstanceTemplate instanceTemplateResource = InstanceTemplate.newBuilder().build();
       Operation response =
           regionInstanceTemplatesClient
               .insertAsync(project, region, instanceTemplateResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`instanceTemplateResource` | `[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionInstanceTemplateRequest,Operation> insertCallable()

Creates an instance template in the specified project and region using the global instance template whose URL is included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       InsertRegionInstanceTemplateRequest request =
           InsertRegionInstanceTemplateRequest.newBuilder()
               .setInstanceTemplateResource(InstanceTemplate.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceTemplatesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionInstanceTemplateRequest,Operation,Operation> insertOperationCallable()

Creates an instance template in the specified project and region using the global instance template whose URL is included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       InsertRegionInstanceTemplateRequest request =
           InsertRegionInstanceTemplateRequest.newBuilder()
               .setInstanceTemplateResource(InstanceTemplate.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceTemplatesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionInstanceTemplatesRequest request)
    
    
    public final RegionInstanceTemplatesClient.ListPagedResponse list(ListRegionInstanceTemplatesRequest request)

Retrieves a list of instance templates that are contained within the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       ListRegionInstanceTemplatesRequest request =
           ListRegionInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (InstanceTemplate element : regionInstanceTemplatesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceTemplatesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionInstanceTemplatesClient.ListPagedResponse list(String project, String region)

Retrieves a list of instance templates that are contained within the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (InstanceTemplate element :
           regionInstanceTemplatesClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the regions for this request.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceTemplatesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionInstanceTemplatesRequest,InstanceTemplateList> listCallable()

Retrieves a list of instance templates that are contained within the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       ListRegionInstanceTemplatesRequest request =
           ListRegionInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         InstanceTemplateList response = regionInstanceTemplatesClient.listCallable().call(request);
         for (InstanceTemplate element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceTemplatesRequest),[InstanceTemplateList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplateList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionInstanceTemplatesRequest,RegionInstanceTemplatesClient.ListPagedResponse> listPagedCallable()

Retrieves a list of instance templates that are contained within the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceTemplatesClient regionInstanceTemplatesClient =
         RegionInstanceTemplatesClient.create()) {
       ListRegionInstanceTemplatesRequest request =
           ListRegionInstanceTemplatesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstanceTemplate> future =
           regionInstanceTemplatesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstanceTemplate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstanceTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceTemplatesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceTemplatesClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
