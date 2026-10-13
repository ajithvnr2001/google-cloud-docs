---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceGrpc.EssentialContactsServiceStub
title: Class EssentialContactsServiceGrpc.EssentialContactsServiceStub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:32.205134+00:00
---

# Class EssentialContactsServiceGrpc.EssentialContactsServiceStub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceGrpc.EssentialContactsServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EssentialContactsServiceGrpc.EssentialContactsServiceStub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.6  2.2.0  2.1.11 
    
    
    public static final class EssentialContactsServiceGrpc.EssentialContactsServiceStub extends AbstractAsyncStub<EssentialContactsServiceGrpc.EssentialContactsServiceStub>

A stub to allow clients to do asynchronous rpc calls to service EssentialContactsService.

Manages contacts for important Google Cloud notifications.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > EssentialContactsServiceGrpc.EssentialContactsServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected EssentialContactsServiceGrpc.EssentialContactsServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[EssentialContactsServiceGrpc.EssentialContactsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.EssentialContactsServiceGrpc.EssentialContactsServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### computeContacts(ComputeContactsRequest request, StreamObserver<ComputeContactsResponse> responseObserver)
    
    
    public void computeContacts(ComputeContactsRequest request, StreamObserver<ComputeContactsResponse> responseObserver)

Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ComputeContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ComputeContactsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ComputeContactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ComputeContactsResponse)>`  
  
  
### createContact(CreateContactRequest request, StreamObserver<Contact> responseObserver)
    
    
    public void createContact(CreateContactRequest request, StreamObserver<Contact> responseObserver)

Adds a new contact for a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.CreateContactRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)>`  
  
  
### deleteContact(DeleteContactRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteContact(DeleteContactRequest request, StreamObserver<Empty> responseObserver)

Deletes a contact.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.DeleteContactRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getContact(GetContactRequest request, StreamObserver<Contact> responseObserver)
    
    
    public void getContact(GetContactRequest request, StreamObserver<Contact> responseObserver)

Gets a single contact.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.GetContactRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)>`  
  
  
### listContacts(ListContactsRequest request, StreamObserver<ListContactsResponse> responseObserver)
    
    
    public void listContacts(ListContactsRequest request, StreamObserver<ListContactsResponse> responseObserver)

Lists the contacts that have been set on a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ListContactsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListContactsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.ListContactsResponse)>`  
  
  
### sendTestMessage(SendTestMessageRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void sendTestMessage(SendTestMessageRequest request, StreamObserver<Empty> responseObserver)

Allows a contact admin to send a test message to contact to verify that it has been configured correctly.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SendTestMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.SendTestMessageRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### updateContact(UpdateContactRequest request, StreamObserver<Contact> responseObserver)
    
    
    public void updateContact(UpdateContactRequest request, StreamObserver<Contact> responseObserver)

Updates a contact. Note: A contact's email address cannot be changed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateContactRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.UpdateContactRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-essential-contacts/latest/com.google.cloud.essentialcontacts.v1.Contact)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
