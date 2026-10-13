---
url: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient
title: Class MarketingplatformAdminServiceClient (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:00.542632+00:00
---

# Class MarketingplatformAdminServiceClient (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MarketingplatformAdminServiceClient (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-marketingplatformadminapi/admin/src/main/java/com/google/ads/marketingplatform/admin/v1alpha/MarketingplatformAdminServiceClient.java)| [Product Reference](https://developers.google.com/analytics/devguides/config/gmp/v1)  
---|---  
  
Service Description: Service Interface for the Google Marketing Platform Admin API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       OrganizationName name = OrganizationName.of("[ORGANIZATION]");
       Organization response = marketingplatformAdminServiceClient.getOrganization(name);
     }
     

Note: close() needs to be called on the MarketingplatformAdminServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetOrganization |  Looks up a single organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getOrganization(GetOrganizationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getOrganization(OrganizationName name) 
  * getOrganization(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getOrganizationCallable() 

  
ListOrganizations |  Returns a list of organizations that the user has access to. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOrganizations(ListOrganizationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOrganizationsPagedCallable() 
  * listOrganizationsCallable() 

  
FindSalesPartnerManagedClients |  Returns a list of clients managed by the sales partner organization.  User needs to be an OrgAdmin/BillingAdmin on the sales partner organization in order to view the end clients. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * findSalesPartnerManagedClientsCallable() 

  
ListAnalyticsAccountLinks |  Lists the Google Analytics accounts link to the specified Google Marketing Platform organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAnalyticsAccountLinks(OrganizationName parent) 
  * listAnalyticsAccountLinks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAnalyticsAccountLinksPagedCallable() 
  * listAnalyticsAccountLinksCallable() 

  
CreateAnalyticsAccountLink |  Creates the link between the Analytics account and the Google Marketing Platform organization.  User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAnalyticsAccountLink(OrganizationName parent, AnalyticsAccountLink analyticsAccountLink) 
  * createAnalyticsAccountLink(String parent, AnalyticsAccountLink analyticsAccountLink) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAnalyticsAccountLinkCallable() 

  
DeleteAnalyticsAccountLink |  Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization.  User needs to be an org user, and admin on the Analytics account in order to delete the link. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteAnalyticsAccountLink(AnalyticsAccountLinkName name) 
  * deleteAnalyticsAccountLink(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAnalyticsAccountLinkCallable() 

  
SetPropertyServiceLevel |  Updates the service level for an Analytics property. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setPropertyServiceLevel(SetPropertyServiceLevelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setPropertyServiceLevel(String analyticsAccountLink) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setPropertyServiceLevelCallable() 

  
ReportPropertyUsage |  Gets the usage and billing data for properties within the organization for the specified month.  Per direct client org, user needs to be OrgAdmin/BillingAdmin on the organization in order to view the billing and usage data.  Per sales partner client org, user needs to be OrgAdmin/BillingAdmin on the sales partner org in order to view the billing and usage data, or OrgAdmin/BillingAdmin on the sales partner client org in order to view the usage data only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * reportPropertyUsage(ReportPropertyUsageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * reportPropertyUsage(String organization) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * reportPropertyUsageCallable() 

  
GetUserGroup |  Looks up a single user group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUserGroup(GetUserGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUserGroup(UserGroupName name) 
  * getUserGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUserGroupCallable() 

  
ListUserGroups |  Returns a list of user groups in the specified GMP organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUserGroups(ListUserGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUserGroups(OrganizationName parent) 
  * listUserGroups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUserGroupsPagedCallable() 
  * listUserGroupsCallable() 

  
CreateUserGroup |  Creates a user group in the specified GMP organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUserGroup(CreateUserGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUserGroup(OrganizationName parent, UserGroup userGroup) 
  * createUserGroup(String parent, UserGroup userGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUserGroupCallable() 

  
UpdateUserGroup |  Updates a user group in the specified GMP organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUserGroup(UpdateUserGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUserGroup(UserGroup userGroup, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUserGroupCallable() 

  
DeleteUserGroup |  Deletes a user group in the specified GMP organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUserGroup(DeleteUserGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUserGroup(UserGroupName name) 
  * deleteUserGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUserGroupCallable() 

  
GetUserGroupMember |  Looks up a single user group member. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUserGroupMember(GetUserGroupMemberRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUserGroupMember(UserGroupMemberName name) 
  * getUserGroupMember(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUserGroupMemberCallable() 

  
ListUserGroupMembers |  Returns a list of members in the specified user group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUserGroupMembers(ListUserGroupMembersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUserGroupMembers(UserGroupName parent) 
  * listUserGroupMembers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUserGroupMembersPagedCallable() 
  * listUserGroupMembersCallable() 

  
CreateUserGroupMember |  Adds a member to the specified GMP user group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUserGroupMember(CreateUserGroupMemberRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUserGroupMember(UserGroupName parent, UserGroupMember userGroupMember) 
  * createUserGroupMember(String parent, UserGroupMember userGroupMember) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUserGroupMemberCallable() 

  
UpdateUserGroupMember |  Updates a member in the specified GMP user group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUserGroupMember(UpdateUserGroupMemberRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateUserGroupMember(UserGroupMember userGroupMember, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUserGroupMemberCallable() 

  
DeleteUserGroupMember |  Deletes a member in the specified GMP user group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUserGroupMember(DeleteUserGroupMemberRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUserGroupMember(UserGroupMemberName name) 
  * deleteUserGroupMember(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUserGroupMemberCallable() 

  
GetAdminAccessBinding |  Looks up a single admin access binding. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAdminAccessBinding(GetAdminAccessBindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAdminAccessBinding(AdminAccessBindingName name) 
  * getAdminAccessBinding(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAdminAccessBindingCallable() 

  
ListAdminAccessBindings |  Returns a list of admin access bindings in the specified GMP organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAdminAccessBindings(ListAdminAccessBindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAdminAccessBindings(OrganizationName parent) 
  * listAdminAccessBindings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAdminAccessBindingsPagedCallable() 
  * listAdminAccessBindingsCallable() 

  
CreateAdminAccessBinding |  Creates an admin access binding in the specified GMP organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAdminAccessBinding(CreateAdminAccessBindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAdminAccessBinding(OrganizationName parent, AdminAccessBinding adminAccessBinding) 
  * createAdminAccessBinding(String parent, AdminAccessBinding adminAccessBinding) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAdminAccessBindingCallable() 

  
UpdateAdminAccessBinding |  Updates an admin access binding in the specified GMP organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAdminAccessBinding(UpdateAdminAccessBindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAdminAccessBinding(AdminAccessBinding adminAccessBinding, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAdminAccessBindingCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MarketingplatformAdminServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MarketingplatformAdminServiceSettings marketingplatformAdminServiceSettings =
         MarketingplatformAdminServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create(marketingplatformAdminServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MarketingplatformAdminServiceSettings marketingplatformAdminServiceSettings =
         MarketingplatformAdminServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create(marketingplatformAdminServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MarketingplatformAdminServiceSettings marketingplatformAdminServiceSettings =
         MarketingplatformAdminServiceSettings.newHttpJsonBuilder().build();
     MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create(marketingplatformAdminServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MarketingplatformAdminServiceClient

## Static Methods 

### create()
    
    
    public static final MarketingplatformAdminServiceClient create()

Constructs an instance of MarketingplatformAdminServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MarketingplatformAdminServiceSettings settings)
    
    
    public static final MarketingplatformAdminServiceClient create(MarketingplatformAdminServiceSettings settings)

Constructs an instance of MarketingplatformAdminServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MarketingplatformAdminServiceSettings](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MarketingplatformAdminServiceStub stub)
    
    
    public static final MarketingplatformAdminServiceClient create(MarketingplatformAdminServiceStub stub)

Constructs an instance of MarketingplatformAdminServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(MarketingplatformAdminServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MarketingplatformAdminServiceStub](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.stub.MarketingplatformAdminServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient)` |   
  
## Constructors 

### MarketingplatformAdminServiceClient(MarketingplatformAdminServiceSettings settings)
    
    
    protected MarketingplatformAdminServiceClient(MarketingplatformAdminServiceSettings settings)

Constructs an instance of MarketingplatformAdminServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MarketingplatformAdminServiceSettings](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceSettings)`  
  
  
### MarketingplatformAdminServiceClient(MarketingplatformAdminServiceStub stub)
    
    
    protected MarketingplatformAdminServiceClient(MarketingplatformAdminServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MarketingplatformAdminServiceStub](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.stub.MarketingplatformAdminServiceStub)`  
  
  
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

### createAdminAccessBinding(@Nullable OrganizationName parent, AdminAccessBinding adminAccessBinding)
    
    
    public final AdminAccessBinding createAdminAccessBinding(@Nullable OrganizationName parent, AdminAccessBinding adminAccessBinding)

Creates an admin access binding in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       AdminAccessBinding adminAccessBinding = AdminAccessBinding.newBuilder().build();
       AdminAccessBinding response =
           marketingplatformAdminServiceClient.createAdminAccessBinding(parent, adminAccessBinding);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.OrganizationName`  
Required. The parent organization, which owns this Admin Access Binding. Format: organizations/{org_id}  
`adminAccessBinding` | `[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)`  
Required. The Admin Access Binding to create. Only 'user_email' input is allowed.  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
  
### createAdminAccessBinding(CreateAdminAccessBindingRequest request)
    
    
    public final AdminAccessBinding createAdminAccessBinding(CreateAdminAccessBindingRequest request)

Creates an admin access binding in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       CreateAdminAccessBindingRequest request =
           CreateAdminAccessBindingRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setAdminAccessBinding(AdminAccessBinding.newBuilder().build())
               .build();
       AdminAccessBinding response =
           marketingplatformAdminServiceClient.createAdminAccessBinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAdminAccessBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
  
### createAdminAccessBinding(String parent, AdminAccessBinding adminAccessBinding)
    
    
    public final AdminAccessBinding createAdminAccessBinding(String parent, AdminAccessBinding adminAccessBinding)

Creates an admin access binding in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       AdminAccessBinding adminAccessBinding = AdminAccessBinding.newBuilder().build();
       AdminAccessBinding response =
           marketingplatformAdminServiceClient.createAdminAccessBinding(parent, adminAccessBinding);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent organization, which owns this Admin Access Binding. Format: organizations/{org_id}  
`adminAccessBinding` | `[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)`  
Required. The Admin Access Binding to create. Only 'user_email' input is allowed.  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
  
### createAdminAccessBindingCallable()
    
    
    public final UnaryCallable<CreateAdminAccessBindingRequest,AdminAccessBinding> createAdminAccessBindingCallable()

Creates an admin access binding in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       CreateAdminAccessBindingRequest request =
           CreateAdminAccessBindingRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setAdminAccessBinding(AdminAccessBinding.newBuilder().build())
               .build();
       ApiFuture<AdminAccessBinding> future =
           marketingplatformAdminServiceClient
               .createAdminAccessBindingCallable()
               .futureCall(request);
       // Do something.
       AdminAccessBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAdminAccessBindingRequest),[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>` |   
  
### createAnalyticsAccountLink(@Nullable OrganizationName parent, AnalyticsAccountLink analyticsAccountLink)
    
    
    public final AnalyticsAccountLink createAnalyticsAccountLink(@Nullable OrganizationName parent, AnalyticsAccountLink analyticsAccountLink)

Creates the link between the Analytics account and the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       AnalyticsAccountLink analyticsAccountLink = AnalyticsAccountLink.newBuilder().build();
       AnalyticsAccountLink response =
           marketingplatformAdminServiceClient.createAnalyticsAccountLink(
               parent, analyticsAccountLink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.OrganizationName`  
Required. The parent resource where this Analytics account link will be created. Format: organizations/{org_id}  
`analyticsAccountLink` | `[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)`  
Required. The Analytics account link to create.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)` |   
  
### createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request)
    
    
    public final AnalyticsAccountLink createAnalyticsAccountLink(CreateAnalyticsAccountLinkRequest request)

Creates the link between the Analytics account and the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       CreateAnalyticsAccountLinkRequest request =
           CreateAnalyticsAccountLinkRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setAnalyticsAccountLink(AnalyticsAccountLink.newBuilder().build())
               .build();
       AnalyticsAccountLink response =
           marketingplatformAdminServiceClient.createAnalyticsAccountLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAnalyticsAccountLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)` |   
  
### createAnalyticsAccountLink(String parent, AnalyticsAccountLink analyticsAccountLink)
    
    
    public final AnalyticsAccountLink createAnalyticsAccountLink(String parent, AnalyticsAccountLink analyticsAccountLink)

Creates the link between the Analytics account and the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       AnalyticsAccountLink analyticsAccountLink = AnalyticsAccountLink.newBuilder().build();
       AnalyticsAccountLink response =
           marketingplatformAdminServiceClient.createAnalyticsAccountLink(
               parent, analyticsAccountLink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this Analytics account link will be created. Format: organizations/{org_id}  
`analyticsAccountLink` | `[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)`  
Required. The Analytics account link to create.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)` |   
  
### createAnalyticsAccountLinkCallable()
    
    
    public final UnaryCallable<CreateAnalyticsAccountLinkRequest,AnalyticsAccountLink> createAnalyticsAccountLinkCallable()

Creates the link between the Analytics account and the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account to create the link. If the account is already linked to an organization, user needs to unlink the account from the current organization, then try link again.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       CreateAnalyticsAccountLinkRequest request =
           CreateAnalyticsAccountLinkRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setAnalyticsAccountLink(AnalyticsAccountLink.newBuilder().build())
               .build();
       ApiFuture<AnalyticsAccountLink> future =
           marketingplatformAdminServiceClient
               .createAnalyticsAccountLinkCallable()
               .futureCall(request);
       // Do something.
       AnalyticsAccountLink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateAnalyticsAccountLinkRequest),[AnalyticsAccountLink](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLink)>` |   
  
### createUserGroup(@Nullable OrganizationName parent, UserGroup userGroup)
    
    
    public final UserGroup createUserGroup(@Nullable OrganizationName parent, UserGroup userGroup)

Creates a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       UserGroup userGroup = UserGroup.newBuilder().build();
       UserGroup response = marketingplatformAdminServiceClient.createUserGroup(parent, userGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.OrganizationName`  
Required. The parent resource where this UserGroup will be created. Format: organizations/{org_id}  
`userGroup` | `[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)`  
Required. The user group to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
  
### createUserGroup(CreateUserGroupRequest request)
    
    
    public final UserGroup createUserGroup(CreateUserGroupRequest request)

Creates a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       CreateUserGroupRequest request =
           CreateUserGroupRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setUserGroup(UserGroup.newBuilder().build())
               .build();
       UserGroup response = marketingplatformAdminServiceClient.createUserGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
  
### createUserGroup(String parent, UserGroup userGroup)
    
    
    public final UserGroup createUserGroup(String parent, UserGroup userGroup)

Creates a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       UserGroup userGroup = UserGroup.newBuilder().build();
       UserGroup response = marketingplatformAdminServiceClient.createUserGroup(parent, userGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this UserGroup will be created. Format: organizations/{org_id}  
`userGroup` | `[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)`  
Required. The user group to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
  
### createUserGroupCallable()
    
    
    public final UnaryCallable<CreateUserGroupRequest,UserGroup> createUserGroupCallable()

Creates a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       CreateUserGroupRequest request =
           CreateUserGroupRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setUserGroup(UserGroup.newBuilder().build())
               .build();
       ApiFuture<UserGroup> future =
           marketingplatformAdminServiceClient.createUserGroupCallable().futureCall(request);
       // Do something.
       UserGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupRequest),[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>` |   
  
### createUserGroupMember(@Nullable UserGroupName parent, UserGroupMember userGroupMember)
    
    
    public final UserGroupMember createUserGroupMember(@Nullable UserGroupName parent, UserGroupMember userGroupMember)

Adds a member to the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UserGroupName parent = UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]");
       UserGroupMember userGroupMember = UserGroupMember.newBuilder().build();
       UserGroupMember response =
           marketingplatformAdminServiceClient.createUserGroupMember(parent, userGroupMember);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.UserGroupName`  
Required. The parent resource where this UserGroupMember will be created. Format: organizations/{org_id}/userGroups/{user_group_id}  
`userGroupMember` | `[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)`  
Required. The user group member to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
  
### createUserGroupMember(CreateUserGroupMemberRequest request)
    
    
    public final UserGroupMember createUserGroupMember(CreateUserGroupMemberRequest request)

Adds a member to the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       CreateUserGroupMemberRequest request =
           CreateUserGroupMemberRequest.newBuilder()
               .setParent(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .setUserGroupMember(UserGroupMember.newBuilder().build())
               .build();
       UserGroupMember response = marketingplatformAdminServiceClient.createUserGroupMember(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupMemberRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
  
### createUserGroupMember(String parent, UserGroupMember userGroupMember)
    
    
    public final UserGroupMember createUserGroupMember(String parent, UserGroupMember userGroupMember)

Adds a member to the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String parent = UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString();
       UserGroupMember userGroupMember = UserGroupMember.newBuilder().build();
       UserGroupMember response =
           marketingplatformAdminServiceClient.createUserGroupMember(parent, userGroupMember);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this UserGroupMember will be created. Format: organizations/{org_id}/userGroups/{user_group_id}  
`userGroupMember` | `[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)`  
Required. The user group member to create.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
  
### createUserGroupMemberCallable()
    
    
    public final UnaryCallable<CreateUserGroupMemberRequest,UserGroupMember> createUserGroupMemberCallable()

Adds a member to the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       CreateUserGroupMemberRequest request =
           CreateUserGroupMemberRequest.newBuilder()
               .setParent(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .setUserGroupMember(UserGroupMember.newBuilder().build())
               .build();
       ApiFuture<UserGroupMember> future =
           marketingplatformAdminServiceClient.createUserGroupMemberCallable().futureCall(request);
       // Do something.
       UserGroupMember response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.CreateUserGroupMemberRequest),[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>` |   
  
### deleteAnalyticsAccountLink(@Nullable AnalyticsAccountLinkName name)
    
    
    public final void deleteAnalyticsAccountLink(@Nullable AnalyticsAccountLinkName name)

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account in order to delete the link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       AnalyticsAccountLinkName name =
           AnalyticsAccountLinkName.of("[ORGANIZATION]", "[ANALYTICS_ACCOUNT_LINK]");
       marketingplatformAdminServiceClient.deleteAnalyticsAccountLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.AnalyticsAccountLinkName`  
Required. The name of the Analytics account link to delete. Format: organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}  
  
### deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request)
    
    
    public final void deleteAnalyticsAccountLink(DeleteAnalyticsAccountLinkRequest request)

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account in order to delete the link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       DeleteAnalyticsAccountLinkRequest request =
           DeleteAnalyticsAccountLinkRequest.newBuilder()
               .setName(
                   AnalyticsAccountLinkName.of("[ORGANIZATION]", "[ANALYTICS_ACCOUNT_LINK]")
                       .toString())
               .build();
       marketingplatformAdminServiceClient.deleteAnalyticsAccountLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteAnalyticsAccountLinkRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteAnalyticsAccountLink(String name)
    
    
    public final void deleteAnalyticsAccountLink(String name)

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account in order to delete the link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String name =
           AnalyticsAccountLinkName.of("[ORGANIZATION]", "[ANALYTICS_ACCOUNT_LINK]").toString();
       marketingplatformAdminServiceClient.deleteAnalyticsAccountLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Analytics account link to delete. Format: organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}  
  
### deleteAnalyticsAccountLinkCallable()
    
    
    public final UnaryCallable<DeleteAnalyticsAccountLinkRequest,Empty> deleteAnalyticsAccountLinkCallable()

Deletes the AnalyticsAccountLink, which detaches the Analytics account from the Google Marketing Platform organization.

User needs to be an org user, and admin on the Analytics account in order to delete the link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       DeleteAnalyticsAccountLinkRequest request =
           DeleteAnalyticsAccountLinkRequest.newBuilder()
               .setName(
                   AnalyticsAccountLinkName.of("[ORGANIZATION]", "[ANALYTICS_ACCOUNT_LINK]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           marketingplatformAdminServiceClient
               .deleteAnalyticsAccountLinkCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAnalyticsAccountLinkRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteAnalyticsAccountLinkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUserGroup(@Nullable UserGroupName name)
    
    
    public final void deleteUserGroup(@Nullable UserGroupName name)

Deletes a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UserGroupName name = UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]");
       marketingplatformAdminServiceClient.deleteUserGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.UserGroupName`  
Required. The name of the user group to delete. Format: organizations/{org_id}/userGroups/{user_group_id}  
  
### deleteUserGroup(DeleteUserGroupRequest request)
    
    
    public final void deleteUserGroup(DeleteUserGroupRequest request)

Deletes a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       DeleteUserGroupRequest request =
           DeleteUserGroupRequest.newBuilder()
               .setName(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .build();
       marketingplatformAdminServiceClient.deleteUserGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUserGroup(String name)
    
    
    public final void deleteUserGroup(String name)

Deletes a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String name = UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString();
       marketingplatformAdminServiceClient.deleteUserGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the user group to delete. Format: organizations/{org_id}/userGroups/{user_group_id}  
  
### deleteUserGroupCallable()
    
    
    public final UnaryCallable<DeleteUserGroupRequest,Empty> deleteUserGroupCallable()

Deletes a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       DeleteUserGroupRequest request =
           DeleteUserGroupRequest.newBuilder()
               .setName(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .build();
       ApiFuture<Empty> future =
           marketingplatformAdminServiceClient.deleteUserGroupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUserGroupMember(@Nullable UserGroupMemberName name)
    
    
    public final void deleteUserGroupMember(@Nullable UserGroupMemberName name)

Deletes a member in the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UserGroupMemberName name =
           UserGroupMemberName.of("[ORGANIZATION]", "[USER_GROUP]", "[MEMBER]");
       marketingplatformAdminServiceClient.deleteUserGroupMember(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.UserGroupMemberName`  
Required. The name of the user group member to delete. Format: organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}  
  
### deleteUserGroupMember(DeleteUserGroupMemberRequest request)
    
    
    public final void deleteUserGroupMember(DeleteUserGroupMemberRequest request)

Deletes a member in the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       DeleteUserGroupMemberRequest request =
           DeleteUserGroupMemberRequest.newBuilder()
               .setName(
                   UserGroupMemberName.of("[ORGANIZATION]", "[USER_GROUP]", "[MEMBER]").toString())
               .build();
       marketingplatformAdminServiceClient.deleteUserGroupMember(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupMemberRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUserGroupMember(String name)
    
    
    public final void deleteUserGroupMember(String name)

Deletes a member in the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String name = UserGroupMemberName.of("[ORGANIZATION]", "[USER_GROUP]", "[MEMBER]").toString();
       marketingplatformAdminServiceClient.deleteUserGroupMember(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the user group member to delete. Format: organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}  
  
### deleteUserGroupMemberCallable()
    
    
    public final UnaryCallable<DeleteUserGroupMemberRequest,Empty> deleteUserGroupMemberCallable()

Deletes a member in the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       DeleteUserGroupMemberRequest request =
           DeleteUserGroupMemberRequest.newBuilder()
               .setName(
                   UserGroupMemberName.of("[ORGANIZATION]", "[USER_GROUP]", "[MEMBER]").toString())
               .build();
       ApiFuture<Empty> future =
           marketingplatformAdminServiceClient.deleteUserGroupMemberCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.DeleteUserGroupMemberRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request)
    
    
    public final FindSalesPartnerManagedClientsResponse findSalesPartnerManagedClients(FindSalesPartnerManagedClientsRequest request)

Returns a list of clients managed by the sales partner organization.

User needs to be an OrgAdmin/BillingAdmin on the sales partner organization in order to view the end clients.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       FindSalesPartnerManagedClientsRequest request =
           FindSalesPartnerManagedClientsRequest.newBuilder()
               .setOrganization(OrganizationName.of("[ORGANIZATION]").toString())
               .setIsActive(true)
               .build();
       FindSalesPartnerManagedClientsResponse response =
           marketingplatformAdminServiceClient.findSalesPartnerManagedClients(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FindSalesPartnerManagedClientsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsResponse)` |   
  
### findSalesPartnerManagedClientsCallable()
    
    
    public final UnaryCallable<FindSalesPartnerManagedClientsRequest,FindSalesPartnerManagedClientsResponse> findSalesPartnerManagedClientsCallable()

Returns a list of clients managed by the sales partner organization.

User needs to be an OrgAdmin/BillingAdmin on the sales partner organization in order to view the end clients.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       FindSalesPartnerManagedClientsRequest request =
           FindSalesPartnerManagedClientsRequest.newBuilder()
               .setOrganization(OrganizationName.of("[ORGANIZATION]").toString())
               .setIsActive(true)
               .build();
       ApiFuture<FindSalesPartnerManagedClientsResponse> future =
           marketingplatformAdminServiceClient
               .findSalesPartnerManagedClientsCallable()
               .futureCall(request);
       // Do something.
       FindSalesPartnerManagedClientsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FindSalesPartnerManagedClientsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsRequest),[FindSalesPartnerManagedClientsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.FindSalesPartnerManagedClientsResponse)>` |   
  
### getAdminAccessBinding(@Nullable AdminAccessBindingName name)
    
    
    public final AdminAccessBinding getAdminAccessBinding(@Nullable AdminAccessBindingName name)

Looks up a single admin access binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       AdminAccessBindingName name =
           AdminAccessBindingName.of("[ORGANIZATION]", "[ADMIN_ACCESS_BINDING]");
       AdminAccessBinding response = marketingplatformAdminServiceClient.getAdminAccessBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBindingName`  
Required. The name of the AdminAccessBinding to retrieve. Format: organizations/{org_id}/adminAccessBindings/{admin_access_binding_id}  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
  
### getAdminAccessBinding(GetAdminAccessBindingRequest request)
    
    
    public final AdminAccessBinding getAdminAccessBinding(GetAdminAccessBindingRequest request)

Looks up a single admin access binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       GetAdminAccessBindingRequest request =
           GetAdminAccessBindingRequest.newBuilder()
               .setName(
                   AdminAccessBindingName.of("[ORGANIZATION]", "[ADMIN_ACCESS_BINDING]").toString())
               .build();
       AdminAccessBinding response =
           marketingplatformAdminServiceClient.getAdminAccessBinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetAdminAccessBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
  
### getAdminAccessBinding(String name)
    
    
    public final AdminAccessBinding getAdminAccessBinding(String name)

Looks up a single admin access binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String name =
           AdminAccessBindingName.of("[ORGANIZATION]", "[ADMIN_ACCESS_BINDING]").toString();
       AdminAccessBinding response = marketingplatformAdminServiceClient.getAdminAccessBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the AdminAccessBinding to retrieve. Format: organizations/{org_id}/adminAccessBindings/{admin_access_binding_id}  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
  
### getAdminAccessBindingCallable()
    
    
    public final UnaryCallable<GetAdminAccessBindingRequest,AdminAccessBinding> getAdminAccessBindingCallable()

Looks up a single admin access binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       GetAdminAccessBindingRequest request =
           GetAdminAccessBindingRequest.newBuilder()
               .setName(
                   AdminAccessBindingName.of("[ORGANIZATION]", "[ADMIN_ACCESS_BINDING]").toString())
               .build();
       ApiFuture<AdminAccessBinding> future =
           marketingplatformAdminServiceClient.getAdminAccessBindingCallable().futureCall(request);
       // Do something.
       AdminAccessBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetAdminAccessBindingRequest),[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>` |   
  
### getOrganization(@Nullable OrganizationName name)
    
    
    public final Organization getOrganization(@Nullable OrganizationName name)

Looks up a single organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       OrganizationName name = OrganizationName.of("[ORGANIZATION]");
       Organization response = marketingplatformAdminServiceClient.getOrganization(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.OrganizationName`  
Required. The name of the Organization to retrieve. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[Organization](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.Organization)` |   
  
### getOrganization(GetOrganizationRequest request)
    
    
    public final Organization getOrganization(GetOrganizationRequest request)

Looks up a single organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       GetOrganizationRequest request =
           GetOrganizationRequest.newBuilder()
               .setName(OrganizationName.of("[ORGANIZATION]").toString())
               .build();
       Organization response = marketingplatformAdminServiceClient.getOrganization(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetOrganizationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Organization](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.Organization)` |   
  
### getOrganization(String name)
    
    
    public final Organization getOrganization(String name)

Looks up a single organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String name = OrganizationName.of("[ORGANIZATION]").toString();
       Organization response = marketingplatformAdminServiceClient.getOrganization(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Organization to retrieve. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[Organization](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.Organization)` |   
  
### getOrganizationCallable()
    
    
    public final UnaryCallable<GetOrganizationRequest,Organization> getOrganizationCallable()

Looks up a single organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       GetOrganizationRequest request =
           GetOrganizationRequest.newBuilder()
               .setName(OrganizationName.of("[ORGANIZATION]").toString())
               .build();
       ApiFuture<Organization> future =
           marketingplatformAdminServiceClient.getOrganizationCallable().futureCall(request);
       // Do something.
       Organization response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOrganizationRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetOrganizationRequest),[Organization](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.Organization)>` |   
  
### getSettings()
    
    
    public final @Nullable MarketingplatformAdminServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceSettings` |   
  
### getStub()
    
    
    public MarketingplatformAdminServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceStub](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.stub.MarketingplatformAdminServiceStub)` |   
  
### getUserGroup(@Nullable UserGroupName name)
    
    
    public final UserGroup getUserGroup(@Nullable UserGroupName name)

Looks up a single user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UserGroupName name = UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]");
       UserGroup response = marketingplatformAdminServiceClient.getUserGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.UserGroupName`  
Required. The name of the UserGroup to retrieve. Format: organizations/{org_id}/userGroups/{user_group_id}  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
  
### getUserGroup(GetUserGroupRequest request)
    
    
    public final UserGroup getUserGroup(GetUserGroupRequest request)

Looks up a single user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       GetUserGroupRequest request =
           GetUserGroupRequest.newBuilder()
               .setName(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .build();
       UserGroup response = marketingplatformAdminServiceClient.getUserGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
  
### getUserGroup(String name)
    
    
    public final UserGroup getUserGroup(String name)

Looks up a single user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String name = UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString();
       UserGroup response = marketingplatformAdminServiceClient.getUserGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the UserGroup to retrieve. Format: organizations/{org_id}/userGroups/{user_group_id}  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
  
### getUserGroupCallable()
    
    
    public final UnaryCallable<GetUserGroupRequest,UserGroup> getUserGroupCallable()

Looks up a single user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       GetUserGroupRequest request =
           GetUserGroupRequest.newBuilder()
               .setName(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .build();
       ApiFuture<UserGroup> future =
           marketingplatformAdminServiceClient.getUserGroupCallable().futureCall(request);
       // Do something.
       UserGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupRequest),[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>` |   
  
### getUserGroupMember(@Nullable UserGroupMemberName name)
    
    
    public final UserGroupMember getUserGroupMember(@Nullable UserGroupMemberName name)

Looks up a single user group member.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UserGroupMemberName name =
           UserGroupMemberName.of("[ORGANIZATION]", "[USER_GROUP]", "[MEMBER]");
       UserGroupMember response = marketingplatformAdminServiceClient.getUserGroupMember(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.UserGroupMemberName`  
Required. The name of the user group member to retrieve. Format: organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
  
### getUserGroupMember(GetUserGroupMemberRequest request)
    
    
    public final UserGroupMember getUserGroupMember(GetUserGroupMemberRequest request)

Looks up a single user group member.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       GetUserGroupMemberRequest request =
           GetUserGroupMemberRequest.newBuilder()
               .setName(
                   UserGroupMemberName.of("[ORGANIZATION]", "[USER_GROUP]", "[MEMBER]").toString())
               .build();
       UserGroupMember response = marketingplatformAdminServiceClient.getUserGroupMember(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupMemberRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
  
### getUserGroupMember(String name)
    
    
    public final UserGroupMember getUserGroupMember(String name)

Looks up a single user group member.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String name = UserGroupMemberName.of("[ORGANIZATION]", "[USER_GROUP]", "[MEMBER]").toString();
       UserGroupMember response = marketingplatformAdminServiceClient.getUserGroupMember(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the user group member to retrieve. Format: organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
  
### getUserGroupMemberCallable()
    
    
    public final UnaryCallable<GetUserGroupMemberRequest,UserGroupMember> getUserGroupMemberCallable()

Looks up a single user group member.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       GetUserGroupMemberRequest request =
           GetUserGroupMemberRequest.newBuilder()
               .setName(
                   UserGroupMemberName.of("[ORGANIZATION]", "[USER_GROUP]", "[MEMBER]").toString())
               .build();
       ApiFuture<UserGroupMember> future =
           marketingplatformAdminServiceClient.getUserGroupMemberCallable().futureCall(request);
       // Do something.
       UserGroupMember response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.GetUserGroupMemberRequest),[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>` |   
  
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
  
### listAdminAccessBindings(@Nullable OrganizationName parent)
    
    
    public final MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse listAdminAccessBindings(@Nullable OrganizationName parent)

Returns a list of admin access bindings in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (AdminAccessBinding element :
           marketingplatformAdminServiceClient.listAdminAccessBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.OrganizationName`  
Required. The parent organization, which owns this collection of Admin Access Bindings. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse)` |   
  
### listAdminAccessBindings(ListAdminAccessBindingsRequest request)
    
    
    public final MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse listAdminAccessBindings(ListAdminAccessBindingsRequest request)

Returns a list of admin access bindings in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListAdminAccessBindingsRequest request =
           ListAdminAccessBindingsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (AdminAccessBinding element :
           marketingplatformAdminServiceClient.listAdminAccessBindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdminAccessBindingsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse)` |   
  
### listAdminAccessBindings(String parent)
    
    
    public final MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse listAdminAccessBindings(String parent)

Returns a list of admin access bindings in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       for (AdminAccessBinding element :
           marketingplatformAdminServiceClient.listAdminAccessBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent organization, which owns this collection of Admin Access Bindings. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse)` |   
  
### listAdminAccessBindingsCallable()
    
    
    public final UnaryCallable<ListAdminAccessBindingsRequest,ListAdminAccessBindingsResponse> listAdminAccessBindingsCallable()

Returns a list of admin access bindings in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListAdminAccessBindingsRequest request =
           ListAdminAccessBindingsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListAdminAccessBindingsResponse response =
             marketingplatformAdminServiceClient.listAdminAccessBindingsCallable().call(request);
         for (AdminAccessBinding element : response.getAdminAccessBindingsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdminAccessBindingsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsRequest),[ListAdminAccessBindingsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsResponse)>` |   
  
### listAdminAccessBindingsPagedCallable()
    
    
    public final UnaryCallable<ListAdminAccessBindingsRequest,MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse> listAdminAccessBindingsPagedCallable()

Returns a list of admin access bindings in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListAdminAccessBindingsRequest request =
           ListAdminAccessBindingsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<AdminAccessBinding> future =
           marketingplatformAdminServiceClient
               .listAdminAccessBindingsPagedCallable()
               .futureCall(request);
       // Do something.
       for (AdminAccessBinding element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdminAccessBindingsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAdminAccessBindingsRequest),[ListAdminAccessBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListAdminAccessBindingsPagedResponse)>` |   
  
### listAnalyticsAccountLinks(@Nullable OrganizationName parent)
    
    
    public final MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse listAnalyticsAccountLinks(@Nullable OrganizationName parent)

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (AnalyticsAccountLink element :
           marketingplatformAdminServiceClient.listAnalyticsAccountLinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.OrganizationName`  
Required. The parent organization, which owns this collection of Analytics account links. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse)` |   
  
### listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request)
    
    
    public final MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse listAnalyticsAccountLinks(ListAnalyticsAccountLinksRequest request)

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListAnalyticsAccountLinksRequest request =
           ListAnalyticsAccountLinksRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (AnalyticsAccountLink element :
           marketingplatformAdminServiceClient.listAnalyticsAccountLinks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse)` |   
  
### listAnalyticsAccountLinks(String parent)
    
    
    public final MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse listAnalyticsAccountLinks(String parent)

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       for (AnalyticsAccountLink element :
           marketingplatformAdminServiceClient.listAnalyticsAccountLinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent organization, which owns this collection of Analytics account links. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse)` |   
  
### listAnalyticsAccountLinksCallable()
    
    
    public final UnaryCallable<ListAnalyticsAccountLinksRequest,ListAnalyticsAccountLinksResponse> listAnalyticsAccountLinksCallable()

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListAnalyticsAccountLinksRequest request =
           ListAnalyticsAccountLinksRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListAnalyticsAccountLinksResponse response =
             marketingplatformAdminServiceClient.listAnalyticsAccountLinksCallable().call(request);
         for (AnalyticsAccountLink element : response.getAnalyticsAccountLinksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksRequest),[ListAnalyticsAccountLinksResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksResponse)>` |   
  
### listAnalyticsAccountLinksPagedCallable()
    
    
    public final UnaryCallable<ListAnalyticsAccountLinksRequest,MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse> listAnalyticsAccountLinksPagedCallable()

Lists the Google Analytics accounts link to the specified Google Marketing Platform organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListAnalyticsAccountLinksRequest request =
           ListAnalyticsAccountLinksRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<AnalyticsAccountLink> future =
           marketingplatformAdminServiceClient
               .listAnalyticsAccountLinksPagedCallable()
               .futureCall(request);
       // Do something.
       for (AnalyticsAccountLink element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAnalyticsAccountLinksRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListAnalyticsAccountLinksRequest),[ListAnalyticsAccountLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListAnalyticsAccountLinksPagedResponse)>` |   
  
### listOrganizations(ListOrganizationsRequest request)
    
    
    public final MarketingplatformAdminServiceClient.ListOrganizationsPagedResponse listOrganizations(ListOrganizationsRequest request)

Returns a list of organizations that the user has access to.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListOrganizationsRequest request =
           ListOrganizationsRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Organization element :
           marketingplatformAdminServiceClient.listOrganizations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrganizationsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListOrganizationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListOrganizationsPagedResponse)` |   
  
### listOrganizationsCallable()
    
    
    public final UnaryCallable<ListOrganizationsRequest,ListOrganizationsResponse> listOrganizationsCallable()

Returns a list of organizations that the user has access to.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListOrganizationsRequest request =
           ListOrganizationsRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListOrganizationsResponse response =
             marketingplatformAdminServiceClient.listOrganizationsCallable().call(request);
         for (Organization element : response.getOrganizationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrganizationsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsRequest),[ListOrganizationsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsResponse)>` |   
  
### listOrganizationsPagedCallable()
    
    
    public final UnaryCallable<ListOrganizationsRequest,MarketingplatformAdminServiceClient.ListOrganizationsPagedResponse> listOrganizationsPagedCallable()

Returns a list of organizations that the user has access to.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListOrganizationsRequest request =
           ListOrganizationsRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Organization> future =
           marketingplatformAdminServiceClient.listOrganizationsPagedCallable().futureCall(request);
       // Do something.
       for (Organization element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrganizationsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListOrganizationsRequest),[ListOrganizationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListOrganizationsPagedResponse)>` |   
  
### listUserGroupMembers(@Nullable UserGroupName parent)
    
    
    public final MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse listUserGroupMembers(@Nullable UserGroupName parent)

Returns a list of members in the specified user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UserGroupName parent = UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]");
       for (UserGroupMember element :
           marketingplatformAdminServiceClient.listUserGroupMembers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.UserGroupName`  
Required. The parent user group where this UserGroupMember will be listed. Format: organizations/{org_id}/userGroups/{user_group_id}  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse)` |   
  
### listUserGroupMembers(ListUserGroupMembersRequest request)
    
    
    public final MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse listUserGroupMembers(ListUserGroupMembersRequest request)

Returns a list of members in the specified user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListUserGroupMembersRequest request =
           ListUserGroupMembersRequest.newBuilder()
               .setParent(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (UserGroupMember element :
           marketingplatformAdminServiceClient.listUserGroupMembers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserGroupMembersRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse)` |   
  
### listUserGroupMembers(String parent)
    
    
    public final MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse listUserGroupMembers(String parent)

Returns a list of members in the specified user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String parent = UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString();
       for (UserGroupMember element :
           marketingplatformAdminServiceClient.listUserGroupMembers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent user group where this UserGroupMember will be listed. Format: organizations/{org_id}/userGroups/{user_group_id}  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse)` |   
  
### listUserGroupMembersCallable()
    
    
    public final UnaryCallable<ListUserGroupMembersRequest,ListUserGroupMembersResponse> listUserGroupMembersCallable()

Returns a list of members in the specified user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListUserGroupMembersRequest request =
           ListUserGroupMembersRequest.newBuilder()
               .setParent(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListUserGroupMembersResponse response =
             marketingplatformAdminServiceClient.listUserGroupMembersCallable().call(request);
         for (UserGroupMember element : response.getUserGroupMembersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserGroupMembersRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersRequest),[ListUserGroupMembersResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersResponse)>` |   
  
### listUserGroupMembersPagedCallable()
    
    
    public final UnaryCallable<ListUserGroupMembersRequest,MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse> listUserGroupMembersPagedCallable()

Returns a list of members in the specified user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListUserGroupMembersRequest request =
           ListUserGroupMembersRequest.newBuilder()
               .setParent(UserGroupName.of("[ORGANIZATION]", "[USER_GROUP]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<UserGroupMember> future =
           marketingplatformAdminServiceClient
               .listUserGroupMembersPagedCallable()
               .futureCall(request);
       // Do something.
       for (UserGroupMember element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserGroupMembersRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupMembersRequest),[ListUserGroupMembersPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListUserGroupMembersPagedResponse)>` |   
  
### listUserGroups(@Nullable OrganizationName parent)
    
    
    public final MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse listUserGroups(@Nullable OrganizationName parent)

Returns a list of user groups in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (UserGroup element :
           marketingplatformAdminServiceClient.listUserGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.marketingplatform.admin.v1alpha.OrganizationName`  
Required. The parent org where this UserGroup will be listed. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse)` |   
  
### listUserGroups(ListUserGroupsRequest request)
    
    
    public final MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse listUserGroups(ListUserGroupsRequest request)

Returns a list of user groups in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListUserGroupsRequest request =
           ListUserGroupsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (UserGroup element :
           marketingplatformAdminServiceClient.listUserGroups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserGroupsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse)` |   
  
### listUserGroups(String parent)
    
    
    public final MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse listUserGroups(String parent)

Returns a list of user groups in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String parent = OrganizationName.of("[ORGANIZATION]").toString();
       for (UserGroup element :
           marketingplatformAdminServiceClient.listUserGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent org where this UserGroup will be listed. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse)` |   
  
### listUserGroupsCallable()
    
    
    public final UnaryCallable<ListUserGroupsRequest,ListUserGroupsResponse> listUserGroupsCallable()

Returns a list of user groups in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListUserGroupsRequest request =
           ListUserGroupsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListUserGroupsResponse response =
             marketingplatformAdminServiceClient.listUserGroupsCallable().call(request);
         for (UserGroup element : response.getUserGroupsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserGroupsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsRequest),[ListUserGroupsResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsResponse)>` |   
  
### listUserGroupsPagedCallable()
    
    
    public final UnaryCallable<ListUserGroupsRequest,MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse> listUserGroupsPagedCallable()

Returns a list of user groups in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ListUserGroupsRequest request =
           ListUserGroupsRequest.newBuilder()
               .setParent(OrganizationName.of("[ORGANIZATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<UserGroup> future =
           marketingplatformAdminServiceClient.listUserGroupsPagedCallable().futureCall(request);
       // Do something.
       for (UserGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserGroupsRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ListUserGroupsRequest),[ListUserGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.MarketingplatformAdminServiceClient.ListUserGroupsPagedResponse)>` |   
  
### reportPropertyUsage(ReportPropertyUsageRequest request)
    
    
    public final ReportPropertyUsageResponse reportPropertyUsage(ReportPropertyUsageRequest request)

Gets the usage and billing data for properties within the organization for the specified month.

Per direct client org, user needs to be OrgAdmin/BillingAdmin on the organization in order to view the billing and usage data.

Per sales partner client org, user needs to be OrgAdmin/BillingAdmin on the sales partner org in order to view the billing and usage data, or OrgAdmin/BillingAdmin on the sales partner client org in order to view the usage data only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ReportPropertyUsageRequest request =
           ReportPropertyUsageRequest.newBuilder()
               .setOrganization("organization1178922291")
               .setMonth("month104080000")
               .build();
       ReportPropertyUsageResponse response =
           marketingplatformAdminServiceClient.reportPropertyUsage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReportPropertyUsageRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReportPropertyUsageResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse)` |   
  
### reportPropertyUsage(String organization)
    
    
    public final ReportPropertyUsageResponse reportPropertyUsage(String organization)

Gets the usage and billing data for properties within the organization for the specified month.

Per direct client org, user needs to be OrgAdmin/BillingAdmin on the organization in order to view the billing and usage data.

Per sales partner client org, user needs to be OrgAdmin/BillingAdmin on the sales partner org in order to view the billing and usage data, or OrgAdmin/BillingAdmin on the sales partner client org in order to view the usage data only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String organization = "organization1178922291";
       ReportPropertyUsageResponse response =
           marketingplatformAdminServiceClient.reportPropertyUsage(organization);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Specifies the organization whose property usage will be listed. Format: organizations/{org_id}  
**Returns**  
---  
**Type** | **Description**  
`[ReportPropertyUsageResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse)` |   
  
### reportPropertyUsageCallable()
    
    
    public final UnaryCallable<ReportPropertyUsageRequest,ReportPropertyUsageResponse> reportPropertyUsageCallable()

Gets the usage and billing data for properties within the organization for the specified month.

Per direct client org, user needs to be OrgAdmin/BillingAdmin on the organization in order to view the billing and usage data.

Per sales partner client org, user needs to be OrgAdmin/BillingAdmin on the sales partner org in order to view the billing and usage data, or OrgAdmin/BillingAdmin on the sales partner client org in order to view the usage data only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       ReportPropertyUsageRequest request =
           ReportPropertyUsageRequest.newBuilder()
               .setOrganization("organization1178922291")
               .setMonth("month104080000")
               .build();
       ApiFuture<ReportPropertyUsageResponse> future =
           marketingplatformAdminServiceClient.reportPropertyUsageCallable().futureCall(request);
       // Do something.
       ReportPropertyUsageResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReportPropertyUsageRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageRequest),[ReportPropertyUsageResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.ReportPropertyUsageResponse)>` |   
  
### setPropertyServiceLevel(SetPropertyServiceLevelRequest request)
    
    
    public final SetPropertyServiceLevelResponse setPropertyServiceLevel(SetPropertyServiceLevelRequest request)

Updates the service level for an Analytics property.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       SetPropertyServiceLevelRequest request =
           SetPropertyServiceLevelRequest.newBuilder()
               .setAnalyticsAccountLink("analyticsAccountLink-397570975")
               .setAnalyticsProperty(PropertyName.of("[PROPERTY]").toString())
               .setServiceLevel(AnalyticsServiceLevel.forNumber(0))
               .build();
       SetPropertyServiceLevelResponse response =
           marketingplatformAdminServiceClient.setPropertyServiceLevel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetPropertyServiceLevelRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SetPropertyServiceLevelResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelResponse)` |   
  
### setPropertyServiceLevel(String analyticsAccountLink)
    
    
    public final SetPropertyServiceLevelResponse setPropertyServiceLevel(String analyticsAccountLink)

Updates the service level for an Analytics property.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       String analyticsAccountLink = "analyticsAccountLink-397570975";
       SetPropertyServiceLevelResponse response =
           marketingplatformAdminServiceClient.setPropertyServiceLevel(analyticsAccountLink);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`analyticsAccountLink` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent AnalyticsAccountLink scope where this property is in. Format: organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}  
**Returns**  
---  
**Type** | **Description**  
`[SetPropertyServiceLevelResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelResponse)` |   
  
### setPropertyServiceLevelCallable()
    
    
    public final UnaryCallable<SetPropertyServiceLevelRequest,SetPropertyServiceLevelResponse> setPropertyServiceLevelCallable()

Updates the service level for an Analytics property.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       SetPropertyServiceLevelRequest request =
           SetPropertyServiceLevelRequest.newBuilder()
               .setAnalyticsAccountLink("analyticsAccountLink-397570975")
               .setAnalyticsProperty(PropertyName.of("[PROPERTY]").toString())
               .setServiceLevel(AnalyticsServiceLevel.forNumber(0))
               .build();
       ApiFuture<SetPropertyServiceLevelResponse> future =
           marketingplatformAdminServiceClient.setPropertyServiceLevelCallable().futureCall(request);
       // Do something.
       SetPropertyServiceLevelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetPropertyServiceLevelRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelRequest),[SetPropertyServiceLevelResponse](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.SetPropertyServiceLevelResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAdminAccessBinding(AdminAccessBinding adminAccessBinding, FieldMask updateMask)
    
    
    public final AdminAccessBinding updateAdminAccessBinding(AdminAccessBinding adminAccessBinding, FieldMask updateMask)

Updates an admin access binding in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       AdminAccessBinding adminAccessBinding = AdminAccessBinding.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AdminAccessBinding response =
           marketingplatformAdminServiceClient.updateAdminAccessBinding(
               adminAccessBinding, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`adminAccessBinding` | `[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)`  
Required. The AdminAccessBinding to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update. Field names must be in snake case (for example, "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
  
### updateAdminAccessBinding(UpdateAdminAccessBindingRequest request)
    
    
    public final AdminAccessBinding updateAdminAccessBinding(UpdateAdminAccessBindingRequest request)

Updates an admin access binding in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UpdateAdminAccessBindingRequest request =
           UpdateAdminAccessBindingRequest.newBuilder()
               .setAdminAccessBinding(AdminAccessBinding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AdminAccessBinding response =
           marketingplatformAdminServiceClient.updateAdminAccessBinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateAdminAccessBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)` |   
  
### updateAdminAccessBindingCallable()
    
    
    public final UnaryCallable<UpdateAdminAccessBindingRequest,AdminAccessBinding> updateAdminAccessBindingCallable()

Updates an admin access binding in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UpdateAdminAccessBindingRequest request =
           UpdateAdminAccessBindingRequest.newBuilder()
               .setAdminAccessBinding(AdminAccessBinding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AdminAccessBinding> future =
           marketingplatformAdminServiceClient
               .updateAdminAccessBindingCallable()
               .futureCall(request);
       // Do something.
       AdminAccessBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAdminAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateAdminAccessBindingRequest),[AdminAccessBinding](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding)>` |   
  
### updateUserGroup(UpdateUserGroupRequest request)
    
    
    public final UserGroup updateUserGroup(UpdateUserGroupRequest request)

Updates a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UpdateUserGroupRequest request =
           UpdateUserGroupRequest.newBuilder()
               .setUserGroup(UserGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       UserGroup response = marketingplatformAdminServiceClient.updateUserGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
  
### updateUserGroup(UserGroup userGroup, FieldMask updateMask)
    
    
    public final UserGroup updateUserGroup(UserGroup userGroup, FieldMask updateMask)

Updates a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UserGroup userGroup = UserGroup.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       UserGroup response =
           marketingplatformAdminServiceClient.updateUserGroup(userGroup, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`userGroup` | `[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)`  
Required. The user group to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update. Field names must be in snake case (for example, "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)` |   
  
### updateUserGroupCallable()
    
    
    public final UnaryCallable<UpdateUserGroupRequest,UserGroup> updateUserGroupCallable()

Updates a user group in the specified GMP organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UpdateUserGroupRequest request =
           UpdateUserGroupRequest.newBuilder()
               .setUserGroup(UserGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<UserGroup> future =
           marketingplatformAdminServiceClient.updateUserGroupCallable().futureCall(request);
       // Do something.
       UserGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUserGroupRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupRequest),[UserGroup](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroup)>` |   
  
### updateUserGroupMember(UpdateUserGroupMemberRequest request)
    
    
    public final UserGroupMember updateUserGroupMember(UpdateUserGroupMemberRequest request)

Updates a member in the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UpdateUserGroupMemberRequest request =
           UpdateUserGroupMemberRequest.newBuilder()
               .setUserGroupMember(UserGroupMember.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       UserGroupMember response = marketingplatformAdminServiceClient.updateUserGroupMember(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupMemberRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
  
### updateUserGroupMember(UserGroupMember userGroupMember, FieldMask updateMask)
    
    
    public final UserGroupMember updateUserGroupMember(UserGroupMember userGroupMember, FieldMask updateMask)

Updates a member in the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UserGroupMember userGroupMember = UserGroupMember.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       UserGroupMember response =
           marketingplatformAdminServiceClient.updateUserGroupMember(userGroupMember, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`userGroupMember` | `[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)`  
Required. The user group member to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update. Field names must be in snake case (for example, "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.  
**Returns**  
---  
**Type** | **Description**  
`[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)` |   
  
### updateUserGroupMemberCallable()
    
    
    public final UnaryCallable<UpdateUserGroupMemberRequest,UserGroupMember> updateUserGroupMemberCallable()

Updates a member in the specified GMP user group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MarketingplatformAdminServiceClient marketingplatformAdminServiceClient =
         MarketingplatformAdminServiceClient.create()) {
       UpdateUserGroupMemberRequest request =
           UpdateUserGroupMemberRequest.newBuilder()
               .setUserGroupMember(UserGroupMember.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<UserGroupMember> future =
           marketingplatformAdminServiceClient.updateUserGroupMemberCallable().futureCall(request);
       // Do something.
       UserGroupMember response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUserGroupMemberRequest](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UpdateUserGroupMemberRequest),[UserGroupMember](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.UserGroupMember)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
