---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.CloudBillingGrpc.CloudBillingStub
title: Class CloudBillingGrpc.CloudBillingStub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:41.009997+00:00
---

# Class CloudBillingGrpc.CloudBillingStub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.CloudBillingGrpc.CloudBillingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudBillingGrpc.CloudBillingStub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.5  2.2.1  2.1.12 
    
    
    public static final class CloudBillingGrpc.CloudBillingStub extends AbstractAsyncStub<CloudBillingGrpc.CloudBillingStub>

A stub to allow clients to do asynchronous rpc calls to service CloudBilling.

Retrieves the Google Cloud Console billing accounts and associates them with projects.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > CloudBillingGrpc.CloudBillingStub

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
    
    
    protected CloudBillingGrpc.CloudBillingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudBillingGrpc.CloudBillingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.CloudBillingGrpc.CloudBillingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createBillingAccount(CreateBillingAccountRequest request, StreamObserver<BillingAccount> responseObserver)
    
    
    public void createBillingAccount(CreateBillingAccountRequest request, StreamObserver<BillingAccount> responseObserver)

This method creates [billing subaccounts](https://cloud.google.com/billing/docs/concepts#subaccounts). Google Cloud resellers should use the Channel Services APIs, [accounts.customers.create](https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/create) and [accounts.customers.entitlements.create](https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create). When creating a subaccount, the current authenticated user must have the `billing.accounts.update` IAM permission on the parent account, which is typically given to billing account [administrators](https://cloud.google.com/billing/docs/how-to/billing-access). This method will return an error if the parent account has not been provisioned for subaccounts.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBillingAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.CreateBillingAccountRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BillingAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.BillingAccount)>`  
  
  
### getBillingAccount(GetBillingAccountRequest request, StreamObserver<BillingAccount> responseObserver)
    
    
    public void getBillingAccount(GetBillingAccountRequest request, StreamObserver<BillingAccount> responseObserver)

Gets information about a billing account. The current authenticated user must be a [viewer of the billing account](https://cloud.google.com/billing/docs/how-to/billing-access).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBillingAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.GetBillingAccountRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BillingAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.BillingAccount)>`  
  
  
### getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public void getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Gets the access control policy for a billing account. The caller must have the `billing.accounts.getIamPolicy` permission on the account, which is often given to billing account [viewers](https://cloud.google.com/billing/docs/how-to/billing-access).

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### getProjectBillingInfo(GetProjectBillingInfoRequest request, StreamObserver<ProjectBillingInfo> responseObserver)
    
    
    public void getProjectBillingInfo(GetProjectBillingInfoRequest request, StreamObserver<ProjectBillingInfo> responseObserver)

Gets the billing information for a project. The current authenticated user must have the `resourcemanager.projects.get` permission for the project, which can be granted by assigning the [Project Viewer](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles) role.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProjectBillingInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.GetProjectBillingInfoRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ProjectBillingInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.ProjectBillingInfo)>`  
  
  
### listBillingAccounts(ListBillingAccountsRequest request, StreamObserver<ListBillingAccountsResponse> responseObserver)
    
    
    public void listBillingAccounts(ListBillingAccountsRequest request, StreamObserver<ListBillingAccountsResponse> responseObserver)

Lists the billing accounts that the current authenticated user has permission to [view](https://cloud.google.com/billing/docs/how-to/billing-access).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBillingAccountsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.ListBillingAccountsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBillingAccountsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.ListBillingAccountsResponse)>`  
  
  
### listProjectBillingInfo(ListProjectBillingInfoRequest request, StreamObserver<ListProjectBillingInfoResponse> responseObserver)
    
    
    public void listProjectBillingInfo(ListProjectBillingInfoRequest request, StreamObserver<ListProjectBillingInfoResponse> responseObserver)

Lists the projects associated with a billing account. The current authenticated user must have the `billing.resourceAssociations.list` IAM permission, which is often given to billing account [viewers](https://cloud.google.com/billing/docs/how-to/billing-access).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProjectBillingInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.ListProjectBillingInfoRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListProjectBillingInfoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.ListProjectBillingInfoResponse)>`  
  
  
### moveBillingAccount(MoveBillingAccountRequest request, StreamObserver<BillingAccount> responseObserver)
    
    
    public void moveBillingAccount(MoveBillingAccountRequest request, StreamObserver<BillingAccount> responseObserver)

Changes which parent organization a billing account belongs to.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveBillingAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.MoveBillingAccountRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BillingAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.BillingAccount)>`  
  
  
### setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public void setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Sets the access control policy for a billing account. Replaces any existing policy. The caller must have the `billing.accounts.setIamPolicy` permission on the account, which is often given to billing account [administrators](https://cloud.google.com/billing/docs/how-to/billing-access).

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)
    
    
    public void testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)

Tests the access control policy for a billing account. This method takes the resource and a set of permissions as input and returns the subset of the input permissions that the caller is allowed for that resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.TestIamPermissionsResponse>`  
  
  
### updateBillingAccount(UpdateBillingAccountRequest request, StreamObserver<BillingAccount> responseObserver)
    
    
    public void updateBillingAccount(UpdateBillingAccountRequest request, StreamObserver<BillingAccount> responseObserver)

Updates a billing account's fields. Currently the only field that can be edited is `display_name`. The current authenticated user must have the `billing.accounts.update` IAM permission, which is typically given to the [administrator](https://cloud.google.com/billing/docs/how-to/billing-access) of the billing account.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBillingAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.UpdateBillingAccountRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BillingAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.BillingAccount)>`  
  
  
### updateProjectBillingInfo(UpdateProjectBillingInfoRequest request, StreamObserver<ProjectBillingInfo> responseObserver)
    
    
    public void updateProjectBillingInfo(UpdateProjectBillingInfoRequest request, StreamObserver<ProjectBillingInfo> responseObserver)

Sets or updates the billing account associated with a project. You specify the new billing account by setting the `billing_account_name` in the `ProjectBillingInfo` resource to the resource name of a billing account. Associating a project with an open billing account enables billing on the project and allows charges for resource usage. If the project already had a billing account, this method changes the billing account used for resource usage charges. _Note:_ Incurred charges that have not yet been reported in the transaction history of the Google Cloud Console might be billed to the new billing account, even if the charge occurred before the new billing account was assigned to the project. The current authenticated user must have ownership privileges for both the [project](https://cloud.google.com/docs/permissions-overview#h.bgs0oxofvnoo) and the [billing account](https://cloud.google.com/billing/docs/how-to/billing-access). You can disable billing on the project by setting the `billing_account_name` field to empty. This action disassociates the current billing account from the project. Any billable activity of your in-use services will stop, and your application could stop functioning as expected. Any unbilled charges to date will be billed to the previously associated account. The current authenticated user must be either an owner of the project or an owner of the billing account for the project. Note that associating a project with a _closed_ billing account will have much the same effect as disabling billing on the project: any paid resources used by the project will be shut down. Thus, unless you wish to disable billing, you should always call this method with the name of an _open_ billing account.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProjectBillingInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.UpdateProjectBillingInfoRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ProjectBillingInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-billing/latest/com.google.cloud.billing.v1.ProjectBillingInfo)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
