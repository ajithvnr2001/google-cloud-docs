---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient
title: Class AccessApprovalAdminClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:24.716236+00:00
---

# Class AccessApprovalAdminClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AccessApprovalAdminClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.10  2.3.1  2.2.4  2.1.12 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-accessapproval/google-cloud-accessapproval/src/main/java/com/google/cloud/accessapproval/v1/AccessApprovalAdminClient.java)| [Product Reference](https://cloud.google.com/access-approval/docs/)  
---|---  
  
Service Description: This API allows a customer to manage accesses to cloud resources by Google personnel. It defines the following resource model:

\- The API has a collection of ApprovalRequest resources, named `approvalRequests/{approval_request}` \- The API has top-level settings per Project/Folder/Organization, named `accessApprovalSettings`

The service also periodically emails a list of recipients, defined at the Project/Folder/Organization level in the accessApprovalSettings, when there is a pending ApprovalRequest for them to act on. The ApprovalRequests can also optionally be published to a Pub/Sub topic owned by the customer (contact support if you would like to enable Pub/Sub notifications).

ApprovalRequests can be approved or dismissed. Google personnel can only access the indicated resource or resources if the request is approved (subject to some exclusions: <https://cloud.google.com/access-approval/docs/overview#exclusions>).

Note: Using Access Approval functionality will mean that Google may not be able to meet the SLAs for your chosen products, as any support response times may be dramatically increased. As such the SLAs do not apply to any service disruption to the extent impacted by Customer's use of Access Approval. Do not enable Access Approval for projects where you may require high service availability and rapid response by Google Cloud Support.

After a request is approved or dismissed, no further action may be taken on it. Requests with the requested_expiration in the past or with no activity for 14 days are considered dismissed. When an approval expires, the request is considered dismissed.

If a request is not approved or dismissed, we call it pending.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       ApprovalRequestName name =
           ApprovalRequestName.ofProjectApprovalRequestName("[PROJECT]", "[APPROVAL_REQUEST]");
       ApprovalRequest response = accessApprovalAdminClient.getApprovalRequest(name);
     }
     

