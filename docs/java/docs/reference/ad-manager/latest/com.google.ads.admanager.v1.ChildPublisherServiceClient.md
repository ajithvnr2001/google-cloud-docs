---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient
title: Class ChildPublisherServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:31.926091+00:00
---

# Class ChildPublisherServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ChildPublisherServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ChildPublisherServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling ChildPublisher objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       ChildPublisherName name = ChildPublisherName.of("[NETWORK_CODE]", "[CHILD_PUBLISHER]");
       ChildPublisher response = childPublisherServiceClient.getChildPublisher(name);
     }
     

Note: close() needs to be called on the ChildPublisherServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetChildPublisher |  Retrieves a ChildPublisher object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getChildPublisher(GetChildPublisherRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getChildPublisher(ChildPublisherName name) 
  * getChildPublisher(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getChildPublisherCallable() 

  
ListChildPublishers |  Lists ChildPublisher objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listChildPublishers(ListChildPublishersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listChildPublishers(NetworkName parent) 
  * listChildPublishers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listChildPublishersPagedCallable() 
  * listChildPublishersCallable() 

  
CreateChildPublisher |  Creates a ChildPublisher object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createChildPublisher(CreateChildPublisherRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createChildPublisher(NetworkName parent, ChildPublisher childPublisher) 
  * createChildPublisher(String parent, ChildPublisher childPublisher) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createChildPublisherCallable() 

  
BatchCreateChildPublishers |  Creates ChildPublisher objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateChildPublishers(NetworkName parent, List<CreateChildPublisherRequest> requests) 
  * batchCreateChildPublishers(String parent, List<CreateChildPublisherRequest> requests) 
  * batchCreateChildPublishers(BatchCreateChildPublishersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateChildPublishersCallable() 

  
UpdateChildPublisher |  Updates a ChildPublisher object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateChildPublisher(UpdateChildPublisherRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateChildPublisher(ChildPublisher childPublisher, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateChildPublisherCallable() 

  
BatchUpdateChildPublishers |  Batch updates ChildPublisher objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateChildPublishers(NetworkName parent, List<UpdateChildPublisherRequest> requests) 
  * batchUpdateChildPublishers(String parent, List<UpdateChildPublisherRequest> requests) 
  * batchUpdateChildPublishers(BatchUpdateChildPublishersRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateChildPublishersCallable() 

  
BatchResendChildPublisherInvitationEmails |  Batch resends invitation emails to ChildPublishers.  Only expired and pending ChildPublishers can be sent invitation emails. Rejected, withdrawn, and accepted ChildPublishers will be ignored. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchResendChildPublisherInvitationEmails(BatchResendChildPublisherInvitationEmailsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchResendChildPublisherInvitationEmails(NetworkName parent, List<String> names) 
  * batchResendChildPublisherInvitationEmails(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchResendChildPublisherInvitationEmailsCallable() 

  
BatchRenegotiateChildPublisherAgreements |  Batch renegotiates ChildPublisher agreements (i.e., invite with updated terms).  Only the agreements of rejected or withdrawn ChildPublishers can be renegotiated. Expired, pending, and accepted ChildPublishers will be ignored. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRenegotiateChildPublisherAgreements(NetworkName parent, List<RenegotiateChildPublisherAgreementRequest> requests) 
  * batchRenegotiateChildPublisherAgreements(String parent, List<RenegotiateChildPublisherAgreementRequest> requests) 
  * batchRenegotiateChildPublisherAgreements(BatchRenegotiateChildPublisherAgreementsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRenegotiateChildPublisherAgreementsCallable() 

  
BatchRejectChildPublishers |  Batch rejects ChildPublishers.  Only pending or active ChildPublishers can be rejected. Expired, rejected, and withdrawn ChildPublishers will be ignored.  This method is only intended to be called in response to a child user rejecting an invitation and exists to support the rejection of ChildPublishers that are not yet associated with an Ad Manager network.  To sever the relationship from the parent publisher's side, use [BatchWithdrawChildPublisher][]. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRejectChildPublishers(BatchRejectChildPublishersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchRejectChildPublishers(NetworkName parent, List<String> names) 
  * batchRejectChildPublishers(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRejectChildPublishersCallable() 

  
BatchWithdrawChildPublishers |  Batch withdraws ChildPublishers.  Only expired, pending, and accepted ChildPublishers can be withdrawn. Rejected or withdrawn ChildPublishers will be ignored. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchWithdrawChildPublishers(BatchWithdrawChildPublishersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchWithdrawChildPublishers(NetworkName parent, List<String> names) 
  * batchWithdrawChildPublishers(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchWithdrawChildPublishersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ChildPublisherServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ChildPublisherServiceSettings childPublisherServiceSettings =
         ChildPublisherServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create(childPublisherServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ChildPublisherServiceSettings childPublisherServiceSettings =
         ChildPublisherServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create(childPublisherServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ChildPublisherServiceClient

## Static Methods 

### create()
    
    
    public static final ChildPublisherServiceClient create()

Constructs an instance of ChildPublisherServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ChildPublisherServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ChildPublisherServiceSettings settings)
    
    
    public static final ChildPublisherServiceClient create(ChildPublisherServiceSettings settings)

Constructs an instance of ChildPublisherServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ChildPublisherServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisherServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ChildPublisherServiceStub stub)
    
    
    public static final ChildPublisherServiceClient create(ChildPublisherServiceStub stub)

Constructs an instance of ChildPublisherServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ChildPublisherServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ChildPublisherServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ChildPublisherServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisherServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient)` |   
  
## Constructors 

### ChildPublisherServiceClient(ChildPublisherServiceSettings settings)
    
    
    protected ChildPublisherServiceClient(ChildPublisherServiceSettings settings)

Constructs an instance of ChildPublisherServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ChildPublisherServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceSettings)`  
  
  
### ChildPublisherServiceClient(ChildPublisherServiceStub stub)
    
    
    protected ChildPublisherServiceClient(ChildPublisherServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ChildPublisherServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ChildPublisherServiceStub)`  
  
  
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
  
### batchCreateChildPublishers(@Nullable NetworkName parent, List<CreateChildPublisherRequest> requests)
    
    
    public final BatchCreateChildPublishersResponse batchCreateChildPublishers(@Nullable NetworkName parent, List<CreateChildPublisherRequest> requests)

Creates ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateChildPublisherRequest> requests = new ArrayList<>();
       BatchCreateChildPublishersResponse response =
           childPublisherServiceClient.batchCreateChildPublishers(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where ChildPublishers will be created. Format: `networks/{network_code}` The parent field in the CreateChildPublisherRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateChildPublisherRequest)>`  
Required. The ChildPublisher objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateChildPublishersResponse)` |   
  
### batchCreateChildPublishers(BatchCreateChildPublishersRequest request)
    
    
    public final BatchCreateChildPublishersResponse batchCreateChildPublishers(BatchCreateChildPublishersRequest request)

Creates ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchCreateChildPublishersRequest request =
           BatchCreateChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateChildPublisherRequest>())
               .build();
       BatchCreateChildPublishersResponse response =
           childPublisherServiceClient.batchCreateChildPublishers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateChildPublishersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateChildPublishersResponse)` |   
  
### batchCreateChildPublishers(String parent, List<CreateChildPublisherRequest> requests)
    
    
    public final BatchCreateChildPublishersResponse batchCreateChildPublishers(String parent, List<CreateChildPublisherRequest> requests)

Creates ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateChildPublisherRequest> requests = new ArrayList<>();
       BatchCreateChildPublishersResponse response =
           childPublisherServiceClient.batchCreateChildPublishers(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where ChildPublishers will be created. Format: `networks/{network_code}` The parent field in the CreateChildPublisherRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateChildPublisherRequest)>`  
Required. The ChildPublisher objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateChildPublishersResponse)` |   
  
### batchCreateChildPublishersCallable()
    
    
    public final UnaryCallable<BatchCreateChildPublishersRequest,BatchCreateChildPublishersResponse> batchCreateChildPublishersCallable()

Creates ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchCreateChildPublishersRequest request =
           BatchCreateChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateChildPublisherRequest>())
               .build();
       ApiFuture<BatchCreateChildPublishersResponse> future =
           childPublisherServiceClient.batchCreateChildPublishersCallable().futureCall(request);
       // Do something.
       BatchCreateChildPublishersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateChildPublishersRequest),[BatchCreateChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateChildPublishersResponse)>` |   
  
### batchRejectChildPublishers(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchRejectChildPublishersResponse batchRejectChildPublishers(@Nullable NetworkName parent, List<String> names)

Batch rejects ChildPublishers.

Only pending or active ChildPublishers can be rejected. Expired, rejected, and withdrawn ChildPublishers will be ignored.

This method is only intended to be called in response to a child user rejecting an invitation and exists to support the rejection of ChildPublishers that are not yet associated with an Ad Manager network.

To sever the relationship from the parent publisher's side, use [BatchWithdrawChildPublisher][].

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchRejectChildPublishersResponse response =
           childPublisherServiceClient.batchRejectChildPublishers(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names of the ChildPublishers to reject. Format: `networks/{network_code}/childPublisher/{child_publisher_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRejectChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectChildPublishersResponse)` |   
  
### batchRejectChildPublishers(BatchRejectChildPublishersRequest request)
    
    
    public final BatchRejectChildPublishersResponse batchRejectChildPublishers(BatchRejectChildPublishersRequest request)

Batch rejects ChildPublishers.

Only pending or active ChildPublishers can be rejected. Expired, rejected, and withdrawn ChildPublishers will be ignored.

This method is only intended to be called in response to a child user rejecting an invitation and exists to support the rejection of ChildPublishers that are not yet associated with an Ad Manager network.

To sever the relationship from the parent publisher's side, use [BatchWithdrawChildPublisher][].

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchRejectChildPublishersRequest request =
           BatchRejectChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchRejectChildPublishersResponse response =
           childPublisherServiceClient.batchRejectChildPublishers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRejectChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectChildPublishersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRejectChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectChildPublishersResponse)` |   
  
### batchRejectChildPublishers(String parent, List<String> names)
    
    
    public final BatchRejectChildPublishersResponse batchRejectChildPublishers(String parent, List<String> names)

Batch rejects ChildPublishers.

Only pending or active ChildPublishers can be rejected. Expired, rejected, and withdrawn ChildPublishers will be ignored.

This method is only intended to be called in response to a child user rejecting an invitation and exists to support the rejection of ChildPublishers that are not yet associated with an Ad Manager network.

To sever the relationship from the parent publisher's side, use [BatchWithdrawChildPublisher][].

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchRejectChildPublishersResponse response =
           childPublisherServiceClient.batchRejectChildPublishers(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names of the ChildPublishers to reject. Format: `networks/{network_code}/childPublisher/{child_publisher_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRejectChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectChildPublishersResponse)` |   
  
### batchRejectChildPublishersCallable()
    
    
    public final UnaryCallable<BatchRejectChildPublishersRequest,BatchRejectChildPublishersResponse> batchRejectChildPublishersCallable()

Batch rejects ChildPublishers.

Only pending or active ChildPublishers can be rejected. Expired, rejected, and withdrawn ChildPublishers will be ignored.

This method is only intended to be called in response to a child user rejecting an invitation and exists to support the rejection of ChildPublishers that are not yet associated with an Ad Manager network.

To sever the relationship from the parent publisher's side, use [BatchWithdrawChildPublisher][].

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchRejectChildPublishersRequest request =
           BatchRejectChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchRejectChildPublishersResponse> future =
           childPublisherServiceClient.batchRejectChildPublishersCallable().futureCall(request);
       // Do something.
       BatchRejectChildPublishersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRejectChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectChildPublishersRequest),[BatchRejectChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRejectChildPublishersResponse)>` |   
  
### batchRenegotiateChildPublisherAgreements(@Nullable NetworkName parent, List<RenegotiateChildPublisherAgreementRequest> requests)
    
    
    public final BatchRenegotiateChildPublisherAgreementsResponse batchRenegotiateChildPublisherAgreements(@Nullable NetworkName parent, List<RenegotiateChildPublisherAgreementRequest> requests)

Batch renegotiates ChildPublisher agreements (i.e., invite with updated terms).

Only the agreements of rejected or withdrawn ChildPublishers can be renegotiated. Expired, pending, and accepted ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<RenegotiateChildPublisherAgreementRequest> requests = new ArrayList<>();
       BatchRenegotiateChildPublisherAgreementsResponse response =
           childPublisherServiceClient.batchRenegotiateChildPublisherAgreements(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RenegotiateChildPublisherAgreementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RenegotiateChildPublisherAgreementRequest)>`  
Required. The requests to renegotiate ChildPublisher agreements.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRenegotiateChildPublisherAgreementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRenegotiateChildPublisherAgreementsResponse)` |   
  
### batchRenegotiateChildPublisherAgreements(BatchRenegotiateChildPublisherAgreementsRequest request)
    
    
    public final BatchRenegotiateChildPublisherAgreementsResponse batchRenegotiateChildPublisherAgreements(BatchRenegotiateChildPublisherAgreementsRequest request)

Batch renegotiates ChildPublisher agreements (i.e., invite with updated terms).

Only the agreements of rejected or withdrawn ChildPublishers can be renegotiated. Expired, pending, and accepted ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchRenegotiateChildPublisherAgreementsRequest request =
           BatchRenegotiateChildPublisherAgreementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<RenegotiateChildPublisherAgreementRequest>())
               .build();
       BatchRenegotiateChildPublisherAgreementsResponse response =
           childPublisherServiceClient.batchRenegotiateChildPublisherAgreements(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRenegotiateChildPublisherAgreementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRenegotiateChildPublisherAgreementsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRenegotiateChildPublisherAgreementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRenegotiateChildPublisherAgreementsResponse)` |   
  
### batchRenegotiateChildPublisherAgreements(String parent, List<RenegotiateChildPublisherAgreementRequest> requests)
    
    
    public final BatchRenegotiateChildPublisherAgreementsResponse batchRenegotiateChildPublisherAgreements(String parent, List<RenegotiateChildPublisherAgreementRequest> requests)

Batch renegotiates ChildPublisher agreements (i.e., invite with updated terms).

Only the agreements of rejected or withdrawn ChildPublishers can be renegotiated. Expired, pending, and accepted ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<RenegotiateChildPublisherAgreementRequest> requests = new ArrayList<>();
       BatchRenegotiateChildPublisherAgreementsResponse response =
           childPublisherServiceClient.batchRenegotiateChildPublisherAgreements(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RenegotiateChildPublisherAgreementRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RenegotiateChildPublisherAgreementRequest)>`  
Required. The requests to renegotiate ChildPublisher agreements.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRenegotiateChildPublisherAgreementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRenegotiateChildPublisherAgreementsResponse)` |   
  
### batchRenegotiateChildPublisherAgreementsCallable()
    
    
    public final UnaryCallable<BatchRenegotiateChildPublisherAgreementsRequest,BatchRenegotiateChildPublisherAgreementsResponse> batchRenegotiateChildPublisherAgreementsCallable()

Batch renegotiates ChildPublisher agreements (i.e., invite with updated terms).

Only the agreements of rejected or withdrawn ChildPublishers can be renegotiated. Expired, pending, and accepted ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchRenegotiateChildPublisherAgreementsRequest request =
           BatchRenegotiateChildPublisherAgreementsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<RenegotiateChildPublisherAgreementRequest>())
               .build();
       ApiFuture<BatchRenegotiateChildPublisherAgreementsResponse> future =
           childPublisherServiceClient
               .batchRenegotiateChildPublisherAgreementsCallable()
               .futureCall(request);
       // Do something.
       BatchRenegotiateChildPublisherAgreementsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRenegotiateChildPublisherAgreementsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRenegotiateChildPublisherAgreementsRequest),[BatchRenegotiateChildPublisherAgreementsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRenegotiateChildPublisherAgreementsResponse)>` |   
  
### batchResendChildPublisherInvitationEmails(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchResendChildPublisherInvitationEmailsResponse batchResendChildPublisherInvitationEmails(@Nullable NetworkName parent, List<String> names)

Batch resends invitation emails to ChildPublishers.

Only expired and pending ChildPublishers can be sent invitation emails. Rejected, withdrawn, and accepted ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchResendChildPublisherInvitationEmailsResponse response =
           childPublisherServiceClient.batchResendChildPublisherInvitationEmails(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names of the ChildPublishers that should be resent invitation emails. Format: `networks/{network_code}/childPublisher/{child_publisher_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchResendChildPublisherInvitationEmailsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResendChildPublisherInvitationEmailsResponse)` |   
  
### batchResendChildPublisherInvitationEmails(BatchResendChildPublisherInvitationEmailsRequest request)
    
    
    public final BatchResendChildPublisherInvitationEmailsResponse batchResendChildPublisherInvitationEmails(BatchResendChildPublisherInvitationEmailsRequest request)

Batch resends invitation emails to ChildPublishers.

Only expired and pending ChildPublishers can be sent invitation emails. Rejected, withdrawn, and accepted ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchResendChildPublisherInvitationEmailsRequest request =
           BatchResendChildPublisherInvitationEmailsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchResendChildPublisherInvitationEmailsResponse response =
           childPublisherServiceClient.batchResendChildPublisherInvitationEmails(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchResendChildPublisherInvitationEmailsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResendChildPublisherInvitationEmailsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchResendChildPublisherInvitationEmailsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResendChildPublisherInvitationEmailsResponse)` |   
  
### batchResendChildPublisherInvitationEmails(String parent, List<String> names)
    
    
    public final BatchResendChildPublisherInvitationEmailsResponse batchResendChildPublisherInvitationEmails(String parent, List<String> names)

Batch resends invitation emails to ChildPublishers.

Only expired and pending ChildPublishers can be sent invitation emails. Rejected, withdrawn, and accepted ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchResendChildPublisherInvitationEmailsResponse response =
           childPublisherServiceClient.batchResendChildPublisherInvitationEmails(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names of the ChildPublishers that should be resent invitation emails. Format: `networks/{network_code}/childPublisher/{child_publisher_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchResendChildPublisherInvitationEmailsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResendChildPublisherInvitationEmailsResponse)` |   
  
### batchResendChildPublisherInvitationEmailsCallable()
    
    
    public final UnaryCallable<BatchResendChildPublisherInvitationEmailsRequest,BatchResendChildPublisherInvitationEmailsResponse> batchResendChildPublisherInvitationEmailsCallable()

Batch resends invitation emails to ChildPublishers.

Only expired and pending ChildPublishers can be sent invitation emails. Rejected, withdrawn, and accepted ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchResendChildPublisherInvitationEmailsRequest request =
           BatchResendChildPublisherInvitationEmailsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchResendChildPublisherInvitationEmailsResponse> future =
           childPublisherServiceClient
               .batchResendChildPublisherInvitationEmailsCallable()
               .futureCall(request);
       // Do something.
       BatchResendChildPublisherInvitationEmailsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchResendChildPublisherInvitationEmailsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResendChildPublisherInvitationEmailsRequest),[BatchResendChildPublisherInvitationEmailsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchResendChildPublisherInvitationEmailsResponse)>` |   
  
### batchUpdateChildPublishers(@Nullable NetworkName parent, List<UpdateChildPublisherRequest> requests)
    
    
    public final BatchUpdateChildPublishersResponse batchUpdateChildPublishers(@Nullable NetworkName parent, List<UpdateChildPublisherRequest> requests)

Batch updates ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateChildPublisherRequest> requests = new ArrayList<>();
       BatchUpdateChildPublishersResponse response =
           childPublisherServiceClient.batchUpdateChildPublishers(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where ChildPublishers will be updated. Format: `networks/{network_code}` The parent field in the UpdateChildPublisherRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateChildPublisherRequest)>`  
Required. The ChildPublisher objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateChildPublishersResponse)` |   
  
### batchUpdateChildPublishers(BatchUpdateChildPublishersRequest request)
    
    
    public final BatchUpdateChildPublishersResponse batchUpdateChildPublishers(BatchUpdateChildPublishersRequest request)

Batch updates ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchUpdateChildPublishersRequest request =
           BatchUpdateChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateChildPublisherRequest>())
               .build();
       BatchUpdateChildPublishersResponse response =
           childPublisherServiceClient.batchUpdateChildPublishers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateChildPublishersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateChildPublishersResponse)` |   
  
### batchUpdateChildPublishers(String parent, List<UpdateChildPublisherRequest> requests)
    
    
    public final BatchUpdateChildPublishersResponse batchUpdateChildPublishers(String parent, List<UpdateChildPublisherRequest> requests)

Batch updates ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateChildPublisherRequest> requests = new ArrayList<>();
       BatchUpdateChildPublishersResponse response =
           childPublisherServiceClient.batchUpdateChildPublishers(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where ChildPublishers will be updated. Format: `networks/{network_code}` The parent field in the UpdateChildPublisherRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateChildPublisherRequest)>`  
Required. The ChildPublisher objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateChildPublishersResponse)` |   
  
### batchUpdateChildPublishersCallable()
    
    
    public final UnaryCallable<BatchUpdateChildPublishersRequest,BatchUpdateChildPublishersResponse> batchUpdateChildPublishersCallable()

Batch updates ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchUpdateChildPublishersRequest request =
           BatchUpdateChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateChildPublisherRequest>())
               .build();
       ApiFuture<BatchUpdateChildPublishersResponse> future =
           childPublisherServiceClient.batchUpdateChildPublishersCallable().futureCall(request);
       // Do something.
       BatchUpdateChildPublishersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateChildPublishersRequest),[BatchUpdateChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateChildPublishersResponse)>` |   
  
### batchWithdrawChildPublishers(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchWithdrawChildPublishersResponse batchWithdrawChildPublishers(@Nullable NetworkName parent, List<String> names)

Batch withdraws ChildPublishers.

Only expired, pending, and accepted ChildPublishers can be withdrawn. Rejected or withdrawn ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchWithdrawChildPublishersResponse response =
           childPublisherServiceClient.batchWithdrawChildPublishers(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names of the ChildPublishers to withdraw. Format: `networks/{network_code}/childPublisher/{child_publisher_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchWithdrawChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchWithdrawChildPublishersResponse)` |   
  
### batchWithdrawChildPublishers(BatchWithdrawChildPublishersRequest request)
    
    
    public final BatchWithdrawChildPublishersResponse batchWithdrawChildPublishers(BatchWithdrawChildPublishersRequest request)

Batch withdraws ChildPublishers.

Only expired, pending, and accepted ChildPublishers can be withdrawn. Rejected or withdrawn ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchWithdrawChildPublishersRequest request =
           BatchWithdrawChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchWithdrawChildPublishersResponse response =
           childPublisherServiceClient.batchWithdrawChildPublishers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchWithdrawChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchWithdrawChildPublishersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchWithdrawChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchWithdrawChildPublishersResponse)` |   
  
### batchWithdrawChildPublishers(String parent, List<String> names)
    
    
    public final BatchWithdrawChildPublishersResponse batchWithdrawChildPublishers(String parent, List<String> names)

Batch withdraws ChildPublishers.

Only expired, pending, and accepted ChildPublishers can be withdrawn. Rejected or withdrawn ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchWithdrawChildPublishersResponse response =
           childPublisherServiceClient.batchWithdrawChildPublishers(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names of the ChildPublishers to withdraw. Format: `networks/{network_code}/childPublisher/{child_publisher_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchWithdrawChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchWithdrawChildPublishersResponse)` |   
  
### batchWithdrawChildPublishersCallable()
    
    
    public final UnaryCallable<BatchWithdrawChildPublishersRequest,BatchWithdrawChildPublishersResponse> batchWithdrawChildPublishersCallable()

Batch withdraws ChildPublishers.

Only expired, pending, and accepted ChildPublishers can be withdrawn. Rejected or withdrawn ChildPublishers will be ignored.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       BatchWithdrawChildPublishersRequest request =
           BatchWithdrawChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchWithdrawChildPublishersResponse> future =
           childPublisherServiceClient.batchWithdrawChildPublishersCallable().futureCall(request);
       // Do something.
       BatchWithdrawChildPublishersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchWithdrawChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchWithdrawChildPublishersRequest),[BatchWithdrawChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchWithdrawChildPublishersResponse)>` |   
  
### close()
    
    
    public final void close()

### createChildPublisher(@Nullable NetworkName parent, ChildPublisher childPublisher)
    
    
    public final ChildPublisher createChildPublisher(@Nullable NetworkName parent, ChildPublisher childPublisher)

Creates a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       ChildPublisher childPublisher = ChildPublisher.newBuilder().build();
       ChildPublisher response =
           childPublisherServiceClient.createChildPublisher(parent, childPublisher);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this ChildPublisher will be created. Format: `networks/{network_code}`  
`childPublisher` | `[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)`  
Required. The ChildPublisher to create.  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)` |   
  
### createChildPublisher(CreateChildPublisherRequest request)
    
    
    public final ChildPublisher createChildPublisher(CreateChildPublisherRequest request)

Creates a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       CreateChildPublisherRequest request =
           CreateChildPublisherRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setChildPublisher(ChildPublisher.newBuilder().build())
               .build();
       ChildPublisher response = childPublisherServiceClient.createChildPublisher(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateChildPublisherRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)` |   
  
### createChildPublisher(String parent, ChildPublisher childPublisher)
    
    
    public final ChildPublisher createChildPublisher(String parent, ChildPublisher childPublisher)

Creates a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       ChildPublisher childPublisher = ChildPublisher.newBuilder().build();
       ChildPublisher response =
           childPublisherServiceClient.createChildPublisher(parent, childPublisher);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this ChildPublisher will be created. Format: `networks/{network_code}`  
`childPublisher` | `[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)`  
Required. The ChildPublisher to create.  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)` |   
  
### createChildPublisherCallable()
    
    
    public final UnaryCallable<CreateChildPublisherRequest,ChildPublisher> createChildPublisherCallable()

Creates a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       CreateChildPublisherRequest request =
           CreateChildPublisherRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setChildPublisher(ChildPublisher.newBuilder().build())
               .build();
       ApiFuture<ChildPublisher> future =
           childPublisherServiceClient.createChildPublisherCallable().futureCall(request);
       // Do something.
       ChildPublisher response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateChildPublisherRequest),[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)>` |   
  
### getChildPublisher(@Nullable ChildPublisherName name)
    
    
    public final ChildPublisher getChildPublisher(@Nullable ChildPublisherName name)

Retrieves a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       ChildPublisherName name = ChildPublisherName.of("[NETWORK_CODE]", "[CHILD_PUBLISHER]");
       ChildPublisher response = childPublisherServiceClient.getChildPublisher(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ChildPublisherName`  
Required. The resource name of the ChildPublisher. Format: `networks/{network_code}/childPublishers/{child_publisher_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)` |   
  
### getChildPublisher(GetChildPublisherRequest request)
    
    
    public final ChildPublisher getChildPublisher(GetChildPublisherRequest request)

Retrieves a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       GetChildPublisherRequest request =
           GetChildPublisherRequest.newBuilder()
               .setName(ChildPublisherName.of("[NETWORK_CODE]", "[CHILD_PUBLISHER]").toString())
               .build();
       ChildPublisher response = childPublisherServiceClient.getChildPublisher(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetChildPublisherRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)` |   
  
### getChildPublisher(String name)
    
    
    public final ChildPublisher getChildPublisher(String name)

Retrieves a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String name = ChildPublisherName.of("[NETWORK_CODE]", "[CHILD_PUBLISHER]").toString();
       ChildPublisher response = childPublisherServiceClient.getChildPublisher(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ChildPublisher. Format: `networks/{network_code}/childPublishers/{child_publisher_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)` |   
  
### getChildPublisherCallable()
    
    
    public final UnaryCallable<GetChildPublisherRequest,ChildPublisher> getChildPublisherCallable()

Retrieves a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       GetChildPublisherRequest request =
           GetChildPublisherRequest.newBuilder()
               .setName(ChildPublisherName.of("[NETWORK_CODE]", "[CHILD_PUBLISHER]").toString())
               .build();
       ApiFuture<ChildPublisher> future =
           childPublisherServiceClient.getChildPublisherCallable().futureCall(request);
       // Do something.
       ChildPublisher response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetChildPublisherRequest),[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)>` |   
  
### getSettings()
    
    
    public final @Nullable ChildPublisherServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ChildPublisherServiceSettings` |   
  
### getStub()
    
    
    public ChildPublisherServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ChildPublisherServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ChildPublisherServiceStub)` |   
  
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
  
### listChildPublishers(@Nullable NetworkName parent)
    
    
    public final ChildPublisherServiceClient.ListChildPublishersPagedResponse listChildPublishers(@Nullable NetworkName parent)

Lists ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (ChildPublisher element :
           childPublisherServiceClient.listChildPublishers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of ChildPublishers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisherServiceClient.ListChildPublishersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient.ListChildPublishersPagedResponse)` |   
  
### listChildPublishers(ListChildPublishersRequest request)
    
    
    public final ChildPublisherServiceClient.ListChildPublishersPagedResponse listChildPublishers(ListChildPublishersRequest request)

Lists ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       ListChildPublishersRequest request =
           ListChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (ChildPublisher element :
           childPublisherServiceClient.listChildPublishers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListChildPublishersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisherServiceClient.ListChildPublishersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient.ListChildPublishersPagedResponse)` |   
  
### listChildPublishers(String parent)
    
    
    public final ChildPublisherServiceClient.ListChildPublishersPagedResponse listChildPublishers(String parent)

Lists ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (ChildPublisher element :
           childPublisherServiceClient.listChildPublishers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of ChildPublishers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisherServiceClient.ListChildPublishersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient.ListChildPublishersPagedResponse)` |   
  
### listChildPublishersCallable()
    
    
    public final UnaryCallable<ListChildPublishersRequest,ListChildPublishersResponse> listChildPublishersCallable()

Lists ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       ListChildPublishersRequest request =
           ListChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListChildPublishersResponse response =
             childPublisherServiceClient.listChildPublishersCallable().call(request);
         for (ChildPublisher element : response.getChildPublishersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListChildPublishersRequest),[ListChildPublishersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListChildPublishersResponse)>` |   
  
### listChildPublishersPagedCallable()
    
    
    public final UnaryCallable<ListChildPublishersRequest,ChildPublisherServiceClient.ListChildPublishersPagedResponse> listChildPublishersPagedCallable()

Lists ChildPublisher objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       ListChildPublishersRequest request =
           ListChildPublishersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<ChildPublisher> future =
           childPublisherServiceClient.listChildPublishersPagedCallable().futureCall(request);
       // Do something.
       for (ChildPublisher element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListChildPublishersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListChildPublishersRequest),[ListChildPublishersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisherServiceClient.ListChildPublishersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateChildPublisher(ChildPublisher childPublisher, FieldMask updateMask)
    
    
    public final ChildPublisher updateChildPublisher(ChildPublisher childPublisher, FieldMask updateMask)

Updates a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       ChildPublisher childPublisher = ChildPublisher.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ChildPublisher response =
           childPublisherServiceClient.updateChildPublisher(childPublisher, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`childPublisher` | `[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)`  
Required. The ChildPublisher to update. The ChildPublisher's `name` is used to identify the ChildPublisher to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)` |   
  
### updateChildPublisher(UpdateChildPublisherRequest request)
    
    
    public final ChildPublisher updateChildPublisher(UpdateChildPublisherRequest request)

Updates a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       UpdateChildPublisherRequest request =
           UpdateChildPublisherRequest.newBuilder()
               .setChildPublisher(ChildPublisher.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ChildPublisher response = childPublisherServiceClient.updateChildPublisher(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateChildPublisherRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)` |   
  
### updateChildPublisherCallable()
    
    
    public final UnaryCallable<UpdateChildPublisherRequest,ChildPublisher> updateChildPublisherCallable()

Updates a ChildPublisher object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChildPublisherServiceClient childPublisherServiceClient =
         ChildPublisherServiceClient.create()) {
       UpdateChildPublisherRequest request =
           UpdateChildPublisherRequest.newBuilder()
               .setChildPublisher(ChildPublisher.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ChildPublisher> future =
           childPublisherServiceClient.updateChildPublisherCallable().futureCall(request);
       // Do something.
       ChildPublisher response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateChildPublisherRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateChildPublisherRequest),[ChildPublisher](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ChildPublisher)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
