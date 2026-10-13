---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient
title: Class ContactServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:35.598222+00:00
---

# Class ContactServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ContactServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/ContactServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Contact` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       ContactName name = ContactName.of("[NETWORK_CODE]", "[CONTACT]");
       Contact response = contactServiceClient.getContact(name);
     }
     

Note: close() needs to be called on the ContactServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetContact |  Retrieves a `Contact` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getContact(GetContactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getContact(ContactName name) 
  * getContact(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getContactCallable() 

  
ListContacts |  Lists `Contact` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listContacts(ListContactsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listContacts(NetworkName parent) 
  * listContacts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listContactsPagedCallable() 
  * listContactsCallable() 

  
CreateContact |  Creates a `Contact` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createContact(CreateContactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createContact(NetworkName parent, Contact contact) 
  * createContact(String parent, Contact contact) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createContactCallable() 

  
BatchCreateContacts |  Creates `Contact` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateContacts(NetworkName parent, List<CreateContactRequest> requests) 
  * batchCreateContacts(String parent, List<CreateContactRequest> requests) 
  * batchCreateContacts(BatchCreateContactsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateContactsCallable() 

  
UpdateContact |  Updates a `Contact` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateContact(UpdateContactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateContact(Contact contact, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateContactCallable() 

  
BatchUpdateContacts |  Batch updates `Contact` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateContacts(NetworkName parent, List<UpdateContactRequest> requests) 
  * batchUpdateContacts(String parent, List<UpdateContactRequest> requests) 
  * batchUpdateContacts(BatchUpdateContactsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateContactsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ContactServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ContactServiceSettings contactServiceSettings =
         ContactServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ContactServiceClient contactServiceClient = ContactServiceClient.create(contactServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ContactServiceSettings contactServiceSettings =
         ContactServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ContactServiceClient contactServiceClient = ContactServiceClient.create(contactServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ContactServiceClient

## Static Methods 

### create()
    
    
    public static final ContactServiceClient create()

Constructs an instance of ContactServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ContactServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ContactServiceSettings settings)
    
    
    public static final ContactServiceClient create(ContactServiceSettings settings)

Constructs an instance of ContactServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ContactServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContactServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ContactServiceStub stub)
    
    
    public static final ContactServiceClient create(ContactServiceStub stub)

Constructs an instance of ContactServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ContactServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ContactServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContactServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContactServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient)` |   
  
## Constructors 

### ContactServiceClient(ContactServiceSettings settings)
    
    
    protected ContactServiceClient(ContactServiceSettings settings)

Constructs an instance of ContactServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ContactServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceSettings)`  
  
  
### ContactServiceClient(ContactServiceStub stub)
    
    
    protected ContactServiceClient(ContactServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ContactServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContactServiceStub)`  
  
  
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
  
### batchCreateContacts(@Nullable NetworkName parent, List<CreateContactRequest> requests)
    
    
    public final BatchCreateContactsResponse batchCreateContacts(@Nullable NetworkName parent, List<CreateContactRequest> requests)

Creates `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateContactRequest> requests = new ArrayList<>();
       BatchCreateContactsResponse response =
           contactServiceClient.batchCreateContacts(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Contacts` will be created. Format: `networks/{network_code}` The parent field in the CreateContactRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateContactRequest)>`  
Required. The `Contact` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateContactsResponse)` |   
  
### batchCreateContacts(BatchCreateContactsRequest request)
    
    
    public final BatchCreateContactsResponse batchCreateContacts(BatchCreateContactsRequest request)

Creates `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       BatchCreateContactsRequest request =
           BatchCreateContactsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateContactRequest>())
               .build();
       BatchCreateContactsResponse response = contactServiceClient.batchCreateContacts(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateContactsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateContactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateContactsResponse)` |   
  
### batchCreateContacts(String parent, List<CreateContactRequest> requests)
    
    
    public final BatchCreateContactsResponse batchCreateContacts(String parent, List<CreateContactRequest> requests)

Creates `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateContactRequest> requests = new ArrayList<>();
       BatchCreateContactsResponse response =
           contactServiceClient.batchCreateContacts(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Contacts` will be created. Format: `networks/{network_code}` The parent field in the CreateContactRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateContactRequest)>`  
Required. The `Contact` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateContactsResponse)` |   
  
### batchCreateContactsCallable()
    
    
    public final UnaryCallable<BatchCreateContactsRequest,BatchCreateContactsResponse> batchCreateContactsCallable()

Creates `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       BatchCreateContactsRequest request =
           BatchCreateContactsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateContactRequest>())
               .build();
       ApiFuture<BatchCreateContactsResponse> future =
           contactServiceClient.batchCreateContactsCallable().futureCall(request);
       // Do something.
       BatchCreateContactsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateContactsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateContactsRequest),[BatchCreateContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateContactsResponse)>` |   
  
### batchUpdateContacts(@Nullable NetworkName parent, List<UpdateContactRequest> requests)
    
    
    public final BatchUpdateContactsResponse batchUpdateContacts(@Nullable NetworkName parent, List<UpdateContactRequest> requests)

Batch updates `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateContactRequest> requests = new ArrayList<>();
       BatchUpdateContactsResponse response =
           contactServiceClient.batchUpdateContacts(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Contacts` will be updated. Format: `networks/{network_code}` The parent field in the UpdateContactRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateContactRequest)>`  
Required. The `Contact` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateContactsResponse)` |   
  
### batchUpdateContacts(BatchUpdateContactsRequest request)
    
    
    public final BatchUpdateContactsResponse batchUpdateContacts(BatchUpdateContactsRequest request)

Batch updates `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       BatchUpdateContactsRequest request =
           BatchUpdateContactsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateContactRequest>())
               .build();
       BatchUpdateContactsResponse response = contactServiceClient.batchUpdateContacts(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateContactsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateContactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateContactsResponse)` |   
  
### batchUpdateContacts(String parent, List<UpdateContactRequest> requests)
    
    
    public final BatchUpdateContactsResponse batchUpdateContacts(String parent, List<UpdateContactRequest> requests)

Batch updates `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateContactRequest> requests = new ArrayList<>();
       BatchUpdateContactsResponse response =
           contactServiceClient.batchUpdateContacts(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Contacts` will be updated. Format: `networks/{network_code}` The parent field in the UpdateContactRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateContactRequest)>`  
Required. The `Contact` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateContactsResponse)` |   
  
### batchUpdateContactsCallable()
    
    
    public final UnaryCallable<BatchUpdateContactsRequest,BatchUpdateContactsResponse> batchUpdateContactsCallable()

Batch updates `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       BatchUpdateContactsRequest request =
           BatchUpdateContactsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateContactRequest>())
               .build();
       ApiFuture<BatchUpdateContactsResponse> future =
           contactServiceClient.batchUpdateContactsCallable().futureCall(request);
       // Do something.
       BatchUpdateContactsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateContactsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateContactsRequest),[BatchUpdateContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateContactsResponse)>` |   
  
### close()
    
    
    public final void close()

### createContact(@Nullable NetworkName parent, Contact contact)
    
    
    public final Contact createContact(@Nullable NetworkName parent, Contact contact)

Creates a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Contact contact = Contact.newBuilder().build();
       Contact response = contactServiceClient.createContact(parent, contact);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `Contact` will be created. Format: `networks/{network_code}`  
`contact` | `[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)`  
Required. The `Contact` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)` |   
  
### createContact(CreateContactRequest request)
    
    
    public final Contact createContact(CreateContactRequest request)

Creates a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       CreateContactRequest request =
           CreateContactRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setContact(Contact.newBuilder().build())
               .build();
       Contact response = contactServiceClient.createContact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateContactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)` |   
  
### createContact(String parent, Contact contact)
    
    
    public final Contact createContact(String parent, Contact contact)

Creates a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Contact contact = Contact.newBuilder().build();
       Contact response = contactServiceClient.createContact(parent, contact);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `Contact` will be created. Format: `networks/{network_code}`  
`contact` | `[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)`  
Required. The `Contact` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)` |   
  
