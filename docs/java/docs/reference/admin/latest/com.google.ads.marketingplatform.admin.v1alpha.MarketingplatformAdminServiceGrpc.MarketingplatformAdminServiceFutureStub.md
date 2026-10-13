---
url: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub
title: Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:26.578154+00:00
---

# Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub extends AbstractFutureStub<MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service MarketingplatformAdminService.

Service Interface for the Google Marketing Platform Admin API.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAdminAccessBinding(CreateAdminAccessBindingRequest request)
    
    
    public ListenableFuture<AdminAccessBinding> createAdminAccessBinding(CreateAdminAccessBindingRequest request)

Creates an admin access binding in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAdminAccessBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>` |   
  
### createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request)
    
    
    public ListenableFuture<AnalyticsAccountLink> createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request)

Creates the link between the Analytics account and the Google Marketing Platform organization. User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAnalyticsAccountLinkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)>` |   
  
### createUserGroup(CreateUserGroupRequest request)
    
    
    public ListenableFuture<UserGroup> createUserGroup(CreateUserGroupRequest request)

Creates a user group in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>` |   
  
### createUserGroupMember(CreateUserGroupMemberRequest request)
    
    
    public ListenableFuture<UserGroupMember> createUserGroupMember(CreateUserGroupMemberRequest request)

Adds a member to the specified GMP user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupMemberRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>` |   
  
### deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request)
    
    
    public ListenableFuture<Empty> deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request)

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization. User needs to be an org user, and admin on the Analytics account in order to delete the link.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteAnalyticsAccountLinkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUserGroup(DeleteUserGroupRequest request)
    
    
    public ListenableFuture<Empty> deleteUserGroup(DeleteUserGroupRequest request)

Deletes a user group in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUserGroupMember(DeleteUserGroupMemberRequest request)
    
    
    public ListenableFuture<Empty> deleteUserGroupMember(DeleteUserGroupMemberRequest request)

Deletes a member in the specified GMP user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupMemberRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request)
    
    
    public ListenableFuture<FindSalesPartnerManagedClientsResponse> findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request)

Returns a list of clients managed by the sales partner organization. User needs to be an OrgAdmin/BillingAdmin on the sales partner organization in order to view the end clients.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[FindSalesPartnerManagedClientsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsResponse)>` |   
  
### getAdminAccessBinding(GetAdminAccessBindingRequest request)
    
    
    public ListenableFuture<AdminAccessBinding> getAdminAccessBinding(GetAdminAccessBindingRequest request)

Looks up a single admin access binding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetAdminAccessBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>` |   
  
### getOrganization(GetOrganizationRequest request)
    
    
    public ListenableFuture<Organization> getOrganization(GetOrganizationRequest request)

Looks up a single organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetOrganizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Organization](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.Organization)>` |   
  
### getUserGroup(GetUserGroupRequest request)
    
    
    public ListenableFuture<UserGroup> getUserGroup(GetUserGroupRequest request)

Looks up a single user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>` |   
  
### getUserGroupMember(GetUserGroupMemberRequest request)
    
    
    public ListenableFuture<UserGroupMember> getUserGroupMember(GetUserGroupMemberRequest request)

Looks up a single user group member.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupMemberRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>` |   
  
### listAdminAccessBindings(ListAdminAccessBindingsRequest request)
    
    
    public ListenableFuture<ListAdminAccessBindingsResponse> listAdminAccessBindings(ListAdminAccessBindingsRequest request)

Returns a list of admin access bindings in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdminAccessBindingsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAdminAccessBindingsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsResponse)>` |   
  
### listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request)
    
    
    public ListenableFuture<ListAnalyticsAccountLinksResponse> listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request)

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAnalyticsAccountLinksResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksResponse)>` |   
  
### listOrganizations(ListOrganizationsRequest request)
    
    
    public ListenableFuture<ListOrganizationsResponse> listOrganizations(ListOrganizationsRequest request)

Returns a list of organizations that the user has access to.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrganizationsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListOrganizationsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsResponse)>` |   
  
### listUserGroupMembers(ListUserGroupMembersRequest request)
    
    
    public ListenableFuture<ListUserGroupMembersResponse> listUserGroupMembers(ListUserGroupMembersRequest request)

Returns a list of members in the specified user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserGroupMembersRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListUserGroupMembersResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersResponse)>` |   
  
### listUserGroups(ListUserGroupsRequest request)
    
    
    public ListenableFuture<ListUserGroupsResponse> listUserGroups(ListUserGroupsRequest request)

Returns a list of user groups in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserGroupsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListUserGroupsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsResponse)>` |   
  
### reportPropertyUsage(ReportPropertyUsageRequest request)
    
    
    public ListenableFuture<ReportPropertyUsageResponse> reportPropertyUsage(ReportPropertyUsageRequest request)

Gets the usage and billing data for properties within the organization for the specified month. Per direct client org, user needs to be OrgAdmin/BillingAdmin on the organization in order to view the billing and usage data. Per sales partner client org, user needs to be OrgAdmin/BillingAdmin on the sales partner org in order to view the billing and usage data, or OrgAdmin/BillingAdmin on the sales partner client org in order to view the usage data only.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReportPropertyUsageRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ReportPropertyUsageResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse)>` |   
  
### setPropertyServiceLevel(SetPropertyServiceLevelRequest request)
    
    
    public ListenableFuture<SetPropertyServiceLevelResponse> setPropertyServiceLevel(SetPropertyServiceLevelRequest request)

Updates the service level for an Analytics property.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetPropertyServiceLevelRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SetPropertyServiceLevelResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelResponse)>` |   
  
### updateAdminAccessBinding(UpdateAdminAccessBindingRequest request)
    
    
    public ListenableFuture<AdminAccessBinding> updateAdminAccessBinding(UpdateAdminAccessBindingRequest request)

Updates an admin access binding in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateAdminAccessBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>` |   
  
### updateUserGroup(UpdateUserGroupRequest request)
    
    
    public ListenableFuture<UserGroup> updateUserGroup(UpdateUserGroupRequest request)

Updates a user group in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>` |   
  
### updateUserGroupMember(UpdateUserGroupMemberRequest request)
    
    
    public ListenableFuture<UserGroupMember> updateUserGroupMember(UpdateUserGroupMemberRequest request)

Updates a member in the specified GMP user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupMemberRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
