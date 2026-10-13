---
url: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub
title: Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:26.442368+00:00
---

# Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub extends AbstractAsyncStub<MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub>

A stub to allow clients to do asynchronous rpc calls to service MarketingplatformAdminService.

Service Interface for the Google Marketing Platform Admin API.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub

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
    
    
    protected MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAdminAccessBinding(CreateAdminAccessBindingRequest request, StreamObserver<AdminAccessBinding> responseObserver)
    
    
    public void createAdminAccessBinding(CreateAdminAccessBindingRequest request, StreamObserver<AdminAccessBinding> responseObserver)

Creates an admin access binding in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAdminAccessBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>`  
  
  
### createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request, StreamObserver<AnalyticsAccountLink> responseObserver)
    
    
    public void createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request, StreamObserver<AnalyticsAccountLink> responseObserver)

Creates the link between the Analytics account and the Google Marketing Platform organization. User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAnalyticsAccountLinkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)>`  
  
  
### createUserGroup(CreateUserGroupRequest request, StreamObserver<UserGroup> responseObserver)
    
    
    public void createUserGroup(CreateUserGroupRequest request, StreamObserver<UserGroup> responseObserver)

Creates a user group in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>`  
  
  
### createUserGroupMember(CreateUserGroupMemberRequest request, StreamObserver<UserGroupMember> responseObserver)
    
    
    public void createUserGroupMember(CreateUserGroupMemberRequest request, StreamObserver<UserGroupMember> responseObserver)

Adds a member to the specified GMP user group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupMemberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>`  
  
  
### deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request, StreamObserver<Empty> responseObserver)

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization. User needs to be an org user, and admin on the Analytics account in order to delete the link.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteAnalyticsAccountLinkRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteUserGroup(DeleteUserGroupRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteUserGroup(DeleteUserGroupRequest request, StreamObserver<Empty> responseObserver)

Deletes a user group in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteUserGroupMember(DeleteUserGroupMemberRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteUserGroupMember(DeleteUserGroupMemberRequest request, StreamObserver<Empty> responseObserver)

Deletes a member in the specified GMP user group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupMemberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request, StreamObserver<FindSalesPartnerManagedClientsResponse> responseObserver)
    
    
    public void findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request, StreamObserver<FindSalesPartnerManagedClientsResponse> responseObserver)

Returns a list of clients managed by the sales partner organization. User needs to be an OrgAdmin/BillingAdmin on the sales partner organization in order to view the end clients.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FindSalesPartnerManagedClientsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsResponse)>`  
  
  
### getAdminAccessBinding(GetAdminAccessBindingRequest request, StreamObserver<AdminAccessBinding> responseObserver)
    
    
    public void getAdminAccessBinding(GetAdminAccessBindingRequest request, StreamObserver<AdminAccessBinding> responseObserver)

Looks up a single admin access binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetAdminAccessBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>`  
  
  
### getOrganization(GetOrganizationRequest request, StreamObserver<Organization> responseObserver)
    
    
    public void getOrganization(GetOrganizationRequest request, StreamObserver<Organization> responseObserver)

Looks up a single organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetOrganizationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Organization](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.Organization)>`  
  
  
### getUserGroup(GetUserGroupRequest request, StreamObserver<UserGroup> responseObserver)
    
    
    public void getUserGroup(GetUserGroupRequest request, StreamObserver<UserGroup> responseObserver)

Looks up a single user group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>`  
  
  
### getUserGroupMember(GetUserGroupMemberRequest request, StreamObserver<UserGroupMember> responseObserver)
    
    
    public void getUserGroupMember(GetUserGroupMemberRequest request, StreamObserver<UserGroupMember> responseObserver)

Looks up a single user group member.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupMemberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>`  
  
  
### listAdminAccessBindings(ListAdminAccessBindingsRequest request, StreamObserver<ListAdminAccessBindingsResponse> responseObserver)
    
    
    public void listAdminAccessBindings(ListAdminAccessBindingsRequest request, StreamObserver<ListAdminAccessBindingsResponse> responseObserver)

Returns a list of admin access bindings in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAdminAccessBindingsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAdminAccessBindingsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsResponse)>`  
  
  
### listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request, StreamObserver<ListAnalyticsAccountLinksResponse> responseObserver)
    
    
    public void listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request, StreamObserver<ListAnalyticsAccountLinksResponse> responseObserver)

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAnalyticsAccountLinksResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksResponse)>`  
  
  
### listOrganizations(ListOrganizationsRequest request, StreamObserver<ListOrganizationsResponse> responseObserver)
    
    
    public void listOrganizations(ListOrganizationsRequest request, StreamObserver<ListOrganizationsResponse> responseObserver)

Returns a list of organizations that the user has access to.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOrganizationsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListOrganizationsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsResponse)>`  
  
  
### listUserGroupMembers(ListUserGroupMembersRequest request, StreamObserver<ListUserGroupMembersResponse> responseObserver)
    
    
    public void listUserGroupMembers(ListUserGroupMembersRequest request, StreamObserver<ListUserGroupMembersResponse> responseObserver)

Returns a list of members in the specified user group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserGroupMembersRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUserGroupMembersResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersResponse)>`  
  
  
### listUserGroups(ListUserGroupsRequest request, StreamObserver<ListUserGroupsResponse> responseObserver)
    
    
    public void listUserGroups(ListUserGroupsRequest request, StreamObserver<ListUserGroupsResponse> responseObserver)

Returns a list of user groups in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserGroupsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUserGroupsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsResponse)>`  
  
  
### reportPropertyUsage(ReportPropertyUsageRequest request, StreamObserver<ReportPropertyUsageResponse> responseObserver)
    
    
    public void reportPropertyUsage(ReportPropertyUsageRequest request, StreamObserver<ReportPropertyUsageResponse> responseObserver)

Gets the usage and billing data for properties within the organization for the specified month. Per direct client org, user needs to be OrgAdmin/BillingAdmin on the organization in order to view the billing and usage data. Per sales partner client org, user needs to be OrgAdmin/BillingAdmin on the sales partner org in order to view the billing and usage data, or OrgAdmin/BillingAdmin on the sales partner client org in order to view the usage data only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReportPropertyUsageRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReportPropertyUsageResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse)>`  
  
  
### setPropertyServiceLevel(SetPropertyServiceLevelRequest request, StreamObserver<SetPropertyServiceLevelResponse> responseObserver)
    
    
    public void setPropertyServiceLevel(SetPropertyServiceLevelRequest request, StreamObserver<SetPropertyServiceLevelResponse> responseObserver)

Updates the service level for an Analytics property.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetPropertyServiceLevelRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SetPropertyServiceLevelResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelResponse)>`  
  
  
### updateAdminAccessBinding(UpdateAdminAccessBindingRequest request, StreamObserver<AdminAccessBinding> responseObserver)
    
    
    public void updateAdminAccessBinding(UpdateAdminAccessBindingRequest request, StreamObserver<AdminAccessBinding> responseObserver)

Updates an admin access binding in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateAdminAccessBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>`  
  
  
### updateUserGroup(UpdateUserGroupRequest request, StreamObserver<UserGroup> responseObserver)
    
    
    public void updateUserGroup(UpdateUserGroupRequest request, StreamObserver<UserGroup> responseObserver)

Updates a user group in the specified GMP organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>`  
  
  
### updateUserGroupMember(UpdateUserGroupMemberRequest request, StreamObserver<UserGroupMember> responseObserver)
    
    
    public void updateUserGroupMember(UpdateUserGroupMemberRequest request, StreamObserver<UserGroupMember> responseObserver)

Updates a member in the specified GMP user group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupMemberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
