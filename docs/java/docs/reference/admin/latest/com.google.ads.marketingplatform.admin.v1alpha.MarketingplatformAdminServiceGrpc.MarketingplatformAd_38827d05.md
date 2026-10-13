---
url: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub
title: Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:26.020512+00:00
---

# Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub extends AbstractBlockingStub<MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service MarketingplatformAdminService.

Service Interface for the Google Marketing Platform Admin API.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceGrpc.MarketingplatformAdminServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAdminAccessBinding(CreateAdminAccessBindingRequest request)
    
    
    public AdminAccessBinding createAdminAccessBinding(CreateAdminAccessBindingRequest request)

Creates an admin access binding in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAdminAccessBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request)
    
    
    public AnalyticsAccountLink createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request)

Creates the link between the Analytics account and the Google Marketing Platform organization. User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAnalyticsAccountLinkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createUserGroup(CreateUserGroupRequest request)
    
    
    public UserGroup createUserGroup(CreateUserGroupRequest request)

Creates a user group in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createUserGroupMember(CreateUserGroupMemberRequest request)
    
    
    public UserGroupMember createUserGroupMember(CreateUserGroupMemberRequest request)

Adds a member to the specified GMP user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupMemberRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request)
    
    
    public Empty deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request)

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization. User needs to be an org user, and admin on the Analytics account in order to delete the link.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteAnalyticsAccountLinkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteUserGroup(DeleteUserGroupRequest request)
    
    
    public Empty deleteUserGroup(DeleteUserGroupRequest request)

Deletes a user group in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteUserGroupMember(DeleteUserGroupMemberRequest request)
    
    
    public Empty deleteUserGroupMember(DeleteUserGroupMemberRequest request)

Deletes a member in the specified GMP user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupMemberRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request)
    
    
    public FindSalesPartnerManagedClientsResponse findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request)

Returns a list of clients managed by the sales partner organization. User needs to be an OrgAdmin/BillingAdmin on the sales partner organization in order to view the end clients.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FindSalesPartnerManagedClientsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getAdminAccessBinding(GetAdminAccessBindingRequest request)
    
    
    public AdminAccessBinding getAdminAccessBinding(GetAdminAccessBindingRequest request)

Looks up a single admin access binding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetAdminAccessBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getOrganization(GetOrganizationRequest request)
    
    
    public Organization getOrganization(GetOrganizationRequest request)

Looks up a single organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetOrganizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Organization](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.Organization)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getUserGroup(GetUserGroupRequest request)
    
    
    public UserGroup getUserGroup(GetUserGroupRequest request)

Looks up a single user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getUserGroupMember(GetUserGroupMemberRequest request)
    
    
    public UserGroupMember getUserGroupMember(GetUserGroupMemberRequest request)

Looks up a single user group member.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupMemberRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listAdminAccessBindings(ListAdminAccessBindingsRequest request)
    
    
    public ListAdminAccessBindingsResponse listAdminAccessBindings(ListAdminAccessBindingsRequest request)

Returns a list of admin access bindings in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdminAccessBindingsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAdminAccessBindingsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request)
    
    
    public ListAnalyticsAccountLinksResponse listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request)

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAnalyticsAccountLinksResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listOrganizations(ListOrganizationsRequest request)
    
    
    public ListOrganizationsResponse listOrganizations(ListOrganizationsRequest request)

Returns a list of organizations that the user has access to.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrganizationsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListOrganizationsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listUserGroupMembers(ListUserGroupMembersRequest request)
    
    
    public ListUserGroupMembersResponse listUserGroupMembers(ListUserGroupMembersRequest request)

Returns a list of members in the specified user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserGroupMembersRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListUserGroupMembersResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listUserGroups(ListUserGroupsRequest request)
    
    
    public ListUserGroupsResponse listUserGroups(ListUserGroupsRequest request)

Returns a list of user groups in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserGroupsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListUserGroupsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### reportPropertyUsage(ReportPropertyUsageRequest request)
    
    
    public ReportPropertyUsageResponse reportPropertyUsage(ReportPropertyUsageRequest request)

Gets the usage and billing data for properties within the organization for the specified month. Per direct client org, user needs to be OrgAdmin/BillingAdmin on the organization in order to view the billing and usage data. Per sales partner client org, user needs to be OrgAdmin/BillingAdmin on the sales partner org in order to view the billing and usage data, or OrgAdmin/BillingAdmin on the sales partner client org in order to view the usage data only.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReportPropertyUsageRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReportPropertyUsageResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### setPropertyServiceLevel(SetPropertyServiceLevelRequest request)
    
    
    public SetPropertyServiceLevelResponse setPropertyServiceLevel(SetPropertyServiceLevelRequest request)

Updates the service level for an Analytics property.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetPropertyServiceLevelRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SetPropertyServiceLevelResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateAdminAccessBinding(UpdateAdminAccessBindingRequest request)
    
    
    public AdminAccessBinding updateAdminAccessBinding(UpdateAdminAccessBindingRequest request)

Updates an admin access binding in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateAdminAccessBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateUserGroup(UpdateUserGroupRequest request)
    
    
    public UserGroup updateUserGroup(UpdateUserGroupRequest request)

Updates a user group in the specified GMP organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateUserGroupMember(UpdateUserGroupMemberRequest request)
    
    
    public UserGroupMember updateUserGroupMember(UpdateUserGroupMemberRequest request)

Updates a member in the specified GMP user group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupMemberRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
