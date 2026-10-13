---
url: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBindingOrBuilder
title: Interface AdminAccessBindingOrBuilder (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:20.890606+00:00
---

# Interface AdminAccessBindingOrBuilder (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBindingOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AdminAccessBindingOrBuilder (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface AdminAccessBindingOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccessTargetCase()
    
    
    public abstract AdminAccessBinding.AccessTargetCase getAccessTargetCase()

**Returns**  
---  
**Type** | **Description**  
`[AdminAccessBinding.AccessTargetCase](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.AdminAccessBinding.AccessTargetCase)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of this AdminAccessBinding.

Format: organizations/{org_id}/adminAccessBindings/{admin_access_binding_id} Example: "organizations/123abc/adminAccessBindings/456def"

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of this AdminAccessBinding.

Format: organizations/{org_id}/adminAccessBindings/{admin_access_binding_id} Example: "organizations/123abc/adminAccessBindings/456def"

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOrganizationRoles(int index)
    
    
    public abstract OrganizationRole getOrganizationRoles(int index)

Optional. A list of roles granted to the parent organization.

USER_ADMIN_ROLE and BILLING_ADMIN_ROLE will be automatically added if ORG_ADMIN_ROLE is assigned.

No roles will be assigned if no roles are specified.

` repeated .google.marketingplatform.admin.v1alpha.OrganizationRole organization_roles = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationRole](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.OrganizationRole)` | The organizationRoles at the given index.  
  
### getOrganizationRolesCount()
    
    
    public abstract int getOrganizationRolesCount()

Optional. A list of roles granted to the parent organization.

USER_ADMIN_ROLE and BILLING_ADMIN_ROLE will be automatically added if ORG_ADMIN_ROLE is assigned.

No roles will be assigned if no roles are specified.

` repeated .google.marketingplatform.admin.v1alpha.OrganizationRole organization_roles = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of organizationRoles.  
  
### getOrganizationRolesList()
    
    
    public abstract List<OrganizationRole> getOrganizationRolesList()

Optional. A list of roles granted to the parent organization.

USER_ADMIN_ROLE and BILLING_ADMIN_ROLE will be automatically added if ORG_ADMIN_ROLE is assigned.

No roles will be assigned if no roles are specified.

` repeated .google.marketingplatform.admin.v1alpha.OrganizationRole organization_roles = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[OrganizationRole](https://docs.cloud.google.com/java/docs/reference/admin/latest/com.google.ads.marketingplatform.admin.v1alpha.OrganizationRole)>` | A list containing the organizationRoles.  
  
### getOrganizationRolesValue(int index)
    
    
    public abstract int getOrganizationRolesValue(int index)

Optional. A list of roles granted to the parent organization.

USER_ADMIN_ROLE and BILLING_ADMIN_ROLE will be automatically added if ORG_ADMIN_ROLE is assigned.

No roles will be assigned if no roles are specified.

` repeated .google.marketingplatform.admin.v1alpha.OrganizationRole organization_roles = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of organizationRoles at the given index.  
  
### getOrganizationRolesValueList()
    
    
    public abstract List<Integer> getOrganizationRolesValueList()

Optional. A list of roles granted to the parent organization.

USER_ADMIN_ROLE and BILLING_ADMIN_ROLE will be automatically added if ORG_ADMIN_ROLE is assigned.

No roles will be assigned if no roles are specified.

` repeated .google.marketingplatform.admin.v1alpha.OrganizationRole organization_roles = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for organizationRoles.  
  
### getUserEmail()
    
    
    public abstract String getUserEmail()

Email address of the user.

`string user_email = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userEmail.  
  
### getUserEmailBytes()
    
    
    public abstract ByteString getUserEmailBytes()

Email address of the user.

`string user_email = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userEmail.  
  
### getUserGroup()
    
    
    public abstract String getUserGroup()

Resource name of the user group.

`string user_group = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userGroup.  
  
### getUserGroupBytes()
    
    
    public abstract ByteString getUserGroupBytes()

Resource name of the user group.

`string user_group = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userGroup.  
  
### hasUserEmail()
    
    
    public abstract boolean hasUserEmail()

Email address of the user.

`string user_email = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userEmail field is set.  
  
### hasUserGroup()
    
    
    public abstract boolean hasUserGroup()

Resource name of the user group.

`string user_group = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userGroup field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