Note: close() needs to be called on the AccessApprovalAdminClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListApprovalRequests |  Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listApprovalRequests(ListApprovalRequestsMessage request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listApprovalRequests(FolderName parent) 
  * listApprovalRequests(OrganizationName parent) 
  * listApprovalRequests(ProjectName parent) 
  * listApprovalRequests(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listApprovalRequestsPagedCallable() 
  * listApprovalRequestsCallable() 

  
GetApprovalRequest |  Gets an approval request. Returns NOT_FOUND if the request does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getApprovalRequest(GetApprovalRequestMessage request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getApprovalRequest(ApprovalRequestName name) 
  * getApprovalRequest(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getApprovalRequestCallable() 

  
ApproveApprovalRequest |  Approves a request and returns the updated ApprovalRequest.  Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * approveApprovalRequest(ApproveApprovalRequestMessage request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * approveApprovalRequestCallable() 

  
DismissApprovalRequest |  Dismisses a request. Returns the updated ApprovalRequest.  NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether.  Returns NOT_FOUND if the request does not exist.  Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * dismissApprovalRequest(DismissApprovalRequestMessage request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * dismissApprovalRequestCallable() 

  
InvalidateApprovalRequest |  Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest.  NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval.  Returns FAILED_PRECONDITION if the request exists but is not in an approved state. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * invalidateApprovalRequest(InvalidateApprovalRequestMessage request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * invalidateApprovalRequestCallable() 

  
GetAccessApprovalSettings |  Gets the settings associated with a project, folder, or organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAccessApprovalSettings(GetAccessApprovalSettingsMessage request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAccessApprovalSettings(AccessApprovalSettingsName name) 
  * getAccessApprovalSettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAccessApprovalSettingsCallable() 

  
UpdateAccessApprovalSettings |  Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAccessApprovalSettings(UpdateAccessApprovalSettingsMessage request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAccessApprovalSettings(AccessApprovalSettings settings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAccessApprovalSettingsCallable() 

  
DeleteAccessApprovalSettings |  Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAccessApprovalSettings(DeleteAccessApprovalSettingsMessage request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteAccessApprovalSettings(AccessApprovalSettingsName name) 
  * deleteAccessApprovalSettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAccessApprovalSettingsCallable() 

  
GetAccessApprovalServiceAccount |  Retrieves the service account that is used by Access Approval to access KMS keys for signing approved approval requests. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAccessApprovalServiceAccount(GetAccessApprovalServiceAccountMessage request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAccessApprovalServiceAccount(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAccessApprovalServiceAccountCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AccessApprovalAdminSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AccessApprovalAdminSettings accessApprovalAdminSettings =
         AccessApprovalAdminSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AccessApprovalAdminClient accessApprovalAdminClient =
         AccessApprovalAdminClient.create(accessApprovalAdminSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AccessApprovalAdminSettings accessApprovalAdminSettings =
         AccessApprovalAdminSettings.newBuilder().setEndpoint(myEndpoint).build();
     AccessApprovalAdminClient accessApprovalAdminClient =
         AccessApprovalAdminClient.create(accessApprovalAdminSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AccessApprovalAdminSettings accessApprovalAdminSettings =
         AccessApprovalAdminSettings.newHttpJsonBuilder().build();
     AccessApprovalAdminClient accessApprovalAdminClient =
         AccessApprovalAdminClient.create(accessApprovalAdminSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AccessApprovalAdminClient

## Static Methods 

### create()
    
    
    public static final AccessApprovalAdminClient create()

Constructs an instance of AccessApprovalAdminClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AccessApprovalAdminSettings settings)
    
    
    public static final AccessApprovalAdminClient create(AccessApprovalAdminSettings settings)

Constructs an instance of AccessApprovalAdminClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AccessApprovalAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AccessApprovalStub stub)
    
    
    public static final AccessApprovalAdminClient create(AccessApprovalStub stub)

Constructs an instance of AccessApprovalAdminClient, using the given stub for making calls. This is for advanced usage - prefer using create(AccessApprovalAdminSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AccessApprovalStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.stub.AccessApprovalStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient)` |   
  
## Constructors 

### AccessApprovalAdminClient(AccessApprovalAdminSettings settings)
    
    
    protected AccessApprovalAdminClient(AccessApprovalAdminSettings settings)

Constructs an instance of AccessApprovalAdminClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AccessApprovalAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminSettings)`  
  
  
### AccessApprovalAdminClient(AccessApprovalStub stub)
    
    
    protected AccessApprovalAdminClient(AccessApprovalStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AccessApprovalStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.stub.AccessApprovalStub)`  
  
  
## Methods 

### approveApprovalRequest(ApproveApprovalRequestMessage request)
    
    
    public final ApprovalRequest approveApprovalRequest(ApproveApprovalRequestMessage request)

Approves a request and returns the updated ApprovalRequest.

Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       ApproveApprovalRequestMessage request =
           ApproveApprovalRequestMessage.newBuilder()
               .setName(
                   ApprovalRequestName.ofProjectApprovalRequestName(
                           "[PROJECT]", "[APPROVAL_REQUEST]")
                       .toString())
               .setExpireTime(Timestamp.newBuilder().build())
               .build();
       ApprovalRequest response = accessApprovalAdminClient.approveApprovalRequest(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ApproveApprovalRequestMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApproveApprovalRequestMessage)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)` |   
  
### approveApprovalRequestCallable()
    
    
    public final UnaryCallable<ApproveApprovalRequestMessage,ApprovalRequest> approveApprovalRequestCallable()

Approves a request and returns the updated ApprovalRequest.

Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       ApproveApprovalRequestMessage request =
           ApproveApprovalRequestMessage.newBuilder()
               .setName(
                   ApprovalRequestName.ofProjectApprovalRequestName(
                           "[PROJECT]", "[APPROVAL_REQUEST]")
                       .toString())
               .setExpireTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<ApprovalRequest> future =
           accessApprovalAdminClient.approveApprovalRequestCallable().futureCall(request);
       // Do something.
       ApprovalRequest response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ApproveApprovalRequestMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApproveApprovalRequestMessage),[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)>` |   
  
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

### deleteAccessApprovalSettings(@Nullable AccessApprovalSettingsName name)
    
    
    public final void deleteAccessApprovalSettings(@Nullable AccessApprovalSettingsName name)

Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       AccessApprovalSettingsName name = AccessApprovalSettingsName.ofProjectName("[PROJECT]");
       accessApprovalAdminClient.deleteAccessApprovalSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.accessapproval.v1.AccessApprovalSettingsName`  
Name of the AccessApprovalSettings to delete.  
  
### deleteAccessApprovalSettings(DeleteAccessApprovalSettingsMessage request)
    
    
    public final void deleteAccessApprovalSettings(DeleteAccessApprovalSettingsMessage request)

Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       DeleteAccessApprovalSettingsMessage request =
           DeleteAccessApprovalSettingsMessage.newBuilder()
               .setName(AccessApprovalSettingsName.ofProjectName("[PROJECT]").toString())
               .build();
       accessApprovalAdminClient.deleteAccessApprovalSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAccessApprovalSettingsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.DeleteAccessApprovalSettingsMessage)`  
The request object containing all of the parameters for the API call.  
  
### deleteAccessApprovalSettings(String name)
    
    
    public final void deleteAccessApprovalSettings(String name)

Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       String name = AccessApprovalSettingsName.ofProjectName("[PROJECT]").toString();
       accessApprovalAdminClient.deleteAccessApprovalSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the AccessApprovalSettings to delete.  
  
### deleteAccessApprovalSettingsCallable()
    
    
    public final UnaryCallable<DeleteAccessApprovalSettingsMessage,Empty> deleteAccessApprovalSettingsCallable()

Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       DeleteAccessApprovalSettingsMessage request =
           DeleteAccessApprovalSettingsMessage.newBuilder()
               .setName(AccessApprovalSettingsName.ofProjectName("[PROJECT]").toString())
               .build();
       ApiFuture<Empty> future =
           accessApprovalAdminClient.deleteAccessApprovalSettingsCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAccessApprovalSettingsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.DeleteAccessApprovalSettingsMessage),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### dismissApprovalRequest(DismissApprovalRequestMessage request)
    
    
    public final ApprovalRequest dismissApprovalRequest(DismissApprovalRequestMessage request)

Dismisses a request. Returns the updated ApprovalRequest.

NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether.

Returns NOT_FOUND if the request does not exist.

Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       DismissApprovalRequestMessage request =
           DismissApprovalRequestMessage.newBuilder()
               .setName(
                   ApprovalRequestName.ofProjectApprovalRequestName(
                           "[PROJECT]", "[APPROVAL_REQUEST]")
                       .toString())
               .build();
       ApprovalRequest response = accessApprovalAdminClient.dismissApprovalRequest(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DismissApprovalRequestMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.DismissApprovalRequestMessage)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)` |   
  
### dismissApprovalRequestCallable()
    
    
    public final UnaryCallable<DismissApprovalRequestMessage,ApprovalRequest> dismissApprovalRequestCallable()

Dismisses a request. Returns the updated ApprovalRequest.

NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether.

Returns NOT_FOUND if the request does not exist.

Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       DismissApprovalRequestMessage request =
           DismissApprovalRequestMessage.newBuilder()
               .setName(
                   ApprovalRequestName.ofProjectApprovalRequestName(
                           "[PROJECT]", "[APPROVAL_REQUEST]")
                       .toString())
               .build();
       ApiFuture<ApprovalRequest> future =
           accessApprovalAdminClient.dismissApprovalRequestCallable().futureCall(request);
       // Do something.
       ApprovalRequest response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DismissApprovalRequestMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.DismissApprovalRequestMessage),[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)>` |   
  
### getAccessApprovalServiceAccount(GetAccessApprovalServiceAccountMessage request)
    
    
    public final AccessApprovalServiceAccount getAccessApprovalServiceAccount(GetAccessApprovalServiceAccountMessage request)

Retrieves the service account that is used by Access Approval to access KMS keys for signing approved approval requests.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       GetAccessApprovalServiceAccountMessage request =
           GetAccessApprovalServiceAccountMessage.newBuilder().setName("name3373707").build();
       AccessApprovalServiceAccount response =
           accessApprovalAdminClient.getAccessApprovalServiceAccount(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAccessApprovalServiceAccountMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.GetAccessApprovalServiceAccountMessage)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalServiceAccount)` |   
  
### getAccessApprovalServiceAccount(String name)
    
    
    public final AccessApprovalServiceAccount getAccessApprovalServiceAccount(String name)

Retrieves the service account that is used by Access Approval to access KMS keys for signing approved approval requests.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       String name = "name3373707";
       AccessApprovalServiceAccount response =
           accessApprovalAdminClient.getAccessApprovalServiceAccount(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the AccessApprovalServiceAccount to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalServiceAccount)` |   
  
### getAccessApprovalServiceAccountCallable()
    
    
    public final UnaryCallable<GetAccessApprovalServiceAccountMessage,AccessApprovalServiceAccount> getAccessApprovalServiceAccountCallable()

Retrieves the service account that is used by Access Approval to access KMS keys for signing approved approval requests.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       GetAccessApprovalServiceAccountMessage request =
           GetAccessApprovalServiceAccountMessage.newBuilder().setName("name3373707").build();
       ApiFuture<AccessApprovalServiceAccount> future =
           accessApprovalAdminClient.getAccessApprovalServiceAccountCallable().futureCall(request);
       // Do something.
       AccessApprovalServiceAccount response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAccessApprovalServiceAccountMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.GetAccessApprovalServiceAccountMessage),[AccessApprovalServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalServiceAccount)>` |   
  
### getAccessApprovalSettings(@Nullable AccessApprovalSettingsName name)
    
    
    public final AccessApprovalSettings getAccessApprovalSettings(@Nullable AccessApprovalSettingsName name)

Gets the settings associated with a project, folder, or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       AccessApprovalSettingsName name = AccessApprovalSettingsName.ofProjectName("[PROJECT]");
       AccessApprovalSettings response = accessApprovalAdminClient.getAccessApprovalSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.accessapproval.v1.AccessApprovalSettingsName`  
The name of the AccessApprovalSettings to retrieve. Format: "{projects|folders|organizations}/{id}/accessApprovalSettings"  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalSettings)` |   
  
### getAccessApprovalSettings(GetAccessApprovalSettingsMessage request)
    
    
    public final AccessApprovalSettings getAccessApprovalSettings(GetAccessApprovalSettingsMessage request)

Gets the settings associated with a project, folder, or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       GetAccessApprovalSettingsMessage request =
           GetAccessApprovalSettingsMessage.newBuilder()
               .setName(AccessApprovalSettingsName.ofProjectName("[PROJECT]").toString())
               .build();
       AccessApprovalSettings response =
           accessApprovalAdminClient.getAccessApprovalSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAccessApprovalSettingsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.GetAccessApprovalSettingsMessage)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalSettings)` |   
  
### getAccessApprovalSettings(String name)
    
    
    public final AccessApprovalSettings getAccessApprovalSettings(String name)

Gets the settings associated with a project, folder, or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       String name = AccessApprovalSettingsName.ofProjectName("[PROJECT]").toString();
       AccessApprovalSettings response = accessApprovalAdminClient.getAccessApprovalSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the AccessApprovalSettings to retrieve. Format: "{projects|folders|organizations}/{id}/accessApprovalSettings"  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalSettings)` |   
  
### getAccessApprovalSettingsCallable()
    
    
    public final UnaryCallable<GetAccessApprovalSettingsMessage,AccessApprovalSettings> getAccessApprovalSettingsCallable()

Gets the settings associated with a project, folder, or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       GetAccessApprovalSettingsMessage request =
           GetAccessApprovalSettingsMessage.newBuilder()
               .setName(AccessApprovalSettingsName.ofProjectName("[PROJECT]").toString())
               .build();
       ApiFuture<AccessApprovalSettings> future =
           accessApprovalAdminClient.getAccessApprovalSettingsCallable().futureCall(request);
       // Do something.
       AccessApprovalSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAccessApprovalSettingsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.GetAccessApprovalSettingsMessage),[AccessApprovalSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalSettings)>` |   
  
### getApprovalRequest(@Nullable ApprovalRequestName name)
    
    
    public final ApprovalRequest getApprovalRequest(@Nullable ApprovalRequestName name)

Gets an approval request. Returns NOT_FOUND if the request does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       ApprovalRequestName name =
           ApprovalRequestName.ofProjectApprovalRequestName("[PROJECT]", "[APPROVAL_REQUEST]");
       ApprovalRequest response = accessApprovalAdminClient.getApprovalRequest(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.accessapproval.v1.ApprovalRequestName`  
The name of the approval request to retrieve. Format: "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}"  
**Returns**  
---  
**Type** | **Description**  
`[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)` |   
  
### getApprovalRequest(GetApprovalRequestMessage request)
    
    
    public final ApprovalRequest getApprovalRequest(GetApprovalRequestMessage request)

Gets an approval request. Returns NOT_FOUND if the request does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       GetApprovalRequestMessage request =
           GetApprovalRequestMessage.newBuilder()
               .setName(
                   ApprovalRequestName.ofProjectApprovalRequestName(
                           "[PROJECT]", "[APPROVAL_REQUEST]")
                       .toString())
               .build();
       ApprovalRequest response = accessApprovalAdminClient.getApprovalRequest(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetApprovalRequestMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.GetApprovalRequestMessage)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)` |   
  
### getApprovalRequest(String name)
    
    
    public final ApprovalRequest getApprovalRequest(String name)

Gets an approval request. Returns NOT_FOUND if the request does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       String name =
           ApprovalRequestName.ofProjectApprovalRequestName("[PROJECT]", "[APPROVAL_REQUEST]")
               .toString();
       ApprovalRequest response = accessApprovalAdminClient.getApprovalRequest(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the approval request to retrieve. Format: "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}"  
**Returns**  
---  
**Type** | **Description**  
`[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)` |   
  
### getApprovalRequestCallable()
    
    
    public final UnaryCallable<GetApprovalRequestMessage,ApprovalRequest> getApprovalRequestCallable()

Gets an approval request. Returns NOT_FOUND if the request does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       GetApprovalRequestMessage request =
           GetApprovalRequestMessage.newBuilder()
               .setName(
                   ApprovalRequestName.ofProjectApprovalRequestName(
                           "[PROJECT]", "[APPROVAL_REQUEST]")
                       .toString())
               .build();
       ApiFuture<ApprovalRequest> future =
           accessApprovalAdminClient.getApprovalRequestCallable().futureCall(request);
       // Do something.
       ApprovalRequest response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetApprovalRequestMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.GetApprovalRequestMessage),[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)>` |   
  
### getSettings()
    
    
    public final @Nullable AccessApprovalAdminSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.accessapproval.v1.AccessApprovalAdminSettings` |   
  
### getStub()
    
    
    public AccessApprovalStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.stub.AccessApprovalStub)` |   
  
### invalidateApprovalRequest(InvalidateApprovalRequestMessage request)
    
    
    public final ApprovalRequest invalidateApprovalRequest(InvalidateApprovalRequestMessage request)

Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest.

NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval.

Returns FAILED_PRECONDITION if the request exists but is not in an approved state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       InvalidateApprovalRequestMessage request =
           InvalidateApprovalRequestMessage.newBuilder()
               .setName(
                   ApprovalRequestName.ofProjectApprovalRequestName(
                           "[PROJECT]", "[APPROVAL_REQUEST]")
                       .toString())
               .build();
       ApprovalRequest response = accessApprovalAdminClient.invalidateApprovalRequest(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InvalidateApprovalRequestMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.InvalidateApprovalRequestMessage)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)` |   
  
### invalidateApprovalRequestCallable()
    
    
    public final UnaryCallable<InvalidateApprovalRequestMessage,ApprovalRequest> invalidateApprovalRequestCallable()

Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest.

NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval.

Returns FAILED_PRECONDITION if the request exists but is not in an approved state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       InvalidateApprovalRequestMessage request =
           InvalidateApprovalRequestMessage.newBuilder()
               .setName(
                   ApprovalRequestName.ofProjectApprovalRequestName(
                           "[PROJECT]", "[APPROVAL_REQUEST]")
                       .toString())
               .build();
       ApiFuture<ApprovalRequest> future =
           accessApprovalAdminClient.invalidateApprovalRequestCallable().futureCall(request);
       // Do something.
       ApprovalRequest response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InvalidateApprovalRequestMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.InvalidateApprovalRequestMessage),[ApprovalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ApprovalRequest)>` |   
  
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
  
### listApprovalRequests(@Nullable FolderName parent)
    
    
    public final AccessApprovalAdminClient.ListApprovalRequestsPagedResponse listApprovalRequests(@Nullable FolderName parent)

Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       for (ApprovalRequest element :
           accessApprovalAdminClient.listApprovalRequests(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.accessapproval.v1.FolderName`  
The parent resource. This may be "projects/{project}", "folders/{folder}", or "organizations/{organization}".  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalAdminClient.ListApprovalRequestsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient.ListApprovalRequestsPagedResponse)` |   
  
### listApprovalRequests(@Nullable OrganizationName parent)
    
    
    public final AccessApprovalAdminClient.ListApprovalRequestsPagedResponse listApprovalRequests(@Nullable OrganizationName parent)

Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (ApprovalRequest element :
           accessApprovalAdminClient.listApprovalRequests(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.accessapproval.v1.OrganizationName`  
The parent resource. This may be "projects/{project}", "folders/{folder}", or "organizations/{organization}".  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalAdminClient.ListApprovalRequestsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient.ListApprovalRequestsPagedResponse)` |   
  
### listApprovalRequests(@Nullable ProjectName parent)
    
    
    public final AccessApprovalAdminClient.ListApprovalRequestsPagedResponse listApprovalRequests(@Nullable ProjectName parent)

Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (ApprovalRequest element :
           accessApprovalAdminClient.listApprovalRequests(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.accessapproval.v1.ProjectName`  
The parent resource. This may be "projects/{project}", "folders/{folder}", or "organizations/{organization}".  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalAdminClient.ListApprovalRequestsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient.ListApprovalRequestsPagedResponse)` |   
  
### listApprovalRequests(ListApprovalRequestsMessage request)
    
    
    public final AccessApprovalAdminClient.ListApprovalRequestsPagedResponse listApprovalRequests(ListApprovalRequestsMessage request)

Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       ListApprovalRequestsMessage request =
           ListApprovalRequestsMessage.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ApprovalRequest element :
           accessApprovalAdminClient.listApprovalRequests(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListApprovalRequestsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ListApprovalRequestsMessage)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalAdminClient.ListApprovalRequestsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient.ListApprovalRequestsPagedResponse)` |   
  
### listApprovalRequests(String parent)
    
    
    public final AccessApprovalAdminClient.ListApprovalRequestsPagedResponse listApprovalRequests(String parent)

Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (ApprovalRequest element :
           accessApprovalAdminClient.listApprovalRequests(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent resource. This may be "projects/{project}", "folders/{folder}", or "organizations/{organization}".  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalAdminClient.ListApprovalRequestsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient.ListApprovalRequestsPagedResponse)` |   
  
### listApprovalRequestsCallable()
    
    
    public final UnaryCallable<ListApprovalRequestsMessage,ListApprovalRequestsResponse> listApprovalRequestsCallable()

Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       ListApprovalRequestsMessage request =
           ListApprovalRequestsMessage.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListApprovalRequestsResponse response =
             accessApprovalAdminClient.listApprovalRequestsCallable().call(request);
         for (ApprovalRequest element : response.getApprovalRequestsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListApprovalRequestsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ListApprovalRequestsMessage),[ListApprovalRequestsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ListApprovalRequestsResponse)>` |   
  
### listApprovalRequestsPagedCallable()
    
    
    public final UnaryCallable<ListApprovalRequestsMessage,AccessApprovalAdminClient.ListApprovalRequestsPagedResponse> listApprovalRequestsPagedCallable()

Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       ListApprovalRequestsMessage request =
           ListApprovalRequestsMessage.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ApprovalRequest> future =
           accessApprovalAdminClient.listApprovalRequestsPagedCallable().futureCall(request);
       // Do something.
       for (ApprovalRequest element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListApprovalRequestsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.ListApprovalRequestsMessage),[ListApprovalRequestsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalAdminClient.ListApprovalRequestsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAccessApprovalSettings(AccessApprovalSettings settings, FieldMask updateMask)
    
    
    public final AccessApprovalSettings updateAccessApprovalSettings(AccessApprovalSettings settings, FieldMask updateMask)

Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       AccessApprovalSettings settings = AccessApprovalSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AccessApprovalSettings response =
           accessApprovalAdminClient.updateAccessApprovalSettings(settings, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[AccessApprovalSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalSettings)`  
The new AccessApprovalSettings.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The update mask applies to the settings. Only the top level fields of AccessApprovalSettings (notification_emails & enrolled_services) are supported. For each field, if it is included, the currently stored value will be entirely overwritten with the value of the field passed in this request. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask> If this field is left unset, only the notification_emails field will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalSettings)` |   
  
### updateAccessApprovalSettings(UpdateAccessApprovalSettingsMessage request)
    
    
    public final AccessApprovalSettings updateAccessApprovalSettings(UpdateAccessApprovalSettingsMessage request)

Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       UpdateAccessApprovalSettingsMessage request =
           UpdateAccessApprovalSettingsMessage.newBuilder()
               .setSettings(AccessApprovalSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AccessApprovalSettings response =
           accessApprovalAdminClient.updateAccessApprovalSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAccessApprovalSettingsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.UpdateAccessApprovalSettingsMessage)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AccessApprovalSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalSettings)` |   
  
### updateAccessApprovalSettingsCallable()
    
    
    public final UnaryCallable<UpdateAccessApprovalSettingsMessage,AccessApprovalSettings> updateAccessApprovalSettingsCallable()

Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AccessApprovalAdminClient accessApprovalAdminClient = AccessApprovalAdminClient.create()) {
       UpdateAccessApprovalSettingsMessage request =
           UpdateAccessApprovalSettingsMessage.newBuilder()
               .setSettings(AccessApprovalSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AccessApprovalSettings> future =
           accessApprovalAdminClient.updateAccessApprovalSettingsCallable().futureCall(request);
       // Do something.
       AccessApprovalSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAccessApprovalSettingsMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.UpdateAccessApprovalSettingsMessage),[AccessApprovalSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-accessapproval/latest/com.google.cloud.accessapproval.v1.AccessApprovalSettings)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