### createContactCallable()
    
    
    public final UnaryCallable<CreateContactRequest,Contact> createContactCallable()

Creates a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       CreateContactRequest request =
           CreateContactRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setContact(Contact.newBuilder().build())
               .build();
       ApiFuture<Contact> future = contactServiceClient.createContactCallable().futureCall(request);
       // Do something.
       Contact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateContactRequest),[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)>` |   
  
### getContact(@Nullable ContactName name)
    
    
    public final Contact getContact(@Nullable ContactName name)

Retrieves a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       ContactName name = ContactName.of("[NETWORK_CODE]", "[CONTACT]");
       Contact response = contactServiceClient.getContact(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ContactName`  
Required. The resource name of the Contact. Format: `networks/{network_code}/contacts/{contact_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)` |   
  
### getContact(GetContactRequest request)
    
    
    public final Contact getContact(GetContactRequest request)

Retrieves a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       GetContactRequest request =
           GetContactRequest.newBuilder()
               .setName(ContactName.of("[NETWORK_CODE]", "[CONTACT]").toString())
               .build();
       Contact response = contactServiceClient.getContact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetContactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)` |   
  
### getContact(String name)
    
    
    public final Contact getContact(String name)

Retrieves a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       String name = ContactName.of("[NETWORK_CODE]", "[CONTACT]").toString();
       Contact response = contactServiceClient.getContact(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Contact. Format: `networks/{network_code}/contacts/{contact_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)` |   
  
### getContactCallable()
    
    
    public final UnaryCallable<GetContactRequest,Contact> getContactCallable()

Retrieves a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       GetContactRequest request =
           GetContactRequest.newBuilder()
               .setName(ContactName.of("[NETWORK_CODE]", "[CONTACT]").toString())
               .build();
       ApiFuture<Contact> future = contactServiceClient.getContactCallable().futureCall(request);
       // Do something.
       Contact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetContactRequest),[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)>` |   
  
