---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient
title: Class EssentialContactsServiceClient (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:23.294558+00:00
---

# Class EssentialContactsServiceClient (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EssentialContactsServiceClient (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.6  2.2.0  2.1.11 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-essential-contacts/google-cloud-essential-contacts/src/main/java/com/google/cloud/essentialcontacts/v1/EssentialContactsServiceClient.java)| [Product Reference](https://cloud.google.com/resource-manager/docs/managing-notification-contacts/)  
---|---  
  
Service Description: Manages contacts for important Google Cloud notifications.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       Contact contact = Contact.newBuilder().build();
       Contact response = essentialContactsServiceClient.createContact(parent, contact);
     }
     

Note: close() needs to be called on the EssentialContactsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateContact |  Adds a new contact for a resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createContact(CreateContactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createContact(FolderName parent, Contact contact) 
  * createContact(OrganizationName parent, Contact contact) 
  * createContact(ProjectName parent, Contact contact) 
  * createContact(String parent, Contact contact) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createContactCallable() 

  
UpdateContact |  Updates a contact. Note: A contact's email address cannot be changed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateContact(UpdateContactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateContact(Contact contact, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateContactCallable() 

  
ListContacts |  Lists the contacts that have been set on a resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listContacts(ListContactsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listContacts(FolderName parent) 
  * listContacts(OrganizationName parent) 
  * listContacts(ProjectName parent) 
  * listContacts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listContactsPagedCallable() 
  * listContactsCallable() 

  
GetContact |  Gets a single contact. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getContact(GetContactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getContact(ContactName name) 
  * getContact(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getContactCallable() 

  
DeleteContact |  Deletes a contact. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteContact(DeleteContactRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteContact(ContactName name) 
  * deleteContact(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteContactCallable() 

  
ComputeContacts |  Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * computeContacts(ComputeContactsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * computeContactsPagedCallable() 
  * computeContactsCallable() 

  
SendTestMessage |  Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * sendTestMessage(SendTestMessageRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * sendTestMessageCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of EssentialContactsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EssentialContactsServiceSettings essentialContactsServiceSettings =
         EssentialContactsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create(essentialContactsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EssentialContactsServiceSettings essentialContactsServiceSettings =
         EssentialContactsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create(essentialContactsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EssentialContactsServiceSettings essentialContactsServiceSettings =
         EssentialContactsServiceSettings.newHttpJsonBuilder().build();
     EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create(essentialContactsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EssentialContactsServiceClient

## Static Methods 

### create()
    
    
    public static final EssentialContactsServiceClient create()

Constructs an instance of EssentialContactsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EssentialContactsServiceSettings settings)
    
    
    public static final EssentialContactsServiceClient create(EssentialContactsServiceSettings settings)

Constructs an instance of EssentialContactsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EssentialContactsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EssentialContactsServiceStub stub)
    
    
    public static final EssentialContactsServiceClient create(EssentialContactsServiceStub stub)

Constructs an instance of EssentialContactsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(EssentialContactsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EssentialContactsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.stub.EssentialContactsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient)` |   
  
## Constructors 

### EssentialContactsServiceClient(EssentialContactsServiceSettings settings)
    
    
    protected EssentialContactsServiceClient(EssentialContactsServiceSettings settings)

Constructs an instance of EssentialContactsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EssentialContactsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceSettings)`  
  
  
### EssentialContactsServiceClient(EssentialContactsServiceStub stub)
    
    
    protected EssentialContactsServiceClient(EssentialContactsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EssentialContactsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.stub.EssentialContactsServiceStub)`  
  
  
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

### computeContacts(ComputeContactsRequest request)
    
    
    public final EssentialContactsServiceClient.ComputeContactsPagedResponse computeContacts(ComputeContactsRequest request)

Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ComputeContactsRequest request =
           ComputeContactsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .addAllNotificationCategories(new ArrayList<NotificationCategory>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Contact element : essentialContactsServiceClient.computeContacts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ComputeContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ComputeContactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient.ComputeContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient.ComputeContactsPagedResponse)` |   
  
### computeContactsCallable()
    
    
    public final UnaryCallable<ComputeContactsRequest,ComputeContactsResponse> computeContactsCallable()

Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ComputeContactsRequest request =
           ComputeContactsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .addAllNotificationCategories(new ArrayList<NotificationCategory>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ComputeContactsResponse response =
             essentialContactsServiceClient.computeContactsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ComputeContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ComputeContactsRequest),[ComputeContactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ComputeContactsResponse)>` |   
  
### computeContactsPagedCallable()
    
    
    public final UnaryCallable<ComputeContactsRequest,EssentialContactsServiceClient.ComputeContactsPagedResponse> computeContactsPagedCallable()

Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ComputeContactsRequest request =
           ComputeContactsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .addAllNotificationCategories(new ArrayList<NotificationCategory>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Contact> future =
           essentialContactsServiceClient.computeContactsPagedCallable().futureCall(request);
       // Do something.
       for (Contact element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ComputeContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ComputeContactsRequest),[ComputeContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient.ComputeContactsPagedResponse)>` |   
  
### createContact(@Nullable FolderName parent, Contact contact)
    
    
    public final Contact createContact(@Nullable FolderName parent, Contact contact)

Adds a new contact for a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       Contact contact = Contact.newBuilder().build();
       Contact response = essentialContactsServiceClient.createContact(parent, contact);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.FolderName`  
Required. The resource to save this contact for. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}  
`contact` | `[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)`  
Required. The contact to create. Must specify an email address and language tag.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### createContact(@Nullable OrganizationName parent, Contact contact)
    
    
    public final Contact createContact(@Nullable OrganizationName parent, Contact contact)

Adds a new contact for a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       Contact contact = Contact.newBuilder().build();
       Contact response = essentialContactsServiceClient.createContact(parent, contact);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.OrganizationName`  
Required. The resource to save this contact for. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}  
`contact` | `[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)`  
Required. The contact to create. Must specify an email address and language tag.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### createContact(@Nullable ProjectName parent, Contact contact)
    
    
    public final Contact createContact(@Nullable ProjectName parent, Contact contact)

Adds a new contact for a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       Contact contact = Contact.newBuilder().build();
       Contact response = essentialContactsServiceClient.createContact(parent, contact);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.ProjectName`  
Required. The resource to save this contact for. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}  
`contact` | `[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)`  
Required. The contact to create. Must specify an email address and language tag.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### createContact(CreateContactRequest request)
    
    
    public final Contact createContact(CreateContactRequest request)

Adds a new contact for a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       CreateContactRequest request =
           CreateContactRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setContact(Contact.newBuilder().build())
               .build();
       Contact response = essentialContactsServiceClient.createContact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.CreateContactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### createContact(String parent, Contact contact)
    
    
    public final Contact createContact(String parent, Contact contact)

Adds a new contact for a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       Contact contact = Contact.newBuilder().build();
       Contact response = essentialContactsServiceClient.createContact(parent, contact);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource to save this contact for. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}  
`contact` | `[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)`  
Required. The contact to create. Must specify an email address and language tag.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### createContactCallable()
    
    
    public final UnaryCallable<CreateContactRequest,Contact> createContactCallable()

Adds a new contact for a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       CreateContactRequest request =
           CreateContactRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setContact(Contact.newBuilder().build())
               .build();
       ApiFuture<Contact> future =
           essentialContactsServiceClient.createContactCallable().futureCall(request);
       // Do something.
       Contact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.CreateContactRequest),[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)>` |   
  
### deleteContact(@Nullable ContactName name)
    
    
    public final void deleteContact(@Nullable ContactName name)

Deletes a contact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ContactName name = ContactName.ofProjectContactName("[PROJECT]", "[CONTACT]");
       essentialContactsServiceClient.deleteContact(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.ContactName`  
Required. The name of the contact to delete. Format: organizations/{organization_id}/contacts/{contact_id}, folders/{folder_id}/contacts/{contact_id} or projects/{project_id}/contacts/{contact_id}  
  
### deleteContact(DeleteContactRequest request)
    
    
    public final void deleteContact(DeleteContactRequest request)

Deletes a contact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       DeleteContactRequest request =
           DeleteContactRequest.newBuilder()
               .setName(ContactName.ofProjectContactName("[PROJECT]", "[CONTACT]").toString())
               .build();
       essentialContactsServiceClient.deleteContact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.DeleteContactRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteContact(String name)
    
    
    public final void deleteContact(String name)

Deletes a contact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       String name = ContactName.ofProjectContactName("[PROJECT]", "[CONTACT]").toString();
       essentialContactsServiceClient.deleteContact(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the contact to delete. Format: organizations/{organization_id}/contacts/{contact_id}, folders/{folder_id}/contacts/{contact_id} or projects/{project_id}/contacts/{contact_id}  
  
### deleteContactCallable()
    
    
    public final UnaryCallable<DeleteContactRequest,Empty> deleteContactCallable()

Deletes a contact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       DeleteContactRequest request =
           DeleteContactRequest.newBuilder()
               .setName(ContactName.ofProjectContactName("[PROJECT]", "[CONTACT]").toString())
               .build();
       ApiFuture<Empty> future =
           essentialContactsServiceClient.deleteContactCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.DeleteContactRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getContact(@Nullable ContactName name)
    
    
    public final Contact getContact(@Nullable ContactName name)

Gets a single contact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ContactName name = ContactName.ofProjectContactName("[PROJECT]", "[CONTACT]");
       Contact response = essentialContactsServiceClient.getContact(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.ContactName`  
Required. The name of the contact to retrieve. Format: organizations/{organization_id}/contacts/{contact_id}, folders/{folder_id}/contacts/{contact_id} or projects/{project_id}/contacts/{contact_id}  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### getContact(GetContactRequest request)
    
    
    public final Contact getContact(GetContactRequest request)

Gets a single contact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       GetContactRequest request =
           GetContactRequest.newBuilder()
               .setName(ContactName.ofProjectContactName("[PROJECT]", "[CONTACT]").toString())
               .build();
       Contact response = essentialContactsServiceClient.getContact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.GetContactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### getContact(String name)
    
    
    public final Contact getContact(String name)

Gets a single contact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       String name = ContactName.ofProjectContactName("[PROJECT]", "[CONTACT]").toString();
       Contact response = essentialContactsServiceClient.getContact(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the contact to retrieve. Format: organizations/{organization_id}/contacts/{contact_id}, folders/{folder_id}/contacts/{contact_id} or projects/{project_id}/contacts/{contact_id}  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### getContactCallable()
    
    
    public final UnaryCallable<GetContactRequest,Contact> getContactCallable()

Gets a single contact.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       GetContactRequest request =
           GetContactRequest.newBuilder()
               .setName(ContactName.ofProjectContactName("[PROJECT]", "[CONTACT]").toString())
               .build();
       ApiFuture<Contact> future =
           essentialContactsServiceClient.getContactCallable().futureCall(request);
       // Do something.
       Contact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.GetContactRequest),[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)>` |   
  
### getSettings()
    
    
    public final @Nullable EssentialContactsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.EssentialContactsServiceSettings` |   
  
### getStub()
    
    
    public EssentialContactsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.stub.EssentialContactsServiceStub)` |   
  
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
  
### listContacts(@Nullable FolderName parent)
    
    
    public final EssentialContactsServiceClient.ListContactsPagedResponse listContacts(@Nullable FolderName parent)

Lists the contacts that have been set on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       for (Contact element : essentialContactsServiceClient.listContacts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.FolderName`  
Required. The parent resource name. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient.ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient.ListContactsPagedResponse)` |   
  
### listContacts(@Nullable OrganizationName parent)
    
    
    public final EssentialContactsServiceClient.ListContactsPagedResponse listContacts(@Nullable OrganizationName parent)

Lists the contacts that have been set on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (Contact element : essentialContactsServiceClient.listContacts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.OrganizationName`  
Required. The parent resource name. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient.ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient.ListContactsPagedResponse)` |   
  
### listContacts(@Nullable ProjectName parent)
    
    
    public final EssentialContactsServiceClient.ListContactsPagedResponse listContacts(@Nullable ProjectName parent)

Lists the contacts that have been set on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (Contact element : essentialContactsServiceClient.listContacts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.essentialcontacts.v1.ProjectName`  
Required. The parent resource name. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient.ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient.ListContactsPagedResponse)` |   
  
### listContacts(ListContactsRequest request)
    
    
    public final EssentialContactsServiceClient.ListContactsPagedResponse listContacts(ListContactsRequest request)

Lists the contacts that have been set on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ListContactsRequest request =
           ListContactsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Contact element : essentialContactsServiceClient.listContacts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ListContactsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient.ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient.ListContactsPagedResponse)` |   
  
### listContacts(String parent)
    
    
    public final EssentialContactsServiceClient.ListContactsPagedResponse listContacts(String parent)

Lists the contacts that have been set on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (Contact element : essentialContactsServiceClient.listContacts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceClient.ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient.ListContactsPagedResponse)` |   
  
### listContactsCallable()
    
    
    public final UnaryCallable<ListContactsRequest,ListContactsResponse> listContactsCallable()

Lists the contacts that have been set on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ListContactsRequest request =
           ListContactsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListContactsResponse response =
             essentialContactsServiceClient.listContactsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ListContactsRequest),[ListContactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ListContactsResponse)>` |   
  
### listContactsPagedCallable()
    
    
    public final UnaryCallable<ListContactsRequest,EssentialContactsServiceClient.ListContactsPagedResponse> listContactsPagedCallable()

Lists the contacts that have been set on a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       ListContactsRequest request =
           ListContactsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Contact> future =
           essentialContactsServiceClient.listContactsPagedCallable().futureCall(request);
       // Do something.
       for (Contact element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ListContactsRequest),[ListContactsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceClient.ListContactsPagedResponse)>` |   
  
### sendTestMessage(SendTestMessageRequest request)
    
    
    public final void sendTestMessage(SendTestMessageRequest request)

Allows a contact admin to send a test message to contact to verify that it has been configured correctly.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       SendTestMessageRequest request =
           SendTestMessageRequest.newBuilder()
               .addAllContacts(new ArrayList<String>())
               .setResource(ProjectName.of("[PROJECT]").toString())
               .setNotificationCategory(NotificationCategory.forNumber(0))
               .build();
       essentialContactsServiceClient.sendTestMessage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SendTestMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.SendTestMessageRequest)`  
The request object containing all of the parameters for the API call.  
  
### sendTestMessageCallable()
    
    
    public final UnaryCallable<SendTestMessageRequest,Empty> sendTestMessageCallable()

Allows a contact admin to send a test message to contact to verify that it has been configured correctly.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       SendTestMessageRequest request =
           SendTestMessageRequest.newBuilder()
               .addAllContacts(new ArrayList<String>())
               .setResource(ProjectName.of("[PROJECT]").toString())
               .setNotificationCategory(NotificationCategory.forNumber(0))
               .build();
       ApiFuture<Empty> future =
           essentialContactsServiceClient.sendTestMessageCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SendTestMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.SendTestMessageRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateContact(Contact contact, FieldMask updateMask)
    
    
    public final Contact updateContact(Contact contact, FieldMask updateMask)

Updates a contact. Note: A contact's email address cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       Contact contact = Contact.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Contact response = essentialContactsServiceClient.updateContact(contact, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`contact` | `[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)`  
Required. The contact resource to replace the existing saved contact. Note: the email address of the contact cannot be modified.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The update mask applied to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### updateContact(UpdateContactRequest request)
    
    
    public final Contact updateContact(UpdateContactRequest request)

Updates a contact. Note: A contact's email address cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       UpdateContactRequest request =
           UpdateContactRequest.newBuilder()
               .setContact(Contact.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Contact response = essentialContactsServiceClient.updateContact(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.UpdateContactRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)` |   
  
### updateContactCallable()
    
    
    public final UnaryCallable<UpdateContactRequest,Contact> updateContactCallable()

Updates a contact. Note: A contact's email address cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EssentialContactsServiceClient essentialContactsServiceClient =
         EssentialContactsServiceClient.create()) {
       UpdateContactRequest request =
           UpdateContactRequest.newBuilder()
               .setContact(Contact.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Contact> future =
           essentialContactsServiceClient.updateContactCallable().futureCall(request);
       // Do something.
       Contact response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.UpdateContactRequest),[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