### getSettings()
    
    
    public final @Nullable ContactServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.ContactServiceSettings` |   
  
### getStub()
    
    
    public ContactServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ContactServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.ContactServiceStub)` |   
  
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
  
### listContacts(@Nullable NetworkName parent)
    
    
    public final ContactServiceClient.ListContactsPagedResponse listContacts(@Nullable NetworkName parent)

Lists `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Contact element : contactServiceClient.listContacts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Contacts. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ContactServiceClient.ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient.ListContactsPagedResponse)` |   
  
### listContacts(ListContactsRequest request)
    
    
    public final ContactServiceClient.ListContactsPagedResponse listContacts(ListContactsRequest request)

Lists `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       ListContactsRequest request =
           ListContactsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Contact element : contactServiceClient.listContacts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListContactsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ContactServiceClient.ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient.ListContactsPagedResponse)` |   
  
### listContacts(String parent)
    
    
    public final ContactServiceClient.ListContactsPagedResponse listContacts(String parent)

Lists `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Contact element : contactServiceClient.listContacts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Contacts. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[ContactServiceClient.ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient.ListContactsPagedResponse)` |   
  
### listContactsCallable()
    
    
    public final UnaryCallable<ListContactsRequest,ListContactsResponse> listContactsCallable()

Lists `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       ListContactsRequest request =
           ListContactsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListContactsResponse response = contactServiceClient.listContactsCallable().call(request);
         for (Contact element : response.getContactsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContactsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContactsRequest),[ListContactsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContactsResponse)>` |   
  
### listContactsPagedCallable()
    
    
    public final UnaryCallable<ListContactsRequest,ContactServiceClient.ListContactsPagedResponse> listContactsPagedCallable()

Lists `Contact` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       ListContactsRequest request =
           ListContactsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Contact> future =
           contactServiceClient.listContactsPagedCallable().futureCall(request);
       // Do something.
       for (Contact element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContactsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListContactsRequest),[ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContactServiceClient.ListContactsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateContact(Contact contact, FieldMask updateMask)
    
    
    public final Contact updateContact(Contact contact, FieldMask updateMask)

Updates a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       Contact contact = Contact.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Contact response = contactServiceClient.updateContact(contact, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`contact` | `[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)`  
Required. The `Contact` to update. The `Contact`'s `name` is used to identify the `Contact` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)` |   
  
### updateContact(UpdateContactRequest request)
    
    
    public final Contact updateContact(UpdateContactRequest request)

Updates a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       UpdateContactRequest request =
           UpdateContactRequest.newBuilder()
               .setContact(Contact.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Contact response = contactServiceClient.updateContact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateContactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)` |   
  
### updateContactCallable()
    
    
    public final UnaryCallable<UpdateContactRequest,Contact> updateContactCallable()

Updates a `Contact` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ContactServiceClient contactServiceClient = ContactServiceClient.create()) {
       UpdateContactRequest request =
           UpdateContactRequest.newBuilder()
               .setContact(Contact.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Contact> future = contactServiceClient.updateContactCallable().futureCall(request);
       // Do something.
       Contact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateContactRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateContactRequest),[Contact](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Contact)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
